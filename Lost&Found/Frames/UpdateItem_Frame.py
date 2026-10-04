import tkinter
from tkinter import ttk

def UpdateItemList(ItemList,Index,NewStatus):
    ItemList.itemconfig(Index,fg="black" if NewStatus == "LOST" else "blue")

class UpdateItemFrame(tkinter.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        ## GENERATE TOP/CONTENTS FRAME ##
        TOPLABEL = "UPDATE ITEM"
        CONTENTFRAME = parent.GetGenerateContentFrame()(self,parent,TOPLABEL)




        ## CONTENTS
        ITEMLIST , RIGHTFRAME = parent.GetGenerateItemList()(CONTENTFRAME)

        LABEL_TEXT = tkinter.Label(RIGHTFRAME,text="ITEM STATUS : ",font=("Courier New",10),bg=RIGHTFRAME.cget("bg"),anchor="w")
        LABEL_TEXT.grid(column=0,row=0,sticky="w")

        ITEM_TEXT = tkinter.Label(RIGHTFRAME,text="",font=("Courier New",10),bg=RIGHTFRAME.cget("bg"),anchor="w")
        ITEM_TEXT.grid(column=0,row=1,sticky="w")

        STATUS_BOX = ttk.Combobox(RIGHTFRAME,values=["FOUND","LOST"],state="readonly")
        STATUS_BOX.set("")
        STATUS_BOX.grid(column=1,row=1)

        UPDATE_BUTTON = tkinter.Button(RIGHTFRAME,text="Update",font=("Courier New",8,"italic"))
        UPDATE_BUTTON.grid(column=1,row=2,pady=10)





        

        ## FUNCTIONS
        Data = parent.DataManager.GetData()
        for item_id,item_data in Data.items():
            if item_data.get("STATUS","LOST") == "CLAIMED":
                continue

            ITEMLIST.insert(tkinter.END,f"{item_id}|{item_data.get("ITEM_NAME","N/A")}")
            UpdateItemList(ITEMLIST,tkinter.END,item_data.get("STATUS","LOST"))

        SelectedItemId = None
        SelectedIndex = None
        def UnSelect():
            nonlocal SelectedItemId,SelectedIndex

            SelectedItemId = None
            SelectedIndex = None
            ITEM_TEXT.config(text="")
            STATUS_BOX.set("")


        def OnItemSelect(event):
            nonlocal SelectedItemId, SelectedIndex

            selected = event.widget.curselection()
            if not selected:
                return

            SelectedIndex = selected[0]
            SELECTED_ITEM_ID = event.widget.get(selected[0]).split("|")[0]
            ##------------##
            ITEM_TEXT.config(text=SELECTED_ITEM_ID)

            STATUS_BOX.set(Data[SELECTED_ITEM_ID].get("STATUS","LOST"))
            SelectedItemId = SELECTED_ITEM_ID

        def OnUpdate():
            if (not SelectedItemId) or (Data[SelectedItemId]["STATUS"] == STATUS_BOX.get()):
                print("Select Something or Nothing has Changed")
                return

            Data[SelectedItemId]["STATUS"] = STATUS_BOX.get()
            parent.DataManager.OverwriteData(Data)

            UpdateItemList(ITEMLIST,SelectedIndex,STATUS_BOX.get())
            UnSelect()



        UPDATE_BUTTON.config(command=OnUpdate)
        ITEMLIST.bind("<<ListboxSelect>>",OnItemSelect)
        