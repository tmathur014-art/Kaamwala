import os
from flask import Flask, render_template_string

app = Flask(__name__)

# --- DATA ---
workers = [
    {"name": "Ramesh Kumar", "skill": "Plumber", "city": "Delhi", "price": "₹300", "phone": "919999999999"},
    {"name": "Suresh Singh", "skill": "Electrician", "city": "Delhi", "price": "₹400", "phone": "919999999999"},
    {"name": "Priya Sharma", "skill": "Beautician", "city": "Delhi", "price": "₹500", "phone": "919999999999"},
]

HTML = """
<!DOCTYPE html>
<html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>KAAMWALA</title>
<style>
body{font-family:Arial;background:#fff5f5;margin:0;padding:15px}
h1{text-align:center;color:#e11d48}
.card{background:white;padding:15px;border-radius:15px;margin:10px 0;box-shadow:0 2px 10px #ddd}
.btn{display:block;background:#25D366;color:white;text-align:center;padding:12px;border-radius:10px;text-decoration:none;font-weight:bold;margin-top:10px}
.top{text-align:center;color:#e11d48;font-weight:bold}
</style></head>
<body>
<p class="top">Special Thanks to Mohini ❤️</p>
<h1>🔧 KAAMWALA</h1>
<p style="text-align:center">Delhi ke Best Workers - Direct Book Karo</p>
{% for w in workers %}
<div class="card">
<h3>{{ w.name }} - {{ w.skill }}</h3>
<p>📍 {{ w.city }} | 💰 {{ w.price }}</p>
<a class="btn" href="https://wa.me/{{ w.phone }}?text=Hi, mujhe {{ w.skill }} chahiye">WhatsApp Pe Book Karo</a>
</div>
{% endfor %}
</body></html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, workers=workers)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)    
