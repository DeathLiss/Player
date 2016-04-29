import vk_api
import sys

from PyQt4.QtGui import QApplication, QMainWindow, QDirModel, QColumnView



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

    #vk = vk_session.get_api()
    """
        VkApi.method позволяет выполнять запросы к API.
    """
    #response = vk.audio.get()
    #if response['items']:
    #    print(response['items'][0])

    print('-------------------')
    tools = vk_api.VkTools(vk_session)
    audio = tools.get_all('audio.get', 100, {'owner_id': 2041524})
    print('Posts count:', audio['count'])

    #if audio['count']:
    #    print('First post:', audio['items'][0], '\n')

    #if audio['count'] > 1:
    #    print('Last post:', audio['items'][-1])

    #url = 'http://cs1-46v4.vk-cdn.net/p5/83c719ba814630.mp3?extra=B5NUFFVl2-vMP697kI0JzuTZ3AHKI1ddLR_NQ2d5WAfitZNU0Af3RqGJDg04c179ZKTMGWUHVQiLwZ-RVICAUT-uQrou4Lhw-seUoBLdbwj1UACn9muNiKgeQLf_dS3P2NA0TrHD';
    #output = Phonon.AudioOutput(Phonon.MusicCategory)
    #m_media = Phonon.MediaObject()
    #Phonon.createPath(m_media, output)
    #m_media.setCurrentSource(
    #    Phonon.MediaSource(url))
   # m_media.play()

if __name__ == '__main__':
    main()


