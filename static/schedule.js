const gameList = document.getElementById('gameList');

// add search bar


const game_list = document.getElementById('game_list');
searchBar_schedule.addEventListener('keyup', (e) => {
    const searchString = e.target.value.toLowerCase();
    const filteredCharacters = nbaGame.data.filter(character => {
        return ( character.home_team.full_name.toLowerCase().includes(searchString) 
        || character.home_team.division.toLowerCase().includes(searchString) 
        || character.home_team.city.toLowerCase().includes(searchString)
        ||character.visitor_team.full_name.toLowerCase().includes(searchString) 
        || character.visitor_team.division.toLowerCase().includes(searchString) 
        || character.visitor_team.city.toLowerCase().includes(searchString)
        );
    });
    displayCharacters(filteredCharacters)
})
let nbaGame = [];
const loadGames = async () => {
    try {
        const res = await fetch('https://www.balldontlie.io/api/v1/games?seasons[]=2023&team_ids[]=1');
        nbaGame = await res.json();
        displayGames(nbaGame.data);
    } catch (err) {
        console.error(err);
    }
};



const teamImageMap_schedule= {
    //Atlantic Division:

'Boston Celtics' : "../templates/assets/image/boston-celtics.png",
'Brooklyn Nets' : "../templates/assets/image/brooklyn-nets.png",
'New York Knicks': "../templates/assets/image/new_york_knicks.png",
'Philadelphia 76ers' :"../templates/assets/image/philadelphia_76.png",
'Toronto Raptors':"../templates/assets/image/raptors.png",
    
//Central Division:

'Chicago Bulls' : "../templates/assets/image/chicago-bulls.png",
'Cleveland Cavaliers': "../templates/assets/image/cleveland-cavaliers.png",
'Detroit Pistons': "../templates/assets/image/detroit-pistons.png",
'Indiana Pacers' : "../templates/assets/image/indiana-pacers.png",
'Milwaukee Bucks': "../templates/assets/image/milwaukee-bucks.png",


'Atlanta Hawks': "../templates/assets/image/atlanta-hawks.png",
'Charlotte Hornets': "../templates/assets/image/charlotte-hornets.png",
'Miami Heat': "../templates/assets/image/miami-heat.png",
'Orlando Magic': "../templates/assets/image/orlando-magic.png",
'Washington Wizards': "../templates/assets/image/washington-wizards.png",

'Denver Nuggets': "../templates/assets/image/denver-nuggets.png",
'Minnesota Timberwolves': "../templates/assets/image/minnesota-timberwolves.png",
'Oklahoma City Thunder': "../templates/assets/image/oklahoma-city-thunder.png",
'Portland Trail Blazers': "../templates/assets/image/portland-trail-blazers.png",
'Utah Jazz': "../templates/assets/image/utah-jazz-vector.png",

'Golden State Warriors': "../templates/assets/image/golden-state-warriorsr.png",
'LA Clippers': "../templates/assets/image/los-angeles-clippers.png",
'Los Angeles Lakers': "../templates/assets/image/los_angeles_lakers.png",
'Phoenix Suns': "../templates/assets/image/phoenix-suns.png",
'Sacramento Kings': "../templates/assets/image/sacramento-kings-logo.png",

'Dallas Mavericks': "../templates/assets/image/dallas-mavericks.png",
'Houston Rockets': "../templates/assets/image/houston-rockets.png",
'Memphis Grizzlies': "../templates/assets/image/memphis-grizzlies.png",
'New Orleans Pelicans': "../templates/assets/image/new-orleans-pelicans.png",
'San Antonio Spurs': "../templates/assets/image/SanAntonio.png",
};

const getTeamImagePath_schedule = (teamName) => {
    

    if (teamName in teamImageMap_schedule) {
        return teamImageMap_schedule[teamName];
    } else {
        // Return a default image path or handle the case when the team name is not found
        return '../templates/assets/image/icons8-basketball-64.png';
    }
};




const displayCharacters = (characters) => {
    const htmlString = characters.map((character) => {
        const teamImagePath = getTeamImagePath_schedule(game.home_team.full_name);
            return `
            <li class="character">
                <h2>${character.full_name} ${character.abbreviation}</h2>
                <p>City: ${character.city}, 
                    Division:  ${character.division} </p>
                <img src =${teamImagePath}></img>
                
            </li>
        ` })
        .join('');
    game_list.innerHTML = htmlString;
};






const slicetime = (time) => {
    return time.slice(0, 10);
}


const displayGames = (games) => {
    const htmlString = games.map((game) => {
        const teamImagePathhome = getTeamImagePath_schedule(game.home_team.full_name);
        const teamImagePathguest = getTeamImagePath_schedule(game.visitor_team.full_name);
        const get_time =(game.date).slice(0, 10);
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
						${get_time}
					</div>
					<div class="match-score">
						<span class="match-score-number match-score-number--leading">${game.home_team_score}</span>
						<span class="match-score-divider">:</span>
						<span class="match-score-number">${game.visitor_team_score}</span>
					</div>
                    <p1>${game.time}</p1>
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