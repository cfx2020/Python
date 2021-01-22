# Name：圆计算
# function：根据半径计算圆的周长和面积
# Time：2020\1\21

r = float(input('请输入半径'))
per = 2*3.1416*r
area = 3.1416*r**2
print('圆的周长为{:.2f},圆的面积为{:.2f}'.format(per, area))
