from flask import Flask, url_for
import random, sys

app = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD=True)
from flask import render_template

diet_choice_weights = {
    'no alchohol': 50,
    'break': 10,
    'vegetarian': 15,
    '1500 calories': 22,
    'fast one meal': 22,
}

exercise_choice_weights = {
    'break': 10,
    '10k steps': 20,
    'core and back': 20,
    'legs': 20,
    'arm strength': 20,
    'bike': 10,
    'hour+ outside or moderate chores': 10,
    'stretch session / yoga': 25
}

growth_choice_weights = {
    'break': 25,
    'cloud infra focus': 40,
    'raw code focus': 25,
    'trello board management': 10,
    'tidy up github': 25,
}



def pick_random(choice_weights, choice_seed=None, ):
    random.seed(choice_seed)
    choices = list(choice_weights.keys())
    weights = list(choice_weights.values())
    random_choices = []
    for i in range(7):
        random_choices.append(random.choices(choices, weights)[0])
    return random_choices


@app.route('/')
def render():
    seed = random.randrange(sys.maxsize)
    return render_template('week.html',
                           seed=seed,
                           pick_random=pick_random,
                           social=growth_choice_weights,
                           diet=diet_choice_weights,
                           exercise=exercise_choice_weights)
@app.route('/<seed>')
def render_seed(seed):
    return render_template('week.html',
                           seed=seed,
                           pick_random=pick_random,
                           social=growth_choice_weights,
                           diet=diet_choice_weights,
                           exercise=exercise_choice_weights)

