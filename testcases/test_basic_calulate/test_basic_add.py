#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:test_basic_add.py
# @time:2020/8/16 5:12 下午

import pytest
import allure

@allure.epic('[epic]计算器APP')
@allure.feature('[feature]TestBasicAdd模块')
class TestBasicAdd():
    @pytest.mark.systemtest
    @pytest.mark.run(order=2)
    @allure.story('[story]计算器加法测试')
    @allure.title('[title][case01]计算7+9')
    def test_basic_add_case01(self,start_app):
        self.driver = start_app
        self.driver.find_element_by_xpath('//android.widget.Button[@text=7]').click()
        self.driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.android.calculator2:id/op_add"]').click()
        self.driver.find_element_by_xpath('//android.widget.Button[@text=9]').click()
        self.driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.android.calculator2:id/eq"]').click()
        actual_reslut = self.driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.android.calculator2:id/result"]').text
        assert actual_reslut.__eq__('16')

    @pytest.mark.systemtest
    @pytest.mark.run(order=4)
    @allure.story('[story]计算器加法测试')
    @allure.title('[title][case02]计算3+6')
    def test_basic_add_case02(self,start_app):
        self.driver = start_app
        self.driver.find_element_by_xpath('//android.widget.Button[@text=3]').click()
        self.driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.android.calculator2:id/op_add"]').click()
        self.driver.find_element_by_xpath('//android.widget.Button[@text=6]').click()
        self.driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.android.calculator2:id/eq"]').click()
        actual_reslut = self.driver.find_element_by_xpath(
            '//android.widget.TextView[@resource-id="com.android.calculator2:id/result"]').text
        assert actual_reslut.__eq__('9')