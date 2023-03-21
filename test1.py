import json
import random
import urllib.request


def readJson():
    with open('sample.json') as user_file:
        datas = user_file.read()
        results = json.loads(datas)
    # encoding = user_file.info().get_content_charset('utf-8')
    # results = json.loads(data.decode(encoding))
        #print(results)
    
    # for data in results['items']:
    #     videoIds = (data['id']['kind'])
    #     print(videoIds)
    #     IDlist.append(videoIds)
    #     videoId = random.choice(IDlist)
    #     #print(videoIds)
    #     return f'https://www.youtube.com/embed/{videoId}?rel=0'
    
    video_link_array = [f"https://www.youtube.com/watch?v={video['id']['videoId']}"
                        for video in results['items']]
    print(video_link_array)


readJson()