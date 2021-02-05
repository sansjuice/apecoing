from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z = mc.player.getTis()lePo


mc.setBlocks(x,y,z,x+5,y+5,z+5,57)
mc.setBlocks(x+1,y+1,z+1,x+4,y+4,z+4,0)
mc.setBlocks(x+3,y+1,z,x+3,y+2,z,0)
mc.setBlocks(x,y+3,z,x+5,y+3,z+5,20)
    
