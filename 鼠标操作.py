# 鼠标操作
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import pyautogui

action = ActionChains

ScreenWidth, screenHeight = pyautogui.size()  # 屏幕尺寸
print("屏幕尺寸 =", screenHeight, ScreenWidth)
mouseX, MouseY = pyautogui.position()  # 鼠标坐标位置
print('当前鼠标位置 =', mouseX, MouseY)
# 位置
topaskpx = (394,545)
response = (768,924)
box = (567,320)
submit = (1361,704)
time.sleep(0.8)
#pyautogui.moveTo(498,578, duration=0.25)

# 复制粘贴
def auto():
    pyautogui.PAUSE = 0.7  # 函数执行后停顿x秒
    pyautogui.FAILSAFE = True  # 自动防故障
    pyautogui.click()
    pyautogui.moveTo(400,547,duration=0.15)
    pyautogui.tripleClick()
    pyautogui.hotkey('ctrl','c')
    pyautogui.moveTo(response,duration=0.1)
    pyautogui.click()
    pyautogui.moveTo(box)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.moveTo(submit)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'w')
def nextauto():
    pyautogui.moveTo(407,609)
    pyautogui.moveRel(0, 180, duration=0.15)
auto()
nextauto()