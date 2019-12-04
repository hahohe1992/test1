# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 19:14:15 2019

@author: li-yeh.yang
"""
def gamemodule():
    import time
    import random
    dic={}
    score=0
    
    file = open('game1.txt','r')
        
    for line in file:
            
        x=line.split()
        index=int(x[0])
        value=x[1]
        dic[index]=value
        
    tStart = time.time()
    
    while True:    
        randnum=random.randint(2,len(dic))
        print(dic[randnum])
        inputstr= input("請")
        
        if str(inputstr)==dic[randnum]:
            score+=1
        if score==5:
            break
    tEnd = time.time()
    print( "It cost %f sec" % (tEnd - tStart))
gamemodule()



