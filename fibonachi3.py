from timeit import default_timer as timer
import functools
n, m = list(map(int, input().split()))

@functools.lru_cache(maxsize=None)
def feb(k):
	a, b = 0, 1
	for i in range(1, k+1):
	    a_tmp = a
	    a = b
	    b = a_tmp + b
	return(b)

t = timer()
print (feb(n)%m)
elapsed = timer() - t
print("{:.10f} secs.".format(elapsed))
