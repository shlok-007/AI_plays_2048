from random import randint
from copy import deepcopy as dcpy

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
    #if(sz==0):
    ch=randint(1,sz)-1
    l[lz[ch][0]][lz[ch][1]]=n

def game_outcome(l):
    l1=dcpy(l)
    l2=dcpy(l)
    l3=dcpy(l)
    l4=dcpy(l)

    R1=lf(l1)
    R2=rt(l2)
    R3=up(l3)
    R4=dw(l4)
    
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
nm=input("\n\nPlease enter your name: ")
print("\n\n\t\t\t\t\t\tThe game begins !!!")
l=init_game()
display(l)
l1=dcpy(l)
otcm=game_outcome(l)
score=0
print("Current score:",score)
nmv=0

while(otcm[0]):
    
    mv=input("What's your move ?: ")
    
    if(mv=="z"):
        l=dcpy(l1)
        score=pscr
        nmv-=1
        
        print("\nReverted to previous condition")
        display(l)
        print("Current score:",score)
    
    elif(mv=="w"):
        if(otcm[7]):
            l1=dcpy(l)
            l=otcm[3]
            new_no(l)
            display(l)
            pscr=score
            score+=otcm[11]
            nmv+=1
            print("Current score:",score)
        else:
            print("Unable to move up\n")
    elif(mv=="a"):
        if(otcm[5]):
            l1=dcpy(l)
            l=otcm[1]
            new_no(l)
            display(l)
            pscr=score
            score+=otcm[9]
            nmv+=1
            print("Current score:",score)
        else:
            print("Unable to move left\n")
    elif(mv=="s"):
        if(otcm[8]):
            l1=dcpy(l)
            l=otcm[4]
            new_no(l)
            display(l)
            pscr=score
            score+=otcm[12]
            nmv+=1
            print("Current score:",score)
        else:
            print("Unable to move down\n")
    elif(mv=="d"):
        if(otcm[6]):
            l1=dcpy(l)
            l=otcm[2]
            new_no(l)
            display(l)
            pscr=score
            score+=otcm[10]
            nmv+=1
            print("Current score:",score)
        else:
            print("Unable to move right\n")
    elif(mv=="q"):
        print("\n\n\t\t\t\t\t\t\tQuitting Game...")
        break
    else:
        print("\nInvalid Move\n")
        
    otcm=game_outcome(l)
    print("Number of moves:",nmv,end="\n")



print("\t\t\t\t\t-----------------Game Over-----------------")

print("\n\t\t\t\t\t\t\tFinal Score:",score)

hs=open('high_score.txt','r')
high_score=int(hs.readline().split()[-1])
hs.close()
if(score>high_score):
    hs=open('high_score.txt','w')
    hs.write(nm+" : \t"+str(score))
    print("\t\t\t\tCongratulations, you've hit the high score !!!")
    hs.close()
sh=open('score_history.txt','a')
sh.writelines([nm+" "*(21-len(nm))+str(score)+"\n"])
sh.close()

print("\n\n\t\t\t\t-------------------------Thanks for Playing-------------------------")













