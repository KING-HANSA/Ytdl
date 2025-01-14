import yt_dlp
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

@app.route('/get-audio', methods=['GET'])
def get_audio():
    # Extract the YouTube video URL from the query parameters
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({"error": "YouTube URL is required."}), 400

    try:
        # Use yt-dlp to extract the direct audio URL
        ydl_opts = {'format': 'bestaudio'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            audio_url = info['url']
            return jsonify({"audioUrl": audio_url}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Export the Flask app to be used by Vercel
app = app
