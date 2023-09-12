from . import main,objects,scripts,simbad,stelaction,stelproperty,location

class Stellarium:
    def __init__(self, ip="127.0.0.1", port=8090, password="") -> None:
        self.password = password
        self.ip = ip
        self.port = port
        self.main = main.Main(self.ip, self.port, self.password)
        self.objects = objects.Objects(self.ip, self.port, self.password)
        self.scripts = scripts.Scripts(self.ip, self.port, self.password)
        self.simbad = simbad.Simbad(self.ip, self.port, self.password)
        self.stelaction = stelaction.StelAction(self.ip, self.port, self.password)
        self.stelproperty = stelproperty.StelProperty(self.ip, self.port, self.password)
        self.location = location.Location(self.ip, self.port, self.password)