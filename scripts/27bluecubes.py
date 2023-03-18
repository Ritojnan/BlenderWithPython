#importing necessary libraries

import bpy
import mathutils 
import math

#deleting previously created objects

bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)

# main program for creating 27 cubes
for i in range (-1,2):
  for j in range (-1,2):
    for k in range (-1,2):
           x=i*3
           y=j*3
           z=k*3
           bpy.ops.mesh.primitive_cube_add(location=(x,y,z))

#STEPTOADD:Create a material and add to the cubes (Manually done)
#STEPTOADD:Add camera and light (Manually done)
#STEPTOADD:Render using cycles (Manually done)

