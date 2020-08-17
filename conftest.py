#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:conftest.py
# @time:2020/8/16 4:47 下午

import pytest

@pytest.fixture(scope='package')
def driver_setings():
    des = {
        'platformName': 'Android',
        'platformVersion': '8.0',
        'deviceName': 'Samsung Galaxy S9',
        'appPackage': 'com.android.calculator2',
        'appActivity': '.Calculator',
        'udid': '192.168.56.101:5555',
        'noReset': True,
        'unicodeKeyboard': True,
        'resetKeyboard': True,
    }
    return des