import time
import math
import pytuya

class Bulb:

	def __init__(self, id, address, key):
		"""
		Create a new bulb. Needs id, address and key of the bulb.
		See the docs to find out how to optaim them
		"""
		self.d = pytuya.Device(id, address, key, "device")
		
	def status(self): 
		"""
		Return the status of the led bulb. Containing local id and dps.
		"""
		return self.d.status()

	def dps(self):
		"""
		Returns the status registers of the bulb.
		"""
		try: return self.d.status()	
		except: return {}

	def white_mode(self):
		"""
		Sets the lamp to white mode.
		"""
		self.d.set_status('white', 2)	

	def scene_mode(self, i):
		"""
		Sets the lamp to scene mode.
		"""
		self.d.set_status('scene_%s' % i, 2)		

	def turn_on(self):
		"""
		Turn the light off.
		"""
		self.d.set_status(True, 1)

	def turn_off(self):
		"""
		Turn the light off.
		"""
		self.d.set_status(False, 1)		

	def warm(self,a):
		"""
		Set the white warm led.
		"""
		self.d.set_status(a, 3)

	def cold(self,a):
		"""
		Set the white cold led.
		"""
		self.d.set_status(a, 4)	

	def color_mode(self):
		"""
		Set the bulb to color mode. This is necessary to
		use the set_rgb command.
		"""
		self.d.set_status('colour', 2)	

	def set_rgb(self, r,g,b):
		"""
		Set the RGB value of the lamp
		"""
		self.d.set_status("%02x%02x%02xdeadbeef" % (r,g,b), 5)