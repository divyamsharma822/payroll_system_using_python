import pandas as pd
import csv

dataCsv = pd.read_csv('data.csv')
dataCsv.set_index('employeeId',inplace=True)
def search_row(eid):
    name = dataCsv.loc[eid]['name']
    gender = dataCsv.loc[eid]['gender']
    salary = dataCsv.loc[eid]['salary']
    return [eid,name,gender,salary]

def add_row(row_content):
    resultFile = open("data.csv",'a')
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerow(row_content)
    resultFile.close()
    return None


