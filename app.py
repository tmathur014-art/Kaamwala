    from flask import Flask, request, redirect, render_template_string
import json, os

app = Flask(__name__)
FILE = "workers.json"

def load_workers():
    if os.path.exists(FILE):
        try:
            with open(FILE) as f:
                return json.load(f)
        except:
            return []
    # Default workers
    return [
        {"name": "Raju Kumar", "work": "Electrician", "area": "Delhi", "price": "200", "phone": "9876543210"},
        {"name": "Amit Sharma", "work": "Plumber", "area": "Delhi", "price": "250", "phone": "9876543211"},
        {"name": "Vikash Yadav", "work": "Painter", "area": "Delhi", "price": "300", "phone": "9876543212"},
    ]

def save_workers(workers):
    with open(FILE, "w") as f:
        json.dump(workers, f)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>KAAMWALA - Kaam Wala Bhai</title>
<style>
body{font-family:Arial;background:#f5f5f5;margin:0;padding:0}
.header{background:#111;color:white;text-align:center;padding:25px 10px}
.header h1{margin:0;font-size:32px;letter-spacing:2px}
.header p{margin:5px;color:#ccc}
.thanks{background:#ffe0ec;color:#d81b60;text-align:center;padding:15px;margin:15px;border-radius:15px;border:2px solid #ff8fab}
.thanks h2{margin:0;font-size:22px}
.thanks p{margin:5px;font-style:italic}
.btns{display:flex;gap:10px;justify-content:center;padding:0 15px}
.btn{flex:1;text-align:center;padding:14px;border-radius:12px;text-decoration:none;font-weight:bold;color:white}
.join{background:#ff4757}
.book-top{background:#2ed573}
.card{background:white;margin:15px;padding:15px;border-radius:15px;box-shadow:0 2px 10px rgba(0,0,0,0.1)}
.card h3{margin:0}
.badge{background:#eee;padding:4px 10px;border-radius:20px;font-size:12px}
.price{font-size:20px;font-weight:bold;color:green}
.wbtn{display:block;background:#25D366;color:white;text-align:center;padding:12px;border-radius:10px;text-decoration:none;font-weight:bold;margin-top:10px}
.form input,.form select{width:100%;padding:12px;margin:8px 0;border:1px solid #ddd;border-radius:10px;box-sizing:border-box}
.form button{width:100%;padding:14px;background:#111;color:white;border:none;border-radius:10px;font-weight:bold;font-size:16px}
</style>
</head>
<body>
<div class="header">
<h1>KAAMWALA</h1>
<p>Kaam Wala Bhai - Har Kaam Ke Liye</p>
</div>

<div class="thanks">
<h2>Special Thanks to Mohini ❤️</h2>
<p>Is website ke peeche sabse badi inspiration</p>
</div>

<div class="btns">
<a class="btn join" href="/join">+ Worker Bano</a>
<a class="btn book-top" href="#workers">Worker Dekho 👇</a>
</div>

<div id="workers">
{% for w in workers %}
<div class="card">
<h3>{{ w.name }} <span class="badge">{{ w.work }}</span></h3>
<p>📍 {{ w.area }} | 📞 {{ w.phone }}</p>
<p class="price">₹{{ w.price }} / visit</p>
<a class="wbtn" href="https://wa.me/91{{ w.phone }}?text=Hi%20{{ w.name }}%2C%20mujhe%20{{ w.work }}%20ka%20kaam%20karwana%20hai%20-%20KAAMWALA%20se" target="_blank">📱 WhatsApp Pe Book Karo</a>
</div>
{% endfor %}
</div>

<p style="text-align:center;color:#888;padding:20px">Made with ❤️ | KAAMWALA</p>
</body>
</html>
"""

JOIN_HTML = """
<!DOCTYPE html>
<html><head><meta name="viewport" content="width=device-width, initial-scale=1"><title>Worker Bano</title>
<style>body{font-family:Arial;background:#f5f5f5;padding:15px}.box{background:white;padding:20px;border-radius:15px}input,select{width:100%;padding:12px;margin:8px 0;border:1px solid #ddd;border-radius:10px;box-sizing:border-box}button{width:100%;padding:14px;background:#ff4757;color:white;border:none;border-radius:10px;font-weight:bold;font-size:16px}a{display:block;text-align:center;margin-top:15px}</style>
</head><body><div class="box">
<h2>👷 Worker Bano - KAAMWALA</h2>
<form method="POST">
<input name="name" placeholder="Apna Naam" required>
<select name="work" required><option value="">Kaam Chune</option><option>Electrician</option><option>Plumber</option><option>Painter</option><option>Carpenter</option><option>AC Technician</option><option>Cleaner</option><option>Driver</option><option>Mason</option></select>
<input name="area" placeholder="Area / City - jaise Delhi" required>
<input name="price" placeholder="Price - jaise 200" required>
<input name="phone" placeholder="WhatsApp Number - 10 digit" required>
<button type="submit">Join Karo ✅</button>
</form>
<a href="/">← Wapas Homepage Pe</a>
</div></body></html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, workers=load_workers())

@app.route("/join", methods=["GET","POST"])
def join():
    if request.method == "POST":
        workers = load_workers()
        workers.append({
            "name": request.form["name"],
            "work": request.form["work"],
            "area": request.form["area"],
            "price": request.form["price"],
            "phone": request.form["phone"]
        })
        save_workers(workers)
        return redirect("/")
    return JOIN_HTML

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
