import wx

class MyFrame(wx.Frame):

    def __init__(self):
        # Need to pass in the class name and self to the super function to allow the inheritance of the previous class
        super(MyFrame,self).__init__(parent = None, title = "Hello World")
        panel = wx.Panel(self)

        self.text_ctrl = wx.TextCtrl(panel, pos=(5,5))
        my_button = wx.Button(panel, label="Press me", pos=(5,55))

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
