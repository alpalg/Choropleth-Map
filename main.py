import json
from flask import Flask
from flask import render_template
from core.data_source import projects_by_countries
app = Flask(__name__)
        
# Creating a dump of 'projects_by_countries'
dump = json.dumps(projects_by_countries)

@app.route('/')
def index():
    return render_template('index.html', projects_by_countries=dump)

if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=8080)
