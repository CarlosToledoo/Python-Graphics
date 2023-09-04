from core.object3D import Object3D

class MovementRig(Object3D):
   
    def __init__(self, unitsPerSecond=1, degreesPerSecond=60):
        # Initialize the base Object3D; controls movement and turn left/right
        super().__init__()

        # Initialize attached Object3D; controls look up/down
        self.lookAttachment = Object3D()
        self.children = [self.lookAttachment]
        self.lookAttachment.parent = self
        # Control rate of movement
        self.unitsPerSecond = unitsPerSecond
        self.degreesPerSecond = degreesPerSecond

        # customizable key mappings
        self.KEY_MOVE_FORWARDS      = "w" 
        self.KEY_MOVE_BACKWARDS     = "s" 
        self.KEY_MOVE_LEFT          = "a" 
        self.KEY_MOVE_RIGHT         = "d" 
        self.KEY_MOVE_UP            = "r" 
        self.KEY_MOVE_DOWN          = "f" 
        self.KEY_TURN_LEFT          = "q" 
        self.KEY_TURN_RIGHT         = "e" 
        self.KEY_LOOK_UP            = "t" 
        self.KEY_LOOK_DOWN          = "g"




    def add(self, child):
        self.lookAttachment.add(child)

    def update(self, inputObject, deltaTime):
        # Calculate the amount to move and rotate based on time
        moveAmount = self.unitsPerSecond * deltaTime
        rotateAmount = self.degreesPerSecond * (3.1415926 / 180) * deltaTime

        # Check for movement inputs and adjust the rig's position
        if inputObject.isKeyPressed(self.KEY_MOVE_FORWARDS):
            self.translate(0, 0, -moveAmount)
        if inputObject.isKeyPressed(self.KEY_MOVE_BACKWARDS):
            self.translate(0, 0, moveAmount)
        if inputObject.isKeyPressed(self.KEY_MOVE_LEFT):
            self.translate(-moveAmount, 0, 0)
        if inputObject.isKeyPressed(self.KEY_MOVE_RIGHT):
            self.translate(moveAmount, 0, 0)
        if inputObject.isKeyPressed(self.KEY_MOVE_UP):
            self.translate(0, moveAmount, 0)
        if inputObject.isKeyPressed(self.KEY_MOVE_DOWN):
            self.translate(0, -moveAmount, 0)

        # Check for rotation inputs and adjust the rig's orientation
        if inputObject.isKeyPressed(self.KEY_TURN_RIGHT):
            self.rotateY(-rotateAmount)
        if inputObject.isKeyPressed(self.KEY_TURN_LEFT):
            self.rotateY(rotateAmount)

        # Check for looking up and down inputs and adjust the attachment's orientation
        if inputObject.isKeyPressed(self.KEY_LOOK_UP):
            self.lookAttachment.rotateX(rotateAmount)
        if inputObject.isKeyPressed(self.KEY_LOOK_DOWN):
            self.lookAttachment.rotateX(-rotateAmount)

