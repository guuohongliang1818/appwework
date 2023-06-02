# 姓名：郭宏亮
# 时间：2023/5/11 8:50
import pytest


# 夹具要和yield连用，来实现前置和后置操作，同时也能控制前置和后置操作的使用范围
# 通过scope参数来灵活控制家具的使用范围
# 和return连用不能控制操作范围，意义不大


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的用例名name和用例标识nodeid的中文信息显示在控制台上
    """
    for i in items:
        i.name = i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid = i.nodeid.encode("utf-8").decode("unicode_escape")
