from selenium import webdriver
import csv
import os
import sys
import time

input_filename = '/home/system1/work/detelefoongids_scrapper/urls.csv'

if __name__ == '__main__':
    # Taking Control of the browser ....
    browser = None
    try:
        browser = webdriver.Chrome()
    except Exception as error:
        print(error)

    if browser is None:
        print("Selenium not opened")
        sys.exit()

    input_file = open(input_filename, 'r')
    out_file = open('output.csv', 'w')
    csv_reader = csv.reader(input_file)
    writer = csv.writer(out_file)
    writer.writerow(['Name', 'Email', 'Category', 'Website',
                     'Phone', 'Street', 'HouseNo', 'City', 'Zipcode'])
    for row in csv_reader:
        url = row[0]
        browser.get(url)
        time.sleep(50)
        data = browser.execute_script('return window.__data')
        name = data.get('reduxAsyncConnect').get(
            'detailApi').get('details').get('name')
        email = data.get('reduxAsyncConnect').get(
            'detailApi').get('details').get('email')
        category = data.get('reduxAsyncConnect').get(
            'detailApi').get('details').get('category')
        website = data.get('reduxAsyncConnect').get(
            'detailApi').get('details').get('website').get('_link')
        phone = data.get('reduxAsyncConnect').get(
            'detailApi').get('details').get('phone')
        street = data.get('reduxAsyncConnect').get(
            'detailApi').get('details').get('address').get('street')
        house_no = data.get('reduxAsyncConnect').get('detailApi').get(
            'details').get('address').get('houseNoFrom')
        city_name = data.get('reduxAsyncConnect').get('detailApi').get(
            'details').get('address').get('city').get('name')
        zipcode = data.get('reduxAsyncConnect').get(
            'detailApi').get('details').get('address').get('zipCode')

        writer.writerow([name, email, category, website, phone,
                         street, house_no, city_name, zipcode])

    input_file.close()
    out_file.close()