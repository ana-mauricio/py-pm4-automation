# -*- coding: utf-8 -*-
"""
    Dummy conftest.py for py_pm4_automation.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    https://pytest.org/latest/plugins.html
"""

import pytest
import os
from config_loader import Config

Config.init_config()

@pytest.fixture
def data(request):
    request.cls.data = {"server_url": Config.get("server_url"),
                        "username": Config.get("pm_username"),
                        "password": Config.get("pm_password")}
