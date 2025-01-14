import yt_dlp
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get-audio', methods=['GET'])
def get_audio():
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({"error": "YouTube URL is required."}), 400

    try:
        # Use yt-dlp to extract audio URL
        ydl_opts = {'format': 'bestaudio'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            audio_url = info['url']
            return jsonify({"audioUrl": audio_url}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Vercel requires this handler for serverless functions
def handler(event, context):
    from flask_lambda import FlaskLambda
    app_lambda = FlaskLambda(app)
    return app_lambda(event, context)
