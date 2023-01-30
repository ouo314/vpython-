
from vpython import *

v0=1e3                                  #速度初始值
m,r=4.002602/(6.02e23),140e-2           #小球質量、半徑
K=0                                     #總動能
k=1.4e-23                               #波茲曼常數
T=0                                     #溫度
t=0                                     #時間
dt=0.005                                #時間間隔
L=r*50                                  #容器邊長的一半
deltagv=20                              #圖表速度間隔
N=200                                   #氣體數量


#畫面
scene= canvas(width=1000,height=1000,x=500,y=600,background=vector(0.5,0.5,0.5))

#球
ball=[]
for i in range(N):
    b1=sphere(pos=vector((random()-0.5)*2*L,(random()-0.5)*2*L,(random()-0.5)*2*L),radius=r,color=color.blue,v=vector((random()-0.5)*v0,(random()-0.5)*v0,(random()-0.5)*v0)) 
    K+=(m*mag(b1.v)**2)/2
    ball.append(b1)
T=(2*K)/3*N*k
print(K)
print(T)

#圖表
gph=graph(title='各速率下的分子數',xtitle="速率",ytitle="數量")
Nv=[]
Nvt=gvbars(delta=deltagv)
for i in range(50):
    Nv.append([20*(i+.5),2]) 


#框線

x=curve(pos=[(-L,L,L),(L,L,L)],radius=0.1)
y=curve(pos=[(L,-L,L),(L,L,L)],radius=0.1)
z=curve(pos=[(L,L,-L),(L,L,L)],radius=0.1)

x2=curve(pos=[(-L,-L,L),(L,-L,L)],radius=0.1)
y2=curve(pos=[(-L,-L,L),(-L,L,L)],radius=0.1)
z2=curve(pos=[(-L,L,-L),(-L,L,L)],radius=0.1)

x3=curve(pos=[(-L,-L,-L),(L,-L,-L)],radius=0.1)
y2=curve(pos=[(-L,-L,-L),(-L,L,-L)],radius=0.1)
z3=curve(pos=[(-L,-L,-L),(-L,-L,L)],radius=0.1)

x4=curve(pos=[(-L,L,-L),(L,L,-L)],radius=0.1)
y2=curve(pos=[(L,-L,-L),(L,L,-L)],radius=0.1)
z4=curve(pos=[(L,-L,-L),(L,-L,L)],radius=0.1)

#撞擊公式
def v_cal(v1,v2,r1,r2):
    v1_new=v1+(r1-r2)*dot((v2-v1),(r1-r2))/mag2(r1-r2)
    v2_new=v2+(r2-r1)*dot((v1-v2),(r2-r1))/mag2(r2-r1)
    return (v1_new,v2_new)

while t<10:
    rate(300)
    for i in range(N):
        ball[i].pos+=ball[i].v*dt

    #框線碰觸偵測
        if ball[i].pos.x+r>=L :
            ball[i].v.x=-abs(ball[i].v.x)
        if ball[i].pos.x-r<=-L:
            ball[i].v.x=abs(ball[i].v.x)
            

        if ball[i].pos.y+r>=L :
            ball[i].v.y=-abs(ball[i].v.y)
        if ball[i].pos.y-r<=-L:
            ball[i].v.y=abs(ball[i].v.y)
            

        if ball[i].pos.z+r>=L :
            ball[i].v.z=-abs(ball[i].v.z)
        if ball[i].pos.z-r<=-L:
            ball[i].v.z=abs(ball[i].v.z)
        for j in range(i+1,N):
            if mag(ball[i].pos-ball[j].pos)<=2*r and dot((ball[i].pos - ball[j].pos), (ball[i].v - ball[j].v)) <=0:
                ball[i].v,ball[j].v=v_cal(ball[i].v,ball[j].v,ball[i].pos,ball[j].pos)

    #分子速率-數量
    for i in range(50):
        count=0
        for j in range(N):
            if mag(ball[j].v)>=deltagv*i and mag(ball[j].v)<=deltagv*i+deltagv:
                count+=1
        Nv[i][1]=count
    Nvt.data=Nv
    
    t+=dt
