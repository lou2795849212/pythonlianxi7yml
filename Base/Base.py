#先新建一个类
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    #之后先初始化 ,需要传一个参数driver
    def __init__(self,driver):
        self.driver = driver

    #之后声明一个定位点击元素的方法,并且使用显示等待
    def find_element(self,loc,timeout=10,poll=0.5):
        #之后使用显示等待
     return   WebDriverWait(self.driver,timeout,poll).until(lambda x: x.find_element(*loc))


    #之后声明一个基本的点击类型
    def click_element(self,loc):
        self.find_element(loc).click()

    #之后声明一个基本的输入操作
    def input_element(self,loc,text):
     input = self.find_element(loc)
     input.clear() #避免有默认值
     input.send_keys(text)