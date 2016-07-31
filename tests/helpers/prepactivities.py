import subprocess

import time

import desired_capabilities
from appium import webdriver


class PrepActivities:
    driver = None

    def __init__(self):
        self.start_emulator()
        self.start_appium_server()

    def wait_for_process_to_start(self, process, wait_text):
        i = 0
        while True:
            print "value of i ", ++i
            retcode = process.poll()  # returns None while subprocess is running
            print "value from subprocess " + str(retcode) + "."
            line = process.stdout.readline()
            print "GOT ", line
            if wait_text in line:
                break
            if retcode is not None:
                return 0
        return 1

    def wait_for_emulator_to_fully_boot(self):
        print "waiting for emulator to launch ."
        while True:
            output, error = subprocess.Popen(['adb', 'shell', 'getprop', 'init.svc.bootanim'],
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.STDOUT).communicate()
            print '.',
            if 'stopped' in output:
                print " emulator started",
                break
            time.sleep(1)

    def start_emulator(self):
        self.emulator = subprocess.Popen(['emulator', '-avd', 'recrux'])
        self.wait_for_emulator_to_fully_boot()
        print "emulator fully booted"

    def start_appium_server(self):
        self.appium = subprocess.Popen(['/Applications/Appium.app/Contents/Resources/node_modules/.bin/appium'],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT)
        self.wait_for_process_to_start(self.appium, 'Appium REST http interface listener started on 0.0.0.0:4723')

    def create_driver(self):
        PrepActivities.driver = webdriver.Remote('http://localhost:4723/wd/hub',
                                                 desired_capabilities.get_desired_capabilities('andriod-debug.apk'))
        # time.sleep(20)
        PrepActivities.driver.implicitly_wait(40)
        print "after sleep.. app should open.."
        return PrepActivities.driver

    def stop_all(self):
        PrepActivities.driver.quit()
        self.emulator.terminate()
        self.appium.terminate()
        print "**************** DONE *********************"

