#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:conftest.py
# @time:2020/8/16 4:54 下午

import time
import pytest
from appium import webdriver

driver = None

@pytest.fixture()
def start_app(driver_setings):
    global driver
    driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', driver_setings)
    return driver

@pytest.fixture(autouse=True)
def close_app():
    yield driver
    time.sleep(2)
    driver.close_app()