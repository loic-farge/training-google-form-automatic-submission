from services.form_filler import FormFiller
from services.data_provider import DataProvider
from services.web_driver import WebDriver

# Initialize DataProvider with CSV file path
data_provider = DataProvider('./data/data.csv')

# Initialize WebDriver with driver zip path and driver path
web_driver = WebDriver('./chromedriver.zip', './driver/chromedriver-win64/chromedriver.exe')

# Initialize FormFiller with IDs of form fields
form_filler = FormFiller()

# Start the WebDriver
web_driver.start(headless=True)

# Get the data from the DataProvider
companies = data_provider.get_companies()

form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSd3uM0dTtN6sgY3Em-gz8wIZrnfMIZv_BWSSBEOxKzqZLrzyQ/viewform'

# Iterate over the companies and fill the form for each one
for company in companies:
    web_driver.navigate(form_url)
    form_filler.fill_form(web_driver.driver, company['Company Name'], company['Number of employees'])

# Quit the WebDriver
web_driver.quit()