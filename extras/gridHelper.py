from core.mesh import Mesh
from geometry.geometry import Geometry
from material.lineBasicMaterial import LineBasicMaterial

class GridHelper(Mesh):

    def __init__(self, size=10, divisions=10, 
                        gridColor=[1,1,1], centerColor=[1,1,0], lineWidth=4):
       
        geo = Geometry()

        posData = []
        colData = []

        # Create a range of values for the grid lines
        values = []
        deltaSize = size / divisions
        for n in range(divisions + 1):
            values.append(-size/2 + n * deltaSize)

        # Add vertical lines
        for x in values:
            posData.append([x, -size/2, 0])
            posData.append([x, size/2, 0])
            if x == 0:
                colData.append(centerColor)
                colData.append(centerColor)
            else:
                colData.append(gridColor)
                colData.append(gridColor)

        # Add horizontal lines
        for y in values:
            posData.append([-size/2, y, 0])
            posData.append([size/2, y, 0])
            if y == 0:
                colData.append(centerColor)
                colData.append(centerColor)
            else:
                colData.append(gridColor)
                colData.append(gridColor)

        geo.addAttribute("vec3", "vertexPosition", posData)
        geo.addAttribute("vec3", "vertexColor", colData)
        geo.countVertices()

        # Create the line material
        mat = LineBasicMaterial({
            "useVertexColors": 1,
            "lineWidth": lineWidth,
            "lineType": "segments"
        })

        # Initialize the mesh using the geometry and material
        super().__init__(geo, mat)
