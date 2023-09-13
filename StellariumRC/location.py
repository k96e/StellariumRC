import requests

class Location:
    def __init__(self, ip="127.0.0.1", port=8090, password=""):
        self.ip = ip
        self.port = port
        self.password = password
    
    def listLocations(self):
        """
        Returns the list of all stored location IDs (keys of StelLocationMgr::getAllMap) 
        as JSON string array.
        """
        r = requests.get(f"http://{self.ip}:{self.port}/api/location/list",
                         auth=("",self.password))
        try:
            return r.json()
        except requests.exceptions.JSONDecodeError:
            raise Exception(r.text)
        
    def listCountries(self):
        """
        Returns the list of all known countries (StelLocaleMgr::getAllCountryNames), as a 
        JSON array of objects of format.
        """
        r = requests.get(f"http://{self.ip}:{self.port}/api/location/countrylist",
                         auth=("",self.password))
        try:
            return r.json()
        except requests.exceptions.JSONDecodeError:
            raise Exception(r.text)
        
    def listPlanets(self):
        """
        Returns the list of all solar system planet names (SolarSystem::getAllPlanetEnglishNames), 
        as a JSON array of objects of format
        """
        r = requests.get(f"http://{self.ip}:{self.port}/api/location/planetlist",
                         auth=("",self.password))
        try:
            return r.json()
        except requests.exceptions.JSONDecodeError:
            raise Exception(r.text)
        
    def planetImage(self,planet):
        """
        Returns the planet texture image for the planet (english name)
        """
        r = requests.get(f"http://{self.ip}:{self.port}/api/location/planetimage",
                         params={"planet":planet},auth=("",self.password))
        if r.status_code == 200:
            return r.content
        else:
            raise Exception(r.text)
        
    def setLocation(self, id=None,latitude=None,longitude=None,
                    altitude=None,name=None,country=None,planet=None):
        """
        Changes and moves to a new location. If id is given, all other parameters are ignored,
        and a location is searched from the named locations using StelLocationMgr::locationForString 
        with the id. Else, the other parameters change the specific field of the current StelLocation.
        """
        params={}
        if not id == None:
            params["id"] = id
        else:
            if not latitude == None: params["latitude"] = latitude
            if not longitude == None: params["longitude"] = longitude
            if not altitude == None: params["altitude"] = altitude
            if not name == None: params["name"] = name
            if not country == None: params["country"] = country
            if not planet == None: params["planet"] = planet
        r = requests.post(f"http://{self.ip}:{self.port}/api/location/setlocationfields",
                         params=params,auth=("",self.password))
        if r.status_code == 200:
            return r.text
        else:
            raise Exception(r.text)
