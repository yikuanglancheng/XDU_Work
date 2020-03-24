# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:27:51 2019

@author: orange
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 13:56:52 2019

@author: orange
"""
    
import numpy as np
#%matplotlib inline
#import matplotlib.pyplot as plt
#import matplotlib
#from PIL import Image
import random

route_success = 0
route_fail = 0     #record how many routing success and fail to calculate the rate of success

def Xrouting( X_d,Y_d,x_current,y_current,unreach_flag ):
    if unreach_flag:                                 
        if ( X_d > 0 and (routing_lable[y_current][x_current+1] == 0 or routing_lable[y_current][x_current+1] == 255) ):
            if routing_lable[y_current][x_current+1] == 0:
                routing_lable[y_current][x_current+1] = 120  
            x_current+=1                        #x_current++ is forbidden in Python
            X_d-=1
            return 1,X_d,Y_d,x_current,y_current
        elif( X_d < 0 and (routing_lable[y_current][x_current-1] == 0 or routing_lable[y_current][x_current-1] == 255) ):
            if routing_lable[y_current][x_current-1] == 0:
                routing_lable[y_current][x_current-1] = 120  
            x_current-=1  
            X_d+=1
            return 1,X_d,Y_d,x_current,y_current
        else:
            return 0,X_d,Y_d,x_current,y_current
    if unreach_flag == 0:                                 
        if ( X_d > 0 and (routing_lable[y_current][x_current+1] == 0 or routing_lable[y_current][x_current+1] == 50 or  routing_lable[y_current][x_current+1] == 255) ):
            if routing_lable[y_current][x_current+1] !=255:
                routing_lable[y_current][x_current+1] = 120  
            x_current+=1                        #x_current++ is forbidden in Python
            X_d-=1
            return 1,X_d,Y_d,x_current,y_current
        elif( X_d < 0 and (routing_lable[y_current][x_current-1] == 0 or routing_lable[y_current][x_current-1] == 50 or routing_lable[y_current][x_current-1] == 255)):
            if routing_lable[y_current][x_current-1] !=255:
                routing_lable[y_current][x_current-1] = 120  
            x_current-=1  
            X_d+=1
            return 1,X_d,Y_d,x_current,y_current
        else:
            return 0,X_d,Y_d,x_current,y_current
        
def Yrouting( X_d, Y_d,x_current,y_current,unreach_flag ):
    if unreach_flag:                                 
        if  Y_d > 0:
            if routing_lable[y_current+1][x_current] == 0:
                routing_lable[y_current+1][x_current] = 120  
                y_current+=1                        #x_current++ is forbidden in Python
                Y_d-=1
                return 1,X_d,Y_d,x_current,y_current
            elif routing_lable[y_current+1][x_current] == 255:
                y_current+=1                        #x_current++ is forbidden in Python
                Y_d-=1
                return 1,X_d,Y_d,x_current,y_current
                
            else:
                return 0,X_d,Y_d,x_current,y_current
        else:
            if routing_lable[y_current-1][x_current] == 0:
                routing_lable[y_current-1][x_current] = 120  
                y_current-=1  
                Y_d+=1                              #modify because Y_d<0 !!!!!!!!!!!!!!!!!
                return 1,X_d,Y_d,x_current,y_current
            if routing_lable[y_current-1][x_current] == 255: 
                y_current-=1  
                Y_d+=1                              #modify because Y_d<0 !!!!!!!!!!!!!!!!!
                return 1,X_d,Y_d,x_current,y_current
            else:
                return 0,X_d,Y_d,x_current,y_current
    if unreach_flag == 0:                                 
        if ( Y_d > 0 and (routing_lable[y_current+1][x_current] == 0 or routing_lable[y_current+1][x_current] == 50 or routing_lable[y_current+1][x_current] == 255) ):
            if routing_lable[y_current+1][x_current] != 255:
                routing_lable[y_current+1][x_current] = 120  
            y_current+=1                        #x_current++ is forbidden in Python
            Y_d-=1
            return 1,X_d,Y_d,x_current,y_current
        elif( Y_d < 0 and (routing_lable[y_current-1][x_current] == 0 or routing_lable[y_current-1][x_current] == 50 or routing_lable[y_current-1][x_current] == 255)):
            if routing_lable[y_current-1][x_current] != 255:
                routing_lable[y_current-1][x_current] = 120  
            y_current-=1  
            Y_d+=1
            return 1,X_d,Y_d,x_current,y_current
        else:
            return 0,X_d,Y_d,x_current,y_current
        
def Routing(X_d,Y_d,x_current,y_current,unreach_flag,xyyx_flag=1):
    if xyyx_flag == 1:
        #if X_d==0:
         #   state,X_d,Y_d,x_current,y_current = Xrouting(X_d, Y_d,x_current,y_current,unreach_flag)
          #  return state,X_d,Y_d,x_current,y_current
        #elif X_d==0:
         #   print("Routing in Y\n")
            # state,X_d,Y_d,x_current,y_current = Yrouting(X_d, Y_d,x_current,y_current,unreach_flag)
             #return state,X_d,Y_d,x_current,y_current
        if X_d==0:
            #print("Routing in Y\n")
            state,X_d,Y_d,x_current,y_current = Yrouting(X_d, Y_d,x_current,y_current,unreach_flag)
            return state,X_d,Y_d,x_current,y_current
        else:
            #print("Routing in X\n")
            state,X_d,Y_d,x_current,y_current = Xrouting(X_d, Y_d,x_current,y_current,unreach_flag)
            return state,X_d,Y_d,x_current,y_current
    else:
        if Y_d!=0:
            state,X_d,Y_d,x_current,y_current = Yrouting(X_d, Y_d,x_current,y_current,unreach_flag)
            return state,X_d,Y_d,x_current,y_current
        else:
            state,X_d,Y_d,x_current,y_current = Xrouting(X_d, Y_d,x_current,y_current,unreach_flag)
            return state,X_d,Y_d,x_current,y_current
        
for route_size in range(4,13):
    route_success = 0
    for  all_number in range(0,20000):
        for times in range(0,1):
            routing_lable = np.zeros((route_size,route_size))
            for i in range(0,route_size):
                routing_lable[0][i]=62
                routing_lable[i][0]=62
                routing_lable[route_size-1][i]=62
                routing_lable[i][route_size-1]=62
                
            flag_Dnode = 1
            while flag_Dnode:
                Dnode_row = random.randint(1,route_size-3)
                Dnode_col = random.randint(2,route_size-2)
                if routing_lable[Dnode_row][Dnode_col] == 0:
                    routing_lable[Dnode_row][Dnode_col] = 255
                    flag_Dnode = 0
        
            flag_Snode = 1
            while flag_Snode:
                Snode_row = random.randint(1,route_size-2)
                Snode_col = random.randint(1,route_size-2)
                if routing_lable[Snode_row][Snode_col]==0:
                    if Snode_row>Dnode_row:
                        if Snode_col<Dnode_col:
                            routing_lable[Snode_row][Snode_col] = 125
                            flag_Snode = 0
            
            fault_size = round(((route_size-1)*(route_size-1))/10)
            fault_row = np.random.randint(1,route_size-1,size=fault_size)
            fault_col = np.random.randint(1,route_size-1,size=fault_size)
            
            for i in range(0,len(fault_row)):
                row = fault_row[i]
                col = fault_col[i]
                if routing_lable[row][col] == 0:
                    routing_lable[row][col] = 62
                
            
        
            for i in range(1,route_size-1):
                for j in range(route_size-2,0,-1): #因为目标节点在东北方向上，所有应该从东北角开始考虑不可达节点的生成
                    if (routing_lable[1][route_size-2]!=62)and(routing_lable[1][route_size-2]!=255)and(routing_lable[1][route_size-2]!=125):
                        routing_lable[1][route_size-2]=0
                    if (routing_lable[i-1][j]==62)or(routing_lable[i-1][j]==50):
                        if (routing_lable[i][j+1]==62)or(routing_lable[i][j+1]==50):
                            if (routing_lable[i][j]==0)and(j<=Dnode_col)and(i>=Dnode_row):
                                routing_lable[i][j]=50
                    if (i==Dnode_row)and((routing_lable[i][j+1]==62)or(routing_lable[i][j+1]==50))and(j<Dnode_col):
                        if routing_lable[i][j]==0:
                                routing_lable[i][j]=50
                    if (j==Dnode_col)and((routing_lable[i-1][j]==62)or(routing_lable[i-1][j]==50))and(i>Dnode_row):
                        if routing_lable[i][j]==0:
                                routing_lable[i][j]=50
        
            #print("Raw is\n")
            #print(routing_lable)
                
        
        y_current = Snode_row
        x_current = Snode_col
        unreach_flag = 1
        xyyx_flag = 1      #1 for xy, 0 for yx 
        fail_flag = 0
        Y_d = Dnode_row - y_current
        X_d = Dnode_col - x_current
        """
        print("x_current is "+str(x_current)+" \n")
        print("y_current is "+str(y_current)+" \n")
        print("X_d is "+str(X_d)+" \n")
        print("Y_d is "+str(Y_d)+" \n")
        print("Dnode_row is "+str(Dnode_row)+" \n")
        print("Dnode_col is "+str(Dnode_col)+" \n")
        """
        
        
        Y_d = Dnode_row - y_current
        X_d = Dnode_col - x_current
        """
        print("Raw x_current is "+str(x_current)+" \n")
        print("Raw y_current is "+str(y_current)+" \n")
        print("Raw X_d is "+str(X_d)+" \n")
        print("Raw Y_d is "+str(Y_d)+" \n")
        """
        step = 0
        while True:#routing process
            
            step+=1
            #print("Step is "+str(step))
            if step>50:
                route_fail+=1
                #print("Failed\n")
                #print(routing_lable)
                break
    
            if fail_flag == 1:
                route_fail+=1
                #print("Failed\n")
                #print(routing_lable)
                break
            
            elif X_d==0 and Y_d ==0:
                route_success+=1
                """
                print("Step is "+str(step))
                print("\n")
                print("SuccessLable is \n")
                print(routing_lable)
                """
                break
            
            elif(X_d!=0 and Y_d!=0):
                route_state,X_d,Y_d,x_current,y_current = Routing(X_d,Y_d,x_current,y_current,unreach_flag,xyyx_flag) #different methods based on routing results
        
                
                if(route_state):
                    """
                    print("x_current is "+str(x_current)+" \n")
                    print("y_current is "+str(y_current)+" \n")
                    print("X_d is "+str(X_d)+" \n")
                    print("Y_d is "+str(Y_d)+" \n")
                    print(routing_lable)
                    """
                    continue
                    
                else:
                    if xyyx_flag==0:
                        xyyx_flag=1
                    else:
                        xyyx_flag=0
                    route_state,X_d,Y_d,x_current,y_current = Routing(X_d,Y_d,x_current,y_current,unreach_flag,xyyx_flag)
                
                    if(route_state):
                        """
                        print("x_current is "+str(x_current)+" \n")
                        print("y_current is "+str(y_current)+" \n")
                        print("X_d is "+str(X_d)+" \n")
                        print("Y_d is "+str(Y_d)+" \n")
                        print(routing_lable)
                        """
                        continue
                
                    elif(routing_lable[y_current-1][x_current]==50 or routing_lable[y_current][x_current+1]==50):
                        unreach_flag = 0
                        if xyyx_flag==0:
                            xyyx_flag=1
                        else:
                            xyyx_flag=0
                        continue
                
                    elif x_current==Snode_col and y_current==Snode_row:
                        if routing_lable[y_current][x_current-1]==0:
                            if fail_flag == 1:
                                route_fail+=1
                                #print("Failed\n")
                                #print(routing_lable)
                                break
                            else:
                                while route_state==0:
                                    if routing_lable[y_current][x_current-1]==62 and routing_lable[y_current-1][x_current]==62 :
                                        fail_flag = 1
                                        break
                                    elif routing_lable[y_current][x_current-1]!=62:
                                        routing_lable[y_current][x_current-1]=120
                                        x_current-=1
                                        X_d+=1
                                        route_state,X_d,Y_d,x_current,y_current = Yrouting(X_d,Y_d,x_current,y_current,unreach_flag=0)
                                        if route_state:
                                            xyyx_flag=0
                                    elif x_current-1==0:
                                        fail_flag = 1
                                        break
                        elif routing_lable[y_current+1][x_current]==0:
                            if fail_flag == 1:
                                route_fail+=1
                                #print("Failed\n")
                                #print(routing_lable)
                                break
                            else:
                                while route_state==0:
                                    if routing_lable[y_current+1][x_current]==62 and routing_lable[y_current][x_current+1]==62 :
                                        fail_flag = 1
                                        break
                                    elif routing_lable[y_current+1][x_current]!=62:
                                        routing_lable[y_current+1][x_current]=120
                                        y_current+=1
                                        Y_d-=1
                                        route_state,X_d,Y_d,x_current,y_current = Xrouting(X_d,Y_d,x_current,y_current,unreach_flag=0)
                                        if route_state:
                                            xyyx_flag=1
                                    elif x_current-1==0:
                                        fail_flag = 1
                                        break
                        else:
                            route_fail+=1
                            #print("Failed\n")
                            #print(routing_lable)
                            break
                            
                    
                    elif(routing_lable[y_current-1][x_current]==62 and routing_lable[y_current][x_current+1]==62):
                        if routing_lable[y_current+1][x_current]==120 or routing_lable[y_current+1][x_current]==125:
                            route_state,X_d,Y_d,x_current,y_current = Yrouting(X_d, Y_d, x_current, y_current, unreach_flag)
                            if (route_state):
                                continue
                            elif routing_lable[y_current][x_current - 1] != 62:
                                if fail_flag == 1:
                                    route_fail+=1
                                    #print("Failed\n")
                                    #print(routing_lable)
                                    break
                                else:
                                    while (route_state == 0):
                                        if routing_lable[y_current][x_current - 1] == 62 and routing_lable[y_current - 1][x_current] == 62:
                                            fail_flag = 1
                                            break
                                        elif x_current-1 == 0:
                                            fail_flag = 1
                                            break
                                        elif routing_lable[y_current][x_current-1]!=62:
                                            routing_lable[y_current][x_current-1] = 120
                                            x_current -= 1
                                            X_d+=1
                                            route_state,X_d,Y_d,x_current,y_current = Yrouting(X_d, Y_d, x_current, y_current,unreach_flag)
                                            if route_state == 1:
                                                xyyx_flag = 0
                                                break
                                        else:
                                            fail_flag = 1
                                            break
                            elif routing_lable[y_current+1][x_current ] != 62:
                                if fail_flag == 1:
                                    route_fail+=1
                                    #print("Failed\n")
                                    #print(routing_lable)
                                    break
                                else:
                                    while (route_state == 0):
                                        if routing_lable[y_current+1][x_current] == 62 and routing_lable[y_current][x_current+1] == 62:
                                            fail_flag = 1
                                            break
                                        elif y_current+1 == route_size:
                                            fail_flag = 1
                                            break
                                        elif routing_lable[y_current+1][x_current]!=62:
                                            routing_lable[y_current+1][x_current] = 120
                                            y_current += 1
                                            Y_d-=1
                                            route_state,X_d,Y_d,x_current,y_current = Xrouting(X_d, Y_d, x_current, y_current,unreach_flag)
                                            if route_state == 1:
                                                xyyx_flag = 1
                                                break
                                        else:
                                            fail_flag = 1
                                            break
                            else:
                                route_fail+=1
                                #print("Failed\n")
                                #print(routing_lable)
                                break
                        
                        if routing_lable[y_current][x_current-1]==120 or routing_lable[y_current][x_current-1]==125:
                            route_state,X_d,Y_d,x_current,y_current = Yrouting(X_d, Y_d, x_current, y_current, unreach_flag)
                            if (route_state):
                                continue
                            elif routing_lable[y_current+1][x_current] != 62:
                                if fail_flag == 1:
                                    route_fail+=1
                                    #print("Failed\n")
                                    #print(routing_lable)
                                    break
                                else:
                                    while (route_state == 0):
                                         if routing_lable[y_current+1][x_current] == 62 and routing_lable[y_current][x_current+1] == 62:
                                            fail_flag = 1
                                            break
                                         elif y_current+1 == 9:
                                            fail_flag = 1
                                            break
                                         elif routing_lable[y_current+1][x_current]!=62:
                                            routing_lable[y_current+1][x_current] = 120
                                            y_current += 1
                                            Y_d-=1
                                            route_state,X_d,Y_d,x_current,y_current = Xrouting(X_d, Y_d, x_current, y_current,unreach_flag)
                                            if route_state == 1:
                                                xyyx_flag = 1
                                                break
                                         else:
                                            fail_flag = 1
                                            break
                            elif routing_lable[y_current+1][x_current] != 62:
                                if fail_flag == 1:
                                    route_fail+=1
                                    #print("Failed\n")
                                    #print(routing_lable)
                                    break
                                else:
                                    while (route_state == 0):
                                        if routing_lable[y_current][x_current - 1] == 62 and routing_lable[y_current - 1][x_current] == 62:
                                            fail_flag = 1
                                            break
                                        elif x_current-1 == 0:
                                            fail_flag = 1
                                            break
                                        elif routing_lable[y_current][x_current-1]!=62:
                                            routing_lable[y_current][x_current-1] = 120
                                            x_current -= 1
                                            X_d+=1
                                            route_state,X_d,Y_d,x_current,y_current = Yrouting(X_d, Y_d, x_current, y_current,unreach_flag)
                                            if route_state == 1:
                                                xyyx_flag = 0
                                                break
                                        else:
                                            fail_flag = 1
                                            break
                            else:
                                route_fail+=1
                                #print("Failed\n")
                                #print(routing_lable)
                                break
                        
                    
                    
                    
                    
                    
                    elif routing_lable[y_current+1][x_current]==120 or routing_lable[y_current+1][x_current]==125:
                        if routing_lable[y_current][x_current-1]==0 or routing_lable[y_current][x_current-1]==50 :
                            routing_lable[y_current][x_current-1] = 120
                            xyyx_flag = 0
                            x_current-=1
                            X_d+=1
                            continue
                        else:
                            route_fail+=1
                            #print("Failed\n")
                            #print(routing_lable)
                            break
                    elif routing_lable[y_current][x_current-1]==120 or routing_lable[y_current][x_current-1]==125:
                        if routing_lable[y_current+1][x_current]==0 or routing_lable[y_current+1][x_current]==50:
                            routing_lable[y_current+1][x_current] = 120
                            y_current+=1
                            xyyx_flag = 1
                            Y_d-=1
                            continue
                        else:
                            route_fail+=1
                            #print("Failed\n")
                            #print(routing_lable)
                            break
                    
        
                    
                            
            
            elif( X_d == 0 and Y_d != 0 ):
                route_state,X_d,Y_d,x_current,y_current = Yrouting(X_d, Y_d,x_current,y_current,unreach_flag)
                if(route_state):
                    continue
                elif routing_lable[y_current][x_current+1]!=62:
                    if fail_flag == 1:
                        route_fail+=1
                        #print("Failed\n")
                        #print(routing_lable)
                        break
                    else:
                        while route_state==0:
                            if routing_lable[y_current][x_current+1]==62 and routing_lable[y_current-1][x_current]==62 :
                                fail_flag = 1
                                break
                            elif x_current+1 == route_size:
                                fail_flag = 1
                                break
                            elif routing_lable[y_current][x_current+1]!=62:
                                routing_lable[y_current][x_current+1]=120
                                x_current+=1
                                X_d-=1
                                route_state,X_d,Y_d,x_current,y_current = Yrouting(X_d,Y_d,x_current,y_current,unreach_flag)
                                if route_state == 1:
                                    xyyx_flag = 0
                            else:
                                fail_flag = 1
                                break
                elif routing_lable[y_current][x_current-1]!=62:
                    if fail_flag == 1:
                        route_fail+=1
                        #print("Failed\n")
                        #print(routing_lable)
                        break
                    else:
                        while route_state==0:
                            if routing_lable[y_current][x_current-1]==62 and routing_lable[y_current-1][x_current]==62 :
                                fail_flag = 1
                                break
                            elif x_current-1 == 0:
                                fail_flag = 1
                                break
                            elif routing_lable[y_current][x_current-1]!=62:
                                routing_lable[y_current][x_current-1]=120
                                x_current-=1
                                X_d+=1
                                route_state,X_d,Y_d,x_current,y_current = Yrouting(X_d,Y_d,x_current,y_current,unreach_flag)
                                if route_state == 1:
                                    xyyx_flag = 0
                            else:
                                fail_flag = 1
                                break
                else:
                    route_fail+=1
                    #print("Failed\n")
                    #print(routing_lable)
                    break
        
            elif (X_d != 0 and Y_d == 0):
                route_state,X_d,Y_d,x_current,y_current = Xrouting(X_d, Y_d, x_current, y_current, unreach_flag)
                if (route_state):
                    continue
                elif routing_lable[y_current-1][x_current]!=62:
                    if fail_flag == 1:
                        route_fail+=1
                        #print("Failed\n")
                        #print(routing_lable)
                        break
                    else:
                        while (route_state == 0):
                            if routing_lable[y_current][x_current + 1] == 62 and routing_lable[y_current - 1][x_current] == 62:
                                fail_flag = 1
                                break
                            elif y_current-1 == 0:
                                fail_flag = 1
                                break
                            elif routing_lable[y_current-1][x_current]!=62:
                                routing_lable[y_current-1][x_current] = 120
                                y_current -= 1
                                Y_d+=1
                                route_state,X_d,Y_d,x_current,y_current = Xrouting(X_d, Y_d, x_current, y_current,unreach_flag)
                                if route_state == 1:
                                    xyyx_flag = 1
                            else:
                                fail_flag = 1
                                break
                elif routing_lable[y_current+1][x_current]!=62:
                    if fail_flag == 1:
                        route_fail+=1
                        #print("Failed\n")
                        #print(routing_lable)
                        break
                    else:
                        while (route_state == 0):
                            if routing_lable[y_current+1][x_current] == 62 and routing_lable[y_current][x_current+1] == 62:
                                fail_flag = 1
                                break
                            elif y_current+1 == route_size:
                                fail_flag = 1
                                break
                            elif routing_lable[y_current+1][x_current]!=62:
                                routing_lable[y_current-+1][x_current] = 120
                                y_current += 1
                                Y_d-=1
                                route_state,X_d,Y_d,x_current,y_current = Xrouting(X_d, Y_d, x_current, y_current,unreach_flag)
                                if route_state == 1:
                                    xyyx_flag = 1
                            else:
                                fail_flag = 1
                                break
                            
    print("Time is "+str(all_number)+"\n")
    print("Route lable size is "+str(route_size-1)+"\n")
    print("Fault number is "+str(fault_size)+"\n")
    fault_rate = fault_size/((route_size-1)*(route_size-1))
    print("Fault rate is "+str(fault_rate)+"\n")
    if all_number==0:
        continue
    else:
        rate = (route_success-1)/all_number
        print("Rate of success is "+str(rate)+"\n")
                                
