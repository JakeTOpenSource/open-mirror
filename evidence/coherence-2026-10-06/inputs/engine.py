import json, sys
def run(C,U,D,L0,G,INTAKE,R=5,trace=False):
    L=list(L0); M=['NORMAL']*6; lost=0; changes=[]; purges=[]
    for p in range(1,R+1):
        # 1 intake
        for i in range(6): L[i]+=INTAKE[p-1][i]
        # 2 spill-over sequential
        for i in range(6):
            if L[i]>C[i]:
                ex=L[i]-C[i]; L[i]=C[i]
                if i<5: L[i+1]+=ex
                else: lost+=ex
        # 3 mode check
        for i in range(6):
            if M[i]=='NORMAL' and L[i]>=U[i]:
                M[i]='ELEVATED'; changes.append((p,i+1,'NORMAL','ELEVATED'))
            elif M[i]=='ELEVATED' and L[i]<=D[i]:
                M[i]='NORMAL'; changes.append((p,i+1,'ELEVATED','NORMAL'))
        # 4 release simultaneous
        rel=[(L[i]//4 if M[i]=='NORMAL' else L[i]//2) for i in range(6)]
        over_cap_after=[]
        for i in range(6):
            L[i]-=rel[i]
            if M[i]=='NORMAL': lost+=rel[i]
            else:
                if i>0: L[i-1]+=rel[i]
                else: lost+=rel[i]
        for i in range(6):
            if L[i]>C[i]: over_cap_after.append((p,i+1,L[i],C[i]))
        # 5 purge
        tot=sum(L)
        if tot>G:
            for i in range(6):
                h=L[i]//2; lost+=L[i]-h; L[i]=h
            purges.append(p)
        if trace: print(p,L,M,lost,tot, over_cap_after)
    return dict(final=L,modes=M,changes=changes,purges=purges,lost=lost)

C=[10,8,12,6,9,7]; U=[7,6,9,5,7,5]; D=[3,2,4,2,3,2]
L0=[3,6,6,2,2,1]; G=38
INTAKE=[[0,6,3,5,3,3],[4,2,0,1,1,7],[4,4,3,0,0,6],[7,6,7,1,3,0],[0,6,6,3,3,0]]
if __name__ == "__main__":
    r=run(C,U,D,L0,G,INTAKE)
    print(json.dumps(r))
    expected={"final":[6,10,9,7,4,2],"modes":["ELEVATED"]*5+["NORMAL"],
              "changes":[(1,2,"NORMAL","ELEVATED"),(1,3,"NORMAL","ELEVATED"),(1,4,"NORMAL","ELEVATED"),(1,5,"NORMAL","ELEVATED"),(2,1,"NORMAL","ELEVATED"),(2,3,"ELEVATED","NORMAL"),(2,5,"ELEVATED","NORMAL"),(2,6,"NORMAL","ELEVATED"),(3,3,"NORMAL","ELEVATED"),(3,4,"ELEVATED","NORMAL"),(4,4,"NORMAL","ELEVATED"),(4,5,"NORMAL","ELEVATED"),(5,6,"ELEVATED","NORMAL")],
              "purges":[1,4],"lost":76}
    assert r==expected, "engine does not reproduce the frozen ground truth"
    print("reproduces frozen ground truth: True; conservation", sum(L0)+sum(map(sum,INTAKE)), "=", sum(r["final"])+r["lost"])
