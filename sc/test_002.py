#使用yml写入文件,先导入yaml
import yaml


data = {'Search_Data': {
                'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
                'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}
with open("w_data0.yml", "w") as f:
    #第一个参数是要写入的数据,第二个是写的对象,第三个设置字符集为utf-8,第四个是开启字符码格式
    yaml.dump(data,f,encoding='utf-8',allow_unicode=True)