from vpython import *

m1,r1,v1=1,1,vector(8,0,0)
m2,r2,v2=1,1,vector(-10,0,0)

t=0
dt=0.001
L=20

scene= canvas(width=600,height=400,x=500,y=600,background=vector(0.5,0.5,0.5))

b1=sphere(pos=vector(0,0,0),radius=r1,color=color.blue)
b2=sphere(pos=vector(10,0,0),radius=r2,color=color.red)

gd1 = graph(title='v1-t',x=0,y=650,xtitle='t(s)',ytitle='v1(m/s)')
gd2=graph(width=750,height=550,x=0,y=600,title='v1-t',xtitle='t(s)',ytitle='v1(m/s)',xmax=10)

v1t=gcurve(graph=gd1,color=color.blue)
v2t=gcurve(graph=gd2,color=color.blue)

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

    if mag(b1.pos-b2.pos)<=r1+r2 and dot((b1.pos - b2.pos), (v1 - v2)) <=0:
        v1,v2=v_cal(v1,v2,b1.pos,b2.pos)
    if b1.pos.x>=L or b1.pos.x<=-L:
        v1.x=-v1.x
    if b2.pos.x>=L or b2.pos.x<=-L:
        v2.x=-v2.x

    t+=dt

