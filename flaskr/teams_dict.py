"""
Program Name: team_codes
By: Omer Alon
Date: 15/04/17
Program Version: 1.0.0
"""


# Fit the team names in the two information sources
TEAMS_DICT = {"AFC Bournemouth": "AFC Bournemouth",
              "Arsenal FC": "Arsenal",
              "Burnley FC": "Burnley",
              "Brighton & Hove Albion": "Brighton & Hove Albion",
              "Chelsea FC": "Chelsea",
              "Crystal Palace FC": "Crystal Palace",
              "Everton FC": "Everton",
              "Huddersfield Town": "Huddersfield Town",
              "Leicester City FC": "Leicester City",
              "Liverpool FC": "Liverpool",
              "Manchester City FC": "Manchester City",
              "Manchester United FC": "Manchester United",
              "Newcastle United FC": "Newcastle United",
              "Southampton FC": "Southampton",
              "Stoke City FC": "Stoke City",
              "Swansea City FC": "Swansea City",
              "Tottenham Hotspur FC": "Tottenham Hotspur",
              "Watford FC": "Watford",
              "West Bromwich Albion FC": "West Bromwich Albion",
              "West Ham United FC": "West Ham United",
              "Bayer Leverkusen": "Bayer Leverkusen",
              "Borussia Dortmund": "Borussia Dortmund",
              u"Bor. M\xf6nchengladbach": "Borussia Monchengladbach",
              "Eintracht Frankfurt": "Eintracht Frankfurt",
              "FC Augsburg": "FC Augsburg",
              u"FC Bayern M\xfcnchen": "Bayern Munich",
              "FC Schalke 04": "Schalke 04",
              u"1. FC K\xf6ln": "FC Cologne",
              "1. FSV Mainz 05": "Mainz",
              "Hamburger SV": "Hamburg SV",
              "Hertha BSC": "Hertha Berlin",
              "Red Bull Leipzig": "RB Leipzig",
              "SC Freiburg": "SC Freiburg",
              "TSG 1899 Hoffenheim": "TSG Hoffenheim",
              "VfL Wolfsburg": "VfL Wolfsburg",
              "Werder Bremen": "Werder Bremen",
              "Hannover 96": "Hannover 96",
              "VfB Stuttgart": "VfB Stuttgart",
              "Angers SCO": "Angers",
              "AS Monaco FC": "AS Monaco",
              u"AS Saint-\xc9tienne": "St Etienne",
              "Dijon FCO": "Dijon FCO",
              "EA Guingamp": "Guingamp",
              "FC Girondins de Bordeaux": "Bordeaux",
              "FC Metz": "Metz",
              "FC Nantes": "Nantes",
              u"Montpellier H\xe9rault SC": "Montpellier",
              "OGC Nice": "Nice",
              "Olympique de Marseille": "Marseille",
              "Olympique Lyonnais": "Lyon",
              "OSC Lille": "Lille",
              "Paris Saint-Germain": "Paris Saint-Germain",
              "SM Caen": "Caen",
              "Stade Rennais FC": "Stade Rennes",
              "Toulouse FC": "Toulouse",
              "Amiens SC": "SC Amiens",
              "ES Troyes AC": "Troyes",
              "RC Strasbourg Alsace": "Strasbourg",
              "Athletic Club": "Athletic Bilbao",
              "CD Leganes": "Leganes",
              u"Club Atl\xe9tico de Madrid": "Atletico Madrid",
              u"Deportivo Alav\xe9s": "Alav\u00e9s",
              "FC Barcelona": "Barcelona",
              u"M\xe1laga CF": "M\xc3\xa1laga",
              "RC Celta de Vigo": "Celta Vigo",
              "RC Deportivo La Coruna": "Deportivo La Coru\u00f1a",
              "RCD Espanyol": "Espanyol",
              "Real Betis": "Real Betis",
              "Real Madrid CF": "Real Madrid",
              u"Real Sociedad de F\xfatbol": "Real Sociedad",
              "SD Eibar": "Eibar",
              "Sevilla FC": "Sevilla FC",
              "UD Las Palmas": "Las Palmas",
              "Valencia CF": "Valencia",
              "Villarreal CF": "Villarreal",
              "Getafe CF": "Getafe",
              "Girona FC": "Girona",
              "Levante UD": "Levante",
              "AC Chievo Verona": "Chievo Verona",
              "ACF Fiorentina": "Fiorentina",
              "AC Milan": "AC Milan",
              "AS Roma": "AS Roma",
              "Atalanta BC": "Atalanta",
              "Benevento Calcio": "Benevento",
              "Hellas Verona FC": "Hellas Verona",
              "Bologna FC": "Bologna",
              "Cagliari Calcio": "Cagliari",
              "FC Crotone": "Crotone",
              "FC Internazionale Milano": "Internazionale",
              "Genoa CFC": "Genoa",
              "Juventus Turin": "Juventus",
              "SSC Napoli": "Napoli",
              "SS Lazio": "Lazio",
              "Torino FC": "Torino",
              "SPAL Ferrara": "SPAL",
              "UC Sampdoria": "Sampdoria",
              "Udinese Calcio": "Udinese",
              "US Sassuolo Calcio": "Sassuolo",
              "ADO Den Haag": "ADO Den Haag",
              "Ajax Amsterdam": "Ajax Amsterdam",
              "AZ Alkmaar": "AZ Alkmaar",
              "Excelsior": "Excelsior",
              "FC Groningen": "FC Groningen",
              "FC Twente Enschede": "FC Twente",
              "FC Utrecht": "FC Utrecht",
              "Feyenoord Rotterdam": "Feyenoord Rotterdam",
              "SC Heerenveen": "Heerenveen",
              "NAC Breda": "NAC Breda",
              "PEC Zwolle": "PEC Zwolle",
              "PSV Eindhoven": "PSV Eindhoven",
              "Roda JC Kerkrade": "Roda JC Kerkrade",
              "Heracles Almelo": "SC Heracles Almelo",
              "Sparta Rotterdam": "Sparta Rotterdam",
              "Vitesse Arnhem": "Vitesse Arnhem",
              "VVV Venlo": "VVV Venlo",
              "Willem II Tilburg": "Willem II Tilburg",
              "C.F. Os Belenenses": "Belenenses",
              "SL Benfica": "Benfica",
              "Boavista Porto FC": "Boavista",
              "Sporting Braga": "Braga",
              "Desportivo Aves": "Desportivo Aves",
              "GD Estoril Praia": "Estoril",
              "FC Porto": "FC Porto",
              "Feirense": "Feirense",
              "G.D. Chaves": "GD Chaves",
              "Vitoria Guimaraes": "Guimaraes",
              "Maritimo Funchal": "Maritimo",
              "Moreirense FC": "Moreirense",
              u'FC Pa\xe7os de Ferreira': "Pa\u00e7os de Ferreira",
              "Portimonense S.C.": "Portimonense",
              "Rio Ave": "Rio Ave",
              "Sporting CP": "Sporting CP",
              "CD Tondela": "Tondela",
              "Vitoria Setubal": "Vitoria Setubal"}

