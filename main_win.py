#!-*-coding:utf-8-*-
import sys
import vk_api
import datetime
# import PyQt4 QtCore and QtGui modules
from PyQt4 import QtCore, QtGui
from PyQt4 import uic
from PyQt4.QtGui import QFileDialog
from PyQt4.phonon import Phonon

(Ui_MainWindow, QMainWindow) = uic.loadUiType('testIntui.ui')

class MainWindow(QMainWindow):
    """MainWindow inherits QMainWindow"""
    song_list = []

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.m_media = None
        self.delayedInit()
        self.getMyPlaylist()
        self.m_media.setCurrentSource(
            Phonon.MediaSource('/home/liss/Музыка/Темный_мир.mp3'))
        self.connect(self.ui.playButton, QtCore.SIGNAL("clicked()"), self.play)
        self.connect(self.ui.nextButton, QtCore.SIGNAL("clicked()"), self.pause)
        self.connect(self.ui.actionOpenFile_s, QtCore.SIGNAL("clicked()"), self.open())
        self.ui.horizontalSlider.valueChanged.connect(self.slider_value_change)


    def __del__(self):
        self.ui = None

    def play(self):
        print(self.m_media.state())
        if self.m_media.state() == Phonon.PlayingState:
            self.m_media.pause()
        elif self.m_media.state() == Phonon.PausedState or self.m_media.state() == Phonon.StoppedState:
            self.m_media.play()
        # self.m_media.state() == Phonon.PausedState or

    def pause(self):
        self.m_media.pause()

    """
    def stop(self):
        self.m_media.stop()                     #остановить и пересоздать ресурс для проигрывания сначала
        self.m_media.setCurrentSource(
        Phonon.MediaSource(
            "https://cs9-15v4.vk.me/p5/437ded476b919e.mp3?extra=3nV5RppDS-MPkNVZlYbcUxJ7KUQrtwVEhG6JYT769UWZY1Rp_UMd1aj3V2W3oVzDUYkBf20RMHTBTBIsHlJICqdWXJbCeoe0esH8R0bRzXm39A6soFXJYpMn2QA4wZ7VS2Avw1Lz"))
    """

    def slider_value_change(self):
        #if self.m_media.state() == Phonon.PlayingState or self.m_media.state() == Phonon.PausedState:
        value = self.ui.horizontalSlider.value()
        print(value)
        self.m_media.seek(value)
        self.m_media.play()

    def delayedInit(self):
        if not self.m_media:
            self.m_media = Phonon.MediaObject(self)
            audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
            Phonon.createPath(self.m_media, audioOutput)

    def getMyPlaylist(self):
        login, password = 'liseyna1@gmail.com', '9tWmMmJCJk!'

        vk_session = vk_api.VkApi(login, password, captcha_handler=self.capcha)

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
        n = 0  # Номер строки

        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setRowCount(count)
        for n in range(count):
            self.ui.tableWidget.setItem(n, 0, QtGui.QTableWidgetItem(
                str(self.song_list[n]['artist'])))
            self.ui.tableWidget.setItem(n, 1, QtGui.QTableWidgetItem(
                str(self.song_list[n]['title'])))
            self.ui.tableWidget.setItem(n, 2, QtGui.QTableWidgetItem(
                str(datetime.timedelta(seconds=self.song_list[n]['duration']))))

    def capcha(self, captcha):
        key = input("Enter Captcha {0}: ".format(captcha.get_url())).strip()
        return captcha.try_again(key)


    def open(self):
        dialog = QFileDialog()
        dialog.setViewMode(QFileDialog.Detail)
        filename = dialog.getOpenFileName(self,
                                          'Open audio file', '/home',
                                          "Audio Files (*.mp3 *.wav *.ogg)")[0]



# -----------------------------------------------------#
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
