import bpy
import random

# create signatures from groups of cubes with
def createSignature(numBlocks=10,offset=0, diag=None, singleSided=False):
    signatureBlocks = []
    for i in range(numBlocks):
        bpy.ops.mesh.primitive_cube_add()
        sb = bpy.context.object

        if diag or diag == 0:
            if i == diag:
                sb.scale.x = -3.01
                sb.location.x = -3.01
            else:
                scale = random.random() * 2 + 0.1
                sb.scale.x = scale
                if singleSided:
                    sb.location.x = -scale
                else:
                    if random.random() > 0.5:
                        sb.location.x = -scale
                    else:
                        sb.location.x = scale
        sb.location.y = i * 2
        sb.location.z = offset * 2
        signatureBlocks.append(sb)

    bpy.context.scene.objects.active = signatureBlocks[0]
    for sb in signatureBlocks:
        sb.select = True
    bpy.ops.object.join()

for i in range(22):
    createSignature(numBlocks = 22, offset = i-30, diag=21-i, singleSided=True)
