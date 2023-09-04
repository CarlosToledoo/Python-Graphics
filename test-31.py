from core.base 		import Base
from core.renderer 	import Renderer
from core.scene 	import Scene
from core.camera 	import Camera
from core.mesh 		import Mesh

from geometry.planeGeometry import PlaneGeometry
from geometry.boxGeometry import BoxGeometry
from material.surfaceBasicMaterial import SurfaceBasicMaterial

# render a scene

class Test(Base):

	def initialize(self):
		print("Inicializando programa...")

		self.renderer = Renderer()
		self.scene    = Scene()
		self.camera    = Camera()
		# pull camera toward-s viewer
		self.camera.setPosition(0,0,3)

		geometry = PlaneGeometry(width=2)
		material = SurfaceBasicMaterial( {"useVertexColors": 1} )
		self.mesh = Mesh( geometry, material )

		self.scene.add( self.mesh)

	def update(self):

		self.renderer.render( self.scene, self.camera)

# instantiate and run class
Test().run()