import tkinter

def GetHighestData(Data): # Receive Data as List
    highest = 0
    for data_index in Data:
        data_num = int(data_index.split("-")[1])
        if highest < data_num:
            highest = data_num

    return highest
        

class AddItemFrame(tkinter.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        ## GENERATE TOP/CONTENTS FRAME ##

        TOPLABEL = "ADD ITEM"
        CONTENTFRAME = parent.GetGenerateContentFrame()(self,parent,TOPLABEL)
        ##SUBFRAMES
        UPPER_FRAME = tkinter.Frame(CONTENTFRAME,bg=CONTENTFRAME.cget("bg"))
        UPPER_FRAME.pack()

        LOWER_FRAME = tkinter.Frame(CONTENTFRAME,bg=CONTENTFRAME.cget("bg"))
        LOWER_FRAME.pack()






        ## CONTENT FRAME
        #UPPER
        TITLE_LABEL = tkinter.Label(
            UPPER_FRAME,
            text="FILL UP INFORMATION TO ADD IN LOST & FOUND SYSTEM",
            font=("Courier New",10,"italic"),
            bg=CONTENTFRAME.cget("bg")
            )
        TITLE_LABEL.pack(pady=30)
        #LOWER
        ITEM_INFORMATION = {
            "ITEM_NAME":{},
            "LAST-SEEN-ON":{},
            "LAST-SEEN-IN":{}
        }

        for i,INFO_NAME in enumerate(ITEM_INFORMATION.keys()):
            CurrentLabel = tkinter.Label(
                LOWER_FRAME,
                text=INFO_NAME,
                bg=LOWER_FRAME.cget("bg"),
                font=("Courier New",8))
            CurrentLabel.grid(column=0,row=i,pady=5)

            ITEM_INFORMATION[INFO_NAME] = {"ENTRY" : tkinter.Entry(LOWER_FRAME)}
            ITEM_INFORMATION[INFO_NAME]["ENTRY"].grid(column=1,row=i,padx=10)

        SUBMIT_BUTTON = tkinter.Button(LOWER_FRAME,text="Submit",font=("Courier New",8))
        SUBMIT_BUTTON.grid(column=1,row=5,pady=10)






        ## FUNCTIONS

        def OnSubmit():
            Index = GetHighestData(parent.DataManager.GetDataKeys())+1
            NewItemId = f"ID-{Index:04d}"

            Data = parent.DataManager.GetData()
            Data[NewItemId] = {
                "ITEM_NAME" : ITEM_INFORMATION["ITEM_NAME"]["ENTRY"].get(),
                "LAST-SEEN-ON" : ITEM_INFORMATION["LAST-SEEN-ON"]["ENTRY"].get(),
                "LAST-SEEN-IN" : ITEM_INFORMATION["LAST-SEEN-IN"]["ENTRY"].get(),
                "STATUS" : "LOST"
            }

            parent.DataManager.OverwriteData(Data)
            ## CLEAR ENTRY
            for ITEM_DATA in ITEM_INFORMATION.values():
                ITEM_DATA["ENTRY"].delete(0,tkinter.END)

        SUBMIT_BUTTON.config(command=OnSubmit)
        
