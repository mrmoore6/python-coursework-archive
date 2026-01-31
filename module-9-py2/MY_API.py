import csv
import flask
from flask import request, jsonify
with open('FoodData.csv') as file:
    food_ill_data = [{x: y for x, y in row.items()}
                 for row in csv.DictReader(file, delimiter=',')]
    print(food_ill_data)

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Food Illness Data</h1>
    <p>An Api that returns a list of food-bourne illness outbreaks.</p>
        <h2>Documentation</h2>
        <p>to search for state use <a href="http://127.0.0.1:5000/api/v1/food-illness/outbreaks?state=Iowa">
        http://127.0.0.1:5000/api/v1/food-illness/outbreaks?state=</a></p>
        <p>to search for virus use<a href="http://127.0.0.1:5000/api/v1/food-illness/outbreaks/search?search=Noro">
        http://127.0.0.1:5000/api/v1/food-illness/outbreaks/search?search=</a></p>
        <p>to search for all info use<a href="http://127.0.0.1:5000/api/v1/food-illness/outbreaks/all">
        http://127.0.0.1:5000/api/v1/food-illness/outbreaks/all=</a></p>
        '''

@app.route('/api/v1/food-illness/outbreaks', methods=['GET'])
def api_state():
    if 'state' in request.args:
        state = request.args['state']
    else:
        return 'ERROR NO STATE SPECIFIED '
    results = []
    for outbreaks in food_ill_data:
        if outbreaks['State'] == state:
            results.append(outbreaks)

    return jsonify(results)


@app.route('/api/v1/food-illness/outbreaks/search')
def api_virus_search():
    if 'search' in request.args:
        search = request.args['search']
    else:
        return 'ERROR NO SEARCH SPECIFIED'
    results = []

    for outbreaks in food_ill_data:
        if search.lower() in outbreaks['Genus Species'].lower():
            results.append(outbreaks)
    return jsonify(results)



@app.route('/api/v1/food-illness/outbreaks/all', methods=['GET'])
def api_all():
    return jsonify(food_ill_data)


app.run(debug=True, use_reloader=False)







