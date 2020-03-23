from selenium.webdriver.common.by import By

#点击添加用户按钮
add_click = (By.ID,"com.android.contacts:id/floating_action_button")
#之后定位到输入姓名和电话使用xpath
add_user_name = (By.XPATH,"//*[contains(@text,'姓名')]")
add_user_phone = (By.XPATH,"//*[contains(@text,'电话')]")
#之后点击保存按钮
add_save_click = (By.ID,"com.android.contacts:id/menu_save")