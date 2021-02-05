from mcpi.minecraft import Minecraft

mc=Minecraft.create()
x,y,z=mc.player.getPos()
mc.setBlocks(x-39,y,z-20,x+20,y+20,z+20,174)
mc.setBlocks(x-29,y+1,z-19,x+19,y+19,z+19,0)
