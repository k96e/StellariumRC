import requests

class Scripts:
    def __init__(self, ip="127.0.0.1", port=8090, password=""):
        self.ip = ip
        self.port = port
        self.password = password
        
    def listScripts(self):
        """
        Lists all known script files, as a JSON string array.
        """
        r = requests.get(f"http://{self.ip}:{self.port}/api/scripts/list",
                         auth=("",self.password))
        try:
            return r.json()
        except requests.exceptions.JSONDecodeError:
            raise Exception(r.text)
        
    def getInfo(self, id, html=False):
        """
        Returns information about the script identified by id. If the parameter html is true, 
        the info is formatted using StelScriptMgr::getHtmlDescription and suitable for inclusion 
        into an iframe element, otherwise this operation returns a JSON object.
        """
        params = {"id":id}
        if html:
            params["html"] = 1
        r = requests.get(f"http://{self.ip}:{self.port}/api/scripts/info",
                         params=params,auth=("",self.password))
        try:
            if not html:
                return r.json()
            else:
                return r.text
        except requests.exceptions.JSONDecodeError:
            raise Exception(r.text)
        
    def getStatus(self):
        """
        Returns the current script status as a JSON object.
        """
        r = requests.get(f"http://{self.ip}:{self.port}/api/scripts/status"
                         ,auth=("",self.password))
        try:
            return r.json()
        except requests.exceptions.JSONDecodeError:
            raise Exception(r.text)
        
    def runScript(self, id):
        """
        Runs the script with the given id. Will fail if a script is currently running.
        """
        r = requests.post(f"http://{self.ip}:{self.port}/api/scripts/run",
                         data={"id":id},auth=("",self.password))
        if not r.text == 'ok':
            raise Exception(r.text)
        return r
    
    def executeCode(self, code, useIncludes=False):
        """
        Directly executes the given script code. If useIncludes is given and evaluates to true, 
        the standard include folder will be used. Script execution will fail if a script is 
        already running.
        """
        r = requests.post(f"http://{self.ip}:{self.port}/api/scripts/direct",
                         data={"code":code,"useIncludes":useIncludes},
                         auth=("",self.password))
        if not r.text == 'ok':
            raise Exception(r.text)
        return r
    
    def stopScript(self):
        """
        Stops the execution of a running script.
        """
        r = requests.post(f"http://{self.ip}:{self.port}/api/scripts/stop",
                          auth=("",self.password))
        if not r.text == 'ok':
            raise Exception(r.text)
        return r