import requests
import json
requests.packages.urllib3.disable_warnings()
from requests.packages.urllib3.exceptions import InsecureRequestWarning

url = "https://10.10.20.90:8443/dataservice/alarms"

payload={"query":{"condition":"AND","rules":[{"value":["12"],"field":"entry_time","type":"date","operator":"last_n_hours"}]},"size":10000}
payload = json.dumps(payload)
headers = {
  'X-XSRF-TOKEN': '72075D2D30632D0572AEA130C3CD5AC007822035D658B63492F5F6EC5CD1DE58DE957E19563B5F86979B9041F1E6298BFDC8',
  'Content-Type': 'application/json',
  'Cookie': 'JSESSIONID=yUGoAAMzbzF0G4jO5UncuhfdFho1-YirecLTRmkC.81ac6722-a226-4411-9d5d-45c0ca7d567b'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)
