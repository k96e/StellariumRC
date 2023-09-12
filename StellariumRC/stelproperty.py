import requests

class StelProperty:
    def __init__(self, ip="127.0.0.1", port=8090, password=""):
        self.ip = ip
        self.port = port
        self.password = password
        
    def listProperties(self):
        """
        Lists all registered StelProperties in JSON.
        """
        r = requests.get(f"http://{self.ip}:{self.port}/api/stelproperty/list",
                        auth=("",self.password))
        try:
           return r.json()
        except requests.exceptions.JSONDecodeError:
            raise Exception(r.text)
        
    def setProperty(self, id, value):
        """
        Sets the StelProperty identified by id to the value value. The value is converted 
        to the StelProperty type using QVariant logic, an error is returned if this is 
        somehow not possible.
        """
        r = requests.post(f"http://{self.ip}:{self.port}/api/stelproperty/set",
                         data={"id":id,"value":value},auth=("",self.password))
        if not r.text == 'ok':
            raise Exception(r.text)
        return r