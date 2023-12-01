

const charactersList = document.getElementById('charactersList');
searchBar.addEventListener('keyup', (e) => {
    const searchString = e.target.value.toLowerCase();
    const filteredCharacters = hpCharacters.data.filter(character => {
        return ( character.full_name.toLowerCase().includes(searchString) 
        || character.division.toLowerCase().includes(searchString) 
        || character.city.toLowerCase().includes(searchString)
        );
    });
    displayCharacters(filteredCharacters)
})
let hpCharacters = [];

const loadCharacters = async () => {
    try {
        const res = await fetch('https://www.balldontlie.io/api/v1/teams');
        hpCharacters = await res.json();
        displayCharacters(hpCharacters.data);
    } catch (err) {
        console.error(err);
    }
};

const teamImageMap = {
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

const getTeamImagePath = (teamName) => {
    

    if (teamName in teamImageMap) {
        return teamImageMap[teamName];
    } else {
        // Return a default image path or handle the case when the team name is not found
        return '../static/assets/image/icons8-basketball-64.png';
    }
};




const displayCharacters = (characters) => {
    const htmlString = characters.map((character) => {
        const teamImagePath = getTeamImagePath(character.full_name);
            return `
            <li class="character">
                <h2>${character.full_name} ${character.abbreviation}</h2>
                <p>City: ${character.city}, 
                    Division:  ${character.division} </p>
                <img src =${teamImagePath}></img>
                
            </li>
        ` })
        .join('');
    charactersList.innerHTML = htmlString;
};

loadCharacters();
