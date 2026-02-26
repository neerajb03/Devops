from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>NGINX Dashboard</title>

<style>
    body {
        margin: 0;
        font-family: Arial, sans-serif;
        background: linear-gradient(135deg, #ff758c, #ff7eb3);
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    .card {
        background: #ffffff;
        width: 650px;
        padding: 35px;
        border-radius: 18px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.25);
        text-align: center;
    }

    h1 {
        color: #ff4b6e;
        margin-bottom: 20px;
    }

    ul {
        list-style: none;
        padding: 0;
        margin: 20px 0;
    }

    li {
        background: #fff1f5;
        margin: 10px 0;
        padding: 12px;
        border-radius: 8px;
        font-weight: bold;
        color: #444;
    }

    .tag {
        margin-top: 20px;
        padding: 10px;
        background: #ffe3ea;
        border-radius: 10px;
        font-size: 14px;
        color: #666;
    }
</style>
</head>

<body>

<div class="card">
    <h1>⚡ NGINX Server</h1>

    <ul>
        <li>🚀 Reverse Proxy</li>
        <li>⚖️ Load Balancer</li>
        <li>📁 Static File Server</li>
        <li>🔐 SSL Termination</li>
        <li>🌐 API Gateway</li>
    </ul>

    <div class="tag">
        DevOps Practice • Flask + NGINX
    </div>
</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)