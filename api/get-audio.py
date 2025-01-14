import yt_dlp
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

@app.route('/get-audio', methods=['GET'])
def get_audio():
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({"error": "YouTube URL is required."}), 400

    try:
        # Use yt-dlp to extract the audio URL
        ydl_opts = {'format': 'bestaudio'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            audio_url = info['url']
            return jsonify({"audioUrl": audio_url}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Vercel expects a "handler" function
def handler(event, context):
    from werkzeug.middleware.dispatcher import DispatcherMiddleware
    from werkzeug.wrappers import Request, Response

    @Request.application
    def application(request):
        with app.test_request_context(
            base_url=request.base_url,
            method=request.method,
            headers=request.headers,
            query_string=request.query_string,
            data=request.get_data(),
        ):
            response = app.full_dispatch_request()
            return Response(response.get_data(), response.status_code, response.headers)

    return application
