from flask import Flask, request, redirect
import os
import sqlite3
app = Flask(__name__)

def db():
    conn = sqlite3.connect("kaamwala.db")
    conn.execute("CREATE TABLE IF NOT EXISTS bookings (name TEXT, phone TEXT, kaam TEXT)")
    conn.execute("CREATE TABLE IF NOT EXISTS workers (name TEXT, phone TEXT, kaam TEXT, price TEXT)")
    return conn

STYLE = """
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:Arial,sans-serif}
body{background:#f2f4f8;padding:15px}
.header{background:linear-gradient(135deg,#ff6b00,#ff9a00);color:white;padding:25px 20px;border-radius:20px;text-align:center;margin-bottom:20px}
.header h1{font-size:28px}
.header p{opacity:0.9;margin-top:5px;font-size:14px}
.header-dark{background:linear-gradient(135deg,#1e1e2e,#3a3a5c)}
.card{background:white;padding:20px;border-radius:18px;box-shadow:0 4px 15px rgba(0,0,0,0.08);margin-bottom:15px}
.card h2{font-size:20px;margin-bottom:15px}
label{font-size:13px;color:#666;font-weight:bold}
input,select{width:100%;padding:13px;border:1px solid #ddd;border-radius:12px;margin:6px 0 14px 0;font-size:15px;background:#f9f9f9}
.btn{width:100%;background:#ff6b00;color:white;border:none;padding:15px;border-radius:12px;font-size:16px;font-weight:bold;cursor:pointer}
.btn-green{background:#00b894}
.link{display:block;text-align:center;margin-top:15px;color:#ff6b00;font-weight:bold;text-decoration:none}
.services{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:20px}
.service{background:white;padding:18px 10px;border-radius:16px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,0.05)}
.service span{font-size:30px}
.service b{display:block;margin-top:8px;font-size:14px}
.service small{color:#888}
.worker-card{background:white;padding:16px;border-radius:16px;display:flex;align-items:center;gap:12px;margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,0.05)}
.avatar{width:50px;height:50px;background:#ffe0c7;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:24px}
.price{margin-left:auto;background:#e8fff3;color:#00b894;padding:6px 10px;border-radius:20px;font-weight:bold;font-size:14px}
.success{text-align:center;padding:40px 20px}
.success h1{font-size:50px}
.stats{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:20px}
.stat{background:white;padding:20px;border-radius:16px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,0.05)}
.stat h1{font-size:32px;color:#ff6b00}
.stat p{color:#888;font-size:13px;margin-top:5px}
.booking-card{background:white;padding:16px;border-radius:16px;margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,0.05);border-left:4px solid #ff6b00}
.tag{background:#fff0e0;color:#ff6b00;padding:4px 10px;border-radius:20px;font-size:12px;font-weight:bold}
.call-btn{display:inline-block;background:#00b894;color:white;padding:8px 14px;border-radius:20px;text-decoration:none;font-size:13px;font-weight:bold;margin-top:8px}
.del-btn{display:inline-block;background:#ff4757;color:white;padding:8px 14px;border-radius:20px;text-decoration:none;font-size:13px;font-weight:bold;margin-top:8px;margin-left:5px}
</style>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        conn = db()
        conn.execute("INSERT INTO bookings VALUES (?,?,?)", (request.form["name"], request.form["phone"], request.form["kaam"]))
        conn.commit()
        return STYLE + """<div class="card success"><h1>✅</h1><br><h2>Booking Ho Gayi!</h2><p>Worker jald hi contact karega.</p><br><a class="btn" href="/" style="text-decoration:none;display:block">Wapas Jao</a></div>"""
    return STYLE + """
    <div class="header"><h1>KAAMWALA 🔧</h1><p>Ghar ka har kaam, ek click me</p></div>
    <div class="services">
        <div class="service"><span>🔧</span><b>Plumber</b><small>Rs 199 se</small></div>
        <div class="service"><span>⚡</span><b>Electrician</b><small>Rs 149 se</small></div>
        <div class="service"><span>❄️</span><b>AC Wala</b><small>Rs 499 se</small></div>
        <div class="service"><span>🎨</span><b>Painter</b><small>Rs 999 se</small></div>
    </div>
    <div class="card"><h2>Booking Karo 📅</h2>
    <form method="POST">
        <label>TUMHARA NAAM</label><input name="name" placeholder="Ex: Rahul Sharma" required>
        <label>PHONE NUMBER</label><input name="phone" placeholder="98765 43210" required>
        <label>KAUNSA KAAM CHAHIYE?</label>
        <select name="kaam"><option>Plumber</option><option>Electrician</option><option>AC Wala</option><option>Painter</option></select>
        <button class="btn">BOOK KARO →</button>
    </form></div>
    <a class="link" href="/workers">👷 Workers Dekho</a>
    <a class="link" href="/worker">Worker ho? Yaha Register Karo →</a>
    """

@app.route("/worker", methods=["GET", "POST"])
def worker():
    if request.method == "POST":
        conn = db()
        conn.execute("INSERT INTO workers VALUES (?,?,?,?)", (request.form["name"], request.form["phone"], request.form["kaam"], request.form["price"]))
        conn.commit()
        return STYLE + """<div class="card success"><h1>🎉</h1><br><h2>Welcome to KaamWala!</h2><p>Tum register ho gaye ho.</p><br><a class="btn btn-green" href="/workers" style="text-decoration:none;display:block">Workers List Dekho</a></div>"""
    return STYLE + """
    <div class="header"><h1>Worker Bano 👷</h1><p>Roz kaam pao, paisa kamao</p></div>
    <div class="card"><h2>Register Karo</h2>
    <form method="POST">
        <label>TUMHARA NAAM</label><input name="name" placeholder="Ex: Ramesh Kumar" required>
        <label>PHONE NUMBER</label><input name="phone" placeholder="98765 43210" required>
        <label>TUM KYA KAAM KARTE HO?</label>
        <select name="kaam"><option>Plumber</option><option>Electrician</option><option>AC Wala</option><option>Painter</option></select>
        <label>TUMHARI FEES (Rs)</label><input name="price" placeholder="Ex: 300" required>
        <button class="btn btn-green">REGISTER KARO →</button>
    </form></div>
    <a class="link" href="/">← Home Jao</a>
    """

@app.route("/workers")
def workers():
    conn = db()
    rows = conn.execute("SELECT * FROM workers").fetchall()
    html = STYLE + """<div class="header"><h1>Hamare Workers 👷</h1><p>Verified & Trusted</p></div>"""
    emojis = {"Plumber":"🔧","Electrician":"⚡","AC Wala":"❄️","Painter":"🎨"}
    for r in rows:
        e = emojis.get(r[2],"🔧")
        html += f"""<div class="worker-card"><div class="avatar">{e}</div><div><b>{r[0]}</b><br><small>{r[2]} • 📞 {r[1]}</small></div><div class="price">Rs {r[3]}</div></div>"""
    if not rows:
        html += "<div class='card'><p>Abhi koi worker nahi hai.</p></div>"
    html += "<a class='link' href='/'>← Home Jao</a>"
    return html

@app.route("/admin")
def admin():
    conn = db()
    bookings = conn.execute("SELECT rowid, * FROM bookings").fetchall()
    workers_list = conn.execute("SELECT * FROM workers").fetchall()
    html = STYLE + """
    <div class="header header-dark"><h1>ADMIN DASHBOARD 👑</h1><p>KaamWala Boss View</p></div>
    <div class="stats">
        <div class="stat"><h1>""" + str(len(bookings)) + """</h1><p>Total Bookings</p></div>
        <div class="stat"><h1>""" + str(len(workers_list)) + """</h1><p>Total Workers</p></div>
    </div>
    <div class="card"><h2>📅 Nayi Bookings</h2></div>
    """
    if not bookings:
        html += "<div class='card'><p>Abhi koi booking nahi aayi.</p></div>"
    for b in reversed(bookings):
        html += f"""<div class="booking-card"><b>{b[1]}</b> <span class="tag">{b[3]}</span><br><small>📞 {b[2]}</small><br><a class="call-btn" href="tel:{b[2]}">📞 Call Karo</a> <a class="del-btn" href="/delete/{b[0]}">🗑️ Delete</a></div>"""
    html += """<div class="card"><h2>👷 Sab Workers</h2></div>"""
    for w in workers_list:
        html += f"""<div class="worker-card"><div class="avatar">👷</div><div><b>{w[0]}</b><br><small>{w[2]} • 📞 {w[1]}</small></div><div class="price">Rs {w[3]}</div></div>"""
    html += "<a class='link' href='/'>← Home Jao</a>"
    return html

@app.route("/delete/<int:bid>")
def delete_booking(bid):
    conn = db()
    conn.execute("DELETE FROM bookings WHERE rowid=?", (bid,))
    conn.commit()
    return redirect("/admin")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
