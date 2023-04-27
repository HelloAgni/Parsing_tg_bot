"""
Файл настроек.
Доступные расширения файлов для обработки.
Создание папки для загрузки файлов.
"""
import pathlib

EXTENSIONS = ['xls', 'xlsx', 'xlsm', 'xlsb', 'odf', 'ods', 'odt']
TEMP_DIR = ''.join((str(pathlib.Path(__file__).parent), '/temp/'))

pathlib.Path(TEMP_DIR).mkdir(parents=True, exist_ok=True)
