from selenium.webdriver.common.by import By

class FormFiller:
    def fill_form(self, driver, company_name, num_employees):
        inputs = driver.find_elements(By.CSS_SELECTOR, '#mG61Hd input[type="text"]')

        company_field = inputs[0]
        employee_count_field = inputs[1]

        company_field.send_keys(company_name)
        employee_count_field.send_keys(num_employees)

        submit_button = driver.find_element(By.CSS_SELECTOR, 'div[jsname="M2UYVd"]')
        submit_button.click()