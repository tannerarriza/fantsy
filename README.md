# fantsy

# Documentation for Project 

Notes for 4/2/19 meeting
Alan idea to do 

TO DO 
1) create a final dataset
    1. design what we are predicting - I think players fantasy score they got for that period
    1. apply the fantasy formula to data so we can get labels
    1. drop the fantasy formula equations since new games wont have it 
    1. drop all features that we wont have when getting new data
    1. establish a baseline feature set and baseline model 
    
disc:
we are want obsersavtions as players 
use -standings. 
merge standings and box score. each player attached to that row

    * Official dataset: Combine PlayerBoxScore with Standings dataset, because Player dataset is the only one with player roster first and last names. Idea is to join the two datasets based on the game date and team columns, and then group this newly created dataset by players because our observations are represented by players and not on teams. Each player assigned to a row will have certain team stats attached to each row as well. These can include things such as away vs. home, regular season (for now), looking at the number of fouls a player gets, number of days since last game played by team, winning streak, etc. (see below for list of features to consider) 
    
2) split data to a test set and hide that away

3) create features
    
    ideas:
    - if player is the categorized as really good, since teams perfromance is affected by one person 
    - use players height
    - age (create a function to calculate this given the birthdate of the player)
    - points 
    - away/home 
    - foul counts 
    - starting position of player
    - number of days since last game played by team
    - total player minutes on floor 
    - points scored by player
    - assists made by player
    - turnovers made by player
    - field goals/two pointers/three pointers/free throws --> BUT (an idea) DON't inlude the attempts and actual shots...just include the percentages? 
    - personal fouls
   
    
    a) establish a baseline modeline and validation loss.
    b) create visualizations 
    c) do statistical analysis to see what is important
    
4) Establish scaleable and easy to use ML pipeline to evaluate data.

    idea. 

