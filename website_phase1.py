from flask import Flask, render_template, flash, request, redirect, url_for

app = Flask(__name__)


from flask import send_file
import csv


@app.route('/')

#Layout for the website 
#Initial idea for the home page 
#Have an about section -> General description of what we what to achieve 
#Image of a basketball for the website
#Section to add players roster 

def home():
# 	helper()
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

#Trying to open the csv file directly on the website 
# def helper():
# 	input_file = csv.DictReader(open("csvtest.csv"))

# 	return '''
# 	<center><h1>FANTSY</strong></h1></center>
# 	<center><h2>"YOUR IN-BROWSER FANTASY BASKETBALL ADVISOR"</h1></center>
# 	<center><h3>ABOUT</h3></center>
# 	<center><text><em>This project is aimed to assist all Fantasy Basketball owners with point projections and a few statistics all owners need to know.</em></text></center>
# 	<center><text><em>Our goal is to allow users to input a collection of players they're interested in that will return the projected fantasy points to help make a final roster.</em></text></center>

# 	<center>
# 	<img src="https://media.istockphoto.com/photos/basketball-ball-isolated-on-white-picture-id861960130?k=6&m=861960130&s=612x612&w=0&h=E5i0p5fnvti_y3MEbdPeUETkgvJrVtXYZwToJ_k-_a4=">
# 	</center>
# 	<center>
# 	<h3>INPUT PLAYER'S FULL NAME</h3>
# 	<text>Make sure to input player's first name and then last name.</text>
#     <form method="POST" action="/get_id">
#     <textarea name="textbox"></textarea>
#     <button type="submit" name="submit">Submit</button>
#     </form> 
#     <table> <thead><tr><th>Player Name &nbsp  &nbsp  &nbsp</th> 
#     <th>Projected Fantasy Points</th></tr></thead> <tbody> <tr><td>Name1</td><td>Description1</td></tr> <tr><td>Name2</td><td>Description2</td></tr> </tbody> </table>
#     </center>

#    '''

#Sources we used to understanding Flask 
# -> https://github.com/ikhlaqsidhu/data-x/tree/master/12-productionize-deploy-flask/deploy-models
# ->  https://www.youtube.com/watch?v=MwZwr5Tvyxo


if __name__ == '__main__':
    app.run(debug=True)




