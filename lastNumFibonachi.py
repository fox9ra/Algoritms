#ex 2.2.2
num = int(input())
c=0
m = [0,1]
for i in range(2,num):
    m.append((m[i-1]+m[i-2])%10)
    c+=1
    #print (m,c,m[i],num,i)
    if (m[i]==1) and (m[i-1]==0):
        break
print(m[(num%c)])

#для интереса можно еще через список т.к. последовательность чисел каждые 60 
'''
Создаем список из последних цифр чисел Фибоначчи в цикле:

a, b, rFib = 0, 1, [0, 1]

for i in range(58):
    a, b = b, a + b
    rFib.append(b % 10)


Теперь можем моментально узнавать последнюю цифру любого числа Фибоначчи используя остаток от деления на 60:

def fib_digit(n):
    return rFib[n % 60]

n = int(input())    # например n = 317457
print(fib_digit(n)) # 317457 % 60 = 57, rFib[57] = 2
'''

'''
#good from stepic
n=int(input())
i=0
j=1

for k in range(2,n+1):
    c=(i+j)%10
    i=j
    j=c
print(c)
'''