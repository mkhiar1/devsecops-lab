from flask import Flask, request
import subprocess
import hashlib

app = Flask(__name__)

@app.route("/ping", methods=["POST"])
def ping():
    host = request.json.get("host", "")
    cmd = f"ping -c 1 {host}"
    output = subprocess.check_output(cmd, shell=True)
    return {"output": output.decode()}

@app.route("/hash", methods=["POST"])
def hash_password():
    pwd = request.json.get("password", "admin")
    hashed = hashlib.md5(pwd.encode()).hexdigest()
    return {"md5": hashed}
