import os

FILE_PATH = lambda app_file_name: os.path.abspath(
    os.path.join(
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(__file__))), 'apps/android-debug.apk'))


def get_desired_capabilities(app):
    print "path "+FILE_PATH(app)
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '4.2',
        'deviceName': 'Android Emulator',
        # 'fullReset': False,
        # 'noReset': True,
        'app': FILE_PATH(app)
        # ,
        # 'appPackage': 'com.thoughtworks.recruitx',
        # 'appActivity': '',
    }

    return desired_caps
