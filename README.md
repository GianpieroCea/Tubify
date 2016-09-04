# Tubify

At the moment just a set of sparse python scripts written in less than an our. The idea was to write something where I enter the channelId of a YouTube channel 
that posted only songs and albums and I would get an automatically generated playlist on Spotify.

I Succesfully implemented the YouTube searcher (I mean I just used Yotube Client for Python). I tried using [Spotipy](https://github.com/plamere/spotipy) to make the code to create 
the Spotify playlist but setting up the right Authorization flow proved more annoying and longer than I thought.

I still plan on finishing it though!

# What the code can  do at the moment

## Getting the videos of a channel
You can use ChannelVideos.py from the terminal to list the videos of a channel you know the YouTube channelId (this is the code you get from the URL: https://www.youtube.com/channel/channelID)
You'll need to request a Youtube DATA Api Key (which you need to insert in the code!) and you also need to install the [Youtube Client for Python](https://developers.google.com/api-client-library/python/)
Then you clone the repo , navigate to the Tubify folder and you do:

> python ChannelVideo.py channelId

## Searching spotify (non authorised)
You don't need to obtain the authorization from spotify. Just clone the repo, navigate to the Tubify folder and do:

> python SearchSpopipy.py query
