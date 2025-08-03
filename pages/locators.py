from selenium.webdriver.common.by import By

class Locators:
    # LOGIN PAGE
    EMAIL_FIELD = By.XPATH, "//input[@name='email']"
    PASSWORD_FIELD = By.XPATH, "//input[@name='password']"
    LOGIN_BUTTON = By.XPATH, "//button[text()='Login']"

    # POST PAGE
    HAPPY_FOLDER_TAB = By.XPATH, "//div[contains(text(),'Happy Folder')]"
    POSTS_MENU = By.XPATH, "//a[contains(@href,'/admin/resources/Post')]"
    NEW_POST_BUTTON = By.XPATH, "//a[@data-testid='action-new']"
    POST_TITLE_FIELD = By.ID, "title"
    STATUS_ACTIVE_OPTION = By.XPATH, "//div[text()='ACTIVE']"
    POST_SAVE_BUTTON = By.XPATH, "//button[@type='submit']"
