import csv

class DataProvider():
    def __init__(self, file_path):
        self.file_path = file_path

    def get_companies(self):    
        companies = []
        with open(self.file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                companies.append(dict(row))
        return companies
