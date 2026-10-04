import tkinter

def GenerateContentFrames(parent,subparent,toplabel,backframe="MainFrame"):
    ## SUBFRAMES
    TOPFRAME = tkinter.Frame(parent,bg="#6B6A6A",height=35)
    TOPFRAME.pack(side="top",fill="x")

    CONTENTFRAME = tkinter.Frame(parent,bg="#E9E9E9")
    CONTENTFRAME.pack(side="top",fill="both",expand=True)

    ## TOPFRAMES-CONTENTS
    TOPLABEL = tkinter.Label(TOPFRAME,text=toplabel,bg=TOPFRAME.cget("bg"),font=("Courier New",16,"italic"),fg="blue")
    TOPLABEL.place(relx=0.5,rely=0.5,anchor="center")

    BACKBUTTON = tkinter.Button(TOPFRAME,text="BACK")
    BACKBUTTON.place(x=5,rely=0.5, anchor="w")

    ## CONTENTFRAMES-CONTENTS

    ##CONTENTS-FUNCTIONALITY
    def BackCommand():
        subparent.ShowFrame(backframe)

    BACKBUTTON.config(command=BackCommand)

    return CONTENTFRAME

def GenerateItemList(parent):
    LEFT_FRAME = tkinter.Frame(parent)
    RIGHT_FRAME = tkinter.Frame(parent,bg=parent.cget("bg"),padx=10)

    parent.grid_columnconfigure(0,weight=1,uniform="half")
    parent.grid_columnconfigure(1,weight=1,uniform="half")
    parent.grid_rowconfigure(0,weight=1)

    LEFT_FRAME.grid(column=0,row=0,sticky="nsew")
    RIGHT_FRAME.grid(column=1,row=0,sticky="nsew")

    LEFT_FRAME.grid_rowconfigure(0,weight=1)
    LEFT_FRAME.grid_columnconfigure(0,weight=1)
    # ITEM LIST
    ITEMLIST = tkinter.Listbox(LEFT_FRAME)
    SCROLLBAR = tkinter.Scrollbar(LEFT_FRAME)

    ITEMLIST.config(yscrollcommand=SCROLLBAR.set)
    SCROLLBAR.config(command=ITEMLIST.yview)

    ITEMLIST.grid(column=0,row=0,sticky="nsew")
    SCROLLBAR.grid(column=1,row=0,sticky="ns")

    return ITEMLIST,RIGHT_FRAME