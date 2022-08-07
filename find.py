# coding:utf-8
import time
from selenium import webdriver
import unittest


# 引用封装后的日志系统
def TestLog():
    """

    :rtype: object
    """
    pass


log = TestLog().getlog()


class BaiBu(unittest.TestCase):
    u"""【百度.类】"""

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get("http://www.baidu.com")
        self.browser.implicitly_wait(10)
        # self.base = Screen(self.browser)

    def tearDown(self):
        self.browser.quit()

    def test_search(self):
        u"""采用id,class,name等属性识别元素"""
        # <input id="kw" name="wd" class="s_ipt" value="" length="255" autocomplete="off">
        # <input id="su" value="百度一下" class="bg s_btn" type="submit">
        # 识别id属性
        self.browser.find_element_by_id("kw").send_keys("python")
        self.browser.find_element_by_id("su").submit()
        print(self.browser.title)
        self.assertEqual(self.browser.title, u"百度一下，你就知道")
        log.info("识别id属性，执行[find_element_by_id]")

        time.sleep(3)

        # 识别name属性 <input id="su" value="百度一下" class="bg s_btn" type="submit">
        self.browser.find_element_by_name("wd").clear()  # 清空原关键字
        self.browser.find_element_by_name("wd").send_keys("python logging")
        # class属性是比较特殊的一个，属性值可以有多个，中间是用空格隔开的
        # self.browser.find_element_by_class_name("bg s_btn").submit()  #使用class_name会报错
        # self.browser.find_element_by_class_name("s_btn").submit()      #第一种解决办法：class值取其中之一
        # self.browser.find_element_by_class_name("bg").submit()          #第一种解决办法：class值取其中之一
        self.browser.find_element_by_css_selector(".bg.s_btn").submit()  # 第二种解决办法：使用css.selector，每个class值前面加.
        log.info("识别name属性，执行[find_element_by_name]")
        time.sleep(3)

        # 识别class属性
        self.browser.find_element_by_name("wd").clear()  # 清空原关键字
        self.browser.find_element_by_class_name("s_ipt").send_keys("selenium webserver")
        self.browser.find_element_by_class_name("s_btn").submit()
        log.info("识别class属性，执行[find_element_by_class_name]")
        time.sleep(3)

    def test_xpath(self):
        u"""采用xpath识别元素"""
        self.browser.find_element_by_xpath(".//*[@id='kw']").send_keys("xpath test")  # 采用id
        self.browser.find_element_by_xpath(".//*[@id='su']").submit()  # 采用id
        log.info("采用xpath识别页面中的属性，[id]")

        self.browser.find_element_by_xpath(".//*[@name='wd']").clear()  # 清空原关键字        #采用name
        self.browser.find_element_by_xpath(".//*[@class='s_ipt']").send_keys("selenium auto test")  # 采用class
        self.browser.find_element_by_xpath(".//*[@type='submit']").submit()  # 采用type
        log.info("采用xpath识别页面中的属性，[class、type]")


if __name__ == "__main__":
    unittest.main()
