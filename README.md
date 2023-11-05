# StellariumRC

### Control Stellarium by Python

## Installation
```bash
pip install stellariumrc
```

## Requirements
* python3
* requests

## Usage
Before starting, please make sure that Stellarium is running and the RemoteControl plugin is enabled.
```python
from stellariumrc import StellariumRC

s = StellariumRC() # you can pass the host, port and password (if any) as parameters
print(s.main.getStatus()) # get the current state of Stellarium
s.main.setFocus(target='moon',mode='zoom') # focus on moon and auto zoom-in
print(s.objects.getInfo('moon')) # get info about moon
```

For more API descriptions, please refer to the source code comments and Stellarium's [RemoteControl plugin HTTP API description](https://stellarium.org/doc/0.20/remoteControlApi.html).