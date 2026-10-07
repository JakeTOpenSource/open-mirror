"""Engine for the function-match test. One process, with named single-rule variants.
run(variant, L0, INTAKE) returns the end report for that variant on that data.
Variants marked SAME compute the identical function to the base; they exist because
the documents describe them in different words."""
import json, sys
C=[10,8,12,6,9,7]; U=[7,6,9,5,7,5]; D=[3,2,4,2,3,2]; G=38
L0_FROZEN=[3,6,6,2,2,1]
INTAKE_FROZEN=[[0,6,3,5,3,3],[4,2,0,1,1,7],[4,4,3,0,0,6],[7,6,7,1,3,0],[0,6,6,3,3,0]]

VARIANTS = {
  "base": "the frozen process",
  "release_sequential": "SAME: step 4 handled one cell at a time in order 1 to 6, each amount from the cell's level when reached (identical function)",
  "reset_restated": "SAME: step 5 stated as 'remove the larger half (rounded up), keep the rest' (identical function)",
  "reset_keep_larger": "DIFF: step 5 keeps half rounded up",
  "reset_inclusive": "DIFF: step 5 fires at 38 or more",
  "upper_strict": "DIFF: step 3 upper trigger strictly above",
  "lower_strict": "DIFF: step 3 lower trigger strictly below",
  "release_downstream": "DIFF: step 4 elevated transfer goes to cell n+1, cell 6's to LOST",
  "mode_before_spill": "DIFF: step 3 uses levels after intake, before spill-over",
  "reset_skip_normal": "DIFF (hidden on frozen data): step 5 halves only ELEVATED cells",
}

def run(v, L0=None, INTAKE=None, R=5):
    L0 = L0 or L0_FROZEN; INTAKE = INTAKE or INTAKE_FROZEN
    if v in ("release_sequential", "reset_restated"): v = "base"
    L=list(L0); M=['NORMAL']*6; lost=0; changes=[]; purges=[]
    def modecheck(p):
        for i in range(6):
            up = L[i]>U[i] if v=="upper_strict" else L[i]>=U[i]
            dn = L[i]<D[i] if v=="lower_strict" else L[i]<=D[i]
            if M[i]=='NORMAL' and up: M[i]='ELEVATED'; changes.append([p,i+1,'NORMAL','ELEVATED'])
            elif M[i]=='ELEVATED' and dn: M[i]='NORMAL'; changes.append([p,i+1,'ELEVATED','NORMAL'])
    for p in range(1,R+1):
        for i in range(6): L[i]+=INTAKE[p-1][i]
        if v=="mode_before_spill": modecheck(p)
        for i in range(6):
            if L[i]>C[i]:
                ex=L[i]-C[i]; L[i]=C[i]
                if i<5: L[i+1]+=ex
                else: lost+=ex
        if v!="mode_before_spill": modecheck(p)
        rel=[(L[i]//4 if M[i]=='NORMAL' else L[i]//2) for i in range(6)]
        for i in range(6):
            L[i]-=rel[i]
            if M[i]=='NORMAL': lost+=rel[i]
            elif v=="release_downstream":
                if i<5: L[i+1]+=rel[i]
                else: lost+=rel[i]
            elif i>0: L[i-1]+=rel[i]
            else: lost+=rel[i]
        tot=sum(L)
        fire = tot>=G if v=="reset_inclusive" else tot>G
        if fire:
            for i in range(6):
                if v=="reset_skip_normal" and M[i]=='NORMAL': continue
                h = L[i]-L[i]//2 if v=="reset_keep_larger" else L[i]//2
                lost+=L[i]-h; L[i]=h
            purges.append(p)
    return dict(final=L,modes=M,changes=changes,purges=purges,lost=lost)

if __name__ == "__main__":
    base = run("base")
    assert base["final"]==[6,10,9,7,4,2] and base["lost"]==76 and base["purges"]==[1,4], "engine does not reproduce the frozen truth"
    for v in VARIANTS:
        r = run(v); print(f"{v:20s} same_on_frozen={r==base!s:5s} final={r['final']} purges={r['purges']} lost={r['lost']}  {VARIANTS[v]}")
