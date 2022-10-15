from flask import render_template, request
import requests
from . import bp as main

@main.route('/pokemon', methods=['GET'])
def students():
    my_pokedex = ["diana", "caleb", "connor","marco", "lizzette", "marcus", "kevin", "gulfem"]
                                            #name in Jinja = name in python
    return render_template('students.html.j2', students = my_students)