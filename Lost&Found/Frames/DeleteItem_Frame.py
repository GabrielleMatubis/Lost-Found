import tkinter

StatusColor = {
    "LOST" :"black",
    "FOUND" : "blue",
    "CLAIMED" : "green"
}

def UpdateItemList(ItemList,Index,Status):
    if not (Status in StatusColor):
        return

    ItemList.itemconfig(Index,fg=StatusColor[Status])

class DeleteItemFrame(tkinter.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        ## GENERATE TOP/CONTENTS FRAME ##
        TOPLABEL = "DELETE ITEM"
        CONTENTFRAME = parent.GetGenerateContentFrame()(self,parent,TOPLABEL)

        CONTENTFRAME.rowconfigure(0,weight=1)
        CONTENTFRAME.rowconfigure(1,weight=0)

        CONTENTFRAME.columnconfigure(0,weight=1)

        
        ## CONTENTS
        #ITEMLIST, RIGHTFRAME = parent.GetGenerateItemList()(CONTENTFRAME)
        ITEMLIST = tkinter.Listbox(CONTENTFRAME)
        ITEMLIST.grid(row=0,column=0,sticky="nsew")

        BOTTOMFRAME = tkinter.Frame(CONTENTFRAME)
        BOTTOMFRAME.grid(row=1,column=0,sticky="ew")
        BOTTOMFRAME.columnconfigure(0,weight=1)

        DELETE_BUTTON = tkinter.Button(BOTTOMFRAME,text="DELETE",font=("Courier New",10,"italic"))
        DELETE_BUTTON.grid(column=0,row=0,padx=20,pady=10,sticky="e")

        ## FUNCTIONS
        def UpdateListbox():
            ITEMLIST.delete(0, tkinter.END)

            Data = parent.DataManager.GetData()
            for item_id,item_data in Data.items():
                ITEMLIST.insert(tkinter.END,f"{item_id}|{item_data.get("ITEM_NAME","N/A")}")
                UpdateItemList(ITEMLIST,tkinter.END,item_data.get("STATUS","LOST"))

        SelectedItemId = None
        def OnSelect(event):
            nonlocal SelectedItemId

            selectedIndex = event.widget.curselection()[0]
            SelectedItemId = event.widget.get(selectedIndex).split("|")[0]
            ##---------------##


        def OnDelete():
            parent.DataManager.DeleteItemFromData(SelectedItemId)
            UpdateListbox()

        DELETE_BUTTON.config(command=OnDelete)
        ITEMLIST.bind("<<ListboxSelect>>",OnSelect)
        UpdateListbox()
