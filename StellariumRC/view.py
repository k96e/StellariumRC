import requests

class View:
    def __init__(self, ip="127.0.0.1", port=8090, password=""):
        self.ip = ip
        self.port = port
        self.password = password
    
    def listLandscape(self):
        """
        Lists the installed landscapes as JSON.
        """
        r = requests.get(f"http://{self.ip}:{self.port}/api/view/listlandscape",
                         auth=("",self.password))
        try:
            return r.json()
        except requests.exceptions.JSONDecodeError:
            raise Exception(r.text)
        
    def landscapeDesciption(self,path):
        """
        Provides virtual filesystem access to the current landscape directory. The operation 
        can take a longer path in the URL. The remainder is used to access files in the landscape 
        directory. If no longer path is given, the current HTML landscape description (as per 
        LandscapeMgr::getCurrentLandscapeHtmlDescription) is returned. An example: 
        landscapeDesciption("image.png") returns image.png from the current landscape directory.
        This operation allows to set up an HTML iframe or similar for the landscape description, 
        including all images, etc. embedded in the HTML description.
        """
        r = requests.get(f"http://{self.ip}:{self.port}/api/view/landscapedescription/{path}",
                         auth=("",self.password))
        if r.status_code == 200:
            return r.content
        else:
            raise Exception(r.text)
        
    def listSkyculture(self):
        """
        Lists the installed sky cultures as JSON.
        """
        r = requests.get(f"http://{self.ip}:{self.port}/api/view/listskyculture",
                         auth=("",self.password))
        try:
            return r.json()
        except requests.exceptions.JSONDecodeError:
            raise Exception(r.text)
        
    def skycultureDescription(self,path):
        """
        Provides virtual filesystem access to the current skyculture directory. The operation 
        can take a longer path in the URL. The remainder is used to access files in the skyculture 
        directory. If no longer path is given, the current HTML skyculture description (as per 
        StelSkyCultureMgr::getCurrentSkyCultureHtmlDescription) is returned. An example: 
        skycultureDescription("image.png") returns image.png from the current skyculture directory.
        This operation allows to set up an HTML iframe or similar for the skycultures description, 
        including all images, etc. embedded in the HTML description.
        """
        r = requests.get(f"http://{self.ip}:{self.port}/api/view/skyculturedescription/{path}",
                         auth=("",self.password))
        if r.status_code == 200:
            return r.content
        else:
            raise Exception(r.text)
        
    def listProjection(self):
        """
        Lists the available projection types as JSON.
        """
        r = requests.get(f"http://{self.ip}:{self.port}/api/view/listprojection",
                         auth=("",self.password))
        try:
            return r.json()
        except requests.exceptions.JSONDecodeError:
            raise Exception(r.text)
        
    def projectionDescription(self):
        """
        Returns the HTML description of the current projection (StelProjector::getHtmlSummary)
        """
        r = requests.get(f"http://{self.ip}:{self.port}/api/view/projectiondescription",
                         auth=("",self.password))
        if r.status_code == 200:
            return r.content
        else:
            raise Exception(r.text)
