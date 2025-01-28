
---

Instagram Video Downloader API

A lightweight, serverless API service built with Python and Instaloader to extract and download video URLs from Instagram posts or reels. Deployed on Vercel, the service offers a simple endpoint for seamless video URL retrieval.


---

Features

📥 Extract video URLs from public Instagram posts and reels.

🔗 REST API endpoint for easy integration.

⚡ Serverless deployment on Vercel for high availability and scalability.

🛠 Returns direct video URLs in a clean JSON format.



---

API Usage

Endpoint

GET /api/instagram

Query Parameters

Example Request

GET https://your-vercel-app.vercel.app/api/instagram?url=https://www.instagram.com/reel/[POST_ID]

Response Format

{
    "video_url": "https://scontent-xxx.cdninstagram.com/xxx.mp4"
}


---






---

Best Practices

Respect Instagram’s Terms of Service: This tool should be used responsibly and strictly for educational or personal purposes.

Caching: Implement caching mechanisms to reduce API calls and improve performance.

Rate Limiting: Prevent overuse of the API by adding rate-limiting measures.





---

Dependencies

Python 3.9+

Instaloader

Vercel Python Runtime



---

Important Notes

This API works only for publicly accessible Instagram posts and reels. Posts from private accounts require authentication.

Privacy Restrictions: Videos may not be accessible in some cases due to regional or account-specific restrictions.



---

Contributing

We welcome contributions to improve this API! Submit issues, feature requests, or pull requests on the GitHub repository.


---

License

This project is licensed under the MIT License.


---

Disclaimer

This project is not affiliated with Instagram or its parent company, Meta. Use it responsibly and adhere to Instagram’s policies.


---

