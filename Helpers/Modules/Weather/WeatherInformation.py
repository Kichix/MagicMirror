import xml.etree.ElementTree as ET
import datetime

class WeatherInfo:

    currentInfo = {}
    weekdays = {}
    tree = ET.parse('C:\Python\MagicMirror\TestWeather.xml')
    XMLroot = tree.getroot()

    def __init__(self):

        """initiate dictionaries"""
        self.currentInfo = {
        "Day" : " ",
        "Weather" : 0,
        "Temp" : 0,
        "Rain" : 0,
        "minTemp" : 0,
        "maxTemp" : 0
        }

        self.weekdays = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"
        }

        """update values"""
        self.updateXML();
        self.updateVariables();


    def updateVariables(self):
        """initiate current time and dictionary for quick access"""
        curTime = datetime.datetime.now()
        curTimeDic = {"Day": curTime.day,
                      "Hour": curTime.hour,
                      "Weekday": int(curTime.weekday())}

        """Search through XML to set the variables"""
        for curCur in self.XMLroot:
            if curCur.tag == "forecast":
                for subCurCur in curCur:
                    """Check if entry is in current time"""
                    if (int(subCurCur.get("from")[8:10]) == int(curTimeDic["Day"]) and
                        int(subCurCur.get("to")[8:10]) == int(curTimeDic["Day"]) and
                        int(subCurCur.get("from")[11:13]) <= int(curTimeDic["Hour"]) < int(subCurCur.get('to')[11:13])):

                        self.currentInfo["Temp"] = int(round(float(subCurCur.find("temperature").get("value")),0))

        self.currentInfo["Day"] = self.weekdays[curTimeDic["Weekday"]]

    def updateXML(self):
        self.tree = ET.parse('C:\Python\MagicMirror\TestWeather.xml')
        self.XMLroot = self.tree.getroot()

info = WeatherInfo()
print (info.currentInfo["Day"], info.currentInfo["Temp"])