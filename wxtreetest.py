from datetime import datetime


datestring = '20250224183815'

dateformat = '%Y%m%d%H%M%S'

print(datetime.strptime(datestring, dateformat))

then = datetime.now()

import wx 
  
class MainFrame(wx.Frame): 
    def __init__(self): 
        wx.Frame.__init__(self, parent = None, title ='TreeCtrl Demo') 
        self.count = 50
        self.tree = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize) 
        self.root = self.tree.AddRoot('Root ') 
        def addchild():
            if self.count > 0:
                self.subcount = 25
                mainitem = self.tree.AppendItem(self.root, f'Limb {self.count}')
                def morkids():
                    self.subsubcount = 10
                    subitem = self.tree.AppendItem(mainitem, f'Branch{self.subcount}')
                    def mormorkids():
                            subsubitem = self.tree.AppendItem(subitem, f'Leaf{self.subsubcount}')
                            self.subsubcount -=1 
                    while self.subsubcount > 0:
                        mormorkids()
                    self.subcount -=1 
                while self.subcount > 0:
                     morkids()
                self.count -=1
            else:
                return
        while self.count > 0:
            addchild()
        self.tree.Expand(self.root) 
        self.Show()
        now = datetime.now()


        duration = now - then                         # For build-in functions
        duration_in_s = duration.total_seconds()
        print(duration_in_s * 1000)
  
if __name__ == '__main__': 
    app = wx.App(redirect = False) 
    frame = MainFrame() 
    app.MainLoop() 
