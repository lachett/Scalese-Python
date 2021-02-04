ax = int(input("quanto vale ax"))

bx = int(input("quanto vale bx"))

c = int(input("quanto vale c"))

import math

delta = pow(bx,2)-4*ax*c

if delta < 0:

    print("non ci sono soluzioni")

elif delta > 0:
    print(str("ci sono 2 soluzioni reali:"))
    print(int((-1*bx)-(math.sqrt(delta))) / (2*ax))
    print(int((-1*bx)+(math.sqrt(delya))) / (2*ax))
      
      
