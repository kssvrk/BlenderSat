import bpy
import math

scene = bpy.data.scenes["Scene"]
extstat = bpy.ops.mesh.primitive_cube_add()
mycube = bpy.context.object
mycube.rotation_mode = 'XYZ'

cam = bpy.data.cameras.new("Camera")
cam_ob = bpy.data.objects.new("Camera", cam)
bpy.context.scene.collection.objects.link(cam_ob)
bpy.ops.object.camera_add(location=[0,10,20], rotation=[0.436,0,3.1415927410125732])
bpy.data.scenes["Scene"].camera = cam_ob
#bpy.context.scene.collection.objects.active = bpy.context.scene.objects["Camera"]

scene.frame_start = 1
scene.frame_end = 100

mycube.rotation_euler = (0, 0, 0)
mycube.keyframe_insert('rotation_euler', index=2 ,frame=1)

mycube.rotation_euler = (0, 0, math.radians(180))
mycube.keyframe_insert('rotation_euler', index=2 ,frame=100)

scene.render.use_stamp = 1
scene.render.stamp_background = (0,0,0,1)

scene.render.filepath = "animate"
scene.render.image_settings.file_format = "AVI_JPEG"
bpy.ops.render.render(animation=True)
