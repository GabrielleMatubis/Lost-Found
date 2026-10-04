import tkinter

import Frames.FrameHandler as FrameHandler

from Data.data_manager import DataManager

## IMPORT FRAMES
from Frames.Main_Frame import MainFrame

from Frames.LostItem_Frame import LostItemFrame
from Frames.AddItem_Frame import AddItemFrame
from Frames.UpdateItem_Frame import UpdateItemFrame
from Frames.DeleteItem_Frame import DeleteItemFrame
from Frames.ClaimItem_Frame import ClaimItemFrame

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500

## MAIN CLASS
class MAINROOT(tkinter.Tk):
    SUBFRAMES = {
        "MainFrame" : MainFrame,
        "LostItemFrame" : LostItemFrame,
        "AddItemFrame" : AddItemFrame,
        "UpdateItemFrame" : UpdateItemFrame,
        "DeleteItemFrame" : DeleteItemFrame,
        "ClaimItemFrame" : ClaimItemFrame,
    }

    def __init__(self):
        super().__init__()
        self.title("Lost & Found")
        self.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))
    
        self.CurrentFrame = None
        self.ShowFrame("MainFrame") ## DEFAULT FRAME kapag binuksan yung program / nirun program

        self.DataManager = DataManager()
    
    def ShowFrame(self,FRAME_NAME,PassedData=None):
        if self.CurrentFrame:
            self.CurrentFrame.destroy()

        if PassedData:
            self.CurrentFrame = self.SUBFRAMES[FRAME_NAME](self,PassedData)
        else:
            self.CurrentFrame = self.SUBFRAMES[FRAME_NAME](self)
        
        self.CurrentFrame.pack(fill="both",expand=True)

    def Exit(self):
        self.destroy()

    def GetGenerateContentFrame(self):
        return FrameHandler.GenerateContentFrames

    def GetGenerateItemList(self):
        return FrameHandler.GenerateItemList