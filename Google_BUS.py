
from bods_client.client import BODSClient
from bods_client.models import BoundingBox, GTFSRTParams

# An API key can be obtained by registering with the Bus Open Data Service
# https://data.bus-data.dft.gov.uk/account/signup/
API_KEY = "902f5e802a39291a2fc1decc6a1e1f2d78759e7d"

bods = BODSClient(api_key=API_KEY)
box = BoundingBox(min_longitude=-0.54, min_latitude=51.26, max_longitude=0.27, max_latitude=51.75)
params = GTFSRTParams(bounding_box=box)
message = bods.get_gtfs_rt_data_feed(params=params)
message.entity[0]
id: "421354378097713049"

