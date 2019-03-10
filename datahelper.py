from enum import Enum

class LegendIds(Enum):
    NONE = ""
    WRAITH = "legend_1"
    BANGALORE = "legend_2"
    CAUSTIC = "legend_3"
    MIRAGE = "legend_4"
    BLOODHOUND = "legend_5"
    GIBRALTAR = "legend_6"
    LIFELINE = "legend_7"
    PATHFINDER = "legend_8"


class LegendData:
    def __init__(self, legendId, name):
        self.legendId = legendId
        self.name = name
        self.kills = 0  


class PlayerData:
    def __init__(self):
        self.level = 1

        self.legendsData = []

        self.legendsData.append(LegendData(LegendIds.WRAITH, "Wraith"))
        self.legendsData.append(LegendData(LegendIds.BANGALORE, "Bangalore"))
        self.legendsData.append(LegendData(LegendIds.CAUSTIC, "Caustic"))
        self.legendsData.append(LegendData(LegendIds.MIRAGE, "Mirage"))
        self.legendsData.append(LegendData(LegendIds.BLOODHOUND, "Bloodhound"))
        self.legendsData.append(LegendData(LegendIds.GIBRALTAR, "Gibraltar"))
        self.legendsData.append(LegendData(LegendIds.LIFELINE, "Lifeline"))
        self.legendsData.append(LegendData(LegendIds.PATHFINDER, "Pathfinder"))

    def updateLegendKills(self, legendId, newKills):
        for legend in self.legendsData:
            if legend.legendId == legendId:
                legend.kills = newKills

    #def updateAllData(self, newData):
