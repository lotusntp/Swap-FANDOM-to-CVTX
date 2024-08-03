
import requests


class Legacy:


    BASE_URL = 'https://api.carrieverse.io'
    HEADER = None
    def __init__(self,uid,account):
        
        self.HEADER = {
            'uid':uid,
            'Account': account
        }

    def get(self,url):
        response = requests.get(self.BASE_URL + url, headers=self.HEADER)
        if response.status_code == 200:
            return response.json()
        else:
            
            print(f"Error: {response.status_code} Data: {response.json()}")
            return None
        

    def gas_fast(self):
        response = requests.get('https://gpoly.blockscan.com/gasapi.ashx?apikey=key&method=gasoracle')
        if response.status_code == 200:
            return response.json()
        else:
            
            print(f"Error: {response.status_code} Data: {response.json()}")
            return None
        
    def post(self,url,body):
        response = requests.post(self.BASE_URL + url, headers=self.HEADER, json=body)
        if response.status_code == 200:
            return response.json()
        else:
            
            print("Error:", response.status_code)
            return None
