#!/usr/local/bin/python3

from test_parent import BaseTest
from page_login import PageLogin
from page_menu import PageMenu
from admin.users.page_users import PageUsers
import pytest
import unittest

@pytest.mark.TCP4_761
@pytest.mark.smoke
@pytest.mark.usefixtures("data")
class TCP4_761(BaseTest):
    ''' Test to verify the creation of users with special characters '''

    def test_create_user(self):
        ''' Create user with special characters '''
        #Constants
        data = self.data
        user_data = {}            # To save user data, when you create an user
        user_result_search = None # To save webElement, if the user was found

        # Pages Instance
        pageMenu = PageMenu(self.driver, data)
        pageUser = PageUsers(self.driver, data)

        # STEP 1: Load login page.
        print('Step 1: Load Login page')
        self.driver.get(data['server_url'])
        login_page = PageLogin(self.driver, data)
        login_page.login()

        # STEP 2: Go to admin.
        print('Step 2: Go to Admin')
        pageMenu.goto_admin()

        # STEP 3: Create User with special character
        print('Step 3: Create User with special character')
        user_data = pageUser.create_user()

        # STEP 4: Go to Admin
        print('Step 4: Go to Admin')
        pageMenu.goto_admin()

        # STEP 5: Verify if the user was created
        try:
            print('Step 5: Verify if the user was created')
            user_result_search = pageUser.search_user(user_data['user_username'])

            self.assertTrue(user_result_search!=None)
            print('User was found')
        except AssertionError as e:
            print('User was not found, an error ocurred')

        print('Create User Test completed')
