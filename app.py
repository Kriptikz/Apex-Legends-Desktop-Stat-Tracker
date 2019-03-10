import tkinter as tk
import requests
import json
from datahelper import PlayerData
from datahelper import LegendIds
from datahelper import LegendData

class App:
    def __init__(self, title, width, height):
        self.window = tk.Tk()

        self.window.title(title)
        self.window.geometry(f"{width}x{height}")

        self.api_key = {"TRN-Api-Key": ""}
        self.platform = 5
        self.name = "KriptikzX"

        self.playerData = PlayerData()

        self.rawStatsDict = {}


    def addWidgets(self):
        get_api_key_label = tk.Label(text="Get your API key from {link}")
        get_api_key_label.grid(column=0, row=0)

        api_key_label = tk.Label(text="API Key:")
        api_key_label.grid(column=2, row=0)
        
        current_api_key_label_text = tk.StringVar()
        current_api_key_label_text.set(f"Current API Key: {self.api_key['TRN-Api-Key']}")
        current_api_key_label = tk.Label(textvariable=current_api_key_label_text)
        current_api_key_label.grid(column=4, row=0)

        def get(event):
            self.api_key = {"TRN-Api-Key": event.widget.get()}
            current_api_key_label_text.set(f"Current API Key: {self.api_key['TRN-Api-Key']}")

        api_key_entry = tk.Entry()
        api_key_entry.bind('<Return>', get)
        api_key_entry.grid(column=3, row=0)

    def start(self):
        #self.getNewStatsJsonFileFromApi()
        self.loadNewStatsFromFile()
        self.processRawStatsDictToLegendsData()

        self.window.mainloop()


    def getNewStatsJsonFileFromApi(self):
        r = requests.get(f"https://public-api.tracker.gg/apex/v1/standard/profile/{self.platform}/{self.name}", headers=self.api_key)

        file = open("stats.json", "w")
        file.write(r.text)
        file.close()

    def loadNewStatsFromFile(self):
        file = open("stats.json", "r")
        stats = file.read()
    
        self.rawStatsDict = json.loads(stats)

    def processRawStatsDictToLegendsData(self):
        for legendData in self.playerData.legendsData:
            for child in self.rawStatsDict['data']['children']:
                if legendData.legendId.value == child['id']:
                    legendData.name = child['metadata']['legend_name']
                    for stat in child['stats']:
                        if stat['metadata']['key'] == "Kills":
                            legendData.kills = stat['value']           




