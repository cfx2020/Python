# Name:华摄转换
# function:华氏度和摄氏度相互转换
# Time:2021\1\18

print('1.华氏度转换为摄氏度')
print('2.摄氏度转换为华氏度')
ms = int(input('请选择你需要的转换模式数字'))
if ms == 1:
    f = float(input('请输入华氏度'))
    c = (f-32)/1.8
    print('{:.1f}华氏度={:.1f}摄氏度'.format(f, c))
elif ms == 2:
    c = float(input('请输入摄氏度'))
    f = c*1.8+32
    print('{:.1f}摄氏度={:.1f}华氏度'.format(c, f))
else:
    print('请输入正确的数字模式')
