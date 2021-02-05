from mcpi.minecraft import Minecraft
mc=Minecraft.create()

for i in range(150):
    x,y,z = mc.player.getPos()
    x=x+i
    mc.setBlock(x,y-1,z,169)

