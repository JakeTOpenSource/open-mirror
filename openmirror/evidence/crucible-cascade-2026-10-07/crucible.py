V=[10,8,12,6,9,7]; U=[7,6,9,5,7,5]; L=[3,2,4,2,3,2]
q=[3,6,6,2,2,1]; st=['BASE']*6; slag=0
C=[[0,6,3,5,3,3],[4,2,0,1,1,7],[4,4,3,0,0,6],[7,6,7,1,3,0],[0,6,6,3,3,0]]
start=sum(q); charged=0; changes=[]; taps=[]
for c in range(1,6):
    q=[a+b for a,b in zip(q,C[c-1])]; charged+=sum(C[c-1]); print(c,'charge',q)
    for i in range(6):
        if q[i]>V[i]:
            x=q[i]-V[i]; q[i]=V[i]
            if i<5: q[i+1]+=x
            else: slag+=x
    print(c,'overflow',q,'slag',slag)
    for i in range(6):
        old=st[i]
        if st[i]=='BASE' and q[i]>=U[i]: st[i]='SUPERHEATED'
        elif st[i]=='SUPERHEATED' and q[i]<=L[i]: st[i]='BASE'
        if st[i]!=old: changes.append((c,i+1,old,st[i]))
    print(c,'state',q,st)
    mv=[(q[i]//4 if st[i]=='BASE' else q[i]//2) for i in range(6)]
    n=q[:]
    for i in range(6):
        n[i]-=mv[i]
        if st[i]=='BASE' or i==0: slag+=mv[i]
        else: n[i-1]+=mv[i]
    q=n; print(c,'bleed',q,'moves',mv,'slag',slag)
    if sum(q)>38:
        taps.append(c)
        for i in range(6): k=q[i]//2; slag+=q[i]-k; q[i]=k
    print(c,'tap',q,'total',sum(q),'slag',slag)
print(q,st,changes,taps,slag, start,charged,start+charged,sum(q)+slag)
