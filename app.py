import tkinter as tk
import requests
import json
import webbrowser
from datahelper import PlayerData
from datahelper import LegendIds
from datahelper import LegendData

PLATFORM_XBOX = 1
PLATFORM_PSN = 2
PLATFORM_PC = 5

class App:
    def __init__(self, title, width, height):
        self.window = tk.Tk()

        self.window.title(title)
        self.window.geometry(f"{width}x{height}")

        self.api_key = {"TRN-Api-Key": "????????-????-????-????-????????????"}
        self.platform = tk.IntVar()
        self.username = tk.StringVar()

        self.playerData = PlayerData()

        self.rawStatsDict = {}

        self.loadAuthenticationData()

        self.getNewStatsJsonFileFromApi()
        self.loadNewStatsFromFile()
        self.processRawStatsDictToPlayerData()


    def addWidgets(self):

        #---- ROW 0 ---------------

        get_api_key_label = tk.Label(self.window, text="Get your API key here : ")
        get_api_key_label.grid(column=0, row=0, columnspan=2, sticky="e")

        def clickedLink(event):
            webbrowser.open_new(r"https://apex.tracker.gg/site-api")

        hyperlink_label = tk.Label(self.window, text="https://apex.tracker.gg/site-api", foreground='#000080', cursor="hand2")
        hyperlink_label.bind("<Button-1>", clickedLink)
        hyperlink_label.grid(column=2, row=0, columnspan=4, sticky="w")

        api_key_label = tk.Label(text="API Key:")
        api_key_label.grid(column=6, row=0, columnspan=3)


        api_key_entry = tk.Entry(self.window)
        api_key_entry.grid(column=9, row=0, columnspan=2, sticky="w")

        def saveTypedAPIKey():
            self.api_key = {"TRN-Api-Key": api_key_entry.get()}
            current_api_key_label_text.set(f"Current API Key: {self.api_key['TRN-Api-Key']}")

        api_key_save_button = tk.Button(self.window, text="Save", command=saveTypedAPIKey, cursor="right_ptr")
        api_key_save_button.grid(column=11, row=0)
        
        current_api_key_label_text = tk.StringVar()
        current_api_key_label_text.set(f"Current API Key: {self.api_key['TRN-Api-Key']}")
        current_api_key_label = tk.Label(self.window, textvariable=current_api_key_label_text)
        current_api_key_label.grid(column=12, row=0, columnspan=8, sticky="W")
        current_api_key_label.grid_propagate(False)

        #---- /ROW 0 -------------------

        #---- ROW 1--------------------

        username_label = tk.Label(text="Username:")
        username_label.grid(column=6, row=1, columnspan=3, sticky="w")
        username_label.grid_propagate(False)
        
        username_entry = tk.Entry()
        username_entry.grid(column=9, row=1, columnspan=2)

        def saveTypedUsername():
            self.username = username_entry.get()
            current_username_label_text.set(f"Current Username: {self.username}")

        username_save_button = tk.Button(self.window, text="Save", command=saveTypedUsername, cursor="right_ptr")
        username_save_button.grid(column=11, row=1)

        current_username_label_text = tk.StringVar()
        current_username_label_text.set(f"Current Username: {self.username}")
        current_username_label = tk.Label(textvariable=current_username_label_text)
        current_username_label.grid(column=12, row=1, columnspan=5, sticky="w")

        xbox_radio_button = tk.Radiobutton(self.window, text="Xbox", variable=self.platform, value=PLATFORM_XBOX)
        xbox_radio_button.grid(column=0, row=1, sticky="w")

        psn_radio_button = tk.Radiobutton(self.window, text="PSN", variable=self.platform, value=PLATFORM_PSN)
        psn_radio_button.grid(column=1, row=1, sticky="w")

        pc_radio_button = tk.Radiobutton(self.window, text="PC", variable=self.platform, value=PLATFORM_PC)
        pc_radio_button.grid(column=2, row=1, sticky="w")

        def getNewStatsFromApi():
            self.getNewStatsJsonFileFromApi()
            self.saveAuthenticationData()
            self.loadNewStatsFromFile()
            self.processRawStatsDictToPlayerData()

            level_value_text.set(f"{self.playerData.level}")
            total_kills_value_text.set(f"{self.playerData.totalKills}")
            

        get_new_stats_from_api_button = tk.Button(self.window, text="Get New Stats", command=getNewStatsFromApi, cursor="right_ptr")
        get_new_stats_from_api_button.grid(column=3, row=1, sticky="w")
            
        #---- /ROW 1-------------------


        #---- ROW 2--------------------

        level_label = tk.Label(text="Level:")
        level_label.grid(column=0, row=2, sticky="w")

        level_value_text = tk.StringVar()
        level_value_text.set(f"{self.playerData.level}")
        level_value = tk.Label(textvariable=level_value_text)
        level_value.grid(column=1, row=2, sticky="w")

        #---- /ROW 2------------------

        #---- ROW 3-------------------
        total_kills_label= tk.Label(text="Total Kills:")
        total_kills_label.grid(column=0, row=3, sticky="w")

        total_kills_value_text = tk.StringVar()
        total_kills_value_text.set(f"{self.playerData.totalKills}")
        total_kills_value = tk.Label(textvariable=total_kills_value_text)
        total_kills_value.grid(column=1, row=3, sticky="w")

        #---- /ROW 3------------------

    def start(self):
        self.window.mainloop()


    def getNewStatsJsonFileFromApi(self):
        r = requests.get(f"https://public-api.tracker.gg/apex/v1/standard/profile/{self.platform}/{self.username}", headers=self.api_key)

        file = open("stats.json", "w")
        file.write(r.text)
        file.close()

    def loadNewStatsFromFile(self):
        file = open("stats.json", "r")
        stats = file.read()
    
        self.rawStatsDict = json.loads(stats)

    def processRawStatsDictToPlayerData(self):

        # update our level and totalKills
        for stat in self.rawStatsDict['data']['stats']:
            if stat['metadata']['key'] == "Level":
                self.playerData.level = stat['value']
            elif stat['metadata']['key'] == "Kills":
                self.playerData.totalKills = stat['value']
            else:
                pass

        # update our playerData.legendsData
        for legendData in self.playerData.legendsData:
            for child in self.rawStatsDict['data']['children']:
                if legendData.legendId.value == child['id']:
                    legendData.name = child['metadata']['legend_name']
                    for stat in child['stats']:
                        if stat['metadata']['key'] == "Kills":
                            legendData.kills = stat['value']


    def saveAuthenticationData(self):
        ApiAuthDict = {'api_key': self.api_key['TRN-Api-Key'], 'platform': self.platform, 'username': self.username}
        
        ApiAuthJson = json.dumps(ApiAuthDict)
        file = open("savedata.json", "w")
        file.write(ApiAuthJson)
        file.close()


    def loadAuthenticationData(self):
        ApiAuthDict = {}

        file = open("savedata.json", "r")
        savedata = file.read()
        ApiAuthDict = json.loads(savedata)

        self.api_key['TRN-Api-Key'] = ApiAuthDict['api_key']
        self.platform = ApiAuthDict['platform']
        self.username = ApiAuthDict['username']


