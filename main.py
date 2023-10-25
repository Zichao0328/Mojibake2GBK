# This is a sample Python script.
import wx
import os
from MainFrame import MainFrame
from Renamer import Renamer

VERSION = '0.1.0'


class MyFileDropTarget(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self, x, y, filepath):
        """
        当接收到用户拖拽的文件时，运行 renamer
        """
        if os.path.isdir(filepath[0]):
            dirpath = filepath[0]
        self.window.run_renamer(dirpath)
        return True

class AppFrame(MainFrame):
    def __init__(self, parent):
        MainFrame.__init__(self, parent)

        # 使文件能被拖拽到 wx.TextCtrl 组件
        drop_target = MyFileDropTarget(self)
        self.textCtrl.SetDropTarget(drop_target)

    def on_dir_changed_event(self, event):
        """
        当 wx.DirPickerCtrl 组件接收到用户选择的文件夹时，运行 renamer
        """
        root_path = self.dirPicker.GetPath()
        self.run_renamer(root_path)

    def __print_info(self, message: str):
        self.textCtrl.SetDefaultStyle(wx.TextAttr(wx.BLACK))
        self.textCtrl.AppendText(message + '\n')

    def __print_warning(self, message: str):
        self.textCtrl.SetDefaultStyle(wx.TextAttr(wx.BLUE))
        self.textCtrl.AppendText(message + '\n')

    def __print_error(self, message: str):
        self.textCtrl.SetDefaultStyle(wx.TextAttr(wx.RED))
        self.textCtrl.AppendText(message + '\n')

    def run_renamer(self, root_path):
        self.__print_info(f'******************************运行开始,目标文件夹为【{root_path}】******************************\n\n')
        renamer = Renamer(None)
        rename_files_num = renamer.rename_files(root_path)
        self.__print_info(f'******************************运行结束,更改了【{rename_files_num}】个文件(夹)******************************\n\n')

if __name__ == '__main__':
    app = wx.App(False)
    nwid = AppFrame(None)
    nwid.SetTitle(f'DLSite 同人作品日文乱码转换工具 v{VERSION}')
    nwid.Show()
    app.MainLoop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
