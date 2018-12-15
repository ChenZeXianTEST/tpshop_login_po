import time

import pytest
import os
import sys
sys.path.append(os.getcwd())
from base.read_yaml import ReadYaml


from base.get_driver import get_driver
from page.page_login import PageLogin


def get_data():
    list1 = []
    for data in ReadYaml("data_login.yaml").read_yaml_data().values():
        list1.append((data.get("username"), data.get("password"), data.get("number")))

    return list1

class TestLogin():

    def setup_class(self):
        self.login = PageLogin(get_driver())
        self.login.driver.maximize_window()

    def teardown_class(self):
        time.sleep(2)
        self.login.driver.quit()

    @pytest.mark.parametrize("username, password, number", get_data())
    def test_login(self, username, password, number):
        self.login.page_click_login_a()
        self.login.page_input_username(username)
        self.login.page_input_pwd(password)
        self.login.page_input_verify_code(number)
        self.login.page_login_btn_click()
        self.login.page_error_btn()
