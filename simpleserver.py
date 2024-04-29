# python -m venv venv
# VM On Linux: source ./venv/bin/activate
# run python simpleserver.py > it will say No module named 'flask'
# so pip install flask, then rerun python simpleserver.py
# http://127.0.0.1:5000 > hello from simple server
# Crtl + C
# pip freeze > requirement.txt > ls > (requirements.txt will be there)
# git commit to github



from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/', methods=['Get'])

def getAllBands():
    return "hello from simple server"

if __name__ == "__main__":
    app.run(debug=True)

# save to folder deploy2pa