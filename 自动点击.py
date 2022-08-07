# 自动点击
import time

import pyautogui
import time as t
import random
# class Timer:
#     def __init__(self):
#         self.unite = ['年', '月', '天', '小时', '分钟', '秒']
#         self.prompt = "未开始计时！"
#         self.lasted = []
#         self.begin = 0
#         self.end = 0
#
#     # 魔法方法
#     def __str__(self):
#         return self.prompt
#
#     __repr__ = __str__
#
#     # 计时加运算
#     def __add__(self, other):
#         prompt = "总共计时时间："
#         result = []
#         for index in range(6):
#             result.append(self.lasted[index] + other.lasted[index])
#             if result[index]:
#                 prompt += (str(result[index]) + self.unite[index])
#         return prompt
#
#     # 开始计时
#     def start(self):
#         self.begin = t.localtime()
#         self.prompt = "提示：请先调用stop() 停止计时！！！！"
#         print("计时开始！")
#
#     # 停止计时
#     def stop(self):
#         if not self.begin:
#             print("提示：请先调用star() 开始计时！！！！！")
#         else:
#             self.end = t.localtime()
#             self._calc()
#             print("计时结束！")
#
#     # 内部方法，计算差值
#     def _calc(self):
#         self.lasted = []
#         self.prompt = "计时时间："
#         for index in range(6):
#             self.lasted.append(self.end[index] - self.begin[index])
#             if self.lasted[index]:
#                 self.prompt += (str(self.lasted[index]) + self.unite[index])
#
#         # 为下次计时，进行初始化
#         self.begin = 0
#         self.end = 0
# t1 = Timer()
pyautogui.size()
print("屏幕大小:", pyautogui.size())
sizex, sizey = pyautogui.size()
def auto():

    # t1.start()
    w = True


    while w:
            time.sleep(3)
            i = random.randint(10, 34)
            print(i)
            pyautogui.moveRel(680, 70, duration=1.5)
            pyautogui.click(button='left')

            pyautogui.moveRel(-680, -70, duration=1.5)
            pyautogui.click(button='left')
            t.sleep(i)

# def s():
#     # coding:utf-8
#     from PIL import Image, ImageEnhance
#     import pytesseract
#     # 上面都是导包，只需要下面这一行就能实现图片文字识别
#     im = Image.open('merge_source.jpg')
#     # 下面为增强部分
#     enh_con = ImageEnhance.Contrast(im)
#     contrast = 1.5
#     image_contrasted = enh_con.enhance(contrast)
#     # image_contrasted.show()
#
#     # 增强亮度
#     enh_bri = ImageEnhance.Brightness(image_contrasted)
#     brightness = 1.5
#     image_brightened = enh_bri.enhance(brightness)
#     # image_brightened.show()
#     # 增强对比度
#     enh_col = ImageEnhance.Color(image_brightened)
#     color = 1.5
#     image_colored = enh_col.enhance(color)
#     # image_colored.show()
#     # 增强锐度
#     enh_sha = ImageEnhance.Sharpness(image_colored)
#     sharpness = 3.0
#     image_sharped = enh_sha.enhance(sharpness)
#     # image_sharped.show()
#
#     # 灰度处理部分
#     im2 = image_sharped.convert("L")
#     im2.show()
#     text = pytesseract.image_to_string(im2, lang='chi_sim').strip()  # 使用image_to_string识别验证码
#     print(text)
auto()
