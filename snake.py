import numpy as np
import matplotlib.pyplot as plt
import cv2
from math import*
import random


#definations
snake_pos=[[0]]
snake_pos1=[[]]
snake_circle_count=1
img_size=600
step=int(img_size/100)
raduis=int(step/2)


def gen_random():
    global step
    global img_size
    while True:
        X=random.randint(0,img_size-1)
        if X%step==0:
            break
    return X
    
    

def add(y,x):
    global head_X
    global head_y
    global snake_pos
    if len(snake_pos)>1:
        snake_pos.pop(-1)
        snake_pos.insert(0,[y,x])
    else:
        snake_pos.insert(0,[y,x])
 #functions
def draw_snake(ball_X,ball_y,head_X1,head_y1):
   
    global head_X
    global head_y
    global img
    global snake_pos
    global snake_pos1
    global step
    global raduis
    global img_size
    global snake_circle_count
    
    cv2.circle(img,(ball_y,ball_X),raduis,(0,255,0),-1)
    if snake_circle_count==1:

    
        if ball_y==head_y1:


            if ball_X>head_X1:

                cv2.circle(img,(head_y1,head_X1),raduis,(0,255,255),-1)
                head_X+=step
                #snake_pos1.append([head_y1,head_X1])
                add(head_y1,head_X1)

            elif ball_X<head_X1:

                cv2.circle(img,(head_y1,head_X1),raduis,(0,255,255),-1)
                head_X-=step
                #snake_pos1.append([head_y1,head_X1])
                add(head_y1,head_X1)

            else:
                #snake_pos.insert(0,snake_pos1[-1])
                #snake_pos.insert(0,[head_X,head_y])
                cv2.circle(img,(head_y1,head_X1),raduis,(0,255,255),-1)
                add(head_y,head_X)
                snake_circle_count+=1
        elif ball_X==head_X1:
            
            if ball_y>head_y1:

                 cv2.circle(img,(head_y1,head_X1),raduis,(0,255,255),-1)
                 head_y+=step
                 #snake_pos1.append([head_y1,head_X1])
                 add(head_y1,head_X1)

            elif ball_y<head_y1:

                cv2.circle(img,(head_y1,head_X1),raduis,(0,255,255),-1)
                head_y-=step
                #snake_pos1.append([head_y1,head_X1])
                add(head_y1,head_X1)
            
            else:
                #snake_pos.insert(0,snake_pos1[0])
                #snake_pos.insert(0,[head_X,head_y])
                cv2.circle(img,(head_y1,head_X1),raduis,(0,255,255),-1)
                add(head_y,head_X)
                snake_circle_count+=1

        else:
            if ball_y>head_y1:

                    cv2.circle(img,(head_y1,head_X1),raduis,(0,255,255),-1)
                    head_y+=6
                    #snake_pos1.append([head_y1,head_X1])
                    add(head_y1,head_X1)

            elif ball_y<head_y1:

                    cv2.circle(img,(head_y1,head_X1),raduis,(0,255,255),-1)
                    head_y-=6
                    #snake_pos1.append([head_y1,head_X1])
                    add(head_y1,head_X1)
                    
    else:
        if ball_y==head_y1:
            
            if (ball_X>snake_pos[0][1] and snake_pos[1][1]>snake_pos[0][1]) or (ball_X<snake_pos[0][1] and snake_pos[1][1]<snake_pos[0][1]):
                if (head_y-0)==1:
                    head_y+=step
                elif (img_size-head_y)==1:
                    head_y-=step
                else:
                     head_y+=step


                if ball_X>head_X1:

                    for i,j in snake_pos:
                        cv2.circle(img,(i,j),raduis,(0,255,255),-1)
                    head_X+=step
                    snake_pos1.insert(0,snake_pos[-1])
                    snake_pos.pop(-1)
                    snake_pos.insert(0,[head_y,head_X])


                elif ball_X<head_X1:

                    for i,j in snake_pos:
                        cv2.circle(img,(i,j),raduis,(0,255,255),-1)
                    head_X-=step
                    snake_pos1.insert(0,snake_pos[-1])
                    snake_pos.pop(-1)
                    snake_pos.insert(0,[head_y,head_X])
                
                else:
                    if ball_y>head_y1:

                        for i,j in snake_pos:
                            cv2.circle(img,(i,j),raduis,(0,255,255),-1)
                        head_y+=step
                        snake_pos1.insert(0,snake_pos[-1])
                        snake_pos.pop(-1)
                        snake_pos.insert(0,[head_y,head_X])

                    elif ball_y<head_y1:

                        for i,j in snake_pos:
                            cv2.circle(img,(i,j),raduis,(0,255,255),-1)
                        head_y-=step
                        snake_pos1.insert(0,snake_pos[-1])
                        snake_pos.pop(-1)
                        snake_pos.insert(0,[head_y,head_X])
            
                    else:
                        for i,j in snake_pos:
                            cv2.circle(img,(i,j),raduis,(0,255,255),-1)
                        snake_pos.insert(-1,snake_pos1[0])
            else:
                if ball_X>head_X1:

                    for i,j in snake_pos:
                        cv2.circle(img,(i,j),raduis,(0,255,255),-1)
                    head_X+=step
                    snake_pos1.insert(0,snake_pos[-1])
                    snake_pos.pop(-1)
                    snake_pos.insert(0,[head_y,head_X])

                elif ball_X<head_X1:

                    for i,j in snake_pos:
                        cv2.circle(img,(i,j),raduis,(0,255,255),-1)
                    head_X-=step
                    snake_pos1.insert(0,snake_pos[-1])
                    snake_pos.pop(-1)
                    snake_pos.insert(0,[head_y,head_X])
            
                else:
                    for i,j in snake_pos:
                        cv2.circle(img,(i,j),raduis,(0,255,255),-1)
                    snake_pos.insert(-1,snake_pos1[0])
                
        elif ball_X==head_X1:

            if (ball_y>snake_pos[0][1] and snake_pos[1][1]>snake_pos[0][1]) or (ball_y<snake_pos[0][1] and snake_pos[1][1]<snake_pos[0][1]):
                if (head_X-0)==1:
                    head_X+=step
                elif (img_size-head_X)==1:
                    head_X-=step
                else:
                     head_X+=step


                if ball_y>head_y1:

                    for i,j in snake_pos:
                        cv2.circle(img,(i,j),raduis,(0,255,255),-1)
                    head_y+=step
                    snake_pos1.insert(0,snake_pos[-1])
                    snake_pos.pop(-1)
                    snake_pos.insert(0,[head_y,head_X])


                elif ball_y<head_y1:

                    for i,j in snake_pos:
                        cv2.circle(img,(i,j),raduis,(0,255,255),-1)
                    head_y-=step
                    snake_pos1.insert(0,snake_pos[-1])
                    snake_pos.pop(-1)
                    snake_pos.insert(0,[head_y,head_X])
                
                else:
                    if ball_X>head_X1:

                        for i,j in snake_pos:
                            cv2.circle(img,(i,j),raduis,(0,255,255),-1)
                        head_X+=step
                        snake_pos1.insert(0,snake_pos[-1])
                        snake_pos.pop(-1)
                        snake_pos.insert(0,[head_y,head_X])

                    elif ball_X<head_X1:

                        for i,j in snake_pos:
                            cv2.circle(img,(i,j),raduis,(0,255,255),-1)
                        head_X-=step
                        snake_pos1.insert(0,snake_pos[-1])
                        snake_pos.pop(-1)
                        snake_pos.insert(0,[head_y,head_X])
            
                    else:
                        for i,j in snake_pos:
                            cv2.circle(img,(i,j),raduis,(0,255,255),-1)
                        snake_pos.insert(-1,snake_pos1[0])
            else:
                if ball_y>head_y1:

                    for i,j in snake_pos:
                        cv2.circle(img,(i,j),raduis,(0,255,255),-1)
                    head_y+=step
                    snake_pos1.insert(0,snake_pos[-1])
                    snake_pos.pop(-1)
                    snake_pos.insert(0,[head_y,head_X])

                elif ball_y<head_y1:

                    for i,j in snake_pos:
                        cv2.circle(img,(i,j),raduis,(0,255,255),-1)
                    head_y-=step
                    snake_pos1.insert(0,snake_pos[-1])
                    snake_pos.pop(-1)
                    snake_pos.insert(0,[head_y,head_X])
            
                else:
                    for i,j in snake_pos:
                        cv2.circle(img,(i,j),raduis,(0,255,255),-1)
                    snake_pos.insert(-1,snake_pos1[0])  
        else:
            if ball_y>head_y1:

                for i,j in snake_pos:
                    cv2.circle(img,(i,j),raduis,(0,255,255),-1)
                head_y+=step
                snake_pos1.insert(0,snake_pos[-1])
                snake_pos.pop(-1)
                snake_pos.insert(0,[head_y,head_X])

            elif ball_y<head_y1:

                for i,j in snake_pos:
                    cv2.circle(img,(i,j),raduis,(0,255,255),-1)
                head_y-=step
                snake_pos1.insert(0,snake_pos[-1])
                snake_pos.pop(-1)
                snake_pos.insert(0,[head_y,head_X])


head_X=gen_random()
head_y=gen_random()
ball_X=gen_random()
ball_y=gen_random()
img=np.zeros((img_size,img_size,3),dtype=np.uint8)
cv2.namedWindow("snake")


while True:
    img=np.zeros((img_size,img_size,3),dtype=np.uint8)
    ball_X1=ball_X
    ball_y1=ball_y
    
    if ball_X1==head_X and ball_y1==head_y:
        ball_X=gen_random()
        ball_y=gen_random()
        #snake_circle_count+=1
    

    if snake_circle_count==1:
        draw_snake(ball_X1,ball_y1,head_X,head_y)
        cv2.imshow("snake",img)
    else:
        for i,j in snake_pos[1:]:
            if i==ball_X and j==ball_y:
                ball_X=gen_random()
                ball_y=gen_random()
                ball_X1=ball_X
                ball_y1=ball_y
        draw_snake(ball_X1,ball_y1,head_X,head_y)
        cv2.imshow("snake",img)
    k=cv2.waitKey(50)
    if k==ord('q'):
        break
cv2.destroyAllWindows()
            


