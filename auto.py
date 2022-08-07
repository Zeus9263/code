from selenium import webdriver
import time
from time import sleep

from selenium import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.qzone.qq.com/")
driver.maximize_window()
# driver.refresh()
print(driver.name)
# 元素定位法
driver.switch_to.frame('login_frame')
zhanghao = driver.find_element_by_id('switcher_plogin')
zhanghao.click()  # .send_keys("selenium")
driver.find_element("id", "u").send_keys("806229263")
# driver.find_element("id","u").send_keys("3327799750")
# searchElement.send_keys("Hello World!")
# huiche.click()
driver.find_element_by_id("p").send_keys("tao806229263")
# driver.find_element_by_id("p").send_keys("18286664672lhy")
time.sleep(2)
djdl = driver.find_element_by_id('login_button')
djdl.click()
# searchElement.send_keys(Keys.CONTROL,'a')
# searchElement.send_keys(Keys.CONTROL,'c')
# searchElement.send_keys("abcde")
# huiche.click()
time.sleep(2)
# searchElement.send_keys(Keys.CONTROL,'a')
# searchElement.send_keys(Keys.BACKSPACE)
print(driver.current_url)
time.sleep(2)
xzss = driver.find_element_by_link_text("说说")
xzss.click()
sleep(3)
xzly = driver.find_element_by_link_text("留言板")
xzly.click()
# searchElement.send_keys("123")
# huiche.click()
# driver.implicitly_wait(2)  # 隐式等待2秒
# searchButtonElement = driver.find_element("partial link text","必读").click()

# ActionChainsDriver = ActionChains().click()
# ActionChainsDriver.perform()  # 执行鼠标点击
# .find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
time.sleep(5)  # 等待5秒
# driver.quit()  # 退出