# Information server URL codes
TEAM_CODES = {"VfL Wolfsburg": 11,
              "Belenenses": 711,
              "Benfica": 495,
              "Boavista": 810,
              "Braga": 497,
              "Desportivo Aves": 1809,
              "Estoril": 582,
              "FC Porto": 503,
              "Feirense": 500,
              "GD Chaves": 1103,
              "Guimaraes": 502,
              "Maritimo": 504,
              "Moreirense": 583,
              "Pa\u00e7os de Ferreira": 507,
              "Portimonense": 1808,
              "Rio Ave": 496,
              "Sporting CP": 498,
              "Tondela": 1049,
              "Vitoria Setubal": 506,
              "ADO Den Haag": 680,
              "Ajax Amsterdam": 678,
              "AZ Alkmaar": 682,
              "Excelsior": 670,
              "FC Groningen": 677,
              "FC Twente": 666,
              "FC Utrecht": 676,
              "Feyenoord Rotterdam": 675,
              "Heerenveen": 673,
              "NAC Breda": 681,
              "PEC Zwolle": 684,
              "PSV Eindhoven": 674,
              "Roda JC Kerkrade": 665,
              "SC Heracles Almelo": 671,
              "Sparta Rotterdam": 1085,
              "Vitesse Arnhem": 679,
              "VVV Venlo": 668,
              "Willem II Tilburg": 672,
              "Borussia Dortmund": 4,
              "FC Augsburg": 16,
              "TSG Hoffenheim": 2,
              "Hamburg SV": 7,
              "Bayer Leverkusen": 3,
              "Schalke 04": 6,
              "Mainz": 15,
              "Eintracht Frankfurt": 19,
              "SC Freiburg": 17,
              "Hertha Berlin": 9,
              "Werder Bremen": 12,
              "Swansea City": 72,
              "Osasuna": 79,
              "Real Betis": 90,
              "Arsenal": 57,
              "Granada": 83,
              "Athletic Bilbao": 77,
              "Barcelona": 81,
              "Valencia": 95,
              "Manchester United": 66,
              "Villarreal": 94,
              "Everton": 62,
              "AC Milan": 98,
              "Manchester City": 65,
              "Fiorentina": 99,
              "Espanyol": 80,
              "Liverpool": 64,
              "Real Madrid": 86,
              "Benevento": 1106,
              "SPAL": 1107,
              "Tottenham Hotspur": 73,
              "Stoke City": 70,
              "Huddersfield Town": 394,
              "West Bromwich Albion": 74,
              "Chelsea": 61,
              "AS Roma": 100,
              "Cagliari": 104,
              "Bologna": 103,
              "Atalanta": 102,
              "Genoa": 107,
              "Juventus": 109,
              "Hellas Verona": 450,
              "Chievo Verona": 106,
              "Napoli": 113,
              "Internazionale": 108,
              "Udinese": 115,
              "Lazio": 110,
              "Las Palmas": 275,
              "Eibar": 278,
              "Brighton & Hove Albion": 397,
              "Burnley": 328,
              "Watford": 346,
              "Leicester City": 338,
              "Southampton": 340,
              "Newcastle United": 67,
              "Crystal Palace": 354,
              "Empoli": 445,
              "Crotone": 472,
              "Sassuolo": 471,
              "Metz": 545,
              "AS Monaco": 548,
              "Nantes": 543,
              "Lyon": 523,
              "Lille": 521,
              "Dijon FCO": 528,
              "Marseille": 516,
              "Paris Saint-Germain": 524,
              "Caen": 514,
              "Guingamp": 538,
              "Stade Rennais": 529,
              "Bordeaux": 526,
              "Toulouse": 511,
              "Angers": 532,
              "Nice": 522,
              "Celta Vigo": 558,
              "Girona": 298,
              "Levante": 88,
              "US Pescara": 585,
              "Sevilla FC": 559,
              "Deportivo La Coru\u00f1a": 560,
              "Getafe": 82,
              "Sampdoria": 584,
              "Torino": 586,
              "West Ham United": 563,
              "Leganes": 745,
              "RB Leipzig": 721,
              "AFC Bournemouth": 1044,
              "Borussia Monchengladbach": 18,
              "Bayern Munich": 5,
              "FC Cologne": 1,
              "St Etienne": 527,
              "Troyes": 531,
              "Montpellier": 518,
              "SC Amiens": 530,
              "Strasbourg": 576,
              "Atletico Madrid": 78,
              "Hannover 96": 8,
              u"M\xe1laga": 84,
              "Real Sociedad": 92,
              "Palermo": 114,
              "Alav\u00e9s": 263,
              "VfB Stuttgart": 10}