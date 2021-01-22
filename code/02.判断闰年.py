# Name:判断闰年
# function:判断一个年份是不是闰年。是就输出true，不是就输出false
# Time:2020\1\21

year = int(input("请输入待判断年份"))
output = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(output)

'''
另一种方法:
year=int(input("请输入待判断年份"))
if year % 4 == 0 and year % 100 != 0 or year %400 ==0:
    print(True)
else:
    print(False)
'''
