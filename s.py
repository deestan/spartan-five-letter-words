Y={sum([1<<ord(Z)-97 for Z in l]):l for l in open(0).read().split()if len(l)==len(set(l))==5}
W=list(Y.keys())
D=[0]*2**26
def z(A,s,t):
 if len(A)>4:return[print([Y[w]for w in A])]
 if D[t]<1:D[t]=1-any([1 for X in range(s,len(W))if t&W[X]<1 and z(A+[W[X]],X+1,t+W[X])])
 return 1-D[t]
z([],0,0)# <3