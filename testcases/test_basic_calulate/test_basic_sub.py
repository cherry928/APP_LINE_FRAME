#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:test_basic_sub.py
# @time:2020/8/16 5:13 下午

import pytest
import allure

pytestmark=pytest.mark.skip('跳过减法整个模块')
@allure.epic('[epic]计算器APP')
@allure.feature('[feature]TestBasicSub模块')
class TestBasicSub:
    @pytest.mark.systemtest
    @pytest.mark.run(order=3)
    @allure.story('[story]计算器减法测试')
    @allure.title('[title][case01]计算11-7')
    def test_basic_add_case01(self,start_app):
        self.driver = start_app
        self.driver.find_element_by_xpath('//android.widget.Button[@text=1]').click()
        self.driver.find_element_by_xpath('//android.widget.Button[@text=1]').click()
        self.driver.find_element_by_xpath(
            '//android.widget.Button[@resource-id="com.android.calculator2:id/op_sub"]').click()
        self.driver.find_element_by_xpath('//android.widget.Button[@text=7]').click()
        self.driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.android.calculator2:id/eq"]').click()
        actual_reslut = self.driver.find_element_by_xpath(
            '//android.widget.TextView[@resource-id="com.android.calculator2:id/result"]').text
        assert actual_reslut.__eq__('4')

    @pytest.mark.systemtest
    @pytest.mark.run(order=1)
    @allure.story('[story]计算器减法测试')
    @allure.title('[title][case02]计算9-6')
    def test_basic_add_case02(self,start_app):
        self.driver = start_app
        self.driver.find_element_by_xpath('//android.widget.Button[@text=9]').click()
        self.driver.find_element_by_xpath(
            '//android.widget.Button[@resource-id="com.android.calculator2:id/op_sub"]').click()
        self.driver.find_element_by_xpath('//android.widget.Button[@text=6]').click()
        self.driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.android.calculator2:id/eq"]').click()
        actual_reslut = self.driver.find_element_by_xpath(
            '//android.widget.TextView[@resource-id="com.android.calculator2:id/result"]').text
        assert actual_reslut.__eq__('3')