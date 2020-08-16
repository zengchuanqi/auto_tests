import pytest
from wechat_web.comment.base import Base
from wechat_web.page.index import Index


class TestIndex:
    def setup(self):
        self.index = Index(reuse=True)

    # 添加成员
    def test_add_member(self):
        member_msg = {'name': 'aa', 'english_name': 'bb', 'acctid': '125456', 'gender': '男', 'mobile': '1501327456'
            , 'telephone': '7615439', 'email': '15235211@qq.com', 'address': '中国'}
        self.index.add_member().add_member(member_msg)

    # 导入成员
    def test_import_contact(self):
        self.index.import_contact().import_contact()

    # 消息群发
    def test_mass_message(self):
        self.index.mass_message().mass_message()
