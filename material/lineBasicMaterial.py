from material.basicMaterial import BasicMaterial
from OpenGL.GL import *

class LineBasicMaterial(BasicMaterial):

	def __init__(self, properties={}):
		super().__init__()

		# render vertices as continuos by default
		self.settings["drawStyle"] = GL_LINE_STRIP
		# LINE TYPe: "connected" | "loop" | "segments"
		self.settings["lineType"] = "connected"
		# line thickness
		self.settings["lineWidth"] = 4

		self.setProperties(properties)

	def updateRenderSettings(self):

		glLineWidth( self.settings["lineWidth"] )

		if self.settings["lineType"] == "connected":
			self.settings["drawStyle"] = GL_LINE_STRIP
		elif self.settings["lineType"] == "loop":
			self.settings["drawStyle"] = GL_LINE_LOOP
		elif self.settings["lineType"] == "segments":
			self.settings["drawStyle"] = GL_LINES
		else:
			raise Exception("Unknown line type: " + self.settings["lineType"])