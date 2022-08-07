# 自动点击
import time as t


def auto():
    while 1:
        time.sleep(3)
        # pyautogui.moveRel(680, 0, duration=1.5)
        # pyautogui.click(button='left')
        #
        # pyautogui.moveRel(-680, 0, duration=1.5)
        # pyautogui.click(button='left')
        # time.sleep(30)


class Timer:
    def __init__(self):
        self.unite = ['年', '月', '天', '小时', '分钟', '秒']
        self.prompt = "未开始计时！"
        self.lasted = []
        self.begin = 0
        self.end = 0

    # 魔法方法
    def __str__(self):
        return self.prompt

    __repr__ = __str__

    # 计时加运算
    def __add__(self, other):
        prompt = "总共计时时间："
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unite[index])
        return prompt

    # 开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = "提示：请先调用stop() 停止计时！！！！"
        print("计时开始！")

    # 停止计时
    def stop(self):
        if not self.begin:
            print("提示：请先调用star() 开始计时！！！！！")
        else:
            self.end = t.localtime()
            self._calc()
            print("计时结束！")

    # 内部方法，计算差值
    def _calc(self):
        self.lasted = []
        self.prompt = "计时时间："
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unite[index])

        # 为下次计时，进行初始化
        self.begin = 0
        self.end = 0

t1 = Timer()
t1.start()
t.sleep(1)
t1.stop()
