from selenium.webdriver.common.by import By

"""
    管理页面元素
"""
# 弹窗处理
update_alert = (By.XPATH, "//*[contains(@text,'下次再说')]")
"""
    首页
"""
# 我的
my_btn = (By.XPATH, "//*[contains(@resource-id,'io.manong.developerdaily:id/tv_tab_title') and contains(@text,'我的')]")

"""
    我的页面
"""
# 登陆/注册
login_sign_btn = (By.ID, "io.manong.developerdaily:id/login_btn")
"""
    登陆选择页面
"""
# 选择邮箱登陆/注册
select_email_login_sign = (By.ID, "io.manong.developerdaily:id/btn_email")
"""
    邮箱登陆页面
"""
input_login_email = (By.ID, "io.manong.developerdaily:id/edt_email")
input_login_pwd = (By.ID, "io.manong.developerdaily:id/edt_password")
login_email_btn = (By.ID, "io.manong.developerdaily:id/btn_login")

"""
    登陆成功个人信息页面
"""
# 设置
person_info_setting = (By.ID, "io.manong.developerdaily:id/nav_btn_setting")
# 登陆成功用户头像
person_icon = (By.ID, "io.manong.developerdaily:id/nav_img_avatar")
"""
    设置页面
"""
setting_page_logout = (By.ID, "io.manong.developerdaily:id/btn_logout")
"""
     弹窗页面
"""
alert_quit_btn = (By.ID, "io.manong.developerdaily:id/md_buttonDefaultPositive")