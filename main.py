# This is a sample Python script.
import wx
import os
from MainFrame import MainFrame
from Renamer import Renamer

VERSION = '0.1.0'


class AppFrame(MainFrame):

    def on_dir_changed_event(self, event):
        """
        当 wx.DirPickerCtrl 组件接收到用户选择的文件夹时，运行 renamer
        """
        root_path = self.dirPicker.GetPath()
        print(root_path)
        self.run_renamer(root_path)

    def __print_info(self, message: str):
        self.text_ctrl.SetDefaultStyle(wx.TextAttr(wx.BLACK))
        self.text_ctrl.AppendText(message + '\n')

    def __print_warning(self, message: str):
        self.text_ctrl.SetDefaultStyle(wx.TextAttr(wx.BLUE))
        self.text_ctrl.AppendText(message + '\n')

    def __print_error(self, message: str):
        self.text_ctrl.SetDefaultStyle(wx.TextAttr(wx.RED))
        self.text_ctrl.AppendText(message + '\n')

    def run_renamer(self, root_path):
        renamer = Renamer(None)
        renamer.rename_files(root_path)

if __name__ == '__main__':
    gbk_string = '01_wav（効果音あり）'
    app = wx.App(False)
    nwid = AppFrame(None)
    nwid.SetTitle(f'DLSite 同人作品日文乱码转换工具 v{VERSION}')
    nwid.Show()
    app.MainLoop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
