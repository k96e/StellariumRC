import requests

class Main:
    def __init__(self, ip="127.0.0.1", port=8090):
        self.ip = ip
        self.port = port

    def getStatus(self):
        r = requests.get(f"http://{self.ip}:{self.port}/api/main/status")
        try:
            return r.json()
        except requests.exceptions.JSONDecodeError:
            raise Exception(r.text)

    def getPlugins(self):
        r = requests.get(f"http://{self.ip}:{self.port}/api/main/plugins")
        try:
            return r.json()
        except requests.exceptions.JSONDecodeError:
            raise Exception(r.text)

    def getView(self,coord=None,ref=None):
        """
        Returns the current view direction as JSON.
        Without the optional coord, all versions are returned, including j2000, jNow and altAz. The returned 
        values are 3D vectors.
        For the vector in altAz system, the actually returned values are based on an azimuth Az' counted 
        from South (x=1) towards East (y=1), Az'=180-Az.
        If the optional parameter ref is given, it governs refraction setting and it applies to the jNow 
        output only. "On" applies refraction, "off" does not apply, and "auto" (or any other value) applies 
        it when atmosphere setting is active.
        """
        params = {}
        if coord is not None:
            params["coord"] = coord
        if ref is not None:
            params["ref"] = ref
        r = requests.get(f"http://{self.ip}:{self.port}/api/main/view", params=params)
        try:
            return r.json()
        except requests.exceptions.JSONDecodeError:
            raise Exception(r.text)

    def setTimeJD(self,time):
        """
        Sets the current Stellarium simulation time. The time parameter defines the current time (Julian day) 
        as passed to StelCore::setJD.
        """
        r = requests.post(f"http://{self.ip}:{self.port}/api/main/time", data={"time":time})
        return r

    def setTimeRateJD(self,timeRate):
        """
        Sets the current Stellarium simulation timerate.The timerate parameter allows to change the speed at 
        which the simulation time moves (in JDay/sec) as passed to StelCore::setTimeRate.
        """
        r = requests.post(f"http://{self.ip}:{self.port}/api/main/time", data={"timerate":timeRate})
        return r
    
    def setTime(self,dt):
        """
        Sets the current Stellarium simulation time. The dt parameter defines the current time as a datetime
        object in Python standard library.
        """
        jd = dt.timestamp() / 86400.0 + 2440587.5
        r = requests.post(f"http://{self.ip}:{self.port}/api/main/time", data={"time":jd})
        return r

    def setTimeRate(self,timeRate):
        """
        Sets the current Stellarium simulation timerate.The timerate parameter allows to change the speed at
        which the simulation time moves (in seconds per second). Negative timerates are also allowed, which 
        means that time moves backwards.
        """
        r = requests.post(f"http://{self.ip}:{self.port}/api/main/time", data={"timerate":timeRate})
        return r
    
    def setFocus(self,target=None,position=None,mode=None):
        """
        Sets the current app focus/selection. 
        If no parameters are given, the current selection is cleared. 
        If the target parameter was given, the object to be selected is looked up by name (first the localized 
        name is tried, then the english name). 
        If the optional mode parameter is given, it determines how to change the view. The default is 'center' 
        which selects the object and moves it into the view's center. If it is set to 'zoom', it automatically 
        zooms in on the object (StelMovementMgr::autoZoomIn) on selection and automatically zooms out when the 
        selection is cleared. If it is set to 'mark', the selection is just marked, but no view adjustment is done. 
        If the position parameter is used, it is interpreted as a coordinate in the J2000 frame, and focused 
        using StelMovementMgr::moveToJ2000. The mode parameter has no effect here. The target parameter takes 
        precendence over the position parameter, if both are given.
        """
        params = {}
        if target is not None:
            params["target"] = target
        if position is not None:
            params["position"] = position
        if mode is not None:
            params["mode"] = mode
        r = requests.post(f"http://{self.ip}:{self.port}/api/main/focus", data=params)
        return r
    
    def setMove(self,x,y):
        """
        Allows viewport movement, like using the arrow keys in the main program.This operation defines the intended 
        move direction. x and y define the intended move speed in azimuth and altitude (i.e. a negative x means 
        left).
        """
        r = requests.post(f"http://{self.ip}:{self.port}/api/main/move", data={"x":x,"y":y})
        return r
        
    def setView(self,coord=None,vec=None,az=None,alt=None,ref="auto"):
        """
        Sets the view direction.When the coord parameter is given, it defines the coordinate system to use for 
        vec parameter. The possible values are j2000, jNow and altAz. 
        An optional parameter ref governs refraction mode, default auto.
        If the coord and vec parameters are not given, the az and alt parameters are used to define the view 
        in altitude/azimuth spherical coordinates/angles.
        """
        params = {}
        if coord is not None and vec is not None:
            if not coord in ["j2000","jNow","altAz"]:
                raise ValueError("coord must be j2000, jNow or altAz.")
            params[coord] = str(vec)
            params["ref"] = ref
        elif az is not None and alt is not None:
            params["az"] = az
            params["alt"] = alt
        else:
            raise ValueError("Either coord and vec or az and alt must be given.")
        r = requests.post(f"http://{self.ip}:{self.port}/api/main/view", data=params)
        return r
    
    def setFov(self,fov):
        """
        Sets the current field of view using StelCore::setFov.
        """
        r = requests.post(f"http://{self.ip}:{self.port}/api/main/fov", data={"fov":fov})
        return r