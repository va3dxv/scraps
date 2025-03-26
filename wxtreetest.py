import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.SetTitle("test frame")

        sizer_0 = wx.BoxSizer(wx.HORIZONTAL)
        self.window_1 = wx.SplitterWindow(self, wx.ID_ANY)
        self.window_1.SetMinimumPaneSize(20)
        sizer_0.Add(self.window_1, 1, wx.EXPAND, 0)

        self.pane_1 = wx.Panel(self.window_1, wx.ID_ANY)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        self.pane_2 = wx.Panel(self.window_1, wx.ID_ANY)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)

        self.button = wx.Button(self.pane_2, wx.ID_ANY, "test button")
        sizer_2.Add(self.button, 0, 0, 0)

        self.pane_1.SetSizer(sizer_1)
        self.pane_2.SetSizer(sizer_2)
        self.window_1.SplitVertically(self.pane_1, self.pane_2)
        self.SetSizer(sizer_0)
        self.Layout()

        self.Bind(wx.EVT_CONTEXT_MENU, self.OnButtonContextMenu, self.button)
        self.Show()

    def OnButtonContextMenu(self, event):
        self.PopupMenu(ButtonContext(self))

class ButtonContext(wx.Menu):
    def __init__(self, parent):
        super(ButtonContext, self).__init__()
        self.parent = parent
 
        button_popup = wx.MenuItem(self, wx.ID_ANY, 'test popup')
        self.Append(button_popup)        
        submenu = wx.Menu()
        submenu1 = wx.MenuItem(submenu, wx.ID_ANY, 'Submenu 1')
        submenu2 = wx.MenuItem(submenu, wx.ID_ANY, 'Submenu 2')
        submenu3 = wx.MenuItem(submenu, wx.ID_ANY, 'Submenu 3')
        submenu.Append(submenu1)
        submenu.Append(submenu2)
        submenu.Append(submenu3)
        button_popup2 = wx.MenuItem(self, wx.ID_ANY, 'A sub menu')
        button_popup2.SetSubMenu(submenu)
        self.Append(button_popup2)
        self.Bind(wx.EVT_MENU, self.button_action, button_popup)
        self.Bind(wx.EVT_MENU, self.submenu1_action, submenu1)
 
    def button_action(self, event):
        print("Test Menu Button")
        event.Skip()

    def submenu1_action(self, event):
        print("Submenu 1")
        event.Skip()
        
class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
