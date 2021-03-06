from utilities.base_page import BasePage
from selenium.webdriver.common.by import By
from utilities.loggers import log_message


class Insect_shop(BasePage):
    enter_store_name_field = (By.XPATH, "//form/input[@data-testid='store-name-input']")
    enter_password_field = (By.XPATH, "//form/input[@data-testid='password-input']")
    login_to_store_button = (By.XPATH, "//form/button[@data-testid='login-button']")
    register_button = (By.XPATH, "//form/button[@data-testid='register-button']")
    delete_account_button = (By.XPATH, "//form/button[@data-testid='delete-button']")
    message = (By.XPATH, "//p[@data-testid='message']")

    messages_types = {
        'registration_success': "User registered",
        'empty_state': "Input fields can't be blank",
        'invalid_credentials': "Wrong password, try again.",
        'delete_message': "User deleted!",
        'user_exist': "User already exists"
    }

    # Created for exercise in the part2/test6. Useless, because I already have manipulate_user method that do the same
    # and allow me to use any combination I want to use (input fields + any button)
    def login(self, username, password):
        self.enter_store_name(username)
        self.enter_password(password)
        self.press_button(self.login_to_store_button)

    def manipulate_user(self, username, password, button_name):
        self.enter_store_name(username)
        self.enter_password(password)
        self.press_button(button_name)

    def enter_store_name(self, username):
        self.get_present_element(self.enter_store_name_field).clear()
        self.get_present_element(self.enter_store_name_field).send_keys(username)

    def enter_password(self, password):
        self.get_present_element(self.enter_password_field).clear()
        self.get_present_element(self.enter_password_field).send_keys(password)

    def press_button(self, button_name):
        if button_name == self.login_to_store_button:
            self.get_present_element(self.login_to_store_button).click()
        elif button_name == self.register_button:
            self.get_present_element(self.register_button).click()
        elif button_name == self.delete_account_button:
            self.get_present_element(self.delete_account_button).click()
        else:
            log_message("Unexpected button, please double-check the button name")

    def clear_up_input(self, field_name):
        self.get_present_element(field_name).clear()

    def clear_up_all_inputs(self):
        self.get_present_element(self.enter_store_name_field).clear()
        self.get_present_element(self.enter_password_field).clear()

    def get_message_text(self):
        return self.get_present_element(self.message).text
