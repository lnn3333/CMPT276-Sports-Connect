# CMPT276-Sports-Connect

## I. Overview
> Sports Connect is a web application designed for NBA fans to search for information about their favourite players, and teams and get the latest news as well as the game schedules. The web is built using Python with Flask for the backend and HTML, CSS, and JS for the front end.

## II. Features

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

**In-depth features:**
1. Search for team schedule:
Allow to check upcoming game schedules for NBA teams.
2. Players Statistics:
Get the player's game stats based on the season type and the year
3. Team Profile:
Get to know more about the number of wins, losses, percentage, conference rank, division ran of the team
4. Team Statistic:
Dig deeper into the team stats by name-searching the team. 

## III. Access the web app 
Due to constraints imposed by the NBA API server, hosting our website with its full array of features on popular hosting services like Heroku, Netlify, AWS, or PythonAnywhere is restricted. Consequently, there are two alternatives for accessing the web application:

### 1. Official web link
>This version contains the general features
**__http://18.217.42.19__**

Deployment using AWS services
This version is hosted using branch: deploy_1

### 2. How to Host the Website Locally
>This web app version contains the general + in-depth features:

__Follow these steps to host the Sport Connect website locally:__

1. In the terminal, clone the repository:
```
git clone https://github.com/lnn3333/CMPT276-Sports-Connect.git
 ```
2. Navigate to the project directory:
```
cd CMPT276-Sports-Connect
```

3. Install dependencies:
>Get requirements and install

```
pip freeze > requirements.txt
pip install -r requirements.txt
```
>If it not work then run these cmd:

```
pip install flask
pip install pytz
pip install numpy
pip install nba_api
pip install requests
pip install jinja2==2.11.3
pip install markupsafe==2.0.1
pip install --upgrade Flask Jinja2
```
4. Run the application: 
```
python app.py
```
5. Access the web app in your browser at http://localhost:5000

## IV. Issue
>We cannot deploy the website due to:
>NBA API Block on Hosting Services
>Please note that the NBA API currently blocks requests originating from hosting services such as AWS, Heroku, Netlify, PythonAnywhere, Render, Azure, Google Cloud, etc. This is a restriction imposed by the NBA API.
Error:
<img width="863" alt="image" src="https://github.com/lnn3333/CMPT276-Sports-Connect/assets/136864245/caa12bc8-6307-406a-bbcf-60c651e5a10a">
