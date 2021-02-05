from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
x=99
y=255
z=99
mc.player.setPos(x,y,z)
time.sleep(2)
mc.player.setPos(x,y,z+1000)
time.sleep(2)
mc.player.setPos(x,y,z+10)
time.sleep(10)
mc.player.setTilePos(x,y,z)
