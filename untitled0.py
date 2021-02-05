from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from random import randrange

answer = randrange(0,16)
myID = mc.getPlayerEntityId("sansbanana")

while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        
        
        hit = hits[0]
        block = mc.getBlockWithData(hit.pos)
        data = block.data
    
        if data>answer :
            mc.postToChat('答錯了sans來省判你了')
            hit = hits[0]
        elif data<answer :
            mc.postToChat('去死啦')
        else :
            mc.setBlock(hit.pos,20)
            mc.postToTitle(myID,"sans已死亡Fuck you")
            break