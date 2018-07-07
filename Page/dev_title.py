from Base.Base import Base
import Page

class Dev_login(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)
        # 获取屏幕宽高 'width', 'height'
        self.screen_size = self.driver.get_window_size()
    def click_update_alert(self):
        # 点击更新弹窗
        self.click_element(Page.update_alert)

    def click_my_btn(self):
        # 点击下方我的菜单按钮
        self.click_element(Page.my_btn)
    def click_login_sign_btn(self):
        # 点击登陆/注册按钮
        self.click_element(Page.login_sign_btn)
    def select_email_sign_btn(self):
        # 选择邮箱登陆/注册
        self.click_element(Page.select_email_login_sign)
    def input_login_info(self, email, pwd):
        # 输入用户名和密码
        self.input_element(Page.input_login_email, email)
        self.input_element(Page.input_login_pwd, pwd)
    def click_login_email_btn(self):
        # 点击登陆按钮
        self.click_element(Page.login_email_btn)

    def get_login_text(self):
        # 返回登陆文本
        return self.search_element(Page.login_email_btn).text
    def scroll_up(self):
        # 向上滑动页面
        try:
            self.search_element(Page.person_icon)
            # 屏幕80% -> 30%
            self.driver.swipe(self.screen_size.get("width")*0.5,self.screen_size.get("height")*0.8,
                              self.screen_size.get("width") * 0.5, self.screen_size.get("height") * 0.3, 1000)
        except Exception as e:
            print(e)
            return False
    def scroll_down(self):
        # 向下滑动页面
        try:
            self.search_element(Page.person_info_setting)
            # 屏幕30% -> 80%
            self.driver.swipe(self.screen_size.get("width") * 0.5, self.screen_size.get("height") * 0.3,
                              self.screen_size.get("width") * 0.5, self.screen_size.get("height") * 0.8, 1000)
        except Exception as e:
            print(e)
            return False

    def click_setting_btn(self):
        # 点击个人中心设置按钮
        self.click_element(Page.person_info_setting)
    def click_page_logout_btn(self, type_out):
        # 点击设置页面退出登录按钮
        # type_out : 1 - 取消  2 - 退出
        self.click_element(Page.setting_page_logout)
        if type_out == 2:
            self.click_element(Page.alert_quit_btn)
