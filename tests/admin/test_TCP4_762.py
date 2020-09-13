#!/usr/local/bin/python3

# Check if using local environment
from os import getenv
from test_parent import BaseTest
from page_login import PageLogin
from page_menu import PageMenu
from admin.users.page_users import PageUsers
from admin.users.page_user_information import PageUserInformation
import pytest
import unittest

@pytest.mark.TCP4_762
@pytest.mark.smoke
@pytest.mark.usefixtures("data")
class TCP4_762(BaseTest):
    ''' Test to verify the creation of users with special characters '''

    def test_fill_user_information(self):
        data = self.data
        ''' Create user with Complete User information '''
        #Constants
        user_data = {}              # To save user data, when you create an user
        user_data_information = {}  # To save user data information, when you fill fields in userdata information
        user_result_search = None   # To save webElement, if the user was found

        # Pages Instance
        pageMenu = PageMenu(self.driver, data)
        pageUser = PageUsers(self.driver, data)
        pageUserInformation = PageUserInformation(self.driver, data)

        # STEP 1: Load login page.
        print('Step 1: Load Login page')
        self.driver.get(data['server_url'])
        login_page = PageLogin(self.driver, data)
        login_page.login()

        # STEP 2: Go to admin.
        print('Step 2: Go to Admin')
        pageMenu.goto_admin()

        # STEP 3: Create User
        print('Step 3: Create User')
        user_data = pageUser.create_user()

        # STEP 4: Complete User information
        print('Step 4: Complete User information')
        user_data_information = pageUserInformation.fill_user_information()

        # STEP 5: Go to admin.
        print('Step 5: Go to Admin')
        pageMenu.goto_admin()

        # STEP 6: Search user created.
        print('STEP 6: Search user created.')
        try:
            user_result_search = pageUser.search_user(user_data['user_username'])
            self.assertTrue(user_result_search != None)
        except AssertionError as e:
            print('An error occurred')
            raise Exception(e)

        # STEP 7: Edit user.
        print('STEP 7: Edit user created before.')
        pageUser.edit_user(user_result_search)

        # STEP 8: Verify if the user data information was saved.
        print('STEP 8: Verify if the user data information was saved.')
        try:
            # Verify if the user_data_information created is present in the form user_data_information_form
            result_user_information_saved = pageUserInformation.verify_user_data_information(user_data_information)
            self.assertTrue(result_user_information_saved)
            print('The user_data_information was saved successfully')
        except AssertionError as e:
            raise Exception('Error in verify user data information',e)

        print('Fills User data information Test completed')
