from pages.base_page import BasePage
from pages.locators import Locators

class PostPage(BasePage):
    def create_post(self, title):
        if "Post" not in self.driver.page_source:
            self.click(Locators.HAPPY_FOLDER_TAB)
        self.click(Locators.POSTS_MENU)
        self.click(Locators.NEW_POST_BUTTON)
        self.type(Locators.POST_TITLE_FIELD, title)
        self.click(Locators.STATUS_ACTIVE_OPTION)
        self.click(Locators.POST_SAVE_BUTTON)
