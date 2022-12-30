from enum import Enum
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class Term(Enum):
    FALL = 1
    SPRING = 2
    SUMMER = 3


def click_term(driver: WebDriver, term: Term):
    available_terms = driver.find_element(By.ID, 'semesterId')

    term_element = available_terms.find_elements(By.XPATH, "*")[term.value - 1]

    available_terms.click()
    term_element.click()


def get_subjects(driver: WebDriver):
    department_chosen = driver.find_element(By.ID, 'department_chosen')
    department_chosen.click()

    r = department_chosen.find_element(By.CLASS_NAME, 'chosen-results').find_elements(By.XPATH, '*')

    department_chosen.click()  # deselects the dropdown

    return r


def click_subject(driver: WebDriver, i):
    department_chosen = driver.find_element(By.ID, 'department_chosen')
    department_chosen.click()

    department_chosen.find_element(By.CLASS_NAME, 'chosen-results').find_elements(By.XPATH, '*')[i].click()


def click_search_button(driver: WebDriver):
    driver.find_element(By.ID, 'submit_button').click()


def main():
    driver = webdriver.Firefox()
    driver.get('https://classes.iastate.edu/')

    click_term(driver, Term.SPRING)

    # subjects = get_subjects(driver)

    click_subject(driver, 116)  # math

    click_search_button(driver)


if __name__ == '__main__':
    main()
