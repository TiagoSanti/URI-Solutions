code1, num1, value1 = input().split()
code2, num2, value2 = input().split()

code1 = int(code1)
code2 = int(code1)
num1 = int(num1)
num2 = int(num2)
value1 = float(value1)
value2 = float(value2)

total = num1 * value1 + num2 * value2

print('VALOR A PAGAR: R$ {:.2f}'.format(total))
