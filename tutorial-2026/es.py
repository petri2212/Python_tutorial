"""from datetime import datetime
odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,
        29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]

right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print(right_this_minute, " è dispari")
else:
    print(right_this_minute, " è pari")

from os import getcwd

where_am_i = getcwd()

print(where_am_i)

import sys 
sys.platform
"""
"""
#Variables

n = 0
print(n)

n = "abc"
print(n)

#multiple assignments
n, m=0,"abc"

print(n)

n, m, z = 0.125, "abc", False
print(n)
print(m)
print(z)

N = 4
N = None
print(N)
"""
"""
#If stat

n=1

if n > 2:
    n-=n
elif n==2:
    n *=2
else:
    n +=2

n, m=1, 2
if((n>2 and n!=m) or n == m):
    n+=1

print(n," ",m)
"""
"""
#LOOPS

n = 5
while n < 5:
    print(n)
    n -= 1

for i in range(5):
    print(i)

for i in range(2,6):
    print(i)

# i=5 va a i=2 con passo -1
for i in range(5,1,-1):
    print(i)
"""
#Math