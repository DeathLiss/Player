#!-*-coding:utf-8-*-
import sys
import vk_api
# import PyQt4 QtCore and QtGui modules
from PyQt4 import QtCore, QtGui
from PyQt4 import uic
from PyQt4.phonon import Phonon
from vk_player.testIntui import Ui_MainWindow
(UI_WIN, QMainWindow) = uic.loadUiType('testIntui.ui')

class MainWindow(QMainWindow):
    """MainWindow inherits QMainWindow"""
    song_list = []
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.m_media = None
        self.getMyPlaylist()
        self.connect(self.ui.playButton, QtCore.SIGNAL("clicked()"),self.play)
    def __del__(self):
        self.ui = None

    def play(self):
        self.delayedInit()
        self.m_media.setCurrentSource(
            Phonon.MediaSource("http://cs1-46v4.vk-cdn.net/p5/83c719ba814630.mp3?extra=B5NUFFVl2-vMP697kI0JzuTZ3AHKI1ddLR_NQ2d5WAfitZNU0Af3RqGJDg04c179ZKTMGWUHVQiLwZ-RVICAUT-uQrou4Lhw-seUoBLdbwj1UACn9muNiKgeQLf_dS3P2NA0TrHD"))
        self.m_media.play()

    def delayedInit(self):
        if not self.m_media:
            self.m_media = Phonon.MediaObject(self)
            audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
            Phonon.createPath(self.m_media, audioOutput)

    def getMyPlaylist(self):
        login, password = 'liseyna1@gmail.com', '9tWmMmJCJk!'
        vk_session = vk_api.VkApi(login, password)

        try:
          vk_session.authorization()
        except vk_api.AuthorizationError as error_msg:
            print(error_msg)
            return

        vk = vk_session.get_api()
        response = vk.audio.get()
        if response['items']:
            print(response['items'][0])

        print('-------------------')
        tools = vk_api.VkTools(vk_session)
        audio = tools.get_all('audio.get', 100, {'owner_id': 2041524})
        count = audio['count']
        print('Posts count:', count)
        for song in audio['items']:
            self.song_list.append(song)
        n = 0 #Номер строки

        self.ui.tableWidget.setColumnCount(1)
        self.ui.tableWidget.setRowCount(count)
        for n in range(count):
            self.ui.tableWidget.setItem(n,0, QtGui.QTableWidgetItem(str(self.song_list[n]['artist'])+'\t'+str(self.song_list[n]['title'])+'\t'+str(self.song_list[n]['duration'])))

#-----------------------------------------------------#
if __name__ == '__main__':
    # create application
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('untitled')

    # create widget
    w = MainWindow()
    w.setWindowTitle('untitled')
    w.show()

    QtCore.QObject.connect(app, QtCore.SIGNAL('lastWindowClosed()'), app, QtCore.SLOT('quit()'))

    # execute application
    sys.exit(app.exec_())