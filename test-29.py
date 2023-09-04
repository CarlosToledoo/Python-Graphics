from core.base 		import Base
from core.renderer 	import Renderer
from core.scene 	import Scene
from core.camera 	import Camera
from core.mesh 		import Mesh

from geometry.boxGeometry import BoxGeometry
from material.surfaceBasicMaterial import SurfaceBasicMaterial

# render a scene

class Test(Base):

	def initialize(self):
		print("Inicializando programa...")

		self.renderer = Renderer()
		self.scene    = Scene()
		self.camera    = Camera()

		geometry = BoxGeometry()
		material = SurfaceBasicMaterial( {"useVertexColors": 1} )
		self.mesh = Mesh( geometry, material )

		self.scene.add( self.mesh)

		# pull camera towards viewer
		self.camera.setPosition(0,0,4)

		# ADD A BACKROP
		backGeometry = BoxGeometry(width=2, height=2, depth=0.01)
		backMaterial = SurfaceBasicMaterial( {"baseColor" : [1,1,0]})
		backdrop = Mesh( backGeometry, backMaterial)
		#self.scene.add( backdrop)

	def update(self):

		self.mesh.rotateX( 0.0337)
		self.mesh.rotateY( -0.0514)
		self.renderer.render( self.scene, self.camera)

# instantiate and run class
Test().run()