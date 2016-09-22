import os
import sys
import shutil

#
# 
#

version = '0.02'

# -----------------------------------------------------------------------------
def testLogPath(programPath, programName):
    """Создаёт папку для записи логов внутри папки приложения (папка создаётся по названию самого ПО)"""

    # Нормализуем путь под стандарт текущей ОС (преобразуем прямые/обратные слеши)
    logPath = os.path.normpath(''+programPath+'/'+programName+'')

    # Если папка для логов ещё не создана - создаём
    if not os.path.exists(logPath):
        os.makedirs(logPath)
        
# -----------------------------------------------------------------------------
def workingDir():
    """Корректно определяет и изменяет пути в (интерпретаторе/*.exe-файле)"""

    # Узнаём имя и расширение исполняемого файла:
    # ToDo: сделать мультиплатформенным
    currentFile = sys.argv[0].split('\\').pop().split('.')
    currentFileName = currentFile[0]
    currentFileExtension = currentFile.pop()

    # Узнаём текущие директории:
    currentPath = os.getcwd()
    programPath = sys.path[0]

    # Изменяем текущую директорию:
    if currentFileExtension == 'exe':
        os.chdir(os.path.dirname(sys.path[0]))
    else:
        os.chdir(sys.path[0])

    return currentPath, programPath, currentFileName, currentFileExtension

# -----------------------------------------------------------------------------
def copyFile(src, dest):
    """  """

    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: %s' % e.strerror)


# -----------------------------------------------------------------------------
