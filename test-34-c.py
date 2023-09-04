from core.base 		import Base
from core.renderer 	import Renderer
from core.scene 	import Scene
from core.camera 	import Camera
from core.mesh 		import Mesh

from geometry.boxGeometry import BoxGeometry
from geometry.sphereGeometry import SphereGeometry
from material.pointBasicMaterial import PointBasicMaterial
from material.lineBasicMaterial import LineBasicMaterial
from material.surfaceBasicMaterial import SurfaceBasicMaterial
from geometry.geometry import Geometry
from material.material import Material

# render a scene

class Test(Base):

	def initialize(self):
		print("Inicializando programa...")

		self.renderer = Renderer()
		self.scene    = Scene()
		self.camera    = Camera()
		# pull camera towards viewer
		self.camera.setPosition(0,0,7)

		geometry = SphereGeometry(radius=3)

		vsCode = """
		in vec3 vertexPosition;
		out vec3 position;
		uniform mat4 modelMatrix;
		uniform mat4 viewMatrix;
		uniform mat4 projectionMatrix;

		void main() 
		{
		    vec4 pos = vec4(vertexPosition, 1.0);
		    gl_Position = projectionMatrix * viewMatrix * modelMatrix * pos;
		    position = vertexPosition;
		}
		"""

		fsCode = """
		in vec3 position;
		out vec4 fragColor;

		void main()
		{
			vec3 color = fract (position);
			fragColor = vec4(color, 1);
		}
		"""

		material = Material(vsCode, fsCode)
		material.locateUniforms()

		self.mesh = Mesh( geometry, material )

		self.scene.add( self.mesh)

	def update(self):

		self.mesh.rotateY( 0.01337)
		self.renderer.render( self.scene, self.camera)

# instantiate and run class
Test().run()