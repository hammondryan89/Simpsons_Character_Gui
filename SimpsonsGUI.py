import wx, database

class Frame(wx.Frame):
    def __init__(self, title):
        self.fillListCtrl()
        wx.Frame.__init__(self, None,\
                          title=title, size=(800, 600))
        panel = wx.Panel(self)

        #creating the menu bar
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        menuBar.Append(fileMenu, "File")
        exitItem = fileMenu.Append(wx.NewId(), "Exit", "Exit the program")

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.exitProgram, exitItem)

        self.CreateStatusBar()

        text = wx.StaticBox(panel, label="Add a new character", pos =(20, 40), size= (300, 250))
        font = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        text.SetFont(font)

        #setup for adding a new character
        wx.StaticText(panel, label="Character Name:", pos = (30, 80))
        wx.StaticText(panel, label="Gender:", pos = (30, 120))
        wx.StaticText(panel, label="Age:", pos = (30, 160))
        wx.StaticText(panel, label="Occupation:", pos = (30, 200))

        #single line text boxes
        self.sName = wx.TextCtrl(panel, size=(170, -1), pos = (130, 80))
        self.sGen = wx.TextCtrl(panel, size=(170, -1), pos = (130, 120))
        self.sAge = wx.SpinCtrl(panel, value="0", size=(70, 25), pos = (130, 160))
        self.sOcc = wx.TextCtrl(panel, size=(170, -1), pos = (130, 200))


        #save  button
        save = wx.Button(panel, label="Add Character", pos = (100, 250))
        save.Bind(wx.EVT_BUTTON, self.addCharacter)

        #setup the table UI
        # setup table as listCtrl
        self.listCtrl = wx.ListCtrl(panel, size=(400, 400), pos=(350, 40), style=wx.LC_REPORT |wx.BORDER_SUNKEN)
        self.listCtrl.InsertColumn(0, "ID")
        self.listCtrl.InsertColumn(1, "Name")
        self.listCtrl.InsertColumn(2, "Gender")
        self.listCtrl.InsertColumn(3, "Age")
        self.listCtrl.InsertColumn(4, "Occupation")
        

        deleteBtn = wx.Button(panel, label="Eat my shorts!!", pos=(640, 450))
        deleteBtn.Bind(wx.EVT_BUTTON, self.onDelete)

        self.listCtrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onSelect)

        
    def onSelect(self, event):
        self.selectedId = event.GetText()


    def exitProgram(self, event):
        self.Destroy()

    def addCharacter(self, event):
        name = self.sName.GetValue()
        gen = self.sGen.GetValue()
        age = self.sAge.GetValue()
        occ = self.sOcc.GetValue()
        if(name == '') or (gen == '')\
            or (age == '') or (occ == ''):
                dlg = wx.MessageDialog(None, "Whoa!!! You forgot something man", "Aye Carumba!!!", wx.OK)
                dlg.ShowModal()
                dlg.Destroy()
                return False

        print name
        print gen
        print age
        print occ

        self.fillListCtrl()

        #adding a character to the database
        database.newCharacter(name, gen, age, occ)
        print database.viewAll()

   

        #empty text boxes when finished
        self.sName.Clear()
        self.sGen.Clear()
        self.sOcc.Clear()
        self.sAge.SetValue(0)

     #get data from the database
        
     def fillListCtrl(self):
        allData = database.viewAll()
        self.listCtrl.DeleteAllItems()
        for row in allData:
            self.listCtrl.Append(row)
            
    def onDelete(self, event):
        #delete the character
        database.deleteCharacter(self.selectedId)

        self.fillListCtrl()
        


   

app = wx.App()
frame = Frame("Simpsons Characters")
frame.Show()
app.MainLoop()
    
