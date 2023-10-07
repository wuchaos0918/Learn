# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-9-17 15:23
# @Project : Learn.py
# @File    : test01.py


from appium import webdriver
# 设置appium的配置
desired_caps = {}
# desired_caps['platformName'] = 'Android'    #手机类型
# desired_caps['platformVersion'] = '8.1.0'   #手机操作系统版本
# desired_caps['deviceName'] = '68U5T17A17006553'   #使用的手机或模拟器类型
# desired_caps['appPackage'] = 'com.android.bbkcalculator'   # 使用的apk包名
# desired_caps['appActivity'] = '.Calculator'              # 应用包名
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  #调用appium的驱动
desired_caps['platformName'] = 'Android'    #手机类型
desired_caps['platformVersion'] = '7.1.2'   #手机操作系统版本
desired_caps['deviceName'] = '127.0.0.1:62001'   #使用的手机或模拟器类型
desired_caps['appPackage'] = 'com.youdao.calculator'   # 使用的apk包名
desired_caps['appActivity'] = '.activities.MainActivity'              # 应用包名
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  #调用appium的驱动
# 滑动页面
driver.swipe(800,1000,100,1000)
driver.swipe(800,1000,100,1000)
driver.swipe(800,1000,100,1000)
# message_young = driver.find_elements_by_id("开启数学世界")
message_young = driver.find_element_by_id("com.youdao.calculator:id/guide_button")
if message_young:
    message_young.click()
# driver.find_element_by_name("开启数学世界").click()
# 定位元素
driver.find_element_by_name("9").click()
driver.find_element_by_name("6").click()
driver.find_element_by_name("8").click()
driver.find_element_by_name("4").click()
driver.find_element_by_name("6").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("9").click()
# 退出程序
driver.quit()