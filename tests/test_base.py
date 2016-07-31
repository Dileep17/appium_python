from helpers.prepactivities import PrepActivities
from pages import login_screen, home_screen
import pytest


class TestBase(object):
    def setup_method(self, method):
        print ("setup_module")  # first
        self.prep = PrepActivities()  # start emu appium
        self.init_screens(self.prep.create_driver())  # init all classes

    def teardown_method(self, method):
        print ("teardown_module")
        self.prep.stop_all()  # kill all emu, driver, appium

    def init_screens(self, driver):
        self.loginscreen = login_screen.LoginScreen(driver)
        self.homescreen = home_screen.HomeScreen(driver)

    @pytest.yield_fixture
    @pytest.fixture(scope="module")
    def foo(request):
        print('\nfoo setup - module fixture')
        def fin():
            print('foo teardown - module fixture')
        request.addfinalizer(fin)
