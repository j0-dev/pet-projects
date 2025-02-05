import random

games = [
    "American Truck Simulator",
    "Aperture Desk Job",
    "Artifact Foundry",
    "Baldur's Gate: Enhanced Edition",
    "Bioshock Infinite",
    "Bitburner",
    "Black Mesa",
    "Borderlands 2",
    "Bridge Constructor Portal",
    "Cities: Skylines",
    "Comet 64",
    "Company of Heroes 2",
    "Construction-Simulator 2015",
    "Counter-Strike",
    "Counter-Strike 2",
    "Counter-Strike: Condition Zero",
    "Counter-Strike: Condition Zero Deleted Scenes",
    "Counter-Strike: Source",
    "Crypt of the NecroDancer",
    "Darwinia",
    "Day of Defeat",
    "Day of Defeat: Source",
    "Deadlock",
    "Deathmatch Classic",
    "Deus Ex: Mankind Divided",
    "Divinity: Original Sin Enhanced Edition",
    "The Escapists",
    "Euro Truck Simulator 2",
    "Europa Universalis IV",
    "EXAPUNKS: TEC Redshift Player",
    "Factorio",
    "Firewatch",
    "Football Manager 2015",
    "Football Manager 2016",
    "Football Manager 2017",
    "Football Manager 2018",
    "FTL: Faster Than Light",
    "Garry's Mod",
    "Getting Over It with Bennett Foddy",
    "Godot Engine",
    "Hacknet",
    "Half-Life",
    "Half-Life 2",
    "Half-Life 2: Deathmatch",
    "Half-Life 2: Update",
    "Half-Life: Alyx",
    "Half-Life: Blue Shift",
    "Half-Life: C.A.G.E.D.",
    "Half-Life Deathmatch: Source",
    "Half-Life: MMod",
    "Half-Life: Opposing Force",
    "Half-Life: Source",
    "Heartbound Demo",
    "Hexcells",
    "Hotline Miami",
    "Infinifactory",
    "Kerbal Space Program",
    "Left 4 Dead 2",
    "Life is Strange",
    "Metro: Last Light Complete Edition",
    "Metro: Last Light Redux",
    "Mini Metro",
    "NEO Scavenger",
    "NERTS! Online",
    "Northgard",
    "Nuclear Dawn",
    "Oddworld: New 'n' Tasty",
    "OpenTTD",
    "Outlast",
    "Papers, Please",
    "Poly Bridge",
    "Poly Bridge 2",
    "Portal",
    "Portal 2",
    "Portal Reloaded",
    "Prison Architect",
    "Psychonauts",
    "pureya",
    "Quaver",
    "Red Dead Redemption 2",
    "Ricochet",
    "Rise of the Tomb Raider",
    "Robocraft",
    "Sandwalkers: The Fourteenth Caravan",
    "SEGA Mega Drive & Genesis Classics",
    "shapez",
    "SHENZHEN I/O",
    "SHENZHEN Solitaire",
    "Sid Meier's Civilization V",
    "Sid Meier's Civilization VI",
    "SpaceChem",
    "Splitgate",
    "The Stanley Parable",
    "Star Wars: Knights of the Old Republic",
    "Stardew Valley",
    "Starfield",
    "Stellaris",
    "Super Hexagon",
    "SUPERHOT",
    "SUPERHOT: Mind Control Delete",
    "The Talos Principle",
    "Tavern Master",
    "TDS - Tower Defense Strategy Demo",
    "Team Fortress Classic",
    "Team Fortress 2",
    "Terraria",
    "TIS-100",
    "Tomb Raider",
    "Total War: ROME REMASTERED",
    "Transport Fever",
    "Undertale",
    "Uplink",
    "The Witcher 2: Assassins of Kings Enhanced Edition",
    "XCOM: Enemy Unknown",
    "XCOM 2",
    "Zach-Like"
]

num = random.randint(1, len(games))
game = games.pop(num)
print(game)