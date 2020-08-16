import pytest

from test_xueqiu.page.index import Index
from test_xueqiu.page.my import My


class TestMy:
    my = My()

    def test_login_in(self):
        self.my.login_in()