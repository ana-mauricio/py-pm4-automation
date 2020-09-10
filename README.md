# py-pm4-automation

# Files 

## Classes

[`/includes/test_classes.py`](https://github.com/ProcessMaker/pm4-selenium-tests/blob/master/includes/test_classes.py "test_classes.py")
Extended `unittest` classes to create a persistent log for use in debugging.
Class | Extends | Changes
--- | --- | ---
`CustomTestSuite` | `unittest.TestSuite` | Add custom attributes
`CustomTestLoader` | `unittest.TestLoader` | Set custom `suiteClass`
`CustomTextTestResult` | `unittest.TextTestResult` | Add custom attributes to instantiation
`CustomTextTestRunner` | `unittest.TextTestRunner` | Set custom `resultclass`, add custom attributes, and set custom `_makeResult()`

[`/includes/test_parent.py`](https://github.com/ProcessMaker/pm4-selenium-tests/blob/master/includes/test_parent.py "test_parent.py")
Base Test class to set up and tear down webdriver instance.
Class | Function | Extends | Methods | Attributes
--- | --- | --- | --- | ---
`BaseTest` | Defines base test class | `unittest.TestCase` | <ul><li>`setUpClass()`: instantiates webdriver instance</li><li>`tearDownClass()`: closes webdriver instance</li></ul> | <ul><li>`log`: a list initialized with one item</li></ul>

[`/includes/element.py`](https://github.com/ProcessMaker/pm4-selenium-tests/blob/master/includes/element.py "element.py")
Base Page Element class to define descriptors for customizing page elements.
Class | Function | Methods | Attributes
--- | --- | --- | ---
`BasePageElement` | Defines base page element class | <ul><li>`__init__()`: instantiates class</li><li>`__set__()`: assigns value to a page element</li><li>`__get__()`: retrieves value of a page element</li></ul> | <ul><li>`element_type`: string that defines element type as `ID`, `NAME`, or `XPATH`</li></ul>

[`/includes/locators.py`](https://github.com/ProcessMaker/pm4-selenium-tests/blob/master/includes/locators.py "locators.py")
Locator classes to define page element locations.
Class | Function | Attributes
--- | --- | ---
`BasePageLocators` | Defines page element locators | <ul><li>Global page elements:</li><li>`REQUESTS_LINK`: Request link element</li><li>`TASKS_LINK`: Tasks link element</li><li>`DESIGNER_LINK`: Designer link element</li><li>...</li></ul>
`LoginPageLocators` | Defines page element locators | <ul><li>Login page elements</li><li>`USERNAME`: Username field element</li><li>`PASSWORD`: Password field element</li><li>`LOGIN_BUTTON`: Login button element</li></ul>
`[...]PageLocators` | Defines page element locators | <ul><li>[...] page elements</li></ul>

[`/includes/page.py`](https://github.com/ProcessMaker/pm4-selenium-tests/blob/master/includes/page.py "page.py")
Base Page Shell, Base Page, and Page classes to define page element interactions.
Class | Extends | Methods | Attributes
--- | --- | --- | ---
`BasePageShell` | ----- | <ul><li>`__init__()`: instantiates class with attributes</li><li>`go_to_page()`: navigates to `page_url`</li></ul> | <ul>instance attributes:<li>`driver`: webdriver instance created in `BaseTest`</li><li>`data`: configuration defined in Trogdor request or in local `__init__.py`</li><li>`page_url`: server url extracted from `data`</li></ul>
`BasePage` | `BasePageShell` | <ul><li>`click_requests_link()`: clicks on Requests link</li><li>`click_tasks_link()`: click on Tasks link</li><li>`click_designer_link()`: click on Designer link</li><li>`click_admin_link()`: click on Admin link</li><li>`click_avatar()`: click on avatar</li></ul> | -----
`UsernameFieldElement` | `BasePageElement` | ----- | <ul>class attributes:<li>`locator`: element identifier</li></ul>
`PasswordFieldElement` | `BasePageElement` | ----- | <ul>class attributes:<li>`locator`: element identifier</li></ul>
`LoginPage` | `BasePageShell` | <ul><li>`__init__()`: redefines `page_url`</li><li>`login()`: logs in to server</ul> | <ul>class attributes:<li>`username_field_element`: instance of `UsernameFieldElement`</li><li>`password_field_element`: instance of `PasswordFieldElement`</li></ul><ul>instance attributes:<li>`page_url`: extended from `BasePageShell` and redefined</li>
`RequestsPage` | `BasePage` | <ul><li>`__init__()`: redefines `page_url`</li><li>`click_my_requests_button()`: click on My Requests button</li><li>`click_in_progress_button()`: click on In Progress button</li><li>`click_completed_button()`: click on Completed button</li><li>`click_all_requests_button()`: click on All Requests button</li></ul> | <ul><li>`page_url`: extended from `BasePageShell` and redefined</li></ul>
`AdminPage` | `BasePage` | <ul><li>`__init__()`: redefines `page_url`</li><li>`click_users_tab()`: click on Users tab</li><li>`click_deleted_users_tab()`: click on Deleted Users tab</li><li>`click_users_button()`: click on Users button</li><li>`click_groups_button()`: click on Groups button</li><li>`click_auth_clients_button()`:click on Auth Clients button</li><li>`click_customize_ui_button()`: click on Customize UI button</li><li>`click_queue_management_button()`: click on Queue Management button</li><li>`click_script_executors_button()`: click on Script Executors button</ul> | <ul><li>`page_url`: extended from `BasePageShell` and redefined</li></ul>
`DesignerPage` | `BasePage` | <ul><li>`__init__()`: redefines `page_url`</li><li>` click_processes_tab()`: click on Processes tab</li><li>`click_categories_tab()`: click on Categories tab</li><li>`click_archived_processes_tab()`: click on Archived Processes tab</li><li>`click_processes_button()`: click on Processes button</li><li>`click_scripts_button()`: click on Scripts button</li><li>`click_screens_button()`: click on Screens button</li><li>`click_environment_variables_button()`: click on Environment Variables button</li></ul> | <ul><li>`page_url`: extended from `BasePageShell` and redefined</li></ul>

## Methods

[`/includes/util.py`](https://github.com/ProcessMaker/pm4-selenium-tests/blob/master/includes/util.py "util.py")
Helper methods to perform general actions that can be used anywhere.
Method | Function | Parameters | Uses
--- | --- | --- | ---
`run_test()` | <ul><li>Loads and runs test suite, redirects `unittest` results to memory stream</li><li>returns PM4-friendly output dictionary</li></ul> | `classname, data, modulename` | <ul><li>`classname` passes the test class name</li><li>`data` passes the configuration from PM4's config task</li><li>`modulename` passes `__main__` from test file</li></ul>
`parse_results()` | <ul><li>Searches unittest results for `.`, `E`, or `F`</li><li>returns `SUCCESS` or `FAIL`</li></ul> | `buffer` | <ul><li>`buffer` passes memory stream</li></ul>
`parse_log_error()`| <ul><li>Searches text for `'ERROR'`</li><li>returns `ERROR` message</li></ul> | `log_message` | <ul><li>`log_message` passes `HTML` page source</li></ul>
`parse_log_warning()`| <ul><li>Searches text for `'WARNING'`</li><li>returns `WARNING` message</li></ul> | `log_message` | <ul><li>`log_message` passes `HTML` page source</li></ul>
`generate_long_text()` | <ul><li>Generates a 95 character string</li><li>returns string</li></ul> | ----- | -----
`generate_text()` | <ul><li>Generates a 10 character string</li><li>returns string</li></ul> | ----- | -----
`generate_email()` | <ul><li>Generates an email string</li><li>returns string</li> | ----- | -----

### Helpful Links 

(Hover for https:// address)
* [Python unittest Documentation](https://docs.python.org/3.5/library/unittest.html "https://docs.python.org/3.5/library/unittest.html")
* [Python unittest Source Code](https://github.com/python/cpython/tree/3.5/Lib/unittest "https://github.com/python/cpython/tree/3.5/Lib/unittest")
* [Selenium Documentation](https://selenium-python.readthedocs.io "https://selenium-python.readthedocs.io")
* [Selenium - Locating Elements](https://selenium-python.readthedocs.io/locating-elements.html "https://selenium-python.readthedocs.io/locating-elements.html")
* [Selenium - Waits](https://selenium-python.readthedocs.io/waits.html "https://selenium-python.readthedocs.io/waits.html")
* [Selenium - Page Objects](https://selenium-python.readthedocs.io/page-objects.html "https://selenium-python.readthedocs.io/page-objects.html")
* [Xpath cheatsheet](https://devhints.io/xpath "https://devhints.io/xpath")
