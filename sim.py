#imports
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
import numpy
import random
import math
    

#Display and stuff
app = Ursina(title = "3D SOLAR SYSTEM GRAVITY ORBIT", size = (1500, 1200))

#exit key
def input(key):
    if (key == 'x'):       
        quit()
    else:
        pass

#PROPER CODE 
def update():
 # smooth buttons
    if held_keys['z']:
        sun.scale_x += 2 * time.dt
        sun.scale_y += 2 * time.dt
        sun.scale_z += 2 * time.dt
        
    if held_keys['y']:
        sun.scale_x -= 2 * time.dt
        sun.scale_y -= 2 * time.dt
        sun.scale_z -= 2 * time.dt
#constraint
    if sun.scale_x < 0.1:
        sun.scale_x = 0.1
        sun.scale_y = 0.1
        sun.scale_z = 0.1

#the math
    global j
    j = j + 0.01
    angle = math.pi*40/180

#planet radius
    radius_1 = 3.6
    earth.x = math.cos(j)*radius_1
    earth.z = math.sin(j)*radius_1

#Y-axis movement
    sun.rotation_y += time.dt*20
    earth.rotation_y += time.dt*20


#background
class Sky(Entity):
    def __init__(self):    
        super().__init__(
            model = 'sphere',
            texture = 'assets/space',
            parent = scene,
            scale = 45,
            double_sided = True 
        ) 



#planets
# my son aka sun
sun = Entity(model='sphere',texture='assets/suntexture', scale= 1)
#Earthy poo
earth = Entity(model='sphere',texture='assets/earth', scale= 1, position = (1,0,1))



sky = Sky()
EditorCamera()
j = -math.pi
#open and run window
app.run()
