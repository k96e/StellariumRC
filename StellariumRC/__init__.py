from . import main,objects,scripts

class Stellarium:
    def __init__(self, ip="127.0.0.1", port=8090) -> None:
        self.ip = ip
        self.port = port
        self.main = main.Main(self.ip, self.port)
        self.objects = objects.Objects(self.ip, self.port)
        self.scripts = scripts.Scripts(self.ip, self.port)