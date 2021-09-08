from unittest import TestCase
from utilities import driver_builder
from utilities import config


class BaseTest(TestCase):
    def setUp(self):
        self.driver = driver_builder.build_driver()
        self.driver.get(config.BASE_URL)

    def tearDown(self):
        self.driver.quit()
