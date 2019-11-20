import bpy
#from math import *
import mathutils

Name = 'Dimi'
pi2=3.14/4

objs = bpy.data.objects
bpy.ops.object.delete({"selected_objects": objs})
# The primitive_cylinder_add does not return the object, but rather only a status indicating success or failure
exitStatus = bpy.ops.import_scene.fbx( filepath = '/home/radhakrishna/projects/NRSC/BlenderSat/animate/satellite/satellite_fbx.fbx' )

scj = bpy.context.scene

def makeMaterial(name, diffuse, specular, alpha):

    mat = bpy.data.materials.new(name)
    mat.diffuse_color = diffuse
    #mat.diffuse_shader = 'LAMBERT'
    #mat.diffuse_intensity = 1.0
    mat.specular_color = specular
    #mat.specular_shader = 'COOKTORR'
    mat.specular_intensity = 0.5
    mat.alpha_threshold = alpha
    #mat.ambient = 1
    return mat

def setMaterial(ob, mat):

    me = ob.data
    me.materials.append(mat)

# bpy.ops.object.select_by_type(type='MESH')
# bpy.ops.object.delete()

red = makeMaterial('Red',(0,0,1,1),(1,0,1),1)
origin = (0,0,0)
bpy.ops.mesh.primitive_uv_sphere_add(location=origin,radius=6.3)
bpy.ops.transform.translate(value=(1,0,0))
setMaterial(bpy.context.object, red)
# The added cylinder will be the active object afterits created
ob = bpy.context.object
me = ob.data
ob.name = Name

# These two lines are unnecessary and will generate another copy of your cylinder
#ob = bpy.data.objects.new(Name, me1)
#scj.objects.link(ob)

# ob.rotation_mode = 'XYZ'
# # If you want to move your object, simply set its location thus:
ob.location = ( 0, 0, 0 )
#
# # And you can rotate the object the same way
# ob.rotation_euler = (2*pi2,0,0)  # Note that you need to use radians rather.
satg=bpy.data.objects['Satellite_Grp']
satg.location=(7,0,0)
