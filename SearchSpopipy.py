import spotipy
import sys
import pprint
import spotipy.util as util
query = 'Depeche Mode- Speak and Spell'

if len(sys.argv) > 1:
    query = sys.argv[1]
else:
    print "Usage:%s query" %(sys.argv[0],)
    sys.exit()


if __name__ == '__main__':
    #sp = spotipy.Spotify(auth = token)
    sp = spotipy.Spotify()
    results = sp.search(q=query, limit=20)
    print results
    for i, t in enumerate(results['tracks']['items']):
        print ' ', i, t['name'].encode('utf-8')
