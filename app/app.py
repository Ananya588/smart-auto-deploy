from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Coming Soon 🚀</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Segoe UI', sans-serif;
            color: white;
            text-align: center;
            background: linear-gradient(-45deg, #1e3c72, #2a5298, #0f2027, #203a43);
            background-size: 400% 400%;
            animation: gradient 10s ease infinite;
        }

        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .container {
            padding: 40px;
            border-radius: 15px;
            background: rgba(0, 0, 0, 0.5);
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
            backdrop-filter: blur(10px);
        }

        h1 {
            font-size: 3rem;
            margin-bottom: 10px;
        }

        p {
            font-size: 1.2rem;
            color: #ddd;
        }

        .badge {
            margin-top: 20px;
            display: inline-block;
            padding: 10px 20px;
            border-radius: 50px;
            background: #ff9800;
            color: black;
            font-weight: bold;
            animation: pulse 1.5s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.08); }
            100% { transform: scale(1); }
        }

        .footer {
            margin-top: 20px;
            font-size: 0.9rem;
            color: #bbb;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>🚀 Coming Soon</h1>
    <p>Auto Deploy v2 is launching soon!</p>
    <p>We're building something powerful ⚡</p>

    <div class="badge">Stay Tuned 🔥</div>

    <div class="footer">
        Made with ❤️ using Flask
    </div>
</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)