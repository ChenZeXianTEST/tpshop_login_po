import page
from base.base import Base


class PageLogin(Base):

    def page_click_login_a(self):
        self.base_click_element(page.login_a)

    def page_input_username(self, test):
        self.base_input(page.login_username, test)

    def page_input_pwd(self, test):
        self.base_input(page.login_pwd, test)

    def page_input_verify_code(self, test):
        self.base_input(page.login_verify_code, test)

    def page_login_btn_click(self):
        self.base_click_element(page.login_btn)

    def page_error_btn(self):
        self.base_click_element(page.login_error_btn)