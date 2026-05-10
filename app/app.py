from flask import Flask, request, render_template
from datetime import datetime
import os

app = Flask(__name__)

LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
 os.makedirs(LOG_DIR)

def get_client_ip():
 x_forwarded_for = request.headers.get("X-Forwarded-For", "")
 if x_forwarded_for:
 return x_forwarded_for.split(",")[0].strip()
 return request.remote_addr or "unknown"

def log_attempt(ip, status):
 now = datetime.now()
 filename = now.strftime("%Y-%m-%d") + ".log"
 filepath = os.path.join(LOG_DIR, filename)
 user_agent = request.headers.get("User-Agent", "-")
 log_line = f'{ip} - - [{now.strftime("%d/%b/%Y:%H:%M:%S +0000")}] "POST /login HTTP/1.1" {status} 0 "-" "{user_agent}"\n'
 with open(filepath, "a", encoding="utf-8") as f:
 f.write(log_line)

@app.route("/", methods=["GET"])
def index():
 return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    ip = get_client_ip()
    username = request.form.get("username")
    password = request.form.get("password")
    if username == "admin" and password == "admin123":
        log_attempt(ip, 200)
        return "Login correcto"
    else:
        log_attempt(ip, 401)
        return "Login incorrecto", 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
