from http.server import BaseHTTPRequestHandler, HTTPServer
import os

# Update these if using a subfolder for assets
FONT_FILE = "Minecraft.ttf"
HEART_FILE = "heart.png"


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve the Minecraft font
        if self.path.endswith(".ttf"):
            if os.path.exists(FONT_FILE):
                with open(FONT_FILE, "rb") as f:
                    self.send_response(200)
                    self.send_header("Content-type", "font/ttf")
                    self.end_headers()
                    self.wfile.write(f.read())
            else:
                self.send_error(404, "Font not found")
            return

        # Serve the heart image
        if self.path.endswith(".png"):
            if os.path.exists(HEART_FILE):
                with open(HEART_FILE, "rb") as f:
                    self.send_response(200)
                    self.send_header("Content-type", "image/png")
                    self.end_headers()
                    self.wfile.write(f.read())
            else:
                self.send_error(404, "Heart image not found")
            return

        # Serve the main HTML page
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        sweet_note = "You make every day brighter and fill my heart with happiness."

        # Replace localhost in meta tags with your public URL if deploying
        public_url = "https://your-public-url.com"  # <-- update this after deployment

        html_content = f"""
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                <title>For my Darling</title>
                <meta property="og:title" content="For My Darling, Ace <3" />
                <meta property="og:description" content="This is how long we've been together ❤️" />
                <meta property="og:type" content="website" />
                <meta property="og:image" content="{public_url}/heart.png" />
                <meta property="og:url" content="{public_url}/" />

                <style>
                    @font-face {{
                        font-family: 'Minecraft';
                        src: url('{FONT_FILE}') format('truetype');
                    }}
                    body {{
                        background-color: #758fc0;
                        font-family: 'Minecraft', Arial, sans-serif;
                        text-align: center;
                        margin: 0;
                        padding: 0;
                    }}
                    h1 {{
                        color: #ff1493;
                        font-size: 3em;
                        margin-top: 40px;
                    }}
                    p {{
                        font-size: 1.5em;
                        color: #fff;
                        margin-bottom: 40px;
                    }}
                    #counter {{
                        font-size: 1.5em;
                        color: #fff;
                        margin-top: 20px;
                        margin-bottom: 80px;
                    }}
                    .heart {{
                        position: relative;
                        width: 120px;
                        height: 120px;
                        margin: 0 auto;
                        background: red;
                        transform: rotate(-45deg);
                        animation: beat 2s infinite;
                    }}
                    .heart::before,
                    .heart::after {{
                        content: "";
                        position: absolute;
                        width: 120px;
                        height: 120px;
                        border-radius: 50%;
                        background: red;
                    }}
                    .heart::before {{
                        top: -60px;
                        left: 0;
                    }}
                    .heart::after {{
                        left: 60px;
                        top: 0;
                    }}
                    @keyframes beat {{
                        0%, 100% {{
                            transform: rotate(-45deg) scale(1);
                        }}
                        50% {{
                            transform: rotate(-45deg) scale(1.15);
                        }}
                    }}
                    footer {{
                        position: fixed;
                        bottom: 10px;
                        width: 100%;
                        text-align: center;
                        font-size: 1em;
                        color: #fff;
                        font-style: italic;
                    }}
                </style>

                <script>
                    function updateCounter() {{
                        const startDate = new Date("2025-09-06T00:00:00");
                        const now = new Date();
                        let diff = now - startDate;

                        const days = Math.floor(diff / (1000 * 60 * 60 * 24));
                        diff -= days * (1000 * 60 * 60 * 24);

                        const hours = Math.floor(diff / (1000 * 60 * 60));
                        diff -= hours * (1000 * 60 * 60);

                        const minutes = Math.floor(diff / (1000 * 60));
                        diff -= minutes * (1000 * 60);

                        const seconds = Math.floor(diff / 1000);

                        document.getElementById("counter").innerHTML =
                            days + " days, " + hours + " hours, " + minutes + " minutes, " + seconds + " seconds<br>" +
                            "<span style='color:#ffebcd;'>this is how long we've been together &lt;3</span>";
                    }}
                    setInterval(updateCounter, 1000);
                </script>
            </head>
            <body onload="updateCounter()">
                <h1>I love you Ace</h1>
                <p>{sweet_note}</p>
                <div id="counter"></div>
                <div class="heart"></div>
                <footer>made by logan</footer>
            </body>
        </html>
        """

        self.wfile.write(html_content.encode("utf-8"))


def run_server(host="0.0.0.0", port=8080):
    server_address = (host, port)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"Serving on http://{host}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
