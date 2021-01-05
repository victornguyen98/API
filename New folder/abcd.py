import requests
import sys
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
        """Login to vmanage"""
        base_url_str = 'https://%s:8443/'%vmanage_ip

        login_action = 'j_security_check'

        #Format data for loginForm
        login_data = {'j_username' : username, 'j_password' : password}

        #Url for posting login data
        login_url = base_url_str + login_action
        url = base_url_str + login_url
        #print(url)
        sess = requests.session()
        #If the vmanage has a certificate signed by a trusted authority change verify to True
        login_response = sess.post(url=login_url, data=login_data, verify=False)
        
        if b'<html>' in login_response.content:
            print ("Login Failed")
            sys.exit(0)

        self.session[vmanage_ip] = sess
        print(sess)
    def get_request(self, api):
        """GET request"""
        url = "https://%s:8443/dataservice/%s"%(self.vmanage_ip, api)
        #print(url)
        response = self.session[self.vmanage_ip].get(url, verify=False)
        
        return response

    def post_request(self, api, payload, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}):
        """POST request"""
        url = "https://%s:8443/dataservice/%s"%(self.vmanage_ip, api)
        
        payload = json.dumps(payload)
        #print(url)
        #print (payload)

        response = self.session[self.vmanage_ip].post(url=url, data=payload, headers=headers, verify=False)
        print(response)
        data = response.json()
        return data

Sdwan = rest_api_lib(SDWAN_IP, SDWAN_USERNAME, SDWAN_PASSWORD)


def network_device_list():
    try:
        resp = Sdwan.get_request(api = "network/connectionssummary")        
        resp_json = resp.json()
        data = json.dumps(resp_json)
        print(data)
       

network_device_list()








{"header":{"generatedOn":1609037377409},"data":{"connectURL":"/shell/0041200b-6636-4ca4-ae0b-ce8c96f03890","destroyURL":"dataservice/newssh/disconnect/0041200b-6636-4ca4-ae0b-ce8c96f03890","sessionId":"0041200b-6636-4ca4-ae0b-ce8c96f03890","remoteVMSessionId":"73521911-5ef9-4ba8-bc5e-6cd9eb183108","deviceId":"10.10.1.17","uuid":"0140a336-5fd5-9829-10d2-f6ba0b177efd","requestjSessionId":"ZrP9lUp73CttX-h-yHkE0d1Mm3D2S837vn1DBsFo"}}

{"header":{"generatedOn":1609037745986},"data":{"connectURL":"/shell/1b271165-f63c-4e4e-b83a-11e048c9e443","destroyURL":"dataservice/newssh/disconnect/1b271165-f63c-4e4e-b83a-11e048c9e443","sessionId":"1b271165-f63c-4e4e-b83a-11e048c9e443","remoteVMSessionId":"9111be3e-b8d4-4941-9fb0-5530eb34077e","deviceId":"10.10.1.13","uuid":"CSR-807E37A3-537A-07BA-BD71-8FB76DE9DC38","requestjSessionId":"ZrP9lUp73CttX-h-yHkE0d1Mm3D2S837vn1DBsFo"}}
{"header":{"generatedOn":1609037745986},"data":{"connectURL":"/shell/1b271165-f63c-4e4e-b83a-11e048c9e443","destroyURL":"dataservice/newssh/disconnect/1b271165-f63c-4e4e-b83a-11e048c9e443","sessionId":"1b271165-f63c-4e4e-b83a-11e048c9e443","remoteVMSessionId":"9111be3e-b8d4-4941-9fb0-5530eb34077e","deviceId":"10.10.1.13","uuid":"CSR-807E37A3-537A-07BA-BD71-8FB76DE9DC38","requestjSessionId":"ZrP9lUp73CttX-h-yHkE0d1Mm3D2S837vn1DBsFo"}}
{"session":"Z7K7Yr6Y1LRkcTCbBcc1bQ","data":"\r\nsite1-cedge01#show ip route "}