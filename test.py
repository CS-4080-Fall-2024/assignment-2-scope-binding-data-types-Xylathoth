class RubiksCube:
    def __init__(self, size):
        """
        Initialize a Rubik's Cube with a given size.
        :param size: Size of the cube (e.g., 3 for a 3x3 cube).
        """
        self.size = size
        self.faces = {
            "front": self.create_face("G"),  # Green
            "back": self.create_face("B"),   # Blue
            "left": self.create_face("O"),   # Orange
            "right": self.create_face("R"),  # Red
            "top": self.create_face("W"),    # White
            "bottom": self.create_face("Y"), # Yellow
        }

    def create_face(self, color):
        """
        Create a single face of the cube filled with the given color.
        :param color: Color of the face.
        :return: A 2D list representing the face.
        """
        return [[color for _ in range(self.size)] for _ in range(self.size)]

    def rotate_face_clockwise(self, face):
        """
        Rotate a single face clockwise.
        :param face: The face to rotate.
        """
        n = self.size
        self.faces[face] = [[self.faces[face][n - j - 1][i] for j in range(n)] for i in range(n)]

    def rotate_layer(self, face, layer, clockwise=True):
        """
        Rotate a layer of the cube.
        :param face: The face from which the rotation is performed.
        :param layer: The layer index to rotate (0-based).
        :param clockwise: Direction of the rotation.
        """
        # Define neighbors and their edge positions
        neighbors = {
            "top":    [("front", 0), ("right", 0), ("back", 0), ("left", 0)],
            "bottom": [("front", -1), ("left", -1), ("back", -1), ("right", -1)],
            "front":  [("top", -1), ("right", "left"), ("bottom", 0), ("left", "right")],
            "back":   [("top", 0), ("left", "left"), ("bottom", -1), ("right", "right")],
            "left":   [("top", "left"), ("front", "left"), ("bottom", "left"), ("back", "right")],
            "right":  [("top", "right"), ("back", "left"), ("bottom", "right"), ("front", "right")],
        }
        
        # Get the neighbors and their affected edges
        adjacent = neighbors[face]
        
        # Save the edge of the first neighbor
        temp_edge = self.get_edge(adjacent[0])
        
        # Shift the edges of adjacent faces
        for i in range(3):
            self.set_edge(adjacent[i], self.get_edge(adjacent[i + 1]))
        
        # Set the saved edge to the last neighbor
        self.set_edge(adjacent[3], temp_edge)
        
        # Rotate the face if it's the top or bottom layer
        if layer == 0 or layer == self.size - 1:
            self.rotate_face_clockwise(face) if clockwise else self.rotate_face_counter_clockwise(face)

    def get_edge(self, face_and_position):
        """
        Get the edge tiles of a face at the specified position.
        :param face_and_position: Tuple (face_name, position).
        :return: List of edge tiles.
        """
        face, position = face_and_position
        if position == 0:  # Top edge
            return self.faces[face][0]
        elif position == -1:  # Bottom edge
            return self.faces[face][-1]
        elif position == "left":  # Left edge
            return [row[0] for row in self.faces[face]]
        elif position == "right":  # Right edge
            return [row[-1] for row in self.faces[face]]

    def set_edge(self, face_and_position, edge):
        """
        Set the edge tiles of a face at the specified position.
        :param face_and_position: Tuple (face_name, position).
        :param edge: List of edge tiles to set.
        """
        face, position = face_and_position
        if position == 0:  # Top edge
            self.faces[face][0] = edge
        elif position == -1:  # Bottom edge
            self.faces[face][-1] = edge
        elif position == "left":  # Left edge
            for i in range(self.size):
                self.faces[face][i][0] = edge[i]
        elif position == "right":  # Right edge
            for i in range(self.size):
                self.faces[face][i][-1] = edge[i]

    def display(self):
        """
        Display the cube in a readable format.
        """
        for face, grid in self.faces.items():
            print(f"{face.capitalize()} Face:")
            for row in grid:
                print(" ".join(row))
            print()
# Create a 3x3 Rubik's Cube
cube = RubiksCube(3)

# Display the initial state
cube.display()

# Rotate the front face clockwise
print("Rotating the Front face...\n")
cube.rotate_face_clockwise("front")
cube.display()


# Rotate the top layer of the cube
print("Rotating top layer...\n")

cube.rotate_layer("top", 0, clockwise=True)

# Display the updated state
cube.display()