from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z = mc.player.getPos()
def plantTree(x,y,z):
    mc.setBlocks(x+1,y+2,z,x+3,y+5,z+2,46)
    mc.setBlocks(x+2,y,z+1,x+2,y+4,z+1,17)
    
for i in range(20):
    for j in range(20):
        for k in range(20):
            
              plantTree(x+i*j,y+j*k,z+i*k)