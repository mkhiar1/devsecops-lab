from flask import Flask, request
import subprocess
import hashlib
import re
from werkzeug.security import generate_password_hash

app = Flask(__name__)

@app.route("/ping", methods=["POST"])
def ping():
    host = request.json.get("host", "")
    if not re.match(r'^[a-zA-Z0-9._-]{1,253}$', host):
        return {"error": "Hote invalide"}, 400
    try:
        result = subprocess.check_output(
            ["ping", "-c", "1", host],
            text=True, timeout=5
        )
        return {"output": result}
    except Exception as e:
        return {"error": str(e)}, 500


@app.route("/hash", methods=["POST"])
def hash_password():
    pwd = request.json.get("password")
    if not pwd or len(pwd) < 8:
        return {"error": "Mot de passe requis (min 8 caracteres)"}, 400
    hashed = generate_password_hash(pwd)
    return {"password_hash": hashed}, 200
