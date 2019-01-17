# python-brihome

[![PyPI version](https://badge.fury.io/py/python-brihome.svg)](https://badge.fury.io/py/python-brihome)

This library aims to control the brihome smart light bulbs.
It internally uses the pytuya library and is able to control
many parameters on the led bulb.

install via

`pip install python-brihome`

Actually the briihome is part of a family of ESP8266MOD low cost 
WiFi smart devices from Shenzhen Xenon. These bulbs are sold under
different names. If your bulb was around 10-20€, and port `6668` is open
chances are good you can control it with this library.

### Docs
For an example see [examples](examples/rgb.py).

### FAQ
In Order to use the `brihome.Bulb(...)` constructor you need
to obtain the **local device id** and the **device key** that 
your bulb uses. You can find these by sniffing the brihome app's 
traffic. Refer to [this document](https://github.com/clach04/python-tuya/) 
to obtain valid device id and device key.

### Contributing
Pull request are welcome. Not every function the bulb supports are
implemented. Help on error handling and extended functionality
is welcome.
