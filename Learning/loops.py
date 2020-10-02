# if

greeting = "Good Morning"
a = 4
if a == 4:
    print("Good Evening")
#    print("Second Line")
else:
    print(greeting)

# for loop

obj = [11, 12, 13, 14, 15]
for i in obj:
    print(i)
print("************")
# sub of 5 natural numbers 1+2+3+4+5=15
summation = 0
for j in range(1, 6):  # range(i,j) -> i to j-1
    summation = summation + j
#    print(j)
print(summation)
print("************")

for k in range(0, 10, 2): # from to with index diff
    print(k)
print("************")

for l in range(10):
    print(l)