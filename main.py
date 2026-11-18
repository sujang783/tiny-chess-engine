import json,os,urllib.request as R
V=[0,100,320,330,500,900,0]
A=[0,0,8,6,0,3,0];Y=[0,7,0,0,3,0,-12];J=[0,0,-30,-12,0,-8,10]
K=[-19,-8,21,12,19,8,-21,-12];I=[-10,1,10,-1,-9,11,9,-11];B=I[4:];O=I[:4]
D=dict(P=(-10,-20,-11,-9),N=K,B=B,R=O,Q=I,K=I)
P=[0]*840
for t in range(7):
 for s in range(120):
  if s%10:
   r=9-s//10;f=s%10-1;c=min(f,7-f)+min(r,7-r);P[t*120+s]=V[t]+A[t]*c+Y[t]*r+J[t]
N=0;L=60000;H={}
def v(p,s):
 if p<'A':return 0
 t='PNBRQK'.index(p.upper())+1
 return P[t*120+s] if p<'a' else -P[t*120+119-s]
def at(b,s):
 if 'p' in(b[s-9],b[s-11]):return 1
 for i,d in enumerate(K+I):
  if b[s+d]=='nk'[i>7]:return 1
 for d in B+O:
  x=s+d
  while b[x]=='.':x+=d
  p=b[x]
  if p in 'q'+('b' if d in B else 'r'):return 1
 return 0
def G(z):
 b=z[0];w=z[2];e=z[3];M=[]
 for i,p in enumerate(b):
  if p<'A' or p>'Z':continue
  for d in D[p]:
   j=i+d
   while 1:
    q=b[j]
    if q not in '.pnbrqk':break
    if p=='P':
     if (d in(-10,-20))!=(q=='.') and j!=e:break
     if d==-20 and(i<81 or b[i-10]!='.'):break
     if j<29:M+=[(i,j,r) for r in'NBRQ'];break
    M.append((i,j,''))
    if p in 'PNK' or q!='.':break
    j+=d
 k=b.index('K')
 if k in(94,95):
  r=98 if k==95 else 91;q=91 if k==95 else 98
  for g,c in(((r>k)*2-1,2),((q>k)*2-1,1)):
   if w&c and b[r if c==2 else q]=='R' and b[k+g]=='.' and b[k+2*g]=='.' and (c==1 and b[k+3*g]=='.' or c==2) and all(not at(b,k+i*g) for i in(0,1,2)):M.append((k,k+2*g,''))
 return M
def M(z,m):
 b,s,w,e,_=z;i,j,pr=m;p=b[i];q=b[j];d=v(pr or p,j)-v(p,i)-v(q,j)
 n=b[:j]+(pr or p)+b[j+1:];n=n[:i]+'.'+n[i+1:];e2=0
 if p=='P' and j==e and q=='.':
  x=j+10;d-=v(b[x],x);n=n[:x]+'.'+n[x+1:]
 if p=='P' and j==i-20:e2=i-10
 if p=='K' and abs(j-i)==2:
  r=98 if j>i else 91;t=j-1 if j>i else j+1;n=n[:t]+'R'+n[t+1:];n=n[:r]+'.'+n[r+1:];d+=v('R',t)-v('R',r)
 y=w&~(3*(p=='K')|(i==91)+2*(i==98)|4*(j==21)+8*(j==28))
 return (n[::-1].swapcase(),-(s+d),y>>2|y<<2&15,119-e2 if e2 else 0,n)
def S(z,d,a,b,y):
 global N;N+=1
 if N>L:return 0
 t=z[0]
 if 'K' not in t:return -100000+y
 e=H.get(z)
 if e and e[0]>=d and(e[1]<2 or(e[2]>=b if e[1]==2 else e[2]<=a)):return e[2]
 h=at(t,t.index('K'));o=a;B=0
 if d>2 and 1-h:
  v=-S((t[::-1].swapcase(),-z[1],z[2]>>2|z[2]<<2&15,0,t),d-3,-b,1-b,y+1)
  if v>=b:return v
 if d<=0:
  if y>64:return z[1]+10
  s=z[1]+10 if not h else -100000
  if s>=b:return s
  a=max(a,s)
  ms=[m for m in G(z) if h or t[m[1]] not in ' .']
 else:
  s=-100000;ms=G(z)
 ms.sort(key=lambda m:V['.pnbrqk'.index(t[m[1]])]+(9 if m[2] else 0)+(999 if e and m==e[3] else 0),reverse=True);l=0
 for m in ms:
  n=M(z,m)
  if at(n[4],n[4].index('K')):continue
  l+=1
  w=-S(n,d-1,-b,-a,y+1)
  if N>L:return 0
  if w>s:s=w;B=m
  if w>=b:H[z]=(d,2,w,m);return w
  if w>a:a=w
 if not l and (d>0 or h):return -100000+y if h else 0
 H[z]=(d,3 if s<=o else 1,s,B)
 return s
def F(f):
 x=f.split();b=' '*20
 for w in x[0].split('/'):
  b+=' '
  for c in w:b+='.'*int(c) if c.isdigit() else c
  b+=' '
 b+=' '*20;w=0
 for c in x[2]:
  if c in 'QKqk':w|=1<<'QKqk'.index(c)
 e=0
 if len(x)>3 and x[3]!='-':e=C(x[3],0)
 p=(x[1]=='b')
 if p:b=b[::-1].swapcase();w=w>>2|w<<2&15;e=119-e if e else 0
 return (b,sum(map(v,b,range(120))),w,e,b),p
def C(u,p):
 s=(10-int(u[1]))*10+ord(u[0])-96
 return 119-s if p else s
def W(s,p):
 if p:s=119-s
 return chr(96+s%10)+str(10-s//10)
def T(f,lg):
 global N,H;z,p=F(f);ms=[]
 if len(H)>4e5:H.clear()
 for u in lg:
  i=C(u[:2],p);j=C(u[2:4],p);ms.append((i,j,u[4:].upper()))
 bt=ms[0];N=0
 for d in range(1,17):
  a=q=-100001;c=100001;vm=ms[0];o=0
  for m in ms:
   w=-S(M(z,m),d-1,-c,-a,1)
   if N>L and d>1:o=1;break
   if w>q:q=w;vm=m
   if w>a:a=w
  if o:break
  bt=vm;ms.remove(vm);ms.insert(0,vm)
 i,j,pr=bt;u=W(i,p)+W(j,p)
 return u+(pr.lower() if pr else '')
U2=os.environ['MAKEFUN_ENV_URL']
def j(a,b):
 q=R.Request(U2+a,data=json.dumps(b).encode())
 return json.load(R.urlopen(q))
while 1:
 g=j('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':
  m=T(g['fen'],g['legal_moves'])
  if not m:g=j('/resign',{'game':g['game']});break
  g=j('/move',{'game':g['game'],'move':m})
