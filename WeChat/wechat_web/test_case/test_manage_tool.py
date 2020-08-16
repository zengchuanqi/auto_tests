from wechat_web.page.Manage_Tool import ManageTool


class TestManageTool:
    def setup(self):
        self.manage = ManageTool(reuse=True)

    # 素材库
    def test_material(self):
        self.manage.material()
