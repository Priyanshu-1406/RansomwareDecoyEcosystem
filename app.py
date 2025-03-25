from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')

        if username=='*******' and password=='*********':
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Invalid Credentials.")
    return render_template('login.html')
@app.route('/run-script', methods=['POST'])
def run_script():
    try:
        subprocess.Popen(["python", "decoy_manager.py"])  
        return jsonify({"message": "Script started successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/download-log', methods=['GET'])
def download_log():
    log_file_path = 'file_activity.log'
    if os.path.exists(log_file_path):
        return send_file(log_file_path, as_attachment=True)
    else:
        return jsonify({"error": "Log file not found"}), 404
@app.route('/docs')
def docs():
    return render_template('docs.html')
if __name__ == '__main__':
    app.run(debug=True)
