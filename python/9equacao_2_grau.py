import math
import cmath

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = b * b - (4 * a * c)
x1 = (b * (-1) + cmath.sqrt(delta)) / 2 * a
x2 = (b * (-1) - cmath.sqrt(delta)) / 2 * a


print(f"As raízes da equação {a}x²+{b}x+{c}=0 são: x'= {x1} x''= {x2}.")
