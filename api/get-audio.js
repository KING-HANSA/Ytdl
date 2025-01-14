const { exec } = require("child_process");
const path = require("path");

// Function to extract audio URL
export default function handler(req, res) {
  if (req.method !== "GET") {
    return res.status(405).json({ error: "Method not allowed. Use GET." });
  }

  const videoUrl = req.query.url;

  if (!videoUrl) {
    return res.status(400).json({ error: "YouTube URL is required." });
  }

  const command = `yt-dlp -g -f bestaudio ${videoUrl}`;
  exec(command, { cwd: path.resolve() }, (error, stdout, stderr) => {
    if (error) {
      return res.status(500).json({ error: `Error: ${stderr || error.message}` });
    }

    const audioUrl = stdout.trim();
    res.status(200).json({ audioUrl });
  });
}
