from core.base 		import Base
from core.renderer 	import Renderer
from core.scene 	import Scene
from core.camera 	import Camera
from core.mesh 		import Mesh

from geometry.boxGeometry import BoxGeometry
from geometry.cylinderGeometry import CylinderGeometry
from geometry.prismGeometry import PrismGeometry
from geometry.coneGeometry import ConeGeometry
from geometry.pyramidGeometry import PyramidGeometry
from material.surfaceBasicMaterial import SurfaceBasicMaterial

from extras.movementRig import MovementRig
from extras.axesHelper import AxesHelper
from extras.gridHelper import GridHelper

# render a scene

class Test(Base):

	def initialize(self):
		print("Inicializando programa...")

		self.renderer = Renderer()
		self.scene    = Scene()
		self.camera    = Camera()

		self.camera.setPosition(1,1,5)

		geometry = ConeGeometry()
		material = SurfaceBasicMaterial( {"useVertexColors": 1} )
		self.mesh = Mesh( geometry, material )
		self.scene.add( self.mesh)

		self.rig = MovementRig()
		self.rig.add( self.mesh)
		self.scene.add( self.rig)


		self.scene.add( AxesHelper(axisLength=3))
		grid = GridHelper(lineWidth=1, size=40, divisions=40)
		grid.rotateX(-3.14/2)
		self.scene.add(grid)

	def update(self):

		self.rig.update( self.input, 1/60)

		#self.mesh.rotateY( 0.01337)
		self.renderer.render( self.scene, self.camera)

# instantiate and run class
Test().run()