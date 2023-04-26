import pathlib
import re
from config import TEMP_DIR, EXTENSIONS
import lxml.etree
from lxml.etree import XPathSyntaxError


def check_extensions(file_name):
    """
    Перед скачиванием проверяем расширение файла.
    Пока осуществлена поддержка Excel файлов.
    """
    ext = file_name.split('.')[-1]
    if ext in EXTENSIONS:
        return True
    return False


def check_file(doc):
    """
    Проверка расширения файла.
    Получение имени файла и указываем путь для скачивания.
    """
    file_name = doc['file_path'].split('/')[-1]
    if check_extensions(file_name):
        current_dir = pathlib.Path(__file__).parent
        file_path = str(current_dir) + TEMP_DIR + file_name
        return file_path
    return False


def str_is_xpath(xpath):
    """
    Валидация xpath
    """
    try:
        lxml.etree.XPath(xpath)
        return True
    except XPathSyntaxError:
        return False


def str_is_url(url: str):
    """
    Валидация URL
    """
    regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if re.match(regex, url):
        return True
    else:
        return False
