# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

wx.ID_MAIN = 1000

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_MAIN, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		boxSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.staticText = wx.StaticText( self, wx.ID_ANY, u"请将需要恢复文件的根文件夹拖动至窗口，或按【Browse】进行手动选择。", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText.Wrap( -1 )
		boxSizer.Add( self.staticText, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH|wx.TE_RICH2 )
		boxSizer.Add( self.textCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.dirPicker = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, 0 )
		boxSizer.Add( self.dirPicker, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.SetSizer( boxSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

