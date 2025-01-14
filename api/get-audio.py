import instaloader
from flask import jsonify

def handler(request):
    # Extract the reel URL from the request
    reel_url = request.args.get('url')  # You can pass the URL as a query parameter

    if not reel_url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        # Create an instaloader object
        L = instaloader.Instaloader()

        # Get the post object from the reel URL
        shortcode = reel_url.split("/")[-2]
        post = instaloader.Post.from_shortcode(L.context, shortcode)

        # Extract the video URL (MP4 link)
        if post.is_video:
            video_url = post.video_url  # This gives you the direct URL to the video
            return jsonify({"video_url": video_url})

        else:
            return jsonify({"error": "This is not a video post."}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500
