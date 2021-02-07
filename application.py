from flask import Flask, url_for
import random, sys
from datetime import date

app = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD=True)
from flask import render_template

people = ['joe','matt','josh']


def pick_random(choice_weights, choice_seed=None, ):
    random.seed(choice_seed)
    choices = list(choice_weights.keys())
    weights = list(choice_weights.values())
    random_choices = []
    for i in range(7):
        random_choices.append(random.choices(choices, weights)[0])
    return random_choices

def shuffle_random(people: list, weeknumber, day_of_week):
    new_people = people.copy()
    seed = int(f'{weeknumber}{day_of_week}')
    random.seed(seed)
    random.shuffle(new_people)
    return new_people


@app.route('/')
def render():
    year, week_num, _ = date.today().isocalendar()
    weeknumber = (int(f'{year}{week_num}'))
    return render_template('week.html',
                           weeknumber=weeknumber,
                           pick_random=shuffle_random,
                           people=people,
                           isocal = date.today().isocalendar()
                        )

