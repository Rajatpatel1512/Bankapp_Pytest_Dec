import time

import pytest

from pageObjects.User_Search_Page import User_Search_Class
from testCases.conftest import username
from utilities.Logger_utility import logger_class
from utilities.additional_utilities import additional_utilities_class


@pytest.mark.usefixtures("setup")
class Test_User_Search:
    driver = None
    log = logger_class.log_gen_method()

    def test_bankapp_user_search(self, bankapp_login):
        self.log.info("Testcase test_bankapp_user_search is started")
        # again you have to take the methods for login inserted it we have to create one fixture for login at conftest
        us = User_Search_Class(self.driver)
        self.log.info(f"Looking for User Management")
        us.Click_User_management_Link()
        self.log.info("Entering the username")
        us.Enter_UserName(username)
        self.log.info("Clicking on  Search Button")
        us.Click_SearchUser_Button()
        if self.driver.title=="Edit User":
            self.log.info("Testcase test_bankapp_user_search is Pass")
            print("Test Case Passed: User Found")
            self.log.info("Taking the screenshot")
            additional_utilities_class.take_screenshot(self.driver, "test_bankapp_user_search", "Pass")
            self.log.info("Testcase test_bankapp_user_search is Passed")
            assert True
        else:
            self.log.info("Taking the screenshot")
            # self.driver.save_screenshot(".\\Screenshots\\test_bankapp_login_002_fail.png")
            additional_utilities_class.take_screenshot(self.driver, "test_bankapp_user_search", "Fail")
            print("Test Case Failed: User not found")
            self.log.info("Testcase test_bankapp_user_search is Failed")
            assert False
        #assert "No results found" not in us.Get_Search_Result()
