from random import randint
from copy import deepcopy as dcpy
import pickle as pk
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Dense
#nm=input("Enter name of the Trainer: ")

#model = pk.load(open('model_'+nm+'.bin', 'rb'))
#model = pk.load(open('neural_model_tf.bin', 'rb'))

model=load_model('neural_tf')

def val_cell(r,c):
    if(r<0 or r>3 or c<0 or c>3):
        return False
    return True

def giv_wght(a,b):
    if(b==0):
        if(a!=0):
            return 3*(2**a)
        else:
            return 0
    else:
        if(a==b):
            return 5*(2**a)
        elif(a==0):
            return -3*(2**b)
        else:
            return (2**a)-(2**b)

def get_data(l):
    d=[]
    for i in range(4):
        for j in range(4):
            e=l[i][j]
            if(val_cell(i,j-1)):
               d+=[giv_wght(e,l[i][j-1])]
            if(val_cell(i,j+1)):
               d+=[giv_wght(e,l[i][j+1])]
            if(val_cell(i-1,j)):
               d+=[giv_wght(e,l[i-1][j])]
            if(val_cell(i+1,j)):
               d+=[giv_wght(e,l[i+1][j])]
    return d


def display(l):
    #print("\n"*11)
    print("\n")
    for i in range(4):
        print("\t"*6,end="")
        for j in range(4):
            e=l[i][j]
            if(e==0):
                print('*',end=" "*5)
            else:
                n=2**e
                print(n,end=" "*(6-len(str(n))))
        print("\n")
    
    #print("\n"*10)
    print("\n"*2)


def lf(l):
    f=0
    scr=0
    for i in range(4):
        if(0 in l[i]):
            lz=[]
            for z in range(4):
                if(l[i][z]==0):
                    lz.append(z)
                elif(len(lz)!=0):
                    l[i][lz[0]]=l[i][z]
                    l[i][z]=0
                    lz.append(z)
                    f=1
                    del lz[0]
                    
        for j in range(1,4):
            a=l[i][j]
            b=l[i][j-1]

            if(a==b and a!=0):
                l[i][j-1]=a+1
                del l[i][j]
                l[i].append(0)
                scr+=2**(a+1)
                f=1
    if(f):
        return [True,scr]
    else:
        return [False]

def rt(l):
    f=0
    scr=0
    for i in range(4):
        if(0 in l[i]):
            lz=[]
            for z in range(3,-1,-1):
                if(l[i][z]==0):
                    lz.append(z)
                elif(len(lz)!=0):
                    l[i][lz[0]]=l[i][z]
                    l[i][z]=0
                    lz.append(z)
                    f=1
                    del lz[0]      
        for j in range(2,-1,-1):
            a=l[i][j]
            b=l[i][j+1]

            if(a==b and a!=0):
                l[i][j+1]=a+1
                del l[i][j]
                l[i].insert(0,0)
                scr+=2**(a+1)
                f=1
    if(f):
        return [True,scr]
    else:
        return [False]


def dw(l):
    f=0
    scr=0
    for i in range(4):
        lz=[]
        for z in range(3,-1,-1):
            if(l[z][i]==0):
                lz.append(z)
            elif(len(lz)!=0):
                l[lz[0]][i]=l[z][i]
                l[z][i]=0
                lz.append(z)
                f=1
                del lz[0]

        for j in range(2,-1,-1):
            a=l[j][i]
            b=l[j+1][i]

            if(a==b and a!=0):
                l[j+1][i]=a+1
                l[j][i]=0
                for j1 in range(j,0,-1):
                    l[j1][i]=l[j1-1][i]
                    l[j1-1][i]=0
                scr+=2**(a+1)
                f=1
    if(f):
        return [True,scr]
    else:
        return [False]


