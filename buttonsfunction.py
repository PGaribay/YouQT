import json
import urllib.request
import random

durationMenu = ['any', 'short', 'medium', 'long']
API_key = str(input('Please input your Youtube API key to use this app: '))
class buttons:
    durationSet = ['any']

    def __init__(self, duration='any'):
        self.duration = duration
        #print(self.duration)

    def getVideo(self):
        self.API_Key = API_key
        urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults=10&type=video&videoDuration={}&videoEmbeddable=true".format(
            self.API_Key, buttons.durationSet[-1])
        #print(urlData)
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        results = json.loads(data.decode(encoding))
        #print(results)
        video_link_array = [f"https://www.youtube.com/watch?v={video['id']['videoID']}"
                                for video in results['items']]
        return random.choice(video_link_array)
            
            
    @classmethod
    def anydura(cls):
        duration = durationMenu[0]
        return buttons.durationSet.append(duration)

    @classmethod
    def shortdura(cls):
        duration = durationMenu[1]
        return str(buttons.durationSet.append(duration))

    @classmethod
    def mediumdura(cls):
        duration = durationMenu[2]
        return buttons.durationSet.append(duration)

    @classmethod
    def longdura(cls):
        duration = durationMenu[3]
        return buttons.durationSet.append(duration)





if __name__ == "__main__":

    y=buttons(buttons.anydura())
    print(y)
    print(y.getVideo())
    print(buttons.durationSet)
