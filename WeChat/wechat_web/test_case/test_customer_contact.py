from wechat_web.page.customer_contact import Customer_contact


class TestManageTool:
    def setup(self):
        self.customer= Customer_contact(reuse=True)

    # 产品图册
    def test_productAlbum(self):
        self.customer.productAlbum()