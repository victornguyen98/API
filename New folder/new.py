import requests
import json
requests.packages.urllib3.disable_warnings()
from requests.packages.urllib3.exceptions import InsecureRequestWarning


SDWAN_IP = "10.10.20.90"
SDWAN_USERNAME = "admin"
SDWAN_PASSWORD = "C1sco12345"    


class rest_api_lib:
    def __init__(self, vmanage_ip, username, password):
        self.vmanage_ip = vmanage_ip
        self.session = {}
        self.login(self.vmanage_ip, username, password)

    def login(self, vmanage_ip, username, password):       
        #GET SESSION 
        base_url_str = 'https://%s:8443/'%vmanage_ip
        login_action = 'j_security_check'        
        login_data = {'j_username' : username, 'j_password' : password}
        login_url = base_url_str + login_action
        url = base_url_str + login_url
        response = requests.post(url=login_url, data = login_data,verify=False)
        try:
            cookies = response.headers["Set-Cookie"]
            jsessionid = cookies.split(";")
            return(jsessionid[0])
        except:
            print(response.text)

    def get_token(self, vmanage_ip, jsessionid):
        #GET TOKEN
        headers = {'Cookie': jsessionid}
        base_url_str = 'https://%s:8443/'%vmanage_ip
        api = "dataservice/client/token"
        url = base_url_str + api
       
        response = requests.get(url = url, headers=headers,verify=False)
        if response.status_code == 200:
            
            return(response.text)
        else:
            return None
    

    
Sdwan = rest_api_lib(SDWAN_IP, SDWAN_USERNAME, SDWAN_PASSWORD)
jsessionid = Sdwan.login(SDWAN_IP, SDWAN_USERNAME, SDWAN_PASSWORD)
token = Sdwan.get_token(SDWAN_IP, jsessionid)

'''
def Tunnel():
    #Function POST
    try:
        headers ={'Cookie': jsessionid, 'X-XSRF-TOKEN':token, 'Content-Type': 'application/json'}
        payload = {"query":{"condition":"AND","rules":[{"value":["24"],"field":"entry_time","type":"date","operator":"last_n_hours"},{"value":["100"],"field":"loss_percentage","type":"number","operator":"less"},{"value":["10.10.1.15"],"field":"vdevice_name","type":"string","operator":"in"}]},"aggregation":{"field":[{"property":"local_color","order":"asc","sequence":1}],"metrics":[{"property":"loss_percentage","type":"avg"},{"property":"latency","type":"avg"},{"property":"jitter","type":"avg"}]}}
        payload = json.dumps(payload) 
        url = 'https://%s:8443/dataservice/'%SDWAN_IP
        api = 'statistics/approute/aggregation'
        url = url + api        
        resp = requests.post(url, headers=headers, data=payload, verify=False)      
        resp_json = resp.json()
        data = json.dumps(resp_json)
        
        print(data)
    except:
        print("Wrong")
       

Tunnel()'''


'''def alarms():
    
    #Function POST
    try:
        headers ={'Cookie': jsessionid, 'X-XSRF-TOKEN':token, 'Content-Type': 'application/json'}
        payload = {"query":{"condition":"AND","rules":[{"value":["12"],"field":"entry_time","type":"date","operator":"last_n_hours"}]},"size":10000}
        payload = json.dumps(payload) 
        url = 'https://%s:8443/dataservice/'%SDWAN_IP
        api = 'alarms'
        url = url + api        
        resp = requests.post(url, headers=headers, data=payload, verify=False)      
        resp_json = resp.json()
        data = json.dumps(resp_json)
        
        print(data)
    except:
        print("Wrong")
       

alarms()'''


'''def event():
    try:
        headers ={'Cookie': jsessionid, 'X-XSRF-TOKEN':token, 'Content-Type': 'application/json'}
        payload = {"query":{"condition":"AND","rules":[{"value":["168"],"field":"entry_time","type":"date","operator":"last_n_hours"}]},"size":10000}
        payload = json.dumps(payload) 
        url = 'https://%s:8443/dataservice/'%SDWAN_IP
        api = 'event'
        url = url + api        
        resp = requests.post(url, headers=headers, data=payload, verify=False)      
        resp_json = resp.json()
        data = json.dumps(resp_json)
        
        print(data)
    except:
        print("Wrong")


event()'''

'''def tloc():
     try:
        api  = 'statistics/approute/aggregation'
        headers ={'Cookie': jsessionid, 'X-XSRF-TOKEN':token, 'Content-Type': 'application/json'}
        payload = {"query":{"condition":"AND","rules":[{"value":["24"],"field":"entry_time","type":"date","operator":"last_n_hours"},{"value":["100"],"field":"loss_percentage","type":"number","operator":"less"},{"value":["10.10.1.15"],"field":"vdevice_name","type":"string","operator":"in"}]},"aggregation":{"field":[{"property":"local_color","order":"asc","sequence":1}],"metrics":[{"property":"loss_percentage","type":"avg"},{"property":"latency","type":"avg"},{"property":"jitter","type":"avg"}]}}
        payload = json.dumps(payload) 
        url = 'https://%s:8443/dataservice/'%SDWAN_IP        
        url = url + api        
        resp = requests.post(url, headers=headers, data=payload, verify=False)      
        resp_json = resp.json()
        data = json.dumps(resp_json)
        print(data)'''
   

def reboot_History():
    
        headers ={'Cookie': jsessionid, 'X-XSRF-TOKEN':token, 'Content-Type': 'application/json'}
        '''payload = {"action":"install","input":{"vEdgeVPN":0,"vSmartVPN":0,"data":[{"family":"csr1000v","version":"16.12.1e.0.66.1572418900"}],"versionType":"vmanage","reboot":False,"sync":True},"devices":[{"deviceIP":"10.10.1.15","deviceId":"CSR-DE6DAB19-BA1A-E543-959C-FD117F4A6205"}],"deviceType":"vedge"}       
        payload = json.dumps(payload) '''
        url = 'https://%s:8443/dataservice/'%SDWAN_IP
        api = 'template/config/running/CSR-807E37A3-537A-07BA-BD71-8FB76DE9DC38'
        url = url + api        
        resp = requests.post(url, headers=headers,  verify=False)      
        resp_json = resp.json()
        print(resp_json)
    

reboot_History()





