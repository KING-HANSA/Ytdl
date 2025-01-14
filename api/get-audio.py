import instaloader
import json

def handler(request):
    # Extract the reel URL from the request
    reel_url = request.args.get('url')  # URL parameter passed in the query string

    if not reel_url:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "No URL provided"})
        }

    try:
        # Create an instaloader object
        L = instaloader.Instaloader()

        # Get the post object from the reel URL
        shortcode = reel_url.split("/")[-2]
        post = instaloader.Post.from_shortcode(L.context, shortcode)

        # Extract the video URL (MP4 link)
        if post.is_video:
            video_url = post.video_url  # This gives you the direct URL to the video
            return {
                "statusCode": 200,
                "body": json.dumps({"video_url": video_url})
            }
        else:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "This is not a video post."})
            }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
