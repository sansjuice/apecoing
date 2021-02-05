from mcpi.minecraft import Minecraft
mc=Minecraft.create()

banana = []  #Line1 
oh = [] #Line2
haha = [] #Line3

for i in range(1,4):
    banana.append(2*i)
for i in range(1,4):
    oh.append(2*i)
for i in range(1,4):
    haha.append(1*i)
    
x,y,z = mc.player.getPos()
mc.setSign(x,y,z,63,8,str(banana),str(oh),str(haha))
