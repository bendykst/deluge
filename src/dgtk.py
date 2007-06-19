# dgtk.py
#
# Copyright (C) Zach Tibbitts 2006 <zach@collegegeek.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, write to:
# 	The Free Software Foundation, Inc.,
# 	51 Franklin Street, Fifth Floor
# 	Boston, MA  02110-1301, USA.
#
#  In addition, as a special exception, the copyright holders give
#  permission to link the code of portions of this program with the OpenSSL
#  library.
#  You must obey the GNU General Public License in all respects for all of
#  the code used other than OpenSSL. If you modify file(s) with this
#  exception, you may extend this exception to your version of the file(s),
#  but you are not obligated to do so. If you do not wish to do so, delete
#  this exception statement from your version. If you delete this exception
#  statement from all source files in the program, then also delete it here.

# Similar to common, this contains any common functions
# related to gtk that are needed by the client

import common
import gettext
import pygtk
pygtk.require('2.0')
import gtk
import gtk.glade

# This is a dummy tray object to allow Deluge to run on PyGTK < 2.9
class StupidTray:
	def __init__(self):
		pass
	def set_visible(self, value):
		pass
	def set_tooltip(self, value):
		pass

## Functions to create columns

def add_func_column(view, header, func, data, sortid=None):
	column = gtk.TreeViewColumn(header)
	render = gtk.CellRendererText()
	column.pack_start(render, True)
	column.set_cell_data_func(render, func, data)
	if sortid is not None:
		column.set_clickable(True)
		column.set_sort_column_id(sortid)
	else:
		try:
			if len(data) == 1:
				column.set_clickable(True)
				column.set_sort_column_id(data[0])
		except TypeError:
			column.set_clickable(True)
			column.set_sort_column_id(data)
	column.set_resizable(True)
	column.set_expand(False)
	view.append_column(column)
	return column
	

def add_text_column(view, header, cid):
	render = gtk.CellRendererText()
	column = gtk.TreeViewColumn(header, render, text=cid)
	column.set_clickable(True)
	column.set_sort_column_id(cid)
	column.set_resizable(True)
	column.set_expand(False)
	view.append_column(column)
	return column

def add_progress_column(view, header, pid, mid):
	render = gtk.CellRendererProgress()
	column = gtk.TreeViewColumn(header, render, value=pid, text=mid)
	column.set_clickable(True)
	column.set_sort_column_id(pid)
	column.set_resizable(True)
	column.set_expand(False)
	view.append_column(column)
	return column

def add_toggle_column(view, header, cid, toggled_signal=None):
	render = gtk.CellRendererToggle()
	render.set_property('activatable', True)
	column = gtk.TreeViewColumn(header, render, active=cid)
	column.set_clickable(True)
	column.set_resizable(True)
	column.set_expand(False)
	view.append_column(column)
	if toggled_signal is not None:
		render.connect("toggled", toggled_signal)
	return column

def add_texticon_column(view, header, icon_col, text_col):
	column = gtk.TreeViewColumn(header)
	render = gtk.CellRendererPixbuf()
	column.pack_start(render, expand=False)
	column.add_attribute(render, 'pixbuf', icon_col)
	render = gtk.CellRendererText()
	column.pack_start(render, expand=True)
	column.add_attribute(render, 'text', text_col)
	view.append_column(column)
	return column
