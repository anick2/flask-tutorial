from flask import Flask, render_template
import tourdata

app = Flask(__name__)

names = {'nsk':'Новосибирск', 'ekb':'Екатеринург', 'msk':'Москва', 'spb':'Санкт-Петербург','kazan':'Казань'}

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/departures/<departure>/')
def departure(departure):
    return render_template('departure.html')

@app.route('/tours/<id>/')
def tour(id):
    return render_template('tour.html')

@app.route('/data/')
def data():
    return render_template('data.html', tours=tourdata.tours)

@app.route('/data/departures/<goto>')
def data_departures(goto):
    d = {key:tour for key,tour in tourdata.tours.items() if tour['departure'] == goto}
    print(d)
    return render_template('directions.html', name=names[goto], tours=d)

@app.route('/data/tours/<int:id>/')
def data_tour(id):
    return render_template('place.html', tour=tourdata.tours[id])

app.run()