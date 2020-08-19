import pyqrcode
import csv
import pandas as pd

fields = ["Url_Site", "QR_Code"]

rows = [['http://localhost:8000/', 'abcdef']]
filename = "test.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)


def createQRCode():
    df = pd.read_csv("test.csv")
    for index, values  in df.iterrows():
        url = values["Url_Site"]
        code = values["QR_Code"]

        data = f'''
        URL: {url} \n
        CODE: {code}
        '''

        image = pyqrcode.create(data)
        image.png(f"test.png", scale=5)
        print(data)

createQRCode()


