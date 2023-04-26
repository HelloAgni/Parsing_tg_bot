import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
option = webdriver.ChromeOptions()
option.add_argument('headless')
option.add_argument('--window-size=1920,1080')
option.add_argument("--disable-3d-apis")  # Fix for Windows
option.add_argument(
    'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36')
driver = webdriver.Chrome(service=service, options=option)


def rework(item):
    """
    Кодируем и удаляем лишние символы.
    """
    string_encode = item.encode("ascii", "ignore")
    string_decode = string_encode.decode()
    return string_decode.replace(' ', '')


def open_file_and_parsing(file):
    """
    Открытие файла и сбор информации.
    """
    result = ''
    start = time.time()
    df = pd.read_excel(file, header=None)
    data_list = df.values.tolist()
    for items in data_list:
        name, url, xpath = items
        driver.get(url=url)
        driver.implicitly_wait(15)
        elements = driver.find_elements(By.XPATH, xpath)
        items = [int(rework(x.text)) for x in elements]
        average = sum(items) / len(items)
        result += f'{name} средняя цена: {round(average, 2)}\n'
    end = time.time()
    pars_time = end - start
    driver.quit()
    return result, round(pars_time, 3)
