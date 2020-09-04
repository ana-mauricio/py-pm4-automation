# -*- coding: utf-8 -*-

import pytest
from py_pm4_automation.skeleton import fib

__author__ = "amauricio"
__copyright__ = "amauricio"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
