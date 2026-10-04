import tkinter

class ClaimItemFrame(tkinter.Frame):
    def __init__(self,parent,PassedData):
        super().__init__(parent)

        ## GENERATE TOP/CONTENTS FRAME ##
        TOPLABEL = "CLAIM ITEM"
        CONTENTFRAME = parent.GetGenerateContentFrame()(self,parent,TOPLABEL,"LostItemFrame")








        ## CONTENTS ##

        ## SUBFRAMES
        UPPERFRAME = tkinter.Frame(CONTENTFRAME,bg=CONTENTFRAME.cget("bg"))
        UPPERFRAME.pack()

        LOWERFRAME = tkinter.Frame(CONTENTFRAME,bg=CONTENTFRAME.cget("bg"))
        LOWERFRAME.pack()

        ## UPPER FRAMES
        TOPLABEL = tkinter.Label(UPPERFRAME,text="FILL UP PERSONAL INFORMATION TO CLAIM :",font=("Courier New",10,"italic"),bg=UPPERFRAME.cget("bg"))
        TOPLABEL.pack(pady=25)

        PERSONAL_INFO = {
            "NAME":{},
            "STUDENT_ID":{}
        }

        for i,INFO_NAME in enumerate(PERSONAL_INFO.keys()):
            CurrentLabel = tkinter.Label(
                LOWERFRAME,text=INFO_NAME,
                bg=LOWERFRAME.cget("bg"),
                font=("Courier New",8)
            )
            CurrentLabel.grid(column=0,row=i,pady=5)

            PERSONAL_INFO[INFO_NAME] = {"ENTRY" : tkinter.Entry(LOWERFRAME)}
            PERSONAL_INFO[INFO_NAME]["ENTRY"].grid(column=1,row=i,padx=10)

        CLAIM_BUTTON = tkinter.Button(CONTENTFRAME,text="CLAIM",font=("Courier New",8,"italic"))
        CLAIM_BUTTON.pack(pady=10)









        
        ##FUNCTIONS
        Data = parent.DataManager.GetData()

        def OnClaim():
            Claimer_Name = PERSONAL_INFO["NAME"]["ENTRY"].get()
            Claimer_StudentID = PERSONAL_INFO["STUDENT_ID"]["ENTRY"].get()

            Data[PassedData["ITEM_ID"]]["STATUS"] = "CLAIMED"
            Data[PassedData["ITEM_ID"]]["CLAIMER_DATA"] = {
                "NAME" : Claimer_Name,
                "STUDENT_ID" : Claimer_StudentID
            }

            parent.DataManager.OverwriteData(Data)
            parent.ShowFrame("LostItemFrame")

        CLAIM_BUTTON.config(command=OnClaim)