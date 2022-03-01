import unittest
import moodle_locators as locators
import moodle_methods as methods


class MoodleAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_create_new_user():
        methods.setUp()
        methods.log_in(locators.admin_username, locators.admin_password)  # admin-login
        methods.create_new_user()
        methods.search_user()
        methods.log_out()
        methods.log_in(locators.new_username, locators.new_password)
        methods.check_new_user_can_login()
        methods.logger('created')
        methods.log_out()
        methods.log_in(locators.admin_username, locators.admin_password)
        methods.delete_new_user()
        methods.log_out()
        methods.tearDown()

