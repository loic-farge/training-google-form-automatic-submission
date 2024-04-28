# Web Form Automation Training Project

This project is a simple web form automation script for training purposes. It uses Selenium WebDriver to automate form submission on a webpage. The script reads data from a CSV file, fills in the form with this data, and submits it.

## Project Structure

The project is structured into three main modules:

1. `DataProvider`: This module reads data from a CSV file and provides it to the main script.

2. `WebDriver`: This module handles all interactions with the Selenium WebDriver. It initializes the driver, navigates to URLs, and finds elements on the webpage.

3. `FormFiller`: This module fills in the form on the webpage with the provided data.

## Setup

To get started with the Personal Finance Manager, follow these steps:

1. Clone the repository:
```
git clone https://github.com/loic-farge/training-personal-finance-manager.git
```
2. Navigate to the cloned repository:
```
cd personal-finance-manager
```
3. Install the required dependencies (if any):
```
pip install -r requirements.txt
```
4. Run the application:
```
python main.py
```