from ursina import *
import numpy as np

# Initialize the 3D Engine window
app = Ursina(title="3D Gravity Simulator")

# Physics Sandbox Values
G = 100            # Gravitational constant scaled for visibility
time_step = 0.02   # Physics delta time per frame
bodies = []        # Tracks all celestial objects

class CelestialBody(Entity):
    def __init__(self, name, mass, pos, vel, body_color, body_scale):
        super().__init__(model='sphere', color=body_color, position=pos, scale=body_scale)
        self.name = name
        self.mass = mass
        self.velocity = np.array(vel, dtype=float) # Velocity vector [X, Y, Z]
        bodies.append(self)

    def calculate_gravity(self):
        if self.name == "Sun": return # Keep the sun fixed at the center
        
        total_force = np.array([0.0, 0.0, 0.0])
        my_pos = np.array([self.x, self.y, self.z])

        for other in bodies:
            if other == self: continue
            
            other_pos = np.array([other.x, other.y, other.z])
            direction = other_pos - my_pos
            distance = np.linalg.norm(direction)

            if distance < 0.2: continue # Avoid division by zero on collision

            # Newton's Gravity Formula: F = G * (m1 * m2) / r^2
            force_mag = G * (self.mass * other.mass) / (distance ** 2)
            total_force += force_mag * (direction / distance)

        # Update physics values (Acceleration = Force / Mass)
        acceleration = total_force / self.mass
        self.velocity += acceleration * time_step
        
        # Apply velocity vectors to Ursina 3D coordinates
        self.x += self.velocity[0] * time_step
        self.y += self.velocity[1] * time_step
        self.z += self.velocity[2] * time_step

# --- Environment Setup ---
Sky(color=color.black) # Space backdrop
EditorCamera()         # Enables free camera navigation (Hold Right-Click + WASD to fly)

# --- Spawn Objects ---
sun = CelestialBody("Sun", mass=1000, pos=(0,0,0), vel=(0,0,0), body_color=color.yellow, body_scale=3)
earth = CelestialBody("Earth", mass=1, pos=(10,0,0), vel=(0,0,100), body_color=color.cyan, body_scale=1)

# Frame update loop called by Ursina automatically
def update():
    for body in bodies:
        body.calculate_gravity()

app.run()
