def Ev():
 s=ph=wb=bb=0
 for sq,p in enumerate(B):
  if not p:continue
  t=p&7;r=sq>>4;g=1-(p>8)*2;i=(sq&7)+8*(r+(7-2*r)*(g<0))
  ph+=(0,0,1,1,2,4,0)[t]
  s+=g*(vv[t]+_dd[t][i])
  if t==3:wb+=g>0;bb+=g<0
 s+=30*((wb==2)-(bb==2))
 if ph<=10:
  x=Kg[0];y=Kg[1];i=x-(x>>4)*8;j=56-(y>>4)*8+(y&7);s+=_dd[7][i]-_dd[6][i]-_dd[7][j]+_dd[6][j]
 return s if w==0 else-s
def Sr(d,a,b,ply):
 global ndx,w,c,e,k
 ndx+=1
 if ndx>MATE:raise EOFError
 qd=d<=0;tm=0;best=-MATE;ic=At(Kg[w],w^1)if qd else 0
 if qd:
  if not ic:
   st=Ev()
   if st>=b:return st
   best=st;a=max(a,st)
 else:
  en=TX.get(k)
  if en:
   ed,ev,ef,tm=en
   if ed>=d:
    if ef==0:return ev
    if ef==1:a=max(a,ev)
    else:b=min(b,ev)
    if a>=b:return ev
 a0=a;bm=0;fd=0
 ms=Gn(1)if qd and not ic else Gn()
 ms.sort(key=lambda m:(m==tm,(1<<24)+vv[x&7]*16-(B[m&127]&7)if (x:=B[(m>>7)&127])else(1<<23)+vv[pr]if (pr:=(m>>14)&7)else 0),reverse=True)
 for m in ms:
  sv=(B[:],Kg[:],w,c,e,k);Mk(m);il=At(Kg[w^1],w)
  if not il:
   fd+=1;sc=0
   if k not in Hs:
    Hs.add(k);z=max(d-1,0)
    if qd or fd==1:sc=-Sr(z,-b,-a,ply+1)
    else:
     sc=-Sr(z,-a-1,-a,ply+1)
     if a<sc<b:sc=-Sr(z,-b,-a,ply+1)
    Hs.discard(k)
  B[:],Kg[:],w,c,e,k=sv
  if il:continue
  if sc>best:best=sc;bm=m
  a=max(a,sc)
  if a>=b:break
 if not fd:return best if qd and not ic else-MATE+ply if At(Kg[w],w^1) else 0
 if not qd:TX[k]=(d,best,(best>=b)+2*(best<=a0),bm)
 return best
def Wu(m):
 pr=m>>14&7;o=""
 for s in (m&127,m>>7&127):o+="abcdefgh"[s&7]+str(8-(s>>4))
 return o+("nbrq"[pr-2]if pr else"")
def Yu(s):return (8-int(s[1]))*16+ord(s[0])-97
def Du(u):
 z=Yu(u[:2])|Yu(u[2:4])<<7|("nbrq".index(u[4])+2 if u[4:]else 0)<<14
 for m in Gn():
  if m==z:Mk(m);break
P=lambda p,b:json.load(q.urlopen(U+p,json.dumps(b).encode()))
while (g:=P("/game",{}))["status"]!="done":
 while g["status"]>"x":
  Fd(g["start_fen"]);hk={k}
  for u in g["moves"]:Du(u);hk.add(k)
  Fd(g["fen"]);ndx=0;TX={};Hs=hk;best=0;lm=g["legal_moves"]
  for d in range(1,60):
   try:Sr(d,-MATE,MATE,0)
   except EOFError:break
   if k in TX:best=TX[k][3]
  u=Wu(best)if best else""
  g=P("/move",{"game":g["game"],"move":u if u in lm else min(lm)})
