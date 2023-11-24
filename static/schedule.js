const gameList = document.getElementById('gameList');

const loadGames = async () => {
    try {
        const res = await fetch('https://www.balldontlie.io/api/v1/games');
        nbaGame = await res.json();
        displayGames(nbaGame.data);
    } catch (err) {
        console.error(err);
    }
};

let nbaGame = [];
const teamImageMap = {
    //Atlantic Division:

'Boston Celtics' : "./assets/image/boston-celtics.png",
'Brooklyn Nets' : "./assets/image/brooklyn-nets.png",
'New York Knicks': "./assets/image/new_york_knicks.png",
'Philadelphia 76ers' :"./assets/image/philadelphia_76.png",
'Toronto Raptors':"./assets/image/raptors.png",
    
//Central Division:

'Chicago Bulls' : "./assets/image/chicago-bulls.png",
'Cleveland Cavaliers': "./assets/image/cleveland-cavaliers.png",
'Detroit Pistons': "./assets/image/detroit-pistons.png",
'Indiana Pacers' : "./assets/image/indiana-pacers.png",
'Milwaukee Bucks': "./assets/image/milwaukee-bucks.png",


'Atlanta Hawks': "./assets/image/atlanta-hawks.png",
'Charlotte Hornets': "./assets/image/charlotte-hornets.png",
'Miami Heat': "./assets/image/miami-heat.png",
'Orlando Magic': "./assets/image/orlando-magic.png",
'Washington Wizards': "./assets/image/washington-wizards.png",

'Denver Nuggets': "./assets/image/denver-nuggets.png",
'Minnesota Timberwolves': "./assets/image/minnesota-timberwolves.png",
'Oklahoma City Thunder': "./assets/image/oklahoma-city-thunder.png",
'Portland Trail Blazers': "./assets/image/portland-trail-blazers.png",
'Utah Jazz': "./assets/image/utah-jazz-vector.png",

'Golden State Warriors': "./assets/image/golden-state-warriorsr.png",
'LA Clippers': "./assets/image/los-angeles-clippers.png",
'Los Angeles Lakers': "./assets/image/los_angeles_lakers.png",
'Phoenix Suns': "./assets/image/phoenix-suns.png",
'Sacramento Kings': "./assets/image/sacramento-kings-logo.png",

'Dallas Mavericks': "./assets/image/dallas-mavericks.png",
'Houston Rockets': "./assets/image/houston-rockets.png",
'Memphis Grizzlies': "./assets/image/memphis-grizzlies.png",
'New Orleans Pelicans': "./assets/image/new-orleans-pelicans.png",
'San Antonio Spurs': "./assets/image/SanAntonio.png",
};

const getTeamImagePath = (teamName) => {
    

    if (teamName in teamImageMap) {
        return teamImageMap[teamName];
    } else {
        // Return a default image path or handle the case when the team name is not found
        return './assets/image/icons8-basketball-64.png';
    }
};

const displayGames = (games) => {
    const htmlString = games.map((game) => {
        const teamImagePathhome = getTeamImagePath(game.home_team.full_name);
        const teamImagePathguest = getTeamImagePath(game.visitor_team.full_name);
            return `
           

            <li class="team">
            <div class="container">
            <div class="match">
            <div class="match-header">
                <div class="match-status">Live</div>
                <div class="match-tournament"><img src="./assets/image/nba.png" class="img_small"/></div>
            </div>
            <div class="match-content">
                <div class="column">
				<div class="team team--home">
					<div class="team-logo">
                    <img src =${teamImagePathhome}></img>
					</div>
					<h2 class="team-name">${game.home_team.name} </h2>
                </div>
                </div>
                
                <div class="column">
				<div class="match-details">
					<div class="match-date">
						${game.date}
					</div>
					<div class="match-score">
						<span class="match-score-number match-score-number--leading">${game.home_team_score}</span>
						<span class="match-score-divider">:</span>
						<span class="match-score-number">${game.visitor_team_score}</span>
					</div>
                </div>
			    </div>

                <div class="column">
				<div class="team team--home">
					<div class="team-logo">
                    <img src =${teamImagePathguest}></img>
					</div>
					<h2 class="team-name">${game.visitor_team.name} </h2>
                </div>
                </div>
                <p1>${game.time}</p1>
            </div> 
            </div> 
            </li>
        ` })
        .join('');
    gameList.innerHTML = htmlString;
};

loadGames();