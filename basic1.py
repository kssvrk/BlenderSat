import bpy
#from math import *
import mathutils

Name = 'Dimi'
pi2=3.14/4

objs = bpy.data.objects
bpy.ops.object.delete({"selected_objects": objs})
# The primitive_cylinder_add does not return the object, but rather only a status indicating success or failure
exitStatus = bpy.ops.mesh.primitive_cylinder_add(radius = 0.5, depth = 1)
scj = bpy.context.scene

# The added cylinder will be the active object afterits created
ob = bpy.context.object
me = ob.data
ob.name = Name

# These two lines are unnecessary and will generate another copy of your cylinder
#ob = bpy.data.objects.new(Name, me1)
#scj.objects.link(ob)

ob.rotation_mode = 'XYZ'
# If you want to move your object, simply set its location thus:
ob.location = ( 4, 0, 0 )

# And you can rotate the object the same way
ob.rotation_euler = (2*pi2,0,0)  # Note that you need to use radians rather
