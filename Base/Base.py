from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self, driver):
        # 初始化driver -- 供find_element 和 find_elements使用
        self.driver = driver

    def search_element(self, loc, timeout=15):
        """
        定位单个元素 - 显示等待
        :param loc: 元祖 (定位类型，类型属性值) 例子:(By.ID,"com.xx.xx")
        :return: 定位对象
        """
        return WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(*loc))
    def search_elements(self, loc, timeout=15):
        """
        定位单个元素 - 显示等待
        :param loc: 元祖 (定位类型，类型属性值) 例子:(By.ID,"com.xx.xx")
        :return: 定位对象
        """
        return WebDriverWait(self.driver, timeout).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc):
        """
        点击元素
        :param loc:
        :return:
        """
        self.search_element(loc).click()
    def input_element(self, loc, text):
        """
        输入内容
        :param loc:
        :param text: 输入的文本
        :return:
        """
        input_text = self.search_element(loc)
        input_text.clear()
        input_text.send_keys(text)