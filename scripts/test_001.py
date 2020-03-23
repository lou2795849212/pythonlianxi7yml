import pytest,allure

class Test_Abc:

    #添加测试步骤
    @allure.step(title="测试步骤001")
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_001(self):
        #添加测试描述
        allure.attach('描述', '我是测试步骤001的描述～～～')
        assert 0
    #添加测试步骤
    @allure.step(title="测试步骤002")
    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_002(self):
        # 添加测试描述
        allure.attach('描述', '我是测试步骤002的描述～～～')
        assert 1

if __name__ == '__main__':
    pytest.main(["-s --alluredir ../report"],"test_001.py")