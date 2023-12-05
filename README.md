# CMPT276-Sports-Connect

**I. Overview**
Sports Connect is a web application designed for NBA fans to search for information about their favourite players, and teams and get the latest news as well as the game schedules. The web is built using Python with Flask for the backend and HTML, CSS, and JS for the front end.

**II. Features**
**General features**
1. Live Scores
Stay updated with real-time game results, ensuring you never miss a moment of the action.
2. Past season: 
Allow to get access to the previous game using search-by-year tools
3. Team: 
Search up the team and get to see the logos, division, division
4. Latest News
Read engaging articles about teams and players, enhancing your understanding and enjoyment of the sports world.
5. Award Race
Track how the award race is panning out, keeping you informed about the standout players.
6. Players:
Get to know the bio personal information 

**Indepth features:**
7. Search for team schedule:
Allow to check upcoming game schedules for NBA teams.
8. Players Statistics:
Get the player's game stats based on the season type and the year
9. Team Profile:
Get to know more about the number of wins, losses, percentage, conference rank, division ran of the team
10. Team Statistic:
Dig deeper into the team stats by name-searching the team. 

**III. How to Host the Website Locally**
Follow these steps to host the Sport Connect website locally:

1. In the terminal, clone the repository:
run this cmd: 
    ```bash git clone https://github.com/lnn3333/CMPT276-Sports-Connect.git
     ```
2. Navigate to the project directory: 
run this cmd: **cd CMPT276-Sports-Connect**
3. Install dependencies:
run the following cmd

pip install flask
pip install pytz
pip install numpy
pip install nba_api
pip install requests
pip install jinja2==2.11.3
pip install markupsafe==2.0.1
pip install --upgrade Flask Jinja2


5. Run the application: 
run this cmd: **python app.py**
6. Access the web app in your browser at **http://localhost:5000**


**IV. Issue: **
NBA API Block on Hosting Services
  Please note that the NBA API currently blocks requests originating from hosting services such as AWS, Heroku, Netlify, PythonAnywhere, Render, Azure, Google Cloud, etc. This is a restriction imposed by the NBA API.
Error:
<img width="863" alt="image" src="https://github.com/lnn3333/CMPT276-Sports-Connect/assets/136864245/caa12bc8-6307-406a-bbcf-60c651e5a10a">
