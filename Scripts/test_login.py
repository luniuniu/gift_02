import sys, os, pytest, time,allure
sys.path.append(os.getcwd())
from Page.dev_title import Dev_login
from Base.init_driver import get_driver
from Base.read_data import Op_Data

def get_data():
    data_list = []
    data = Op_Data("dev_login_data.yml").read_yaml().get("Dev_login")
    for i in data:
        data_list.append((i.get("login_data").get("email"),
                          i.get("login_data").get("pwd"),
                          i.get("login_data").get("expec")))
    return data_list

class Test_Dev_Login:

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def setup_class(self):
        self.DL = Dev_login(get_driver("io.manong.developerdaily","io.toutiao.android.ui.activity.MainActivity"))
        # 处理弹窗方法
        self.DL.click_update_alert()
        # 点击我的方法
        self.DL.click_my_btn()
        # 点击登陆注册
        self.DL.click_login_sign_btn()
        # 使用邮箱登陆方法
        self.DL.select_email_sign_btn()

    def teardown_class(self):
        self.DL.driver.quit()

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER
    def get_screen(self):
        self.DL.driver.get_screenshot_as_file("./Screen/%s.png"% time.time())
        allure.attach('描述','这里可以截图')


    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title='第一个测试')
    @pytest.mark.parametrize("email, pwd, expect",get_data())
    def test_login(self, email, pwd, expect):

        # 使用输入用户名 密码方法
        self.DL.input_login_info(email, pwd)
        # 使用点击登陆按钮方法
        self.DL.click_login_email_btn()
        allure.attach('描述','已经点击登录')
        assert expect == self.DL.get_login_text(), self.get_screen()
