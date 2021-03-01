from flask import Flask, url_for
import random, sys
from datetime import date

app = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD=True)
from flask import render_template

gfa = ['Joe', 'Matt', 'Josh', 'Susy', 'Evan']
core = ['Brian', 'Quji', 'Susy']
engine = ['Taichi', 'Sam', 'Don', 'Dennis', 'Sean']
placement = {
    0: 'First',
    1: 'Second',
    2: 'Third',
    3: 'Fourth',
    4: 'Fifth',
    5: 'Sixth',
    6: 'Seventh, You should probably get a smaller team',
    7: 'Eighth, Like really this is getting silly',
    8: 'Tenth, is it lunch yet?',
    9: '9000 years later...',
}


def shuffle_random(people: list, weeknumber, day_of_week):
    new_people = people.copy()
    seed = int(f'{weeknumber}{day_of_week}')
    random.seed(seed)
    random.shuffle(new_people)
    return new_people


def render_team_for_today(pm_name, people, isoCal=date.today().isocalendar() ):
    year, week_num, _ = isoCal
    weeknumber = (int(f'{year}{week_num}'))
    return render_template('week.html',
                           pm=pm_name,
                           placement=placement,
                           year=year,
                           week_num=week_num,
                           weeknumber=weeknumber,
                           isoCal=isoCal,
                           pick_random=shuffle_random,
                           people=people
                           )


@app.route('/')
def gfa_render_default():
    return render_team_for_today("Austin", gfa)

@app.route('/gfa')
def gfa_render():
    return render_team_for_today("Austin", gfa)

@app.route('/core')
def core_render():
    return render_team_for_today("Ken", core)

@app.route('/engine')
def engine_render():
    return render_team_for_today("Austin", engine)

# TODO look into https://flask.palletsprojects.com/en/1.1.x/quickstart/#url-building to avoid this hack.
@app.route('/<int:year>/<int:week>')
def gfa_render_default2(year, week):
    return render_team_for_today("Austin", gfa, (year, week, -1))

@app.route('/gfa/<int:year>/<int:week>')
def gfa_render2(year, week):
    return render_team_for_today("Austin", gfa, (year, week, -1))

@app.route('/core/<int:year>/<int:week>')
def core_render2(year, week):
    return render_team_for_today("Ken", core, (year, week, -1))

@app.route('/engine/<int:year>/<int:week>')
def engine_render2(year, week):
    return render_team_for_today("Austin", engine, (year, week, -1))