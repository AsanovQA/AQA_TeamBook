from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_EMAIL = (By.XPATH, '//*[@id=":r0:"]')
    LOGIN_PASSWORD = (By.XPATH, '//*[@id=":r1:"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login_btn')
