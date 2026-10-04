import tkinter
from Frames.LostItem_Frame import LostItemFrame

TOPLABEL_TXT = "LOST & FOUND"
BUTTON_DISTANCE = 20

def GenerateMainFrame(parent):
    parent.grid_columnconfigure(0,weight=1)

    parent.grid_rowconfigure(0,weight=1)
    parent.grid_rowconfigure(1,weight=30)

    TOPLABEL = tkinter.Label(parent,bg="#828181",text=TOPLABEL_TXT,font=("Courier New",20,"bold","italic"),fg="white")
    TOPLABEL.grid(column=0,row=0,sticky="nsew")

    BOTTOMFRAME = tkinter.Frame(parent)
    BOTTOMFRAME.grid(column=0,row=1,sticky="nsew")

    return BOTTOMFRAME

class MainFrame(tkinter.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        BOTTOMFRAME = GenerateMainFrame(self)
        BOTTOMFRAME.grid_columnconfigure(0,weight=1)
        BOTTOMFRAME.grid_columnconfigure(1,weight=6)

        BUTTONS = {
            "LOST_ITEM" : {
                "BUTTON_OBJECT" : tkinter.Button(
                    BOTTOMFRAME,text="VIEW LOST ITEM",font=("Courier New",15,"italic"),padx=10,borderwidth=3
                ),
                "FRAME_NAME" : "LostItemFrame" 
            },
            "ADD_ITEM" : {
                "BUTTON_OBJECT" : tkinter.Button(
                    BOTTOMFRAME,text="ADD ITEM",font=("Courier New",15,"italic"),padx=10,borderwidth=3
                ),
                "FRAME_NAME" : "AddItemFrame"
            },
            "UPDATE_ITEM" : {
                "BUTTON_OBJECT" : tkinter.Button(
                    BOTTOMFRAME,text="UPDATE ITEM",font=("Courier New",15,"italic"),padx=10,borderwidth=3
                ),
                "FRAME_NAME" : "UpdateItemFrame"
            },
            "DELETE_ITEM" : {
                "BUTTON_OBJECT" : tkinter.Button(
                    BOTTOMFRAME,text="DELETE ITEM",font=("Courier New",15,"italic"),padx=10,borderwidth=3
                ),
                "FRAME_NAME" : "DeleteItemFrame"
            },
            "EXIT" : {
                "BUTTON_OBJECT" : tkinter.Button(
                    BOTTOMFRAME,text="EXIT / LOGOUT",font=("Courier New",15,"italic"),padx=10,borderwidth=3
                ),
                "FUNCTION" : parent.Exit
            } 
        }

        for i, BUTTON_DATA in enumerate(BUTTONS.values()):
            CURRENT_BUTTON = BUTTON_DATA["BUTTON_OBJECT"]
            CURRENT_BUTTON.grid(column=1,row=i,sticky="w",pady=BUTTON_DISTANCE)
        
            if "FRAME_NAME" in BUTTON_DATA:
                TARGET_FRAME = BUTTON_DATA["FRAME_NAME"]
                CURRENT_BUTTON.config(command=lambda frame=TARGET_FRAME:parent.ShowFrame(frame))
        
            if "FUNCTION" in BUTTON_DATA:
                BTN_FUNCTION = BUTTON_DATA["FUNCTION"]
                CURRENT_BUTTON.config(command=BTN_FUNCTION)

                