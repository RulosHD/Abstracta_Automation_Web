import allure

def attach_screenshot(driver):
    screenshot = driver.get_screenshot_as_png()
    allure.attach(screenshot,name="screenshot",attachment_type=allure.attachment_type.PNG)