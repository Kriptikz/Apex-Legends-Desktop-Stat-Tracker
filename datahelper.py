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
    def __init__(self, legendId):
        self.legendId = legendId
        self.name = ""
        self.kills = 0  


class PlayerData:
    def __init__(self):
        self.level = 1
        self.totalKills = 0

        self.legendsData = []

        self.legendsData.append(LegendData(LegendIds.WRAITH))
        self.legendsData.append(LegendData(LegendIds.BANGALORE))
        self.legendsData.append(LegendData(LegendIds.CAUSTIC))
        self.legendsData.append(LegendData(LegendIds.MIRAGE))
        self.legendsData.append(LegendData(LegendIds.BLOODHOUND))
        self.legendsData.append(LegendData(LegendIds.GIBRALTAR))
        self.legendsData.append(LegendData(LegendIds.LIFELINE))
        self.legendsData.append(LegendData(LegendIds.PATHFINDER))


