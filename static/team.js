

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
