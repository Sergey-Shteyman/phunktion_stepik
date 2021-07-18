# put your python code here
num1, num2, num3 = int(input()), int(input()), int(input())
if num1 < num2 + num3 and num2 < num3 + num1 and num3 < num1 + num2:
    print('YES')
else:
    print('NO')
