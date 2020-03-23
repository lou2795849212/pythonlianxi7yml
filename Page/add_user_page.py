#之后先导入基本的Base类
from Base.Base import Base
#之后初始化好的参数
import Page,time

class Add_User_Phone(Base):
    #之后先初始化
    def __init__(self,driver):
        Base.__init__(self,driver)


    #之后先定位点击添加用户按钮
    def add_user_btn(self):
        self.click_element(Page.add_click)

    #之后输入用户名和手机号
    def add_username_phone(self,name,phone):
        #添加姓名
        self.input_element(Page.add_user_name,name)
        #添加手机号
        self.input_element(Page.add_user_phone,phone)
        #之后点击保存按钮
        self.click_element(Page.add_save_click)
        #之后等待5秒
        time.sleep(5)
        #之后点击home建返回
        self.driver.keyevent(4)