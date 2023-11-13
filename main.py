from flask import Flask, render_template, request
from utils import find_song
import asyncio


app = Flask(__name__)
app.config['SECRET_KEY'] = "wnbgkjenglkermng#$T#$Tetgege5g6tt2g41e"


@app.route("/", methods=['GET', "POST"])
def home_page():
    context = {}
    error = ""
    if request.method == 'POST':
        try:
            if request.files.get('media_file', False):
                media = request.files.get("media_file")
                media.save(media.filename)
                
                title, subtitle, audio_url, photo_url = asyncio.run(find_song(media.filename))
                context['title'] = title
                context['subtitle'] = subtitle
                context['audio_url'] = audio_url
                context['photo_url'] = photo_url
                return render_template("song.html", context=context, error=error)
        except:
            error = "Нет результатов"
    return render_template("home.html", error=error)
        



if __name__ == '__main__':
    app.run(debug=True)
