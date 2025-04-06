from flask import Flask, render_template, jsonify
import os
import datetime

app = Flask(__name__)

# Get version from environment variable or default to "blue"
VERSION = os.environ.get("APP_VERSION", "blue")
# Get background color based on version
BG_COLOR = "lightblue" if VERSION == "blue" else "lightgreen"

@app.route('/')
def home():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', 
                          version=VERSION, 
                          bg_color=BG_COLOR, 
                          current_time=current_time)

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "version": VERSION})

@app.route('/api/greeting')
def greeting():
    return jsonify({
        "message": f"Hello from {VERSION} version!",
        "timestamp": datetime.datetime.now().isoformat()
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)