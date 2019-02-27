#ex 2.2.1

d={ i:0 for i in range(1,41)}
for i in d:
	if i<=2:
		d[i]=1
	else:
		d[i]=d[i-1] + d[i-2]
#print (d)

def fib(n):
    # put your code here
    if (n<=2):
        return d.get(n)
    else:
        return d.get(n)

def main():
    n = int(input())
    if 1 <= n <= 40:
    	print(fib(n))

if __name__ == "__main__":
    main()