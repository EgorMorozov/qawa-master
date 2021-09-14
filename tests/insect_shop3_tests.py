from utilities.base_test import BaseTest
from pages.insect_shop import Insect_shop
from pages.shop_page import Shop_page
from utilities.loggers import log_message
from common import test_data


class Infinum_insect_shop3(BaseTest):

    def setUp(self):
        super().setUp()
        self.insect_shop = Insect_shop(self.driver)
        self.shop_page = Shop_page(self.driver)

    def test_add_sample_bugs_to_inventory(self):
        log_message("Log in")
        self.insect_shop.manipulate_user(test_data.USERNAME, test_data.PASSWORD, self.insect_shop.login_to_store_button)

        log_message("Adding samples")
        self.shop_page.load_sample_bugs()

        log_message("Checking tables for added elements")
        new_shop_item_count = self.shop_page.get_records_number_from_table(self.shop_page.universal_bug_shop_locator)
        log_message(str(new_shop_item_count))
        new_inventory_item_count = self.shop_page.get_records_number_from_table(
            self.shop_page.universal_inventory_bug_locator)
        log_message(str(new_inventory_item_count))

        self.assertEqual(new_inventory_item_count, test_data.DEFAULT_SAMPLE_BUGS_NUMBER, "Number of actual rows is"
                                                                                         " different from expected")
        self.assertEqual(new_shop_item_count, test_data.DEFAULT_SAMPLE_BUGS_NUMBER, "Number of actual rows is"
                                                                                    " different from expected")

        self.shop_page.clear_inventory()

    def test_remove_one_bug_from_inventory(self):

        log_message("Log in")
        self.insect_shop.manipulate_user(test_data.USERNAME, test_data.PASSWORD, self.insect_shop.login_to_store_button)

        log_message("Adding samples")
        self.shop_page.load_sample_bugs()

        log_message("Removing bug")
        bugs_count = self.shop_page.get_records_number_from_table(self.shop_page.universal_inventory_bug_locator)
        self.shop_page.remove_bug_by_position(0)
        updated_count = self.shop_page.get_records_number_from_table(self.shop_page.universal_inventory_bug_locator)
        self.assertTrue((bugs_count - updated_count) == 1, "More that 1 bug was remove")

        bugs_count = self.shop_page.get_records_number_from_table(self.shop_page.universal_inventory_bug_locator)
        self.shop_page.remove_bug_by_name(test_data.DEFAULT_BUG_NAMES.get('Fly'))
        updated_count = self.shop_page.get_records_number_from_table(self.shop_page.universal_inventory_bug_locator)
        self.assertTrue((bugs_count - updated_count) == 1, "More that 1 bug was remove")

        log_message("Clearing up test environment")
        self.shop_page.clear_inventory()

    def test_remove_specific_buf(self):

        log_message("Log in")
        self.insect_shop.manipulate_user(test_data.USERNAME, test_data.PASSWORD, self.insect_shop.login_to_store_button)

        log_message("Adding samples")
        self.shop_page.load_sample_bugs()

        self.shop_page.remove_bug_by_name(test_data.DEFAULT_BUG_NAMES.get('Fly'))

        self.assertFalse(self.shop_page.is_inventory_record_exits(test_data.DEFAULT_BUG_NAMES.get('Fly')))
