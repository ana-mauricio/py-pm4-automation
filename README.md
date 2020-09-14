# py-pm4-automation

#### Local System Requirements

You can develop and run tests locally. In order to do so, you must have the following:

* [Python 3.6.9](https://www.python.org) or above
* [Pip](https://pip.pypa.io/en/stable/installing/)
* [Chrome](https://www.google.com/chrome/)
* [ChromeDriver 80.0.3987.106](https://chromedriver.chromium.org/getting-started) or above

#### Installing Locally

* Add chromedriver to PATH
* Clone the repository into a directory

#### Running and Writing Tests Locally

* Fill `default.ini` in /tests directory
* Write and save this lines:
  * ENVIRONMENT = local
  * server_url  = your/pm4/server/url/here
  * pm_username = your/username/here
  * pm_password = your/password/here
* Navigate to /
  * Run all tests : `python setup.py test`
  * Run specific test suite annotated: `python setup.py test --addopts -m=[name_annotation]`

Notes: 
  * If you want to view the tests running in the browser, comment out this line in `/src/test_parent.py`:
    * `# chrome_options.add_argument("--headless")`
  If Run doesn't work, update the setuptools with the following command
    * `update setuptools: pip install --upgrade setuptools` 
	
### Helpful Links

* [PyScaffold Documentation](https://pypi.org/project/PyScaffold/ "https://pypi.org/project/PyScaffold/")
* [Pytest Documentation](https://docs.pytest.org/en/stable/getting-started.html "https://docs.pytest.org/en/stable/getting-started.html")
* [Pytest-html](https://pypi.org/project/pytest-html/ "https://pypi.org/project/pytest-html/")
* [Python unittest Documentation](https://docs.python.org/3.5/library/unittest.html "https://docs.python.org/3.5/library/unittest.html")
* [Python unittest Source Code](https://github.com/python/cpython/tree/3.5/Lib/unittest "https://github.com/python/cpython/tree/3.5/Lib/unittest")
* [Selenium Documentation](https://selenium-python.readthedocs.io "https://selenium-python.readthedocs.io")
* [Selenium - Locating Elements](https://selenium-python.readthedocs.io/locating-elements.html "https://selenium-python.readthedocs.io/locating-elements.html")
* [Selenium - Waits](https://selenium-python.readthedocs.io/waits.html "https://selenium-python.readthedocs.io/waits.html")
* [Xpath cheatsheet](https://devhints.io/xpath "https://devhints.io/xpath")
