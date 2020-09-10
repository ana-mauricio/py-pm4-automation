# -*- coding: utf-8 -*-

import pytest
from py_pm4_automation.skeleton import fib
from unittest import TestLoader, TestSuite, TestCase
# from HtmlTestRunner import HTMLTestRunner
# from admin.test_TCP4_761 import TCP4_761
import os
import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

__author__ = "amauricio"
__copyright__ = "amauricio"
__license__ = "mit"

direct = os.getcwd()

def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)

@pytest.mark.my_suite
class ClassTest(TestCase):
     def test_case_compare(self):
        logging.info('Step 1: Load Login page')
        print('my comment is very large')
        self.assertEqual(2, 2)

     def test_case_equal(self):
        self.assertTrue(True)

# COMPOSE SUITE
#example_tests = TestLoader().loadTestsFromTestCase(ClassTest)
#my_tests = TestLoader().loadTestsFromTestCase(TCP4_761)
#suite = TestSuite([example_tests])
#runner = HTMLTestRunner(combine_reports=False, report_name="MyReport", add_timestamp=False, output= direct + '/reports')
#runner.run(suite)

