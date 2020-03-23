from appium import webdriver

#封装初始化类
def init_driver():
    desired_caps = {}
    # 系统
    desired_caps['platformName'] = 'Android'
    # 版本
    desired_caps['platformVersion'] = '6.0'
    # 设备号
    desired_caps['deviceName'] = '192.168.89.101:5555'
    #不重置应用   true代表不重置,flase的话代表重制   默认是false
    desired_caps['noReset'] = 'true'
    # 包名
    desired_caps['appPackage'] = 'com.android.contacts'
    # 启动名
    desired_caps['appActivity'] = '.activities.PeopleActivity'

    # desired_caps['app'] = './xx.apk'

    # 注意：如果要发送中文，服务端启动参数需要配置：
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    # 声明手机驱动对象
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    return driver