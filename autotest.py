from selenium import ActionChains
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get = ("https://www.baidu.com/")
driver.maximize_window()
sleep(3)
print(driver.name)
# 2.定位到要悬停的元素
dw = driver.find_element("id", "s-usersetting-top")

# 3.对定位到的元素执行鼠标悬停操作
ActionChains().move_to_element(dw).perform()

# 找到链接
# elem1 = driver.find_element_by_link_text("搜索设置")
# elem1.click()

# 通过元素选择器找到id=sh_2,并点击设置
# elem2 = driver.find_element_by_id("sh_1")
# elem2.click()

# 保存设置
# elem3 = driver.find_element_by_class_name("prefpanelgo")
# elem3.click()
