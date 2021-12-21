import requests
# from xml.dom import minidom as md
import xml.etree.ElementTree as ET


from requests.models import Response

url = "https://data.bus-data.dft.gov.uk/api/v1/datafeed"
API_Key = "?api_key=902f5e802a39291a2fc1decc6a1e1f2d78759e7d"
bounding_box = "&boundingBox=-2.603121%2C52.629434%2C-2.05838%2C52.842295"
line_ref = "&lineRef=5"
complete_url = url + API_Key + bounding_box + line_ref
# print (complete_url)

response = requests.get(complete_url)
print(response)
data_text = response.text







