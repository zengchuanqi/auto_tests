import pytest
import yaml

from test_xueqiu.comment.base import Base
from test_xueqiu.page.index import Index




class TestIndex:
    def setup(self):
        self.index = Index()
    # 参数化驱动
    # @pytest.mark.parametrize('name,stoke', [('阿里巴巴', 'BABA'), ('baidu', 'BIDU')])
    @pytest.mark.parametrize('name,stoke', Base.yaml_load())
    def test_search(self,name,stoke):
        self.index.search(name,stoke)

    @pytest.mark.parametrize('name,stoke', Base.yaml_load())
    def test_searchs(self,name,stoke):
        self.index.wait_main().search(name,stoke)

    # def test_aa(self):
    #     self.index.goto_my().login_in()
