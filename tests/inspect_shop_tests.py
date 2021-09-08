from utilities.base_test import BaseTest
from utilities.loggers import log_message
from pages.inspect_shop import Inspect_shop
from Services.ramdomizer import Randomizer
import time


class Infinum_inspect_shop(BaseTest):

    def setUp(self):
        super().setUp()
        self.inspect_shop = Inspect_shop(self.driver)

    def test_register_user(self):
        log_message("Registering a new user")
        username = Randomizer.get_random_username()
        password = Randomizer.get_password()
        log_message("Username is: " + username + ", and password is: " + password)

        self.inspect_shop.manipulate_user(username, password, self.inspect_shop.register_button)

        log_message("Expected message is: " + self.inspect_shop.messages_types.get('registration_success'))
        log_message("Actual message is: " + self.inspect_shop.get_message_text())

        self.assertEqual(self.inspect_shop.messages_types.get('registration_success'),
                         self.inspect_shop.get_message_text(), "Actual message is different from expected")

        log_message("Clearing up test data")
        self.inspect_shop.manipulate_user(username, password, self.inspect_shop.delete_accout_button)

    def test_register_without_store_name(self):
        log_message("Create test credentials")
        username = Randomizer.get_random_username()
        password = Randomizer.get_password()

        log_message("Username is: " + username + ", and password is: " + password)

        self.inspect_shop.press_button(self.inspect_shop.register_button)
        self.assertEqual(self.inspect_shop.messages_types.get('empty_state'), self.inspect_shop.get_message_text(),
                         "Actual message is different from expected")

        self.inspect_shop.enter_password(password)
        self.inspect_shop.press_button(self.inspect_shop.register_button)
        self.assertEqual(self.inspect_shop.messages_types.get('empty_state'), self.inspect_shop.get_message_text(),
                         "Actual message is different from expected")

        self.inspect_shop.clear_up_input(self.inspect_shop.enter_password_field)

        self.inspect_shop.enter_store_name(username)
        self.inspect_shop.press_button(self.inspect_shop.register_button)
        self.assertEqual(self.inspect_shop.messages_types.get('empty_state'), self.inspect_shop.get_message_text(),
                         "Actual message is different from expected")

        self.inspect_shop.clear_up_all_inputs()

    def test_double_registration(self):
        log_message("Create test credentials")
        username = Randomizer.get_random_username()
        password = Randomizer.get_password()
        log_message("Username is: " + username + ", and password is: " + password)

        self.inspect_shop.manipulate_user(username, password, self.inspect_shop.register_button)
        self.assertEqual(self.inspect_shop.messages_types.get('registration_success'),
                         self.inspect_shop.get_message_text(), "Actual message is different from expected")

        self.inspect_shop.manipulate_user(username, password, self.inspect_shop.register_button)
        # need to use sleep because selenium works faster than text on the page changes
        # TODO - find the solution how to avoid "sleep" call
        time.sleep(1)
        self.assertEqual(self.inspect_shop.messages_types.get('user_exist'), self.inspect_shop.get_message_text(),
                         "Actual message is different from expected")

        log_message("Clearing up test data")
        self.inspect_shop.manipulate_user(username, password, self.inspect_shop.delete_accout_button)
