import json

class DataManager():
    def __init__(self):
        with open("Data/items.json","r") as raw_data:
            self.data = json.load(raw_data)

    def OverwriteData(self,newData):
        self.data = newData

        with open("Data/items.json","w") as file:
            json.dump(newData,file,indent=4)

    def DeleteItemFromData(self,ItemID):
        if not (ItemID in self.data):
            return

        del self.data[ItemID]
        self.OverwriteData(self.data)
    
    def GetData(self):
        return self.data

    def GetDataKeys(self):
        return list(self.data.keys())