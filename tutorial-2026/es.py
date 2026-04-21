"""
from datetime import datetime
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
"""
#Math

#print(5/2)

#print(5//2) 2

#print(-3//2)  -2 

#print(int(-3/2))

#print(10 % 3) 1

#print(-20 % 3) 2

#print(10 % 3)

import math
from multiprocessing import heap
#print(math.fmod(-10,3)) #returns the module of the reminder

print(math.floor(3/2))
print(math.ceil(3/2))
print(math.sqrt(2))
print(math.pow(2,3)) 

print(math.pow(2, 200))# py num are infinite but never touches inf

print(math.pow(2, 200) < float("inf"))
"""

#ARRAYS
"""
arr = [1,2,3]
print(arr)

arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

arr.insert(1,7)
print(arr)

arr[0] = 0
arr[3] = 0
print(arr)


n=5
arr = [1] * n
print(arr)
print(len(arr))

arr = [1,2,3]
arr[-1]=0 #latest value. -2 second latest value ecc
print(arr)

arr = [1,2,3,4]

print(arr[1:3])

print(arr[0:4])#similar to for loops

print(arr[0:10]) # no out of bound

# Unpacking
a, b, c = [1, 2, 3]
print(a, b, c)

nums = [1, 2, 3]

for i in range(len(nums)):
    print(nums[i])

for g in nums:
    print(g)

for i, n in enumerate(nums): #enumerate allows me to loop and have access to both index and element itself 
    print(i, n)

    # Loop through multiple arrays simultaneously with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

zipped = zip(names, ages)
print(list(zipped))

fruits = ["Apple", "Banana", "Cherry"]
colors = ["Red", "Yellow", "Dark Red"]

for fruit, color in zip(fruits, colors):
    print(f"{fruit} is {color}.")


nums = [1, 2, 3]
nums.reverse()
print(nums)

arr = [5, 4, 7, 3, 8]
arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)

arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr)

# Custom  sort (bylength of string)
arr.sort(key=lambda x: len(x))
print(arr)

arr = [i for i in range(5)]
print(arr)

# 2-D lists
arr = [[0] * 4 for i in range(4)]
print(arr)
print(arr[0][0], arr[3][3])

for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i][j], " ", end='') # flag end e non va piu lo spazio
    print("")
"""
"""
### STRINGS

s = "abc"
print(s[0:2])

#s[0] = "A" # like arrays but are immutable

s += "def"
print(s)

print(int("123") + int("123")) #top
print(str(123) + str(123))

print(ord("a")) #ascii
print(ord("b"))

strings = ["ab", "cd", "ef"]
print("".join(strings))

"""
"""
###QUEUE
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)

queue.popleft()
print(queue)

queue.appendleft(1)
print(queue)

queue.pop()
print(queue)
"""
"""
# HashSet
mySet = set()

mySet.add(1)
mySet.add(2)
print(mySet)
print(len(mySet))

print(1 in mySet)
print(2 in mySet)
print(3 in mySet)

mySet.remove(2)
print(2 in mySet)

# list to set
print(set([1, 2, 3]))


mySet = { i for i in range(5) }
print(mySet)
"""
"""
### HashMap

MyMap = {}
MyMap["alice"] = 88
MyMap["bob"] = 77
print(MyMap)
print(len(MyMap))


MyMap["alice"] = 80
print(MyMap["alice"])

print("alice" in MyMap)
MyMap.pop("alice")
print("alice" in MyMap)

myMap = { "alice": 90, "bob": 70 }
print(myMap)

myMap = { i: 2*i for i in range(3) }
print(myMap)

myMap = { "alice": 90, "bob": 70 }
for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)
"""
"""
### TUPLES
# Tuples are like arrays but immutable
tup = (1, 2, 3)
print(tup)
print(tup[0])
print(tup[-1])

myMap = { (1,2): 3 }
print(myMap[(1,2)])

mySet = set()
mySet.add((1, 2))
print((1, 2) in mySet)

# Lists can't be keys
# myMap[[3, 4]] = 5  
"""
import heapq

# under the hood are arrays
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# Min is always at index 0
print(minHeap[0])

while len(minHeap):
    print(heapq.heappop(minHeap))

# No max heaps by default, work around is
# to use min heap and multiply by -1 when push & pop.
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

# Max is always at index 0
print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

# Build heap from initial values
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))