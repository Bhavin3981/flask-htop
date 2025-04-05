from flask import Flask
import os
import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route("/htop")
def htop():
    # Full name
    name = "Bhavin Giniya"

    # Get system username
    username = os.getenv("USER") or os.getenv("USERNAME") or os.getlogin()

    # Get IST time
    ist = pytz.timezone("Asia/Kolkata")
    time_ist = datetime.datetime.now(ist)

    # Get top command output
    top_output = subprocess.getoutput("top -b -n1 | head -20")

    # Format the response
    response = f"""
    <pre>
    Name: {name}
    User: {username}
    Server Time (IST): {time_ist}
    
    TOP output:
    {top_output}
    </pre>
    """
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
