# encoding: utf-8
#!/usr/bin/python
import HTMLTestRunner
import unittest
from DMP.testcase import case1

suite=unittest.TestSuite()
suite.addTest(case1.Case1("test"))

unittest.TextTestRunner().run(suite)

