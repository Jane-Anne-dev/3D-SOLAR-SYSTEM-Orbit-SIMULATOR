#imports
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
import numpy
import random
import math
    

#Display and stuff
app = Ursina(title = "3D SOLAR SYSTEM GRAVITY ORBIT", size = (1500, 1200))
#image list
image_list = [
    'assets/so you want to be a pilot',
    'assets/ineedspace',
    'assets/kristylockin',
    'assets/physicsjoke1',
    'assets/me',
    'assets/plutomyboy',
    'assets/oh',
    'assets/son',
    'assets/physicsjoke1',
    'assets/physicsjoke2',
    'assets/physicsjoke3',
    'assets/physicsjoke4',
    'assets/physicsjoke5'

]

#exit key
def input(key):
    if (key == 'x'):       
        quit()
    if (key =='r'):
        Audio('assets/boom', loop=False, autoplay=True)
        random_image = random.choice(image_list)
        random_x = random.uniform(-0.1, 0.1)
        random_y = random.uniform(-0.1, 0.1)

        img_pop = Entity(
            model = 'quad',
            texture = random_image,
            parent = camera.ui,
            scale = 0.6,
            position = (random_x, random_y)
        )
        invoke(destroy, img_pop, delay = 1)
    else:  
        pass

#PROPER CODE 
def update():
    global j
    screen = camera
 # smooth buttons
    if held_keys['z']:
        screen.fov += 6 * time.dt
        
    if held_keys['y']:
        screen.fov -= 6 * time.dt


#the math
    j = j + 0.01
    angle = math.pi*40/180
#planet radius
    radius_mercury = 2
    mercury.x = math.cos(j)*radius_mercury
    mercury.z = math.sin(j)*radius_mercury

    radius_venus = 5.2
    venus.x = math.cos(j + angle)*radius_venus
    venus.z = math.sin(j + angle)*radius_venus

    radius_earth = 3.6
    earth.x = math.cos(j + angle*2)*radius_earth
    earth.z = math.sin(j + angle*2)*radius_earth  

    radius_mars = 4.6
    mars.x = math.cos(j+angle*3)*radius_mars
    mars.z = math.sin(j+angle*3)*radius_mars

    radius_jupiter = 2.8
    jupiter.x = math.cos(j+angle*4)*radius_jupiter
    jupiter.z = math.sin(j+angle*4)*radius_jupiter

    radius_saturn = 6
    saturn.x = math.cos(j+angle*5)*radius_saturn
    saturn.z = math.sin(j+angle*5)*radius_saturn

    radius_uranus = 8
    uranus.x = math.cos(j+angle*6)*radius_uranus
    uranus.z = math.sin(j+angle*6)*radius_uranus

    radius_neptune = 4.4
    neptune.x = math.cos(j+angle*7)*radius_neptune
    neptune.z = math.sin(j+angle*7)*radius_neptune

    radius_pluto = 6.8
    pluto.x = math.cos(j+angle*8)*radius_pluto
    pluto.z = math.sin(j+angle*8)*radius_pluto

#axial rotation
    sun.rotation_y += time.dt*20
    mercury.rotation_y += time.dt*20
    venus.rotation_y += time.dt*20
    earth.rotation_y += time.dt*20
    mars.rotation_y += time.dt*20
    jupiter.rotation_y += time.dt*20
    saturn.rotation_y += time.dt*20
    uranus.rotation_y += time.dt*20
    neptune.rotation_y += time.dt*20
    pluto.rotation_y += time.dt*20



#background
class Sky(Entity):
    def __init__(self):    
        super().__init__(
            model = 'sphere',
            texture = 'assets/spacey',
            parent = scene,
            scale = 100,
            double_sided = True 
        ) 

#orbit lines
def orbit_line(radius):
    return Entity(
        model = 'circle',
        scale = radius * 2,
        rotation_x = 90,
        color = color.rgba(1,1,1,0.2),
    )

#extra assets
nav = Entity(model='cube',texture='assets/truenaveve', scale= 3, y = 4, x = 4)


#planets
# my son aka sun
sun = Entity(model='sphere',texture='assets/suntexture', scale= 3)

#mercury (hot)
mercury = Entity(model = 'sphere', texture='assets/mercury', scale = 0.4)
orbit_mercury = orbit_line(2)

#venus fly trap
venus = Entity(model='sphere', texture='assets/venus', scale= 0.7)
orbit_mercury = orbit_line(5.2)
 
#Earthy poo
earth = Entity(model='sphere',texture='assets/earth', scale= 0.8)
orbit_earth = orbit_line(3.6)
#mars argo
mars = Entity(model= 'sphere', texture= 'assets/mars', scale = 0.5)
orbit_mars = orbit_line(4.6)

#boys go to jupiter to get stupider
jupiter = Entity(model='sphere', texture= 'assets/jupiter', scale =1.2)
orbit_jupiter= orbit_line(2.8)

#saturn
saturn = Entity(model='sphere', texture = 'assets/saturn', scale = 1.5)
orbit_saturn = orbit_line(6)

#ur anus
uranus = Entity(model='sphere', texture = 'assets/uranus', scale = 1.2)
orbit_uranus = orbit_line(8)

#king neptune
neptune = Entity(model='sphere', texture = 'assets/neptune',scale = 1.1)
orbit_neptune = orbit_line(4.4)

#pluto (imposter planet)
pluto = Entity(model = 'sphere', texture = 'assets/pluto', scale = 0.3)
orbit_pluto = orbit_line(6.8)


spacesounds = Audio('assets/background_music', loop=True, autoplay=True, volume=2)
sky = Sky()
EditorCamera() 
j = -math.pi
#open and run window
app.run()