def up(l):
    f=0
    scr=0
    for i in range(4):
        lz=[]
        for z in range(4):
            if(l[z][i]==0):
                lz.append(z)
            elif(len(lz)!=0):
                l[lz[0]][i]=l[z][i]
                l[z][i]=0
                lz.append(z)
                f=1
                del lz[0]

        for j in range(1,4):
            a=l[j][i]
            b=l[j-1][i]

            if(a==b and a!=0):
                l[j-1][i]=a+1
                l[j][i]=0
                for j1 in range(j,3):
                    l[j1][i]=l[j1+1][i]
                    l[j1+1][i]=0
                scr+=2**(a+1)
                f=1
    if(f):
        return [True,scr]
    else:
        return [False]

def rand_no():
    p=randint(1,10)
    if(p==10):
        return 2
    else:
        return 1

def init_game():
    l=[ [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0] ]
    r1=randint(0,3)
    c1=randint(0,3)
    r2=randint(0,3)
    c2=randint(0,3)
    l[r1][c1]=rand_no()
    if(r1==r2 and c1==c2):
        l[(r1+1)%4][(c1+2)%4]=rand_no()
    else:
        l[r2][c2]=rand_no()
    return l

def new_no(l):
    n=rand_no()
    lz=[]
    for i in range(4):
        for j in range(4):
            if(l[i][j]==0):
                lz+=[[i,j]]
    sz=len(lz)
    #if(sz!=0):
    ch=randint(1,sz)-1
    l[lz[ch][0]][lz[ch][1]]=n
    #else:
     #   print("invalid list")
      #  display(l)

def game_outcome(l):
    l1=dcpy(l)
    l2=dcpy(l)
    l3=dcpy(l)
    l4=dcpy(l)
    
    R1=up(l1)
    R2=lf(l2)
    R3=dw(l3)
    R4=rt(l4)

    r1=R1[0]
    r2=R2[0]
    r3=R3[0]
    r4=R4[0]

    ans=[True,l1,l2,l3,l4,r1,r2,r3,r4]

    if(r1):
        ans+=[R1[1]]
    else:
        ans+=[0]

    if(r2):
        ans+=[R2[1]]
    else:
        ans+=[0]

    if(r3):
        ans+=[R3[1]]
    else:
        ans+=[0]

    if(r4):
        ans+=[R4[1]]
    else:
        ans+=[0]
    
    if(r1 or r2 or r3 or r4):
        return ans
    else:
        return [False]
    
            
#g=[ [1,5,0,2],[0,5,5,0],[6,2,3,4],[6,0,2,2] ]

target_labels=["w","a","s","d"]
print("\t\t\t\t\t\tThe game begins !!!")
l=init_game()
display(l)
otcm=game_outcome(l)
score=0
print("Current score:",score)
nmv=0

while(otcm[0]):
    
    #ind=model.predict([get_data(l)])[0]
    ind=np.argmax(model.predict([get_data(l)]))
    #yhat = np.argmax(prediction_p)
    if(not otcm[ind+5]):
        if(otcm[7]):
            ind=2
        elif(otcm[8]):
            ind=3
        elif(otcm[6]):
            ind=1
        else:
            ind=0
    
    mv=target_labels[ind]
    print("AI's Move: ",mv)
    #input()
    
    if(mv=="w"):
        l=otcm[1]
        score+=otcm[9]
        nmv+=1
        
    elif(mv=="a"):
        l=otcm[2]
        score+=otcm[10]
        nmv+=1
        

    elif(mv=="s"):
        l=otcm[3]
        score+=otcm[11]
        nmv+=1

    else:
        l=otcm[4]
        score+=otcm[12]
        nmv+=1
        
    new_no(l)
    display(l)
    otcm=game_outcome(l)
    print("Number of moves:",nmv,end="\n")
    print("Current score:",score)

print("-----------------Game Over-----------------")
print("\nFinal Score:",score)

hs=open('high_score.txt','r')
high_score=int(hs.readline().split()[-1])
hs.close()
if(score>high_score):
    hs=open('high_score.txt','w')
    hs.write(nm+"'s AI Model : \t"+str(score))
    print("\t\t\t\tCongratulations, you've hit the high score !!!")
    hs.close()
sh=open('score_history.txt','a')
sh.writelines([nm+"'s AI Model"+" "*(10-len(nm))+str(score)+"\n"])
sh.close()







