"""
对parser中两个函数进行的必要单元测试
"""
import unittest
from unittest.mock import patch
from unittest import mock
from parser import ProcessError,ParserFile,ProcessTokens

class Test_test_1(unittest.TestCase):

    def setUp(self):
        print('每个用例执行前会调用setUp方法准备环境')

    def tearDown(self):
        print('进行环境清理')

    def test_ProcessError(self):
        with patch('builtins.print') as mocked_print:
            ProcessError()
            mocked_print.assert_called_with('Error!输入不符合语法规范\n')

    @mock.patch('parser.ParserLine')
    def test_ParserFile(self,mockpl):
        """测试其中的ParserLine函数是否被正确调用"""
        ParserFile("test.txt","Mr.Foo")#test.txt中有9行数据，其中第一行为注释
        self.assertEqual(mockpl.called,True)
        self.assertEqual(mockpl.call_count,8)
        
    def test_ProcessTokens(self):
        """测试分支处理是否根据tokens0正确进行"""
        with mock.patch('parser.ProcessStep') as mockps:
            ProcessTokens(['step','welcome'],'Mr.Foo')
            self.assertEqual(mockps.called,True)
        with mock.patch('parser.ProcessBranch') as mockpb:
            ProcessTokens(['branch','购票','purchaseProc'],'Mr.Foo')
            self.assertEqual(mockpb.called,True)

if __name__ == '__main__':
    unittest.main()
