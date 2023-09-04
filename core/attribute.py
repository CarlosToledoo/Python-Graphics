import numpy
from OpenGL.GL import *

class Attribute(object):

	def __init__(self,dataType,data):

		# type of elements in data array
		# int | float | vec2| vec3| vec4
		self.dataType = dataType

		# array of data to be stored in buffer
		self.data = data

		#referencia a buffer disponible en GPU
		self.bufferRef = glGenBuffers(1)

		# upload data inmediatamente
		self.uploadData()

	# upload esta data a GPU buffer
	def uploadData(self):

		# convertir data a numpy array format; convertir a floats
		data = numpy.array(self.data).astype( numpy.float32 )

		# seleccionar buffer usado por las siguientes acciones
		glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)

		#store data en currently bound buffer
		glBufferData(GL_ARRAY_BUFFER, data.ravel(),GL_STATIC_DRAW)

	# ASSOCIATE variable en GPU program con este buffer
	def associateVariable(self, programRef, variableName):

		#get reference for program variable with given name
		variableRef = glGetAttribLocation(programRef, variableName)

		# if the program does not reference the variable, exit
		if variableRef == -1:
			return

		# select buffer used by following actions
		glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)

		# especificar como la data puede ser leída
		#	desde el buffer currently bound to GL_ARRAY_BUFFER
		if self.dataType == "int":
			glVertexAttribPointer(variableRef,1,GL_INT, False, 0, None)
		elif self.dataType == "float":
			glVertexAttribPointer(variableRef,1 ,GL_FLOAT, False, 0, None)
		elif self.dataType == "vec2":
			glVertexAttribPointer(variableRef,2,GL_FLOAT, False, 0, None)
		elif self.dataType == "vec3":
			glVertexAttribPointer(variableRef,3 ,GL_FLOAT, False, 0, None)
		elif self.dataType == "vec4":
			glVertexAttribPointer(variableRef,4,GL_FLOAT, False, 0, None)
		else:
			raise Exception("Unknown Attribute type" + self.dataType)

		# indicar data should be streamed to varible from buffer
		glEnableVertexAttribArray(variableRef)


