# fantsy

# Documentation for Project 

Master Notebook: <br>
https://colab.research.google.com/drive/1OWsdIgIVQGvKhcgr5yE028AOM2aoZGcd#scrollTo=DLZKDxFu7wyZ

Google Doc for Midterm Written Report: 
https://docs.google.com/document/d/1Rck-STw5HgW3UXitpnoR5JzEK_BSmb46fGRU7YShxkE/edit

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

Official dataset: Combine PlayerBoxScore with Standings dataset, because Player dataset is the only one with player roster first and last names. Idea is to join the two datasets based on the game date and team columns, and then group this newly created dataset by players because our observations are represented by players and not on teams. Each player assigned to a row will have certain team stats attached to each row as well. These can include things such as away vs. home, regular season (for now), looking at the number of fouls a player gets, number of days since last game played by team, winning streak, etc. (see below for list of features to consider) 
    
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
___________________________________________________________________

Ideas for how should categorical variables be taken care of?

- Season type (Pre/Regular/Post): apply one-hot encoding
- For Primary and Opposition teams
    - team abbreviation codes (about 30): apply binary encoding
    - team conference (2 values of East and West): convert to 0 and 1
    - team division (6 values that are nominal): apply one-hot encoding
- Following two columns can be filtered out for Opposition, as they will be just the reverse of the primary team
    - team location (2 values of Away and Home): convert to 0 and 1
    - team results (2 values of Win and Loss): convert to 0 and 1
 ___________________________________________________________________

for aish --> Can you write the code for the function that calculates fantasy points and additionally add a column to the existing dataset for fantasy points so that we can make visualizations comparing different columns against this one?  

QUESTION - What to do for rookie player - should we just start them off as 0 (probably not a good idea) / potentially use college data for these palyers / potentially average out their teams information 

Helpful Link btw for Python basics: https://data36.com/python-built-in-functions-methods-python-data-science-basics-3/

If we want to include margin of error with our data, use this formula to calculate it: (total points - projected points)/(projected points)

```python
# functions

def cross_validate(train,labels, model, para_list)
    '''
    args:
        train: data to train on
        labels: labels to fit on
        model to fit
        parameters to validate
    returns best parameter and visualziatoins of the tarining and cv validation loss 
    '''
    pass

    return 

def validate(train,labels, model, args*):
    '''
    returns the validation loss on model 
    plots visualizations
    
    example of function call
    
        validate(X)tf
    '''
    pass
    return 

def one_hot(data, feature):
    '''
    args:
        data
        feature: string of the feature name
    returns:
        merged data set of the feature one_hot encoded and orginal feature dropped
    '''
    return 

def feature_engineer(data):
    
    '''
    given our unseen test or validation data, run all the other preprocessing fucntions on the test data 
    '''
    return 

def averageForOutliers(data):
    'used to deal with outliers - used to find the average of the column'
    return 
    
def removeOutliers(data):
    'used to deal with outliers - removing that row from the dataset '
    return 
    
def Playing(data):
    'check that the player is current playing this season and has played at least one season before'
    return
    
def fantasypoints(data):
    'calculate the fantasy points- https://www.nba.com/article/2017/10/05/nba-unveils-new-official-fantasy-scoring'
    return 

```
