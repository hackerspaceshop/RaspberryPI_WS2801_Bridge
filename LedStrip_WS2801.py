# Simple Python Library for accessing WS2801 LED stripes
# Copyright (C) 2013  Philipp Tiefenbacher <wizards23@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# For more information about this project please visit:
# http://www.hackerspaceshop.com/ledstrips/raspberrypi-ws2801.html

class LedStrip_WS2801:	
	def __init__(self, spiDevice, nLeds, nBuffers=1):
		self.f = open(spiDevice, "w")
		self.nLeds = nLeds
		self.nBuffers = nBuffers
		self.buffers = []
		for i in range(0, nBuffers):
			ba = bytearray()
			for l in range(0, nLeds):
				ba.extend([0,0,0])
			self.buffers.append(ba)

	def close(self):
		if (self.f != None):
			self.f.close()
			self.f = None
	
	def update(self, bufferNr=0):
		self.f.write(self.buffers[bufferNr])
		self.f.flush()

	def setAll(self, color, bufferNr=0):
		for i in range(0, self.nLeds):
			self.setPixel(i, color, bufferNr) 

	def setPixel(self, index, color, bufferNr=0):
		self.buffers[bufferNr][index*3:index*3+3] = (color[0], color[2], color[1])

