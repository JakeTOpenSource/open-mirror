cap=[10,8,12,6,9,7]; up=[7,6,9,5,7,5]; lo=[3,2,4,2,3,2]
q=[3,6,6,2,2,1]; M=38
feed=[[0,6,3,5,3,3],[4,2,0,1,1,7],[4,4,3,0,0,6],[7,6,7,1,3,0],[0,6,6,3,3,0]]
st=['LARVAL']*6; tally=0; changes=[]; resets=[]
start=sum(q); allfeed=sum(map(sum,feed))
for c,row in enumerate(feed,1):
    q=[a+b for a,b in zip(q,row)]; print(c,'feed',q)
    for i in range(6):
        ex=max(0,q[i]-cap[i])
        if ex:
            q[i]-=ex
            if i<5: q[i+1]+=ex
            else: tally+=ex
    print(c,'carry',q,tally)
    for i in range(6):
        n=st[i]
        if st[i]=='LARVAL' and q[i]>=up[i]: n='PUPAL'
        elif st[i]=='PUPAL' and q[i]<=lo[i]: n='LARVAL'
        if n!=st[i]: changes.append((c,i+1,st[i],n)); st[i]=n
    print(c,'state',q,st)
    pre=q[:]
    for i in range(6):
        if st[i]=='LARVAL':
            a=pre[i]//4; q[i]-=a; tally+=a
        else:
            a=pre[i]//2; q[i]-=a
            if i>0: q[i-1]+=a
            else: tally+=a
    print(c,'metab',q,tally)
    if sum(q)>M:
        resets.append(c)
        for i in range(6):
            n=q[i]//2; tally+=q[i]-n; q[i]=n
    print(c,'moult',q,tally,sum(q))
print(q,st,changes,resets,tally, start,allfeed,start+allfeed,sum(q)+tally)
