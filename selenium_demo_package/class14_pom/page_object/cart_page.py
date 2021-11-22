'''
    CartPage：购物车页面，校验商品是否添加成功
'''
from selenium_demo_package.class14_pom.base_page.base_page import BasePage


# 购物车页面
class CartPage(BasePage):
    # url
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/cart/index.html'
    # 关键元素
    goods = ('xpath', '//div[@class="goods-base"]')
    goods_counts_attr = ('value')

    # 行为:校验商品是否存在
    def cart_info(self):
        self.visit(self.url)
        self.sleep(1)
        self.wait(self.goods)
