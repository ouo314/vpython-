

from vpython import *

m1,r1,v1=1,1,vector(3,4,5)
m2,r2,v2=1,1,vector(-1.5,-2,0)

r=1
t=0
dt=0.001
L=5

#畫面
scene= canvas(width=600,height=400,x=500,y=600,background=vector(0.5,0.5,0.5))
#球
b1=sphere(pos=vector(0,0,0),radius=r1,color=color.blue)
b2=sphere(pos=vector(1.5,2,2.5),radius=r2,color=color.red)
#圖表
gd1 = graph(title='v1-t',x=0,y=650,xtitle='t(s)',ytitle='v1(m/s)')
gd2=graph(width=750,height=550,x=0,y=600,title='v1-t',xtitle='t(s)',ytitle='v1(m/s)',xmax=10)

v1t=gcurve(graph=gd1,color=color.blue)
v2t=gcurve(graph=gd2,color=color.blue)

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
    rate(1000)
    b1.pos+=v1*dt
    b2.pos+=v2*dt

    v1t.plot(pos=(t,v1.x))
    v2t.plot(pos=(t,v2.x))
    #撞擊偵測
    if mag(b1.pos-b2.pos)<=r1+r2 and dot((b1.pos - b2.pos), (v1 - v2)) <=0:
        v1,v2=v_cal(v1,v2,b1.pos,b2.pos)
    #框線碰觸偵測
    if b1.pos.x+r>=L or b1.pos.x-r<=-L:
        v1.x=-v1.x
    if b2.pos.x+r>=L or b2.pos.x-r<=-L:
        v2.x=-v2.x

    if b1.pos.y+r>=L or b1.pos.y-r<=-L:
        v1.y=-v1.y
    if b2.pos.y+r>=L or b2.pos.y-r<=-L:
        v2.y=-v2.y

    if b1.pos.z+r>=L or b1.pos.z-r<=-L:
        v1.z=-v1.z
    if b2.pos.z+r>=L or b2.pos.z-r<=-L:
        v2.z=-v2.z

    t+=dt
