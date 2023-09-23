import requests

class LocationSearch:
    def __init__(self, ip="127.0.0.1", port=8090, password=""):
        self.ip = ip
        self.port = port
        self.password = password
    
    def search(self,term):
        """
        Searches the term in the list of predefined locations of the StelLocationMgr, and 
        returns a JSON string array of the results.
        """
        r = requests.get(f"http://{self.ip}:{self.port}/api/locationsearch/search",
                         params={"term":term},auth=("",self.password))
        try:
            return r.json()
        except requests.exceptions.JSONDecodeError:
            raise Exception(r.text)
        
    def nearby(self,planet,latitude,longitude,radius):
        """
        Searches near the location defined by planet, latitude and longitude for predefined 
        locations (inside the given radius) using StelLocationMgr::pickLocationsNearby, 
        returns a JSON string array.
        """
        r = requests.get(f"http://{self.ip}:{self.port}/api/locationsearch/nearby",
                         params={"planet":planet,"latitude":latitude,
                                 "longitude":longitude,"radius":radius},
                         auth=("",self.password))
        try:
            return r.json()
        except requests.exceptions.JSONDecodeError:
            raise Exception(r.text)
        