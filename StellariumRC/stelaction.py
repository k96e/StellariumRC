import requests

class StelAction:
    def __init__(self, ip="127.0.0.1", port=8090, password=""):
        self.ip = ip
        self.port = port
        self.password = password
        
    def listActions(self):
        """
        Lists all registered StelActions in JSON.
        """
        r = requests.get(f"http://{self.ip}:{self.port}/api/stelaction/list",
                        auth=("",self.password))
        try:
            return r.json()
        except requests.exceptions.JSONDecodeError:
            raise Exception(r.text)
        
    def doAction(self, id):
        """
        Triggers or toggles the StelAction specified by id. If it was a boolean 
        action, returns the new state of the action.
        """
        r = requests.post(f"http://{self.ip}:{self.port}/api/stelaction/do",
                        data={"id":id},auth=("",self.password))
        if r.text in ['true','false']:
            return r.text == 'true'
        else:
            raise Exception(r.text)
        