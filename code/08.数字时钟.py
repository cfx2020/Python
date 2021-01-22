# Name:数字时钟
# Function:形成类似数显表的效果
# Time:2020\1\22

from time import sleep
# 定义数字时钟类名
class Clock(object):
    #方法初始化
    def __init__(self,hour=0,minute=0,second=0):
        self._hour=hour
        self._minute=minute
        self._second=second
    #走字
    def run(self):
        self._second +=1
        if self._second ==60:
            self._minute +=1
            if self._minute==60:
                self._hour +=1
                if self._hour ==24:
                    self._hour=0
    #显示时间
    def show(self):
        return (f'{self._hour}:{self._minute}:{self._second}')

def main():
    clock=Clock(00,00,00)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()
if __name__=='__main__':
    main()       