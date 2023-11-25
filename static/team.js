

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

const getTeamImagePath = (teamName) => {
    

    if (teamName in teamImageMap) {
        return teamImageMap[teamName];
    } else {
        // Return a default image path or handle the case when the team name is not found
        return '../templates/assets/image/icons8-basketball-64.png';
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
