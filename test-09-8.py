from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from OpenGL.GL import *

# render triángulo y un cuadrado
class Test(Base):

	def initialize(self):
		print("Iniciando programa...")

		vsCode = """
		in vec3 position;
		void main()
		{
			gl_Position = vec4(position.x, position.y, position.z, 1.0);
		}
		"""

		fsCode = """
		void main()
		{
			gl_FragColor = vec4(0.0,1.0,1.0,1.0);
		}
		"""

		self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

		# render settings
		glPointSize(16)
		glLineWidth(8)

		#set de triángulo
		self.vaoTri = glGenVertexArrays(1)
		glBindVertexArray(self.vaoTri)
		positionDataTri= [[-0.5, 0.8, 0.0],
						  [-0.2, 0.2, 0.0],
						  [-0.8, 0.2, 0.0]]
		positionAttributeTri = Attribute("vec3", positionDataTri)
		positionAttributeTri.associateVariable(self.programRef, "position")
		self.vertexCountTri = len(positionDataTri)

		#setup cuadrado
		self.vaoSq = glGenVertexArrays(1)
		glBindVertexArray(self.vaoSq)
		positionDataSq = [[0.8, 0.8, 0.0],
						  [0.8, 0.2, 0.0],
						  [0.2, 0.2, 0.0],
						  [0.2, 0.8, 0.0]]
		positionAttributeSq = Attribute("vec3", positionDataSq)
		positionAttributeSq.associateVariable( self.programRef,"position")
		self.vertexCountSq = len(positionDataSq)

	def update(self):

		glUseProgram(self.programRef)

		glBindVertexArray( self.vaoTri)
		glDrawArrays( GL_LINE_LOOP, 0, self.vertexCountTri)

		glBindVertexArray(self.vaoSq)
		glDrawArrays(GL_LINE_LOOP,0, self.vertexCountSq)

#run the program
Test().run()