p1=int(input())
l1=int(input())
p2=int(input())
l2=int(input())
r=int(input())
w=int(input())
res=int(input())
reading=int((p1*l1)/r)
writing=reading+int((p2*l2)/w)
if res<reading :
    g=int((r*res)/l1)
    if (r*res)%l1==0  :
        v=l1
    else :
        v=(r*res)%l1
    print("READ",g, v)
if reading<res :
    write=(res-reading)*w
    if write%l2==0:
        h=l2
    else :
        h=write%l2
    u=int(write/l2)
    print("WRITE",u,h)
