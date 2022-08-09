W=[l for l in open(0).read().split()if len(l)==len(set(l))==5]
z=lambda A,x,t:print(A)if len(A)>4 else[z(A+[W[X]],X,t+Q)for X in range(x,len(W))if(Q:=sum([1<<ord(Z)-97 for Z in W[X]]))&t<1]
z([],0,0)