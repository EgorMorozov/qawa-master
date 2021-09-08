from utilities.base_test import BaseTest
from utilities.loggers import log_message
from pages.inspect_shop import Init_Page
from Services.ramdomizer import Randomizer
import time


class Infinum_inspect_shop(BaseTest):
    def setUp(self):
        super().setUp()
        self.init_page = Init_Page(self.driver)

    def test_register_user(self):
        log_message("Registering a new user")
        username = Randomizer.get_random_username()
        password = Randomizer.get_password()
        log_message("Username is: " + username + ", and password is: " + password)

        self.init_page.manipulate_user(username, password, self.init_page.register_button)

        log_message("Expected message is: " + self.init_page.messages_types.get('registration_success'))
        log_message("Actual message is: " + self.init_page.get_message_text())

        self.assertEqual(self.init_page.messages_types.get('registration_success'), self.init_page.get_message_text(),
                         "Actual message is different from expected")

        log_message("Clearing up test data")
        self.init_page.manipulate_user(username, password, self.init_page.delete_accout_button)

    def test_register_without_store_name(self):
        log_message("Create test credentials")
        username = Randomizer.get_random_username()
        password = Randomizer.get_password()

        log_message("Username is: " + username + ", and password is: " + password)

        self.init_page.press_button(self.init_page.register_button)
        self.assertEqual(self.init_page.messages_types.get('empty_state'), self.init_page.get_message_text(),
                         "Actual message is different from expected")

        self.init_page.enter_password(password)
        self.init_page.press_button(self.init_page.register_button)
        self.assertEqual(self.init_page.messages_types.get('empty_state'), self.init_page.get_message_text(),
                         "Actual message is different from expected")

        self.init_page.clear_up_input(self.init_page.enter_password_field)

        self.init_page.enter_store_name(username)
        self.init_page.press_button(self.init_page.register_button)
        self.assertEqual(self.init_page.messages_types.get('empty_state'), self.init_page.get_message_text(),
                         "Actual message is different from expected")

        self.init_page.clear_up_all_inputs()

    def test_double_registration(self):
        log_message("Create test credentials")
        username = Randomizer.get_random_username()
        password = Randomizer.get_password()
        log_message("Username is: " + username + ", and password is: " + password)

        self.init_page.manipulate_user(username, password, self.init_page.register_button)
        self.assertEqual(self.init_page.messages_types.get('registration_success'), self.init_page.get_message_text(),
                         "Actual message is different from expected")

        self.init_page.manipulate_user(username, password, self.init_page.register_button)
        # need to use sleep because selenium works faster than text on the page changes
        # TODO - find the solution how to avoid "sleep" call
        time.sleep(1)
        self.assertEqual(self.init_page.messages_types.get('user_exist'), self.init_page.get_message_text(),
                         "Actual message is different from expected")

        log_message("Clearing up test data")
        self.init_page.manipulate_user(username, password, self.init_page.delete_accout_button)
