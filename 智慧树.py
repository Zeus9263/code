import time

from PIL.ImImagePlugin import number
from selenium import webdriver

driver = webdriver.Chrome()
# 登陆页面
driver.get("https://passport.zhihuishu.com/login?service=https://onlineservice.zhihuishu.com/login/gologin")
driver.maximize_window()

time.sleep(3)


# 登陆
def login(number, password):
    phone_number = driver.find_element("id", "lUsername")
    pwd = driver.find_element("id", "lPassword")
    login_btn = driver.find_element_by_class_name("wall-sub-btn")
    phone_number.send_keys("17585409952")
    pwd.send_keys("L20020715l")
    login_btn.click()
    time.sleep(10)

def video(watch):
    watch = driver.find_element_by_class_name('courseName')
    watch.click()

if __name__ == '__main__':
    '''
    number=''#手机号码
    password=''#密码
    key=''#课程名称，可以部分名字

    '''


def password(args):
    pass


login(number,password)


def watch(args):
    pass


video(watch)