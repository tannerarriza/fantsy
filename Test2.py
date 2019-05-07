from flask import Flask, render_template, flash, request, redirect, url_for

app = Flask(__name__)


from flask import send_file
import csv


@app.route('/')
def helper():
	input_file = csv.DictReader(open("csvtest.csv"))
	max_age = None
	oldest_person = None
	for row in input_file:
		age = int(row["Age"])
		if max_age == None or max_age < age:
			max_age = age
			oldest_person = row["Name"]


	return '''
	<center><h1>FANTSY</strong></h1></center>
	<center><h2>"YOUR IN-BROWSER FANTASY BASKETBALL ADVISOR"</h1></center>
	<center><h3>ABOUT</h3></center>
	<center><text><em>This project is aimed to assist all Fantasy Basketball owners with point projections and a few statistics all owners need to know.</em></text></center>
	<center><text><em>Our goal is to allow users to input a collection of players they're interested in that will return the projected fantasy points to help make a final roster.</em></text></center>

	<center>
	<img src="https://media.istockphoto.com/photos/basketball-ball-isolated-on-white-picture-id861960130?k=6&m=861960130&s=612x612&w=0&h=E5i0p5fnvti_y3MEbdPeUETkgvJrVtXYZwToJ_k-_a4=">
	</center>
	<center>
	<h3>INPUT PLAYER'S FULL NAME</h3>
	<text>Make sure to input player's first name and then last name.</text>
    <form method="POST" action="/get_id">
    <textarea name="textbox"></textarea>
    <button type="submit" name="submit">Submit</button>
    </form> 
    <table> <thead><tr><th>Player Name &nbsp  &nbsp  &nbsp</th> 
    <th>Projected Fantasy Points</th></tr></thead> <tbody> <tr><td>Name1</td><td>Description1</td></tr> <tr><td>Name2</td><td>Description2</td></tr> </tbody> </table>
    </center>

   '''


# def home():
# 	helper()
# 	return '''
# <center><h1>FANTSY</strong></h1></center>
# <center><h2>"YOUR IN-BROWSER FANTASY BASKETBALL ADVISOR"</h1></center>
# <center><h3>ABOUT</h3></center>
# <center><text><em>This project is aimed to assist all Fantasy Basketball owners with point projections and a few statistics all owners need to know.</em></text></center>
# <center><text><em>Our goal is to allow users to input a collection of players they're interested in that will return the projected fantasy points to help make a final roster.</em></text></center>

# <center>

# <img src="https://media.istockphoto.com/photos/basketball-ball-isolated-on-white-picture-id861960130?k=6&m=861960130&s=612x612&w=0&h=E5i0p5fnvti_y3MEbdPeUETkgvJrVtXYZwToJ_k-_a4=">

# </center>

# <center>
# <h3>INPUT PLAYER'S FULL NAME</h3>
# <text>Make sure to input player's first name and then last name.</text>
#     <form method="POST" action="/get_id">
#     <textarea name="textbox"></textarea>
#     <button type="submit" name="submit">Submit</button>
#     </form> 

#   <table> <thead><tr><th>Player Name &nbsp  &nbsp  &nbsp</th> 
#   <th>Projected Fantasy Points</th></tr></thead> <tbody> <tr><td>Name1</td><td>Description1</td></tr> <tr><td>Name2</td><td>Description2</td></tr> </tbody> </table>
# </center>

   # '''




if __name__ == '__main__':
    app.run(debug=True)




