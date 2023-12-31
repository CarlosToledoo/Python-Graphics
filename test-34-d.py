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
		uniform mat4 modelMatrix;
		uniform mat4 viewMatrix;
		uniform mat4 projectionMatrix;
		in vec3 vertexPosition;
		in vec3 vertexColor;
		out vec3 color;
		uniform float time;

		void main() 
		{
		    float offset = 0.2 * sin(8.0 * vertexPosition.x + time);
		    vec3 pos = vertexPosition + vec3(0.0, offset, 0.0);
		    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(pos, 1);
		    color = vertexColor;
		}
		"""

		fsCode = """
		in vec3 color;
		uniform float time;
		out vec4 fragColor;

		void main() 
		{
		    float r = abs(sin(time));
		    vec4 c = vec4(r, -0.5*r, -0.5*r, 0.0);
		    fragColor = vec4(color, 1.0) + c;
		}
		"""

		material = Material(vsCode, fsCode)
		material.addUniform("float", "time", 0.0)
		material.locateUniforms()

		self.time = 0


		self.mesh = Mesh(geometry, material)

		self.scene.add(self.mesh)

	def update(self):

		self.time += 1/60

		self.mesh.material.uniforms["time"].data = self.time

		self.renderer.render( self.scene, self.camera)

# instantiate and run class
Test().run()