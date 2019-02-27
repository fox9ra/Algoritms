#from timeit import default_timer as timer

n, m = map(int, input().split())

'''
c=0
T = [0,1]
for i in range(1,n):
    #print (i)
    #T.append((T[i-1]+T[i-2])%m)
    T.append(T[i-1]+T[i-2])
    c+=1
    if (T[i]==1) and (T[i-1]==0):
        break

#t = timer()
print(T[(n%c)],T)
#elapsed = timer() - t
#print("{:.10f} secs.".format(elapsed))
'''
fibPrev = 0
fib = 1
cached = [fibPrev, fib]

for curr in range(1, n):
    fibOld = fib
    fib = (fib + fibPrev) % m
    fibPrev = fibOld

    if fibPrev == 0 and fib == 1:
        cached.pop()
        break
    else:
        cached.append(fib)

print(cached[ n % len(cached)])
