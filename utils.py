from shazamio import Shazam
import os


async def find_song(filename):
    shazam = Shazam()
    shazaming = await shazam.recognize_song(filename)
    
    if shazaming.get('track', False):
        title = shazaming.get('track').get('title')
        subtitle = shazaming.get('track').get('subtitle')
        audio_url = shazaming['track']['hub']['actions'][-1]['uri']
        photo_url = shazaming['track']['images']['background']
        
        os.remove(filename)
        
        return title, subtitle, audio_url, photo_url
    else:
        return False
