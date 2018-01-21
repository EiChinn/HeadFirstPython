#! /usr/local/bin/python3

import athletemodel
import yate
import cgi
import cgitb

cgitb.enable()

athletes = athletemodel.get_from_store()

form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header("Athlete's best 3 score"))
print(yate.para(athlete_name + "'s score"))
print(yate.u_list(athletes[athlete_name].top3))
print(yate.include_footer({"Home": "/index.html", "Select anthoer player": "generate_list.py"}))
