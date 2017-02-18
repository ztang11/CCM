import xlwings as xl
from pymongo import MongoClient
import pandas as pd

_file = 'data.xlxs'

with open(_file, 'w') as f:
    book = xl.Book(_file)
    book.activate()

    sheet = book.sheets[0]

    connection = MongoClient()

    db = connection.ccm

    data = list(db.monte_carlo.find({}, {'_id': 0, 'Future': 1, 'AtM': 1, 'Date': 1}).sort('Date'))

    df = pd.DataFrame(data, columns=['Date', 'Future', 'AtM'])
    df.set_index('Date', inplace=True)

    sheet.range('A1').value = df
    book.save()
    #book.close()