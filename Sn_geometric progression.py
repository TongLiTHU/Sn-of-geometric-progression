"""
Created on Mon Nov 16 14:08:24 2020

@author: TONG
"""
#!/usr/bin/python3

str = "等比数列前n项和计算器"
print (str.center(80, '*'))

b = a = int(input("请输入等比数列的首项："))
q = int(input("请输入等比数列的公比："))

if (b == 0 & q == 0):
    print("提示：等比数列的首项和公比均不能为0")
    b = a = int(input("请输入一个不为0的首项："))
    q = int(input("请输入一个不为0的公比："))
       
if (b != 0 & q == 1):
    n = int(input("请输入项数n："))
    print("首项为 %d 公比为 1 的等比数列前 %d 项之和为: %d" % (b,n,n*b)) #每个%d（十进制整数）对应后面一个数

else:
    n = int(input("请输入项数n："))
    sum = 0
    counter = 10
    while counter <= n:
          sum = sum + a
          a = a * q
          counter += 1
    
str = "计算结果"
print (str.center(80, '*'))
print("首项为 %d 公比为 %d 的等比数列前 %d 项之和为: %d" % (b,q,n,sum)) #每个%d（十进制整数）对应后面一个数


    
