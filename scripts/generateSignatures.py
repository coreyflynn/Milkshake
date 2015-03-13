import bpy
import random

# create signatures from groups of cubes with
def createSignature(numBlocks=10,offset=0):
    signatureBlocks = []
    for i in range(numBlocks):
        bpy.ops.mesh.primitive_cube_add()
        sb = bpy.context.object
        scale = random.random() * 2
        sb.scale.z = scale
        if random.random() > 0.5:
            sb.location.z = -scale
        else:
            sb.location.z = scale
        sb.location.x = i * 2
        sb.location.y = offset * 2
        signatureBlocks.append(sb)

    bpy.context.scene.objects.active = signatureBlocks[0]
    for sb in signatureBlocks:
        sb.select = True
    bpy.ops.object.join()

for i in range(10):
    createSignature(offset=i)
