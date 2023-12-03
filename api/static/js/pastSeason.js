const gameList = document.getElementById('gameList');


// add search bar
//var year;

const game_list = document.getElementById('game_list');
const searchBar_schedule = document.getElementById('searchBar_schedule');
let nbaGame = [];

searchBar_schedule.addEventListener('keyup', async (e) => {
    try {
        const searchYear = e.target.value;
        const res = await fetch(`https://www.balldontlie.io/api/v1/games?seasons[]=${searchYear}&team_ids[]=1`);
        nbaGame = await res.json();
        displayGames(nbaGame.data);
    } catch (err) {
        console.error(err);
    }
});




const teamImageMap_schedule= {
    //Atlantic Division:

'Boston Celtics' : "../static/assets/image/boston-celtics.png",
'Brooklyn Nets' : "../static/assets/image/brooklyn-nets.png",
'New York Knicks': "../static/assets/image/new_york_knicks.png",
'Philadelphia 76ers' :"../static/assets/image/philadelphia_76.png",
'Toronto Raptors':"../static/assets/image/raptors.png",
    
//Central Division:

'Chicago Bulls' : "../static/assets/image/chicago-bulls.png",
'Cleveland Cavaliers': "../static/assets/image/cleveland-cavaliers.png",
'Detroit Pistons': "../static/assets/image/detroit-pistons.png",
'Indiana Pacers' : "../static/assets/image/indiana-pacers.png",
'Milwaukee Bucks': "../static/assets/image/milwaukee-bucks.png",


'Atlanta Hawks': "../static/assets/image/atlanta-hawks.png",
'Charlotte Hornets': "../static/assets/image/charlotte-hornets.png",
'Miami Heat': "../static/assets/image/miami-heat.png",
'Orlando Magic': "../static/assets/image/orlando-magic.png",
'Washington Wizards': "../static/assets/image/washington-wizards.png",

'Denver Nuggets': "../static/assets/image/denver-nuggets.png",
'Minnesota Timberwolves': "../static/assets/image/minnesota-timberwolves.png",
'Oklahoma City Thunder': "../static/assets/image/oklahoma-city-thunder.png",
'Portland Trail Blazers': "../static/assets/image/portland-trail-blazers.png",
'Utah Jazz': "../static/assets/image/utah-jazz-vector.png",

'Golden State Warriors': "../static/assets/image/golden-state-warriorsr.png",
'LA Clippers': "../static/assets/image/los-angeles-clippers.png",
'Los Angeles Lakers': "../static/assets/image/los_angeles_lakers.png",
'Phoenix Suns': "../static/assets/image/phoenix-suns.png",
'Sacramento Kings': "../static/assets/image/sacramento-kings-logo.png",

'Dallas Mavericks': "../static/assets/image/dallas-mavericks.png",
'Houston Rockets': "../static/assets/image/houston-rockets.png",
'Memphis Grizzlies': "../static/assets/image/memphis-grizzlies.png",
'New Orleans Pelicans': "../static/assets/image/new-orleans-pelicans.png",
'San Antonio Spurs': "../static/assets/image/SanAntonio.png",
};

const getTeamImagePath_schedule = (teamName) => {
    

    if (teamName in teamImageMap_schedule) {
        return teamImageMap_schedule[teamName];
    } else {
        // Return a default image path or handle the case when the team name is not found
        return '../static/assets/image/icons8-basketball-64.png';
    }
};





const slicetime = (time) => {
    return time.slice(0, 10);
}


const get_season_status = (game_time)=> {
    if ((game_time) != null ){
        return game_time
    }
    else
        return " "
}

const displayGames = (games) => {
    const htmlString = games.map((game) => {
        const teamImagePathhome = getTeamImagePath_schedule(game.home_team.full_name);
        const teamImagePathguest = getTeamImagePath_schedule(game.visitor_team.full_name);
        const get_season = get_season_status(game.time);
        const get_time =(game.date).slice(0, 10);
        
            return `
           

            <li class="team">
            <div class="container">
            <div class="match">
            <div class="match-header">
                <div class="match-status">Past Result</div>
                <div class="match-tournament"><img src="../static/assets/image/nba.png" class="img_small"/></div>
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
						${get_time}
					</div>
					<div class="match-score">
						<span class="match-score-number match-score-number--leading">${game.home_team_score}</span>
						<span class="match-score-divider">:</span>
						<span class="match-score-number">${game.visitor_team_score}</span>
					</div>
                    <p1>${get_season}</p1>
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
                
            </div> 
            </div> 
            </li>
        ` })
        .join('');
    gameList.innerHTML = htmlString;
};

loadGames();