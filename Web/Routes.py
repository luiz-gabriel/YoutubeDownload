from flask import Flask, request
from Validates.YoutubeUrlValidate import YoutubeUrlValidate as ytv
from flask import escape
from Converters.YoutubeDownloadToConvetMp3 import Mp3DownloadAndToConvert
class dispachant:
    app__ = Flask(__name__)


    @app__.route("/convert/music", methods=["POST"])
    def home():
        link = request.args.get('link')
        if ytv.validate(link):
           return Mp3DownloadAndToConvert.download(link)
        else:
            return {"error": "invalid link"}, 400

    app__.run(debug=False)
