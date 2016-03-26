import vk
import vk_api
import sys

from PyQt4.QtGui import QApplication, QMainWindow, QDirModel, QColumnView
from PyQt4.phonon import Phonon


vkapi = vk.AuthSession(5332707, 'liseyna1@gmail.com', '9tWmMmJCJk!')

print('========================================')
print('======== Характеристики сессии ========')
print('========================================')
print('Login: ' + vkapi._user_login)
print('Passw: ' + vkapi._user_password)
print('Access_token: ' + vkapi._access_token)
print('ID app: ' + str(vkapi.app_id))

client_id = 5332707
m_model = QDirModel()


def main():
    """ Пример получения последнего сообщения со стены """

    login, password = 'liseyna1@gmail.com', '9tWmMmJCJk!'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.authorization()
    except vk_api.AuthorizationError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()
    """
        VkApi.method позволяет выполнять запросы к API.
    """
    response = vk.audio.get()
    if response['items']:
        print(response['items'][0])

    print('-------------------')
    tools = vk_api.VkTools(vk_session)
    audio = tools.get_all('audio.get', 100, {'owner_id': 2041524})
    print('Posts count:', audio['count'])

    if audio['count']:
        print('First post:', audio['items'][0], '\n')

    if audio['count'] > 1:
        print('Last post:', audio['items'][-1])



if __name__ == '__main__':
    main()


