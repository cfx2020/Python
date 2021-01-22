# Name:斐波拉契数列
# function:生成斐波拉契数列的前20个数
# Time:2020\1\21

n1=1
n2=1
print(n1)
print(n2)
for i in range(18):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3