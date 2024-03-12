# laboratorio 1 - ejercicio 3
import math

# version con for
# overflow
a = 1.
for idx in range(10000):
    a = 2*a
    if math.isinf(a):
        print(idx)
        break
# underflow
a = 1.
for idx in range(10000):
    a = a/2
    if a==0:
        print(-idx)
        break
    
# version con while
a = 1.
idx = 0
while not math.isinf(a):
    idx = idx + 1
    a = 2*a
print(idx-1)

a = 1.
idx = 0
while not a==0:
    idx = idx + 1
    a = a/2
print(-idx+1)
