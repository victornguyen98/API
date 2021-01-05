
import json
a={"header": {"generatedOn": 1609141035741}, "data": [{"name": "vSmart", "count": 1, "detailsURL": "/dataservice/device/reachable?personality=vsmart", "status": "error", "statusList": [{"name": "vSmart", "status": "error", "message": "Number of devices down", "detailsURL": "/dataservice/device/unreachable?personality=vsmart", "count": 0}]}, {"name": "WAN Edge", "count": 4, "detailsURL": "/dataservice/device/reachable?personality=vedge", "status": "error", "statusList": [{"name": "vEdge", "status": "error", "message": "Number of devices down", "detailsURL": "/dataservice/device/unreachable?personality=vedge", "count": 0}]}, {"name": "vBond", "count": 1, "detailsURL": "/dataservice/device/reachable?personality=vbond", "status": "error", "statusList": [{"name": "vBond", "status": "error", "message": "Number of devices down", "detailsURL": "/dataservice/device/unreachable?personality=vbond", "count": 0}]}]}

print(a["data"][1])
#print(a["data"][1]["name"])