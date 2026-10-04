import tkinter

def OnClaim(ROOT,ITEM_ID):
    ROOT.ShowFrame("ClaimItemFrame",{"ITEM_ID":ITEM_ID})

def ShowClaimerData(parent,CLAIMER_DATA):
    ClaimerInfo = tkinter.Toplevel(parent)
    ClaimerInfo.title("Claimer Data")
    ClaimerInfo.geometry("300x150")

    ClaimerInfo.grab_set()
    ClaimerInfo.grid_columnconfigure(0,weight=1)
    ##CONTENTS##
    TopLabel = tkinter.Label(ClaimerInfo,text="CLAIMER INFORMATION",font=("Courier New",16,"italic"),bg="#727171",fg="white")
    TopLabel.grid(column=0,row=0,sticky="nsew")

    ContentFrame = tkinter.Frame(ClaimerInfo)
    ContentFrame.grid(column=0,row=1)

    ## CLAIMER INFO LABEL
    tkinter.Label(ContentFrame,text=f"CLAIMER NAME : {CLAIMER_DATA["NAME"]}",font=("Courier New",10,"italic")).pack(pady=15)
    tkinter.Label(ContentFrame,text=f"CLAIMER STUDENT_ID : {CLAIMER_DATA["STUDENT_ID"]}",font=("Courier New",10,"italic")).pack()
    
    

StatusColor = {
    "LOST" :"black",
    "FOUND" : "blue",
    "CLAIMED" : "green"
}

def UpdateItemList(ItemList,Index,Status):
    if not (Status in StatusColor):
        return

    ItemList.itemconfig(Index,fg=StatusColor[Status])

class LostItemFrame(tkinter.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        ## GENERATE TOP/CONTENTS FRAME ##
        TOPLABEL = "LOST ITEM"
        CONTENTFRAME = parent.GetGenerateContentFrame()(self,parent,TOPLABEL)

        ## CONTENTS
        ITEMLIST , RIGHTFRAME = parent.GetGenerateItemList()(CONTENTFRAME)

        INFO_LABEL = [
            "ITEM_ID",
            "ITEM_NAME",
            "LAST-SEEN-ON",
            "LAST-SEEN-IN",
            "STATUS"
        ]

        INFO_DETAILS = {
            "ITEM_ID" : tkinter.Label(RIGHTFRAME,text="",bg=RIGHTFRAME.cget("bg")),
            "ITEM_NAME" : tkinter.Label(RIGHTFRAME,text="",bg=RIGHTFRAME.cget("bg")),
            "LAST-SEEN-ON" : tkinter.Label(RIGHTFRAME,text="",bg=RIGHTFRAME.cget("bg")),
            "LAST-SEEN-IN" : tkinter.Label(RIGHTFRAME,text="",bg=RIGHTFRAME.cget("bg")),
            "STATUS" : tkinter.Label(RIGHTFRAME,text="",bg=RIGHTFRAME.cget("bg")),
        }

        for i,txt in enumerate(INFO_LABEL):
            CURRENT_LABEL = tkinter.Label(RIGHTFRAME,text=txt,bg=RIGHTFRAME.cget("bg"),anchor="w")
            CURRENT_LABEL.grid(column=0,row=i,sticky="w")

            INFO_DETAILS[txt].grid(column=1,row=i,sticky="w",padx=10)

        _,current_row = RIGHTFRAME.grid_size()
        CLAIMBUTTON = tkinter.Button(RIGHTFRAME,text="Claim",font=("Courier New",9,"italic"),anchor="w")













        ## FUNCTIONS
        Data = parent.DataManager.GetData()
        for item_id,item_data in Data.items():
            ITEMLIST.insert(tkinter.END,f"{item_id}|{item_data.get("ITEM_NAME","N/A")}")
            UpdateItemList(ITEMLIST,tkinter.END,item_data.get("STATUS","LOST"))

        SelectedItemID = None
        def OnItemSelect(event):
            nonlocal SelectedItemID

            selected = event.widget.curselection()
            if not selected:
                return

            SELECTED_ITEM_ID = event.widget.get(selected[0]).split("|")[0]
            INFO_DETAILS["ITEM_ID"].config(text=f": {SELECTED_ITEM_ID}")
            for Selected_ItemKey,Selected_ItemValue in Data[SELECTED_ITEM_ID].items():
                if not (Selected_ItemKey in INFO_DETAILS):
                    continue
                INFO_DETAILS[Selected_ItemKey].config(text=f": {Selected_ItemValue}")

            ## CLAIM BUTTON ##
            if (Data[SELECTED_ITEM_ID]["STATUS"] == "FOUND") or (Data[SELECTED_ITEM_ID]["STATUS"] == "CLAIMED"):
                CLAIMBUTTON.config(text="Claim Item!" if Data[SELECTED_ITEM_ID]["STATUS"] == "FOUND" else "Claimer Data")
                CLAIMBUTTON.grid(column=0,row=current_row,pady=15,sticky="w",padx=10)
                SelectedItemID = SELECTED_ITEM_ID
            else:
                CLAIMBUTTON.grid_remove()
                SelectedItemID = None
        
        ITEMLIST.bind("<<ListboxSelect>>",OnItemSelect)
        CLAIMBUTTON.config(
            command=lambda:OnClaim(parent,SelectedItemID) if Data[SelectedItemID]["STATUS"] == "FOUND" else ShowClaimerData(self,Data[SelectedItemID].get("CLAIMER_DATA",{}))
        )