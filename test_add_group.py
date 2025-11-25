# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


@pytest.fixture(scope="function")
def driver():
    # Можно добавить опции, если нужно (например, headless)
    # options = webdriver.FirefoxOptions()
    # driver = webdriver.Firefox(service=FirefoxService(), options=options)
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_add_user_group(driver):
    driver.get("https://localhost/addressbook/")

    # Авторизация
    driver.find_element(By.NAME, "user").send_keys("admin")
    driver.find_element(By.NAME, "pass").send_keys("secret")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()

    # Переход к группам
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "groups"))
    ).click()

    # Создание новой группы
    driver.find_element(By.NAME, "new").click()
    driver.find_element(By.NAME, "group_name").send_keys("123")
    driver.find_element(By.NAME, "submit").click()

    # Выход
    driver.find_element(By.LINK_TEXT, "Logout").click()