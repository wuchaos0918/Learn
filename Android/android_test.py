# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-9-17 11:59
# @Project : Learn.py
# @File    : android_test.py


from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey

desired_caps = {
    'platformName': 'Android',  # 被测手机是安卓
    'platformVersion': '8.1.0',  # 手机安卓版本
    'deviceName': 'xxx',  # 设备名，安卓手机可以随意填写
    'appPackage': 'tv.danmaku.bili',  # 启动APP Package名称
    'appActivity': 'MainActivityV2',  # 启动Activity名称
    'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
    'resetKeyboard': True,  # 执行完程序恢复原来输入法
    'noReset': True,  # 不要重置App
    'newCommandTimeout': 6000,
    'automationName': 'UiAutomator2'
    # 'app': r'd:\apk\bili.apk',
}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 设置缺省等待时间
driver.implicitly_wait(5)

# 如果有`青少年保护`界面，点击`我知道了`
message_young = driver.find_elements_by_id("text3")
if message_young:
    message_young.click()

# 根据id定位搜索位置框，点击
driver.find_element_by_id("expand_search").click()

# 根据id定位搜索输入框，点击
sub_box = driver.find_element_by_id('search_src_text')
sub_box.send_keys('白月黑羽')
# 输入回车键，确定搜索
driver.press_keycode(AndroidKey.ENTER)

# 选择（定位）所有视频标题
titles = driver.find_elements_by_id("title")

for ele in titles:
    # 打印标题
    print(ele.text)

input('**** Press to quit..')
driver.quit()
