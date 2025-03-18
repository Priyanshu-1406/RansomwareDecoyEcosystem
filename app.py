from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-script', methods=['POST'])
def run_script():
    try:
        subprocess.Popen(["python", "decoy_manager.py"])  
        return jsonify({"message": "Script started successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
