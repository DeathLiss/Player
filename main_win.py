#!-*-coding:utf-8-*-
import sys
import vk_api
import datetime
import os
# import PyQt4 QtCore and QtGui modules
from PyQt4 import QtCore, QtGui
from PyQt4 import uic
from PyQt4.QtGui import QFileDialog
from PyQt4.phonon import Phonon

(Ui_MainWindow, QMainWindow) = uic.loadUiType('testIntui.ui')


class MainWindow(QMainWindow):
    """MainWindow inherits QMainWindow"""
    song_list = []
    song_list_local = []
    sources = []
    index = 0


    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.m_media = None
        self.delayedInit()
        #self.getMyPlaylist()    #получение списка музыки из контакта!
        self.connect(self.ui.playButton, QtCore.SIGNAL("clicked()"), self.play)
        self.connect(self.ui.nextButton, QtCore.SIGNAL("clicked()"), self.nextSong)
        self.connect(self.ui.prevButton, QtCore.SIGNAL("clicked()"), self.prevSong)

        self.ui.tableWidget.cellPressed.connect(self.tableClicked)

        self.ui.actionOpenFile_s.triggered.connect(self.open)

        self.ui.horizontalSlider.valueChanged.connect(self.slider_value_change)

    def __del__(self):
        self.ui = None

    def initSource(self, filename):
        self.m_media.setCurrentSource(
            Phonon.MediaSource(filename))
        self.play()

    def alert(msg, icon=QtGui.QMessageBox.Warning):
        d = QtGui.QMessageBox()
        d.setWindowTitle('AutoCanary')
        d.exec_()

    def play(self):
        self.ui.lineEdit.setText("")
        print(len(self.song_list_local))
        if len(self.song_list_local) == 0:
            self.alert("Warning! No songs in playlist")
        print(self.m_media.state())
        if self.m_media.state() == Phonon.PlayingState:
            self.m_media.pause()
        elif self.m_media.state() == Phonon.PausedState or self.m_media.state() == Phonon.StoppedState:
            self.m_media.play()

        self.ui.lineEdit.setText(os.path.basename(self.m_media.currentSource().fileName()))

    #### Пауза ####

    def pause(self):
        self.m_media.pause()

    #### Следующая песня ####
    def nextSong(self):
        self.ui.lineEdit.setText("")
        print(self.sources)
        print(len(self.sources))
        #if self.index == 0:
        #    self.index = len(self.sources)
        #self.index -= 1

        # ПОЛУЧЕНИЕ ИНДЕКСА ТЕКУЩЕЙ ПЕСНИ... ЧТОБЫ УКАЗАТЬ ИНДЕКС СЛЕДУЮЩЕЙ
        # ДЛЯ СРАВНЕНИЯ ИСПОЛЬЗОВАТЬ РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ !!!

        print(self.m_media.currentSource.fileName())
        self.m_media.setCurrentSource(self.sources[self.index])
        self.play()
    #### Предыдущая песня ####

    def prevSong(self):
        print(self.sources)
        print(len(self.sources))
        if self.index == len(self.sources)-1:
            self.index = 0
        self.index += 1
        self.m_media.setCurrentSource(self.sources[self.index])
        self.play()

    """
    def stop(self):
        self.m_media.stop()                     #остановить и пересоздать ресурс для проигрывания сначала
        self.m_media.setCurrentSource(
        Phonon.MediaSource(
            "https://cs9-15v4.vk.me/p5/437ded476b919e.mp3?extra=3nV5RppDS-MPkNVZlYbcUxJ7KUQrtwVEhG6JYT769UWZY1Rp_UMd1aj3V2W3oVzDUYkBf20RMHTBTBIsHlJICqdWXJbCeoe0esH8R0bRzXm39A6soFXJYpMn2QA4wZ7VS2Avw1Lz"))
    """
    #### Окошко About ####
    def about(self):
        QtGui.QMessageBox.information(self, "About Music Player",
                                      "The Music Player example shows how to use Phonon - the "
                                      "multimedia framework that comes with Qt - to create a "
                                      "simple music player.")
    #### Ползунок ####

    def slider_value_change(self):
        # if self.m_media.state() == Phonon.PlayingState or self.m_media.state() == Phonon.PausedState:
        value = self.ui.horizontalSlider.value()
        print(value)
        self.m_media.seek(value)
        self.m_media.play()

    def delayedInit(self):
        if not self.m_media:
            self.m_media = Phonon.MediaObject(self)
            audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
            Phonon.createPath(self.m_media, audioOutput)

    #### Получение плейлиста с конташки

    def getMyPlaylist(self):    # плейлист из вконтакте
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
#### отображение капчи ###
    def capcha(self, captcha):
        key = input("Enter Captcha {0}: ".format(captcha.get_url())).strip()
        return captcha.try_again(key)

    def stateChanged(self, newState, oldState):
        if newState == Phonon.ErrorState:
            if self.mediaObject.errorType() == Phonon.FatalError:
                QtGui.QMessageBox.warning(self, "Fatal Error", self.mediaObject.errorString())
            else:
                QtGui.QMessageBox.warning(self, "Error", self.mediaObject.errorString())

        elif newState == Phonon.PlayingState:
             self.playAction.setEnabled(False)
             self.pauseAction.setEnabled(True)
             self.stopAction.setEnabled(True)

        elif newState == Phonon.StoppedState:
             self.stopAction.setEnabled(False)
             self.playAction.setEnabled(True)
             self.pauseAction.setEnabled(False)
                #self.timeLcd.display("00:00")

        elif newState == Phonon.PausedState:
             self.pauseAction.setEnabled(False)
             self.stopAction.setEnabled(True)

        self.playAction.setEnabled(True)
#### Клик по таблице ####
    def tableClicked(self, row, column):
        wasPlaying = (self.m_media.state() == Phonon.PlayingState)

        self.m_media.stop()
        self.m_media.clearQueue()

        self.m_media.setCurrentSource(self.sources[row])

        if wasPlaying:
            self.play()
        else:
            self.m_media.stop()
#### Открытие файлов ####
    def open(self):
        dialog = QFileDialog()
        dialog.setViewMode(QFileDialog.Detail)

        self.song_list_local = dialog.getOpenFileNames(self,
                                                  'Open audio file', '/home',
                                                  "Audio Files (*.mp3 *.wav *.ogg)")
        self.index = len(self.song_list_local)
        print("index = ", self.index)
        self.sources = []

        for str in self.song_list_local:
            self.sources.append(Phonon.MediaSource(str))

        if self.sources:
            self.m_media.setCurrentSource(self.sources[0])

        self.ui.tableWidget.setColumnCount(1)
        self.ui.tableWidget.setRowCount(len(self.sources))

        for n in range(len(self.sources)):
            self.ui.tableWidget.setItem(n, 0, QtGui.QTableWidgetItem(os.path.basename(self.sources[n].fileName()).split('.')[0]))


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
