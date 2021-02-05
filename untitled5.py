from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time,random

while True:
    x,y,z = mc.player.getPos()
    
    color=random.randrange(0,9)
    mc.setBlock(x,y,z,57,color)
    time.sleep(0.00000000000001