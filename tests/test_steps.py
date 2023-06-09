import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity, AttachmentType

# Подход 1. Более емкий и наглядный подход


def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")
        browser.driver.maximize_window()

    with allure.step("Ищем репозитория"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("eroshenkoam/allure-example")
        s(".header-search-input").submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером 76"):
        s(by.partial_text("#76")).should(be.visible)


# Подход 2. Удобен при переисользовании кода, когда стэпы ставятся общими

@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Zaika")
@allure.feature("Step model testing")
@allure.story("Allure feature testing")
@allure.link("https://github.com", name="Testing")
def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#76")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")
    browser.driver.maximize_window()


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()
    # Добавление аттачмента со скрином
    allure.attach(browser.driver().get_screenshot_as_png(),
                  name="Screen for test_decorator_steps.py",
                  attachment_type=AttachmentType.PNG)
