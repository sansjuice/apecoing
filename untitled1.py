from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

x,y,z = mc.player.getPos()
y = y-1


for i in range(20):
    r = random.choice(range(1,5))
    if r==1:
        mc.setBlocks(x+1,y,z,x+2,y,z,57)
    
