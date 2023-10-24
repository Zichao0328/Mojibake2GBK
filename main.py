# This is a sample Python script.
import wx
import os
from MainFrame import MainFrame
from Renamer import Renamer

VERSION = '0.1.0'



# def rename_files(path):
#     file_abs_path = []
#     '''
#     自底向上遍历，防止更改父文件夹名后找不到子文件夹/子文件
#     '''
#     for root, dirs, files in os.walk(path, topdown=False):
#         for name in files + dirs:
#             old_path = os.path.join(root, name)
#             file_abs_path.append(old_path)
#     '''
#     修改文件名
#     '''
#     for abs_path in file_abs_path:
#         old_path, old_name = os.path.split(abs_path)
#         new_name = old_name.encode('gbk').decode('shift_jis')
#         os.rename(abs_path, os.path.join(old_path, new_name))
#     return file_abs_path


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
    # patten = "^[u4E00-u9FFF]+"
    # print(re.match(patten, gbk_string))
    # shift_jis_string = gbk_string.encode('gbk').decode('shift_jis')
    # print(shift_jis_string)
    path = 'D:\埑敆鋜傔-僀僠儍儔僽媡栭攪偄曇'
    # file_names = rename_files(path)
    app = wx.App(False)
    nwid = AppFrame(None)
    nwid.Show()
    app.MainLoop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
