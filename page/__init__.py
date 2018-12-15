# 登录链接
from selenium.webdriver.common.by import By

login_a = By.LINK_TEXT, "登录"
login_username = By.NAME, "username"
login_pwd = By.ID, "password"
login_verify_code = By.ID, "verify_code"
login_btn = By.NAME, "sbtbutton"
login_error_btn = By.CLASS_NAME, "layui-layer-btn0"