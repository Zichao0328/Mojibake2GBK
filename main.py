# This is a sample Python script.
import wx

from MainFrame import MainFrame

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class AppFrame(MainFrame):
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = wx.App(False)
    nwid = AppFrame(None)
    nwid.Show()
    app.MainLoop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
