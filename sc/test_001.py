#使用yml读取文件


import yaml
def test_001():

    #第一个参数是要读取那个地方的文件,第二个是代表读,第三个是设置字符集
    with open("data.yml", "r", encoding='UTF-8') as f:
        # 第一个值是读的对象        注:5.1版本后的python读取文件需要加Loader=yaml.FullLoader,之前的就不用了
        data = yaml.load(f, Loader=yaml.FullLoader)
        print(data)
        #之后读取配置文件中的内容
        print(data.get("animal"))

        #之后是读取数组中的第一个内容
        print("数组中的第一个内容:",data.get("anima").get("ke1"))
        #之后读取列表
        print("python列表:",data.get("animals"))
        print("字符串",data.get("value"))

        #输出布尔值
        print("正确",data.get("value1"))
        print("错误",data.get("value2"))

        #整数和浮点数
        print("整数",data.get("value3"))
        print("浮点数",data.get("value4"))


        #Null和None都是为空的意思
        print("Null",data.get("value5"))
        print("None",data.get("value6"))


        #日期
        print("日期",data.get("value7"))
        print("日期和时分秒",data.get("value8"))

        #输出登陆一组里面的每一个账号和密码  总共三条    先第一条
        print("test:",data.get("Test_Login").get("login_data01"))
        print("test_name",data.get("Test_Login").get("login_data01").get("name"))
        print("test_pwd", data.get("Test_Login").get("login_data01").get("pwd"))
        print("test_code", data.get("Test_Login").get("login_data01").get("code_info"))


        #第二条
        print("test:", data.get("Test_Login").get("login_data02"))
        print("test_name", data.get("Test_Login").get("login_data02").get("name"))
        print("test_pwd", data.get("Test_Login").get("login_data02").get("pwd"))
        print("test_code", data.get("Test_Login").get("login_data02").get("code_info"))


        #第三条
        print("test:", data.get("Test_Login").get("login_data03"))
        print("test_name", data.get("Test_Login").get("login_data03").get("name"))
        print("test_pwd", data.get("Test_Login").get("login_data03").get("pwd"))
        print("test_code", data.get("Test_Login").get("login_data03").get("code_info"))



    return data

if __name__ == '__main__':
    t = test_001()