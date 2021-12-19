
from bods_client.client import BODSClient
from bods_client.models import BoundingBox, SIRIVMParams
from lxml import etree

# An API key can be obtained by registering with the Bus Open Data Service
# https://data.bus-data.dft.gov.uk/account/signup/
API_KEY = "902f5e802a39291a2fc1decc6a1e1f2d78759e7d"

bods = BODSClient(api_key=API_KEY)
box = BoundingBox(min_longitude=-2.05838, min_latitude=52.629434, max_longitude=-2.603121, max_latitude=52.842295)
params = SIRIVMParams(bounding_box=box)
siri = bods.get_siri_vm_data_feed(params=params)
xml = etree.parse(siri)

# -2.603121	52.629434	-2.05838	52.842295