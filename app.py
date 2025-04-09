from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    #Full name
    full_name = "Preetha S"

    #display Username
    username = os.getenv("USER") or os.getenv("USERNAME") or "unknown"

    #display Server Time in IST
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)

    # top output
    try:
        top_output = subprocess.check_output("top -b -n 1", shell=True, text=True)
    except Exception as e:
        top_output = f"Error running top: {e}"

    #Creating HTML-like plain text response
    result = f"""
    Name: {full_name}
    User: {username}
    Server Time (IST): {ist_time}
    
    TOP output:
    {top_output}
    """

    return f"<pre>{result}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)