from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
x,y,z = mc.player.getPos()
number = 1

time.sleep(15)
for i in range(20):
    for i in range(number):
        mc.spawnEntity(x,y,z,60)
    number*=2

