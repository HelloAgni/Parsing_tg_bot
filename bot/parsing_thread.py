import threading
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def rework(item):
    """
    Кодируем и удаляем лишние символы.
    """
    string_encode = item.encode("ascii", "ignore")
    string_decode = string_encode.decode()
    return string_decode.replace(' ', '')


def parsing_info(items: list, result: dict):
    """
    Функция настройки драйвера selenium и сбора информации из exl файла.
    """
    service = Service(executable_path=ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    option.add_argument('--window-size=1920,1080')
    option.add_argument("--disable-3d-apis")  # Fix for Windows
    option.add_argument(
        'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36')
    driver = webdriver.Chrome(service=service, options=option)
    name, url, xpath = items
    try:
        driver.get(url=url)
        driver.implicitly_wait(5)
        elements = driver.find_elements(By.XPATH, xpath)
        items = [int(rework(x.text)) for x in elements]
        average = sum(items) / len(items)
        result[name] = f'{name} средняя цена: {round(average, 2)}\n'
    except Exception as e:
        print(e)
    finally:
        driver.quit()


def thread(result: dict, data_list: list[list]):
    """
    Функция создания потоков выполнения.
    """
    tasks = []
    for i in range(len(data_list)):
        tasks.append(threading.Thread(
            target=parsing_info, args=(data_list[i], result)))
    for task in tasks:
        task.start()
    for task in tasks:
        task.join()
    return result


def main_parsing(file):
    """
    Открытие файла и сбор информации.
    Использование многопоточности.
    """
    start = time.time()
    result = {}
    df = pd.read_excel(file, header=None)
    data_list = df.values.tolist()
    info = thread(result=result, data_list=data_list)
    end = time.time()
    pars_time = end - start
    pretty_info = ''.join(info.values())
    return pretty_info, round(pars_time, 3)
