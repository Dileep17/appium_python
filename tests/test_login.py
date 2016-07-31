import pytest

from test_base import TestBase


class TestLogin(TestBase):
    """Basic test for appium in python"""

    testdata = [
        ('ppanelist', 'P@ssw0rd', 2, 'Hi panelist!'),
        ('ppanelistp', 'P@ssw0rd', 2, 'Hi panelistnew!')
    ]

    def test_recruiter_login(self):
        """Test the Single Player mode launches correctly"""
        self.loginscreen.login('rrecruitx', 'P@ssw0rd')
        assert self.homescreen.getTitle() == 'Hi recruiter!'

    @pytest.mark.parametrize("username, password, experience, expected", testdata)
    def test_recruiter_login(self, username, password, experience, expected):
        """Test the Single Player mode launches correctly"""
        self.loginscreen.login(username, password)
        self.loginscreen.set_experience(experience)
        assert self.homescreen.getTitle() == expected






        # ,
        # ('ppanelist', 'P@ssw0rd', 'Hi panelist!'),
        # ('ppanelistp', 'P@ssw0rd', 'Hi panelistnew!')
