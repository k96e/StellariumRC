import requests

class Objects:
    def __init__(self, ip="127.0.0.1", port=8090, password=""):
        self.ip = ip
        self.port = port
        self.password = password
    
    def findObject(self, name):
        """
        Finds objects which match the search string str, which may contain greek/unicode 
        characters like in the SearchDialog. Returns a JSON String array of search matches.
        """
        r = requests.get(f"http://{self.ip}:{self.port}/api/objects/find",
                         params={"str":name},auth=("",self.password))
        try:
            return r.json()
        except requests.exceptions.JSONDecodeError:
            raise Exception(r.text)
    
    def getInfo(self, name=None, format="json"):
        """
        Returns an info string about the object identified by name in HTML or JSON format. 
        If no parameter name is given, the currently selected object is used.
        """
        params = {"format":format}
        if name is not None:
            params["name"] = name
        r = requests.get(f"http://{self.ip}:{self.port}/api/objects/info",
                         params=params,auth=("",self.password))
        if format == "json":
            try:
                return r.json()
            except requests.exceptions.JSONDecodeError:
                raise Exception(r.text)
        else:
            return r.text
        
    def listObjectTypes(self):
        """
        Returns all object types available in the internal catalogs as a JSON array of 
        objects of format.
        """
        r = requests.get(f"http://{self.ip}:{self.port}/api/objects/listobjecttypes"
                         ,auth=("",self.password))
        try:
            return r.json()
        except requests.exceptions.JSONDecodeError:
            raise Exception(r.text)
    
    def listObjectsByType(self, type, english=False):
        """
        Returns all objects of the specified type. If english is true, the english names 
        will be returned, otherwise the localized names will be returned. Returns a JSON 
        string array.
        """
        r = requests.get(f"http://{self.ip}:{self.port}/api/objects/listobjectsbytype",
                         params={"type":type,"english":1 if english else 0},
                         auth=("",self.password))
        try:
            return r.json()
        except requests.exceptions.JSONDecodeError:
            raise Exception(r.text)