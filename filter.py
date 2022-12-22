# -*- coding: utf-8 -*-
"""
Created on Fri Oct  12 20:05:25 2022

@author: zencamat
"""
import json


'''
file create&prefilter cleanup
'''

f=open('output.json')
data=json.load(f)
data=json.dumps(data)
data=data[11:]
data=","+data
data=data+";"
print("Starting..")


buffer=""
clean=""
i=0
while(1):
    if(data[i]==";"):
        break

    buffer=buffer+data[i]
    
    if "detected" in buffer:
        indexstart=data[:i].find(",")
        indexend=i+9
        detected=data[indexstart:indexend]
        clean=clean+detected
        data=data[indexend:]
        buffer=""
        i=0
 
    if "result" in buffer:
        wordstart=buffer.find("result")
        data=data[wordstart:]
        indexend=data.find(",")
        clean=clean+" "+data[0:indexend]+"\n"
        data=data[indexend:]
        buffer=""
        i=0
    
    if "update" in buffer:
        indexend=data.find("}")
        data=data[indexend:]
        buffer=""       
    i+=1
    
'''
cleanup&stats
'''
clean=clean.replace("{","")
pos=clean.count("true")
neg=clean.count("false")

'''
savefile
'''
with open('clean.txt','w') as f:
    f.write(clean)
    f.close()
'''
checks pos. flags, output them to file
'''
detected=""
file=open("clean.txt",'r')
lines=file.readlines()
for line in lines:
    if "true" in line:
        detected=detected+line+"\n"
file.close()

'''
outputs results into file
'''
file=open("clean.txt",'w')
file.write(clean)
file.write("\n==================================\n")
file.write("Counts of positive detection: "+str(pos)+"\n")
file.write("Counts of negative detection: "+str(neg)+"\n")
file.write("Positive detections: "+"\n"+detected)
file.close()

print("Done")






