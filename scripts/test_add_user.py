#先导入初始化类和公共的页面类
from Base.InitDriver import init_driver
from Page.PageObj import Page_O
import pytest,allure

class Test_Add_User:
    #之后先初始化
    def setup_class(self):
        self.driver = init_driver()
        self.obj_data = Page_O(self.driver).return_add_user()

    #销毁
    def teardown_class(self):
        #之后关闭
        self.driver.quit()


    #之后先点击添加用户按钮
    @pytest.fixture()
    @allure.step('我是测试步骤001')
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_001(self):
        allure.attach('描述', '我是测试步骤001的描述～～～')
        self.obj_data.add_user_btn()

    #之后开始输入用户信息
    @pytest.mark.usefixtures("test_001")
    @pytest.mark.parametrize("name,phone",[("lousifa1","13145111"),("lousifa2","22334546566")])
    def test_add_user(self,name,phone):
        self.obj_data.add_username_phone(name,phone)
