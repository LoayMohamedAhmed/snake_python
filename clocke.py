import cv2
import numpy as np
from matplotlib import pyplot as plt
from math import *
import datetime

def draw(img,angle):
    angle2=np.arange(0,360,30)
    font=cv2.FONT_HERSHEY_TRIPLEX
    number=['III','IV','V','VI','VII','VIII','IX','X','XI','XII','I','II',]
    X1=np.zeros(60)
    Y1=np.zeros(60)
    for i in range(60):
        X=round(500+320*cos(np.deg2rad(angle[i])))
        Y=round(400+320*sin(np.deg2rad(angle[i])))
        if i%5==0:
            color=(0,0,0)
            raduis=10
        else:
            color=(158,0,114)
            raduis=3
        cv2.circle(img,(X,Y),raduis,color,-1)
    for i in range(len(number)):
        X1=round(500+285*cos(np.deg2rad(angle2[i])))
        Y1=round(400+285*sin(np.deg2rad(angle2[i])))
        if i==0 or i==9 or i==11 or i==1 or i==3:
            cv2.putText(img,f"{number[i]}",(X1-40,Y1+20),font,2,color,1)
        else:
            cv2.putText(img,f"{number[i]}",(X1-15,Y1+20),font,2,color,1)
def clock(par,angle0,img,s):
    global angle1
    global min
    if s=='m':
        X=round(500+250*cos(np.deg2rad(angle0[par])))
        Y=round(400+250*sin(np.deg2rad(angle0[par])))
        cv2.line(img,(500,400),(X,Y),(255,0,0),3)
    elif s=='h':
        if min < 30:
            X=int(500+100*cos(np.deg2rad(angle0[par])))
            Y=int(400+150*sin(np.deg2rad(angle0[par])))
            cv2.line(img,(500,400),(X,Y),(0, 102, 128),4)
        else:
            X=int(500+100*cos(np.deg2rad(angle1[int(((par*30)+15)/6)])))
            Y=int(400+150*sin(np.deg2rad(angle1[int(((par*30)+15)/6)])))
            cv2.line(img,(500,400),(X,Y),(0, 102, 128),4)
    else:
        X=round(500+200*cos(np.deg2rad(angle0[par])))
        Y=round(400+200*sin(np.deg2rad(angle0[par])))
        cv2.line(img,(500,400),(X,Y),(0,0,255))
    

    draw(img,angle1)
    
    def shining(img,angle,i):
    angle2=np.arange(0,360,30)
    X=round(500+320*cos(np.deg2rad(angle[int(i/6)])))
    Y=round(400+320*sin(np.deg2rad(angle[int(i/6)])))
    if int(i/6)%5==0:
            raduis=15
    else:
            raduis=6
    cv2.circle(img,(X,Y),raduis,(204, 163, 0),-1)
    

a=list(np.arange(270,360))
b=list(np.arange(0,270))
for i in range(len(b)):
    a.append(b[i])
angle=a
a=list(np.arange(270,360,6))
b=list(np.arange(0,270,6))
for i in range(len(b)):
    a.append(b[i])
angle1=a
a=list(np.arange(270,360,30))
b=list(np.arange(0,270,30))
for i in range(len(b)):
    a.append(b[i])
angle2=a
angle2

current_time=datetime.datetime.now()
cv2.namedWindow("trackbar")
cv2.resizeWindow("trackbar",1000,1000)
img=np.zeros((1000,1000,3),dtype=np.uint8)
#angle=np.arange(0,360)
#angle2=np.arange(0,360,6)
#angle3=np.arange(0,360,30)
min=(current_time.minute)
sec=(current_time.second)
hour=current_time.hour
day=current_time.day
month=current_time.month
year=current_time.year
if hour >= 12:
    hour-=12
print(hour)


while True:
    current_time=datetime.datetime.now()
    min1=(current_time.minute)
    sec1=(current_time.second)
    hour1=current_time.hour
    
    if  min>30:
        clock(hour,angle2,img,'h')
        if min==60:
            hour+=1
            clock(hour,angle2,img,'h')
            min=0
    if sec==360:
        min+=1
        sec=0
        if min==60:
            clock(0,angle1,img,'m')
        else:
            clock(min,angle1,img,'m')
    cv2.circle(img,(500,400),350,(193,188,179),-1)
    cv2.circle(img,(500,400),350,(0,89,112),10)
    cv2.rectangle(img,(390,270),(630,330),(0,0,0),-1)
    cv2.rectangle(img,(390,270),(630,330),(	255, 215, 0),3)
    cv2.putText(img,f'{hour}:{min}:{int(sec/6)}',(390,320),cv2.FONT_HERSHEY_DUPLEX,2,(255,255,255),2)
    cv2.putText(img,f'{year}/{month}/{day}',(420,250),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    
    if min==60:
        clock(0,angle1,img,'m')
    else:
        clock(min,angle1,img,'m')
    clock(sec,angle,img,'s')
    clock(hour,angle2,img,'h')
    shining(img,angle1,sec)
    cv2.circle(img,(500,400),10,(0,0,0),-1)
    cv2.imshow("trackbar",img[:,:,::-1])
    sec+=1
    k=cv2.waitKey(165)
    if k==ord('e'):
        break
cv2.destroyAllWindows()
    
