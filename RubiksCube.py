""" 
Design a data structure to represent a Rubik's Cube and store its state in memory. The
cube can have an arbitrary number of tiles per side (e.g., 3x3, 4x4, 5x5).
Things to Consider:
- Cube Size: The cube can be of any size (e.g., 3x3, 4x4, 5x5). Your solution should be
flexible enough to handle cubes with different numbers of tiles per side.
- Layer Rotation: Since it's a Rubik's Cube, layers (rows, columns, or faces) need to be
rotatable. Think about how rotating a layer affects adjacent sides and how to efficiently
update the cube's state in memory. 
"""


class RubiksCube:
    def __init__(self, size=3): # Default size
        self.size = size
        # Add labels to faces
        self.faces = {
            "Front": [[f"G" for _ in range(size)] for _ in range(size)],
            "Back": [[f"B" for _ in range(size)] for _ in range(size)],
            "Left": [[f"O" for _ in range(size)] for _ in range(size)],
            "Right": [[f"R" for _ in range(size)] for _ in range(size)],
            "Up": [[f"W" for _ in range(size)] for _ in range(size)],
            "Down": [[f"Y" for _ in range(size)] for _ in range(size)],
        }

    def rotate_face(self, face):
        """Rotate a specific face 90 degrees clockwise."""
        if face in self.faces:
            self.faces[face] = [list(row) for row in zip(*self.faces[face][::-1])]
        else:
            print(f"Invalid face: {face}. Choose from {list(self.faces.keys())}.")

    def display(self):
        """Display the state of the Rubik's Cube."""
        print("\nRubik's Cube State:")
        for label, face in self.faces.items():
            print(f"\nFace: {label}")
            for row in face:
                print(" ".join(row))
        print()

# Initialize cube
cube = RubiksCube(3)
cube.display()  # Display initial cube

# Rotate front face
print("Rotating the Front face...\n")
cube.rotate_face("Front")
cube.display()  # Display front face