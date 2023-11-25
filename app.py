from flask import Flask, render_template
from AwardRacesNBA import getCategories, readData, scoringChampRace, assistChampRace, ReboundChampRace, BlockChampRace, StealsChampRace 

app = Flask(__name__)

#Home page
@app.route('/')
def home():
    return render_template('index.html')

#route for award races 
@app.route('/awards')
def displayAwardRace():
    data=readData()
    Points,Assist,Rebound,Blocks,Steals = getCategories(data)
    
    scoringChampRace(Points)
    assistChampRace(Assist)
    ReboundChampRace(Rebound)
    BlockChampRace(Blocks)
    StealsChampRace(Steals)
    
   
    return render_template('nbaAwards.html',
                           Points=Points,
                           Assist=Assist,
                           Rebound=Rebound,
                           Blocks=Blocks,
                           Steals=Steals)

# Add a route for schedule of recent games     
@app.route('/schedule.html')  
def schedule():
    return render_template('schedule.html')

@app.route('/team.html')  
def teamList():
    return render_template('team.html')

if __name__== '__main__':
    app.run(debug=True)