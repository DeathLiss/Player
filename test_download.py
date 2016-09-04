import vk_api
import os
import requests

song_list = []
class Main:

    def getMyPlaylist(self):  # плейлист из вконтакте
        # данные аккаунта ВК
        login, password = 'lis@gmail.com', 'lalla'

        vk_session = vk_api.VkApi(login, password, captcha_handler=self.capcha)

        try:
            vk_session.authorization()
        except vk_api.AuthorizationError as error_msg:
            print(error_msg)
            return

        tools = vk_api.VkTools(vk_session)
        audio = tools.get_all('audio.get', 100, {'owner_id': 2041524})

        path = "/home/liss/Загрузки/downloads"
        if not os.path.exists(path):
            os.makedirs(path)

        number = audio['count']
        print("Need to download: ", number)

        for song in audio['items']:
            song_list.append(song)

        for i in range(0, number):
            new_filename = path + "/" + song_list[i]['artist'] + " - " + song_list[i]['title'].split("/")[0] + ".mp3"

            if not os.path.exists(new_filename):
                print("FileName: "+new_filename)
                with open(new_filename, "wb") as out:
                    response = requests.get(song_list[i]['url'])
                    out.write(response.content)
        print("Downloading complete")

    def capcha(self, captcha):
        key = input("Enter Captcha {0}: ".format(captcha.get_url())).strip()
        return captcha.try_again(key)

if __name__ == '__main__':
    # create application

    w = Main()
    w.getMyPlaylist()
