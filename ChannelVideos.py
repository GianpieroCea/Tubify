# This script uses Youtube Client to get "some" videos from
# a channel

# AUTHOR: Gianpiero Cea

#load the build method from the Client
from apiclient.discovery import build
#sys module for command line use
import sys


#Properties:

apiKey = 'INSERT_YOUTUBE_API_KEY'  #DON'T SHOW!!
#channelId = 'UCjJg3J-4Ik6HaD4aohVJIvQ'

if len(sys.argv) > 1:
    channelId = sys.argv[1]
else:
    print "Usage:%s channelId" %(sys.argv[0],)
    sys.exit()
#construct the build object:
youtube = build('youtube' , 'v3' , developerKey = apiKey)

#construct the request object:
request = youtube.search().list( part= "id,snippet",channelId = channelId, maxResults = 25)

#save the response:
response = request.execute()




if __name__ == '__main__':


    #print a list of video id and snippet:

    for result in response.get("items",[]):
        if result["id"]["kind"] == "youtube#video":
            print result["id"]["videoId"].encode('utf-8') , result["snippet"]["title"].encode('utf-8')
