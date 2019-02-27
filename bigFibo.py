#from timeit import default_timer as timer
#start_time = timer()

#t = timer()
n, m = list(map(int, input().split()))

def feb(k):
	a, b = 0, 1
	for i in range(2, k+1):
	    a_tmp = a
	    a = b
	    b = a_tmp + b
	return(b)

def febm(k):
	a, b = 0, 1
	for i in range(1, k+1):
	    a_tmp = a
	    a = b
	    b = a_tmp + b
	return(b)	
#n1=feb(n)
#m1=febm(m)

print (feb(n)%febm(m))

#elapsed = timer() - t
#print_format = "{:.10f} secs"
#print(print_format.format(elapsed))
#print("{:.10f} secs".format(elapsed))
