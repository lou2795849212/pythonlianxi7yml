#之后导入添加用户的类
from Page.add_user_page import Add_User_Phone

class Page_O:
    #之后初始化
    def __init__(self,driver):
        self.driver = driver


    #之后声明添加用户类的对象
    def return_add_user(self):
        return Add_User_Phone(self.driver)