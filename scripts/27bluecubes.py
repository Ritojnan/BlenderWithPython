#importing necessary libraries

import bpy
import mathutils 
import math


def create_cube(x, y, z, r, g, b):
    bpy.ops.mesh.primitive_cube_add(location=(x, y, z))
    obj = bpy.context.active_object
    mat = bpy.data.materials.new(name="Material")
    mat.diffuse_color = (r/255, g/255, b/255,1)
    obj.data.materials.append(mat)


def create_sun_light(location, rotation_euler, angle):
    scene = bpy.context.scene
    sun_data = bpy.data.lights.new(name='Sun', type='SUN')
    sun = bpy.data.objects.new(name='Sun', object_data=sun_data)
    scene.collection.objects.link(sun)
    sun.location = location
    sun.rotation_euler = rotation_euler
    sun.data.angle = angle
    return sun

def create_camera(location, rotation_euler, fov):
    scene = bpy.context.scene
    camera_data = bpy.data.cameras.new(name='Camera')
    camera = bpy.data.objects.new('Camera', camera_data)
    scene.collection.objects.link(camera)
    camera.location = location
    camera.rotation_euler = rotation_euler
    camera.data.angle = fov
    return camera

#deleting previously created objects

bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)

# Get all materials in the blend file
materials = bpy.data.materials

# Remove all unused materials
for material in materials:
    if material.users == 0:
        bpy.data.materials.remove(material)

# main program for creating 27 cubes
for i in range (-1,2):
  for j in range (-1,2):
    for k in range (-1,2):
           x=i*3
           y=j*3
           z=k*3
           create_cube(x,y,z,0, 0, 255)

camera = create_camera((60,60,85), (-0.785398,0,-0.785398), 50)

sun_light = create_sun_light((0, 0, 10), (0, 0, 0),  1.0472)


bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.render.resolution_x = 1920*2
bpy.context.scene.render.resolution_y = 1080*2


bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (0,0,0, 1)

