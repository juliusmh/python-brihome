#!/usr/bin/env python3

import brihome

if __name__ == "__main__":

	bulb = brihome.Bulb (
		"DEVICE_ID", 
		"DEVICE_IP", 
		"DEVICE_KEY"
	)

	# Set bulb to color mode
	bulb.color_mode()
	# Set bulb color to red
	bulb.set_rgb(255,0,0)
