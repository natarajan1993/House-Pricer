import pandas as pd
from flask import Flask, render_template
from flask_ask import Ask, question, statement

app = Flask(__name__)
ask = Ask(app, '/alexa')


@ask.launch
def new_ask():
    welcome = render_template('welcome')
    reprompt = render_template('reprompt')
    return question(welcome).reprompt(reprompt)


@ask.intent('ByCityYearIntent')
def city_year(city, year, type_of_house):
    if city is None or year is None or type_of_house is None:
        reprompt_msg = render_template('reprompt_general')
        return question(reprompt_msg)
    else:
        df = pd.read_csv('trulia.csv')
        df.sort_values(by=['state', 'quarter'], ascending=True, inplace=True)
        a = df[(df['city'] == city) & (df['quarter'].str.startswith(year))]
        answer = int(a[str(type_of_house)].mean())
        message = render_template('city_year', city=city, year=year, type_of_house=type_of_house, answer=str(answer))
        return statement(message)


@ask.intent('ByStateYearIntent')
def state_year(state, year, type_of_house):
    if state is None or year is None or type_of_house is None:
        reprompt_msg = render_template('reprompt_general')
        return question(reprompt_msg)
    else:
        df = pd.read_csv('trulia.csv')
        df.sort_values(by=['state', 'quarter'], ascending=True, inplace=True)
        a = df[(df['state'] == state) & (df['quarter'].str.startswith(year))]
        answer = int(a[str(type_of_house)].mean())
        message = render_template('state_year', state=state, year=year, type_of_house=type_of_house, answer=str(answer))
        return statement(message)


@ask.intent('ByCityIntent')
def city_only(city, type_of_house):
    if city is None or type_of_house is None:
        reprompt_msg = render_template('reprompt_general')
        return question(reprompt_msg)
    else:
        df = pd.read_csv('trulia.csv')
        df.sort_values(by=['state', 'quarter'], ascending=True, inplace=True)
        a = df[(df['city'] == city) & (df['quarter'].str.startswith('2012') |
                                       df['quarter'].str.startswith('2013') |
                                       df['quarter'].str.startswith('2014') |
                                       df['quarter'].str.startswith('2015') |
                                       df['quarter'].str.startswith('2016') |
                                       df['quarter'].str.startswith('2017'))]
        answer = int(a[str(type_of_house)].mean())
        message = render_template('city_only', city=city, type_of_house=type_of_house, answer=str(answer))
        return statement(message)


@ask.intent('ByStateIntent')
def state_only(state, type_of_house):
    if state is None or type_of_house is None:
        reprompt_msg = render_template('reprompt_general')
        return question(reprompt_msg)
    else:
        df = pd.read_csv('trulia.csv')
        df.sort_values(by=['state', 'quarter'], ascending=True, inplace=True)
        a = df[(df['state'] == state) & (df['quarter'].str.startswith('2012') |
                                         df['quarter'].str.startswith('2013') |
                                         df['quarter'].str.startswith('2014') |
                                         df['quarter'].str.startswith('2015') |
                                         df['quarter'].str.startswith('2016') |
                                         df['quarter'].str.startswith('2017'))]
        answer = int(a[str(type_of_house)].mean())
        message = render_template('state_only', state=state, type_of_house=type_of_house, answer=str(answer))
        return statement(message)


if __name__ == '__main__':
    app.run(debug=True)
