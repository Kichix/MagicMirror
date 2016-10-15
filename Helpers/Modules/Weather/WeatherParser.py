import xml.etree.ElementTree as ET
from time import gmtime, strftime
import datetime

tree = ET.parse('C:\Python\MagicMirror\TestWeather.xml')
XMLroot = tree.getroot()

ss = datetime.datetime.now() + datetime.timedelta(hours=3)
s = ss.hour
print(s)