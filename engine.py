import json,os,urllib.request as q,random
U=os.getenv("MAKEFUN_ENV_URL");vv=[0,100,320,330,500,900,0]
TS="PPPPZZZZRRTVQQRUPPPTQONPQRRLPPPPFHJJHLPPJPRSJQSTJPSTJQRSHLPQFHJJLNNNNPPPNPQRNQQRNPRRNRRRNQPPLNNNJHHFJHHFJHHFJHHFLJJHNLLLTTPPTVRPFHJLJLNPJNTVJNVXJNVXJNTVJJPPFJJJ"
_dd=[[(ord(TS[j*32+r*4+min(f,7-f)])-80)*5 for r in range(8)for f in range(8)]for j in(0,0,1,2,2,2,3,4)]
g=random.Random(987123).getrandbits
hb=[[g(64)for _ in range(128)]for _ in range(16)];hs=g(64);hc=[g(64)for _ in range(16)]
BD=[-17,-15,15,17];RD=[-16,-1,1,16];K8=sorted(BD+RD);KN=[-33,-31,-18,-14,14,18,31,33]
DR=[KN,BD,RD,K8,K8];KP={0:7,7:11,4:3,112:13,119:14,116:12}
MATE=60000;Kg=[116,4]
def Fd(fen):
 global B,w,c,e,k
 B=[0]*128;a=fen.split()
 for r,row in enumerate(a[0].split('/')):
  f=0
  for ch in row:
   if ch.isdigit():f+=int(ch)
   else:
    t="PNBRQK".index(ch.upper())+1;p=t+8*ch.islower();s=r*16+f;B[s]=p
    if t==6:Kg[p>8]=s
    f+=1
 w=a[1]!='w';c=sum(1<<i for i,x in enumerate('KQkq')if x in a[2]);e=Yu(a[3])if a[3]!='-'else-1
 k=hc[c]
 for s,p in enumerate(B):
  if p:k^=hb[p][s]
 if w:k^=hs
def At(s,by):
 o=8*by
 for x in (2,6,3,4):
  for d in DR[x-2]:
   t=s+d
   while not t&136:
    q=B[t]
    if q==o+x or (2<x<5 and q==o+5) or (x==3 and t==s+d and q==o+1 and (d>0)!=by):return 1
    if q or x%4==2:break
    t+=d
def Gn(cp=0):
 ms=[];ap=ms.append
 for s,p in enumerate(B):
  if not p or (p-1)//8!=w:continue
  t=p&7
  if t==1:
   d=32*w-16;u=s+d;tg=[u]*(not(cp or B[u]))
   if tg and (s>>4)==6-5*w and not B[s+2*d]:ap(s|s+2*d<<7)
   for t2 in (u-1,u+1):
    if not t2&136 and((y:=B[t2])and(y-1)//8!=w or t2==e):tg.append(t2)
   for t2 in tg:
    for v in (5,4,3,2)if (t2>>4)==7*w else(0,):ap(s|t2<<7|v<<14)
  else:
   for d in DR[t-2]:
    t2=s+d
    while not t2&136:
     q=B[t2]
     if q and (q-1)//8!=w or not(q or cp):ap(s|t2<<7)
     if q or t%4==2:break
     t2+=d
 if not cp:
  ks=116-112*w
  for sg,bt,ro in ((1,1,3),(-1,2,-4)):
   if c&(bt<<2*w) and (B[ks]-8*w,B[ks+ro]-8*w)==(6,4) and not any(B[ks+i*sg] for i in range(1,4-(ro>0))) and not any(At(ks+i*sg,w^1) for i in(0,1,2)):ap(ks|ks+2*sg<<7)
 return ms
def Mk(m):
 global w,c,e,k
 f=m&127;t=(m>>7)&127;p=B[f];cap=B[t];ecs=-1;z=p&7
 if z==1 and t==e and not cap and (f&7)!=(t&7):
  ecs=t+16-32*w;cap=B[ecs]
 k^=hs;e=-1
 if cap:
  cs=ecs if ecs+1 else t;k^=hb[cap][cs]
  B[ecs]=0
 B[f]=0;k^=hb[p][f]
 np=pr+8*w if z==1 and (pr:=m>>14&7) else p
 B[t]=np;k^=hb[np][t]
 if z==6:
  Kg[w]=t
  if abs(t-f)==2:
   rf,rt=(f+3,f+1)if t>f else(f-4,f-1)
   rp=B[rf];B[rf]=0;B[rt]=rp;k^=hb[rp][rf]^hb[rp][rt]
 if z==1 and abs(t-f)==32:e=(f+t)//2
 k^=hc[c];c&=KP.get(f,15)&KP.get(t,15);k^=hc[c]
 w^=1
