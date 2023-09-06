import logging
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 設定 log 等級，可以根據需要調整
logging.basicConfig(level=logging.INFO)

# 初始化瀏覽器
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# 測試電子郵件成功登入
def test_email_login(browser):
    try:
        browser.get("https://myviewboard.com/signin")
        logging.info("前往登入頁面")

        email_input = browser.find_element(By.XPATH, "//input[@data-i18n='[placeholder]INPUT_EMAIL']")

        # 請替換為有效的電子郵件和密碼
        email_input.send_keys("a098584674@gmail.com")
        logging.info("輸入信箱")
        browser.find_element(By.XPATH, "//button[@data-i18n='SIGNIN']").click()
        logging.info("點擊登入按鈕")

        password_input = browser.find_element(By.XPATH, "//input[@data-i18n='[placeholder]INPUT_PW']")
        password_input.send_keys("Autotest123!")
        password_input.send_keys(Keys.ENTER)
        logging.info("輸入密碼")
        time.sleep(30)
        browser.refresh()
        time.sleep(60)

        success_login = "a098584674@gmail.com"
        collapse_title = browser.find_element(By.XPATH, "//div[@id='navbarCollapse']")
        # 斷言是否成功登入，這裡可以根據實際情況進行修改
        assert success_login in collapse_title.text

    except Exception as e:
        # 記錄異常情況到 log
        logging.error("測試出現異常: %s", str(e))
        # 擷取異常時的螢幕截圖
        browser.save_screenshot("email_login_failure.png")
        raise e

# 以下因為有個資，所以不會放真實的帳號密碼，只會有腳本

# 測試 Google 登入，因為有防止機器人機制，無法登入成功
def test_google_login(browser):
    try:
        browser.get("https://myviewboard.com/signin")
        time.sleep(10)
        logging.info("前往登入頁面")

        google_login_button = browser.find_element(By.XPATH, "//*[@id='google']//button")
        google_login_button.click()
        logging.info("點擊google登入按鈕")
        time.sleep(5)

        email_input = browser.find_element(By.XPATH, "//input[@type='email']")
        email_continue = browser.find_element(By.XPATH, "//*[@id='identifierNext']")
        password_input = browser.find_element(By.XPATH, "//input[@type='password']")

        # 請替換為您的 Google 帳號和密碼
        email_input.send_keys("你的信箱")
        logging.info("輸入google信箱")

        email_continue.click()
        time.sleep(5)
        password_input.send_keys("你的密碼")
        logging.info("輸入google密碼")
        password_input.send_keys(Keys.ENTER)

        success_login = "你的帳號"
        collapse_title = browser.find_element(By.XPATH, "//div[@id='navbarCollapse']")
        # 斷言是否成功登入，這裡可以根據實際情況進行修改
        assert success_login in collapse_title.text

    except Exception as e:
        # 處理異常情況，可以記錄 log
        print("測試出現異常:", str(e))
        # 擷取異常時的螢幕截圖
        browser.save_screenshot("google_login_failure.png")
        raise e

# 測試 Microsoft 帳號登入，登入會失敗
def test_microsoft_login(browser):
    try:
        browser.get("https://myviewboard.com/signin")
        logging.info("前往登入頁面")

        microsoft_login_button = browser.find_element(By.XPATH, "//button[@class='button microsoft-btn']")
        microsoft_login_button.click()
        logging.info("點擊 Microsoft 登入按鈕")

        email_input = browser.find_element(By.XPATH, "//input[@type='email']")
        continue_btn = browser.find_element(By.XPATH, "//input[@type='submit']")
        password_input = browser.find_element(By.XPATH, "//input[@name='passwd']")
        keep_login_not_btn = browser.find_element(By.XPATH, "//input[@type='button'][@value='否']")

        # 請替換為您的 Microsoft 帳號和密碼
        email_input.send_keys("帳號")
        continue_btn.click()
        password_input.send_keys("密碼")
        continue_btn.click()
        keep_login_not_btn.click()

        success_login = "帳號名稱"
        collapse_title = browser.find_element(By.XPATH, "//div[@id='navbarCollapse']")
        # 斷言是否成功登入，這裡可以根據實際情況進行修改
        assert success_login in collapse_title.text

    except Exception as e:
        # 記錄異常情況到 log
        logging.error("測試出現異常: %s", str(e))
        # 擷取異常時的螢幕截圖
        browser.save_screenshot("microsoft_login_failure.png")
        raise e

# 測試 Apple ID 登入，需要手機認證才能登入
def test_apple_id_login(browser):
    try:
        browser.get("https://myviewboard.com/signin")
        logging.info("前往登入頁面")

        apple_id_login_button = browser.find_element(By.XPATH, "//button[@class='button apple-btn']")
        apple_id_login_button.click()
        logging.info("點擊 Apple ID 登入按鈕")

        apple_id_input = browser.find_element(By.XPATH, "//input[@id='account_name_text_field']")
        password_input = browser.find_element(By.XPATH, "//input[@type='password']")

        # 請替換為您的 Apple ID 和密碼
        apple_id_input.send_keys("帳號")
        apple_id_input.send_keys(Keys.ENTER)
        logging.info("輸入Apple ID帳號")
        time.sleep(10)

        password_input.send_keys("密碼")
        password_input.send_keys(Keys.ENTER)
        logging.info("點擊 Apple ID 密碼")
        time.sleep(10)

        success_login = "pbv5zj5h8x@privaterelay.appleid.com"
        collapse_title = browser.find_element(By.XPATH, "//div[@id='navbarCollapse']")
        # 斷言是否成功登入，這裡可以根據實際情況進行修改
        assert collapse_title.text in success_login

    except Exception as e:
        # 記錄異常情況到 log
        logging.error("測試出現異常: %s", str(e))
        # 擷取異常時的螢幕截圖
        browser.save_screenshot("apple_id_login_failure.png")
        raise e

# 測試教育雲端登入，無法使用此方式登入，因沒有教育雲端帳號
def test_moe_login(browser):
    try:
        browser.get("https://myviewboard.com/signin")
        logging.info("前往登入頁面")

        email_login_button = browser.find_element(By.XPATH, "//*[@id='moe_tw_form']")
        email_login_button.click()
        logging.info("點擊教育雲端登入按鈕")

        email_input = browser.find_element(By.XPATH, "email-input")
        password_input = browser.find_element(By.XPATH, "password-input")

        # 請替換為有效的電子郵件和密碼
        email_input.send_keys("你的信箱")
        password_input.send_keys("你的密碼")
        password_input.send_keys(Keys.ENTER)

        success_login = "帳號名稱"
        collapse_title = browser.find_element(By.XPATH, "//div[@id='navbarCollapse']")
        # 斷言是否成功登入，這裡可以根據實際情況進行修改
        assert success_login in collapse_title.text

    except Exception as e:
        # 記錄異常情況到 log
        logging.error("測試出現異常: %s", str(e))
        # 擷取異常時的螢幕截圖
        browser.save_screenshot("email_login_failure.png")
        raise e

if __name__ == "__main__":
    pytest.main()
