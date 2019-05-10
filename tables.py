from flask_table import Table, Col, LinkCol
 
class Results(Table):
    id = Col('Id', show=False)
    player = Col('Player')
    title = Col('Projected Fantasy Points')