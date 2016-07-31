class Screen(object):

    title = ".bar-header .title"

    def __init__(self, newdriver):
        self.driver = newdriver

    def switchToWebContext(self):
        self.driver.switch_to.context(u'WEBVIEW_com.thoughtworks.recruitx')

    def getTitle(self):
        self.wait_page_load()
        return self.driver.find_element_by_css_selector(Screen.title).text