from core.attribute import Attribute

class Geometry(object):

	def __init__(self):

		# dictionary to store attribute objects
		self.attributes = {}

		# number of vertices
		self.vertexCount = None

	def addAttribute(self, dataType, variableName, data):
		self.attributes[variableName] = Attribute(dataType,data)


	def countVertices(self):
		# el número de vertices is the length of any
		# attribute objects array of data
		attrib = list(self.attributes.values() )[0]
		self.vertexCount = len( attrib.data )