def E():
 s=ph=wb=bb=0
 for sq,p in enumerate(B):
  if not p:continue
  t=p&7;r=sq>>4;g=1-(p>8)*2;i=(sq&7)+8*(r+(7-2*r)*(g<0))
  ph+=(0,0,1,1,2,4,0)[t]
  s+=g*(vl[t]+_d[t][i])
  if t==3:wb+=g>0;bb+=g<0
 s+=30*((wb==2)-(bb==2))
 if ph<=10:
  x=K[0];y=K[1];i=x-(x>>4)*8;j=56-(y>>4)*8+(y&7);s+=pe[i]-_d[6][i]-pe[j]+_d[6][j]
 return s if w==0 else-s
def S(d,a,b,ply):
 global nd,w,c,e,k
 nd+=1
 if nd>MATE:raise Ab
 qd=d<=0;tm=0;best=-MATE;ic=A(K[w],w^1)if qd else 0
 if qd:
  if not ic:
   st=E()
   if st>=b:return st
   best=st;a=max(a,st)
 else:
  en=T.get(k)
  if en:
   ed,ev,ef,tm=en
   if ed>=d:
    if ef==0:return ev
    if ef==1:a=max(a,ev)
    else:b=min(b,ev)
    if a>=b:return ev
 a0=a;bm=0;fd=0
 ms=G(1)if qd and not ic else G()
 ms.sort(key=lambda m:(m==tm,(1<<24)+vl[x&7]*16-(B[m&127]&7)if (x:=B[(m>>7)&127])else(1<<23)+vl[pr]if (pr:=(m>>14)&7)else 0),reverse=True)
 for m in ms:
  sv=(B[:],K[:],w,c,e,k);M(m);il=A(K[w^1],w)
  if not il:
   fd+=1;sc=0
   if k not in H:
    H.add(k);z=max(d-1,0)
    if qd or fd==1:sc=-S(z,-b,-a,ply+1)
    else:
     sc=-S(z,-a-1,-a,ply+1)
     if a<sc<b:sc=-S(z,-b,-a,ply+1)
    H.discard(k)
  B[:],K[:],w,c,e,k=sv
  if il:continue
  if sc>best:best=sc;bm=m
  a=max(a,sc)
  if a>=b:break
 if not fd:return best if qd and not ic else-MATE+ply if A(K[w],w^1) else 0
 if not qd:T[k]=(d,best,(best>=b)+2*(best<=a0),bm)
 return best
def W(m):
 pr=m>>14&7;o=""
 for s in (m&127,m>>7&127):o+="abcdefgh"[s&7]+str(8-(s>>4))
 return o+("nbrq"[pr-2]if pr else"")
def Y(s):return (8-int(s[1]))*16+ord(s[0])-97
def D(u):
 z=Y(u[:2])|Y(u[2:4])<<7|("nbrq".index(u[4])+2 if u[4:]else 0)<<14
 for m in G():
  if m==z:M(m);break
P=lambda p,b:json.load(q.urlopen(U+p,json.dumps(b).encode()))
while (g:=P("/game",{}))["status"]!="done":
 while g["status"]>"x":
  F(g["start_fen"]);hk={k}
  for u in g["moves"]:D(u);hk.add(k)
  F(g["fen"]);nd=0;T={};H=hk;best=0;lm=g["legal_moves"]
  for d in range(1,60):
   try:S(d,-MATE,MATE,0)
   except Ab:break
   if k in T:best=T[k][3]
  u=W(best)if best else""
  g=P("/move",{"game":g["game"],"move":u if u in lm else min(lm)})
