from ff_espn_api import League
from ff_espn_api.trophies import *


##for the league
THE_LEAGUE_SWID = "{AC702CB3-C59E-4EAD-A273-47C8EFA3B5E8}"
THE_LEAGUE_espn_s2 = "AEBrtMduGrOeFF0Yai%2Bh2gIu9%2FTDbj9xCuxORMm6IrSe%2FBjFvTaWjgRFmxl3aJkmw%2FpOJ9NjQidKJZ%2FXaLFPb1kD4766ARu6JjylBALPKZQJAW%2FhumRiGzf3Nnk%2BkTLda1n3ssM3oqJsM7%2Bl1udELfYaHomSyLrMgkkf%2FjbbY6kiy3oQNoO3PUpwMnE5Ng5bq9UoJVQ9RcDGNmlMKiUnjfGowZ5emx5m72qDNqdD4oFXbNOiu81DMpSQD2M1tY0fSFw%3D"
THE_LEAGUE_ID = 893209
year = 2018
league = League(THE_LEAGUE_ID,year,THE_LEAGUE_espn_s2,THE_LEAGUE_SWID)
#for Z league
Z_LEAGUE_ID = 1185741
Z_LEAGUE_SWID = "{AC702CB3-C59E-4EAD-A273-47C8EFA3B5E8}"
Z_LEAGUE_espn_s2 = "AEBrtMduGrOeFF0Yai%2Bh2gIu9%2FTDbj9xCuxORMm6IrSe%2FBjFvTaWjgRFmxl3aJkmw%2FpOJ9NjQidKJZ%2FXaLFPb1kD4766ARu6JjylBALPKZQJAW%2FhumRiGzf3Nnk%2BkTLda1n3ssM3oqJsM7%2Bl1udELfYaHomSyLrMgkkf%2FjbbY6kiy3oQNoO3PUpwMnE5Ng5bq9UoJVQ9RcDGNmlMKiUnjfGowZ5emx5m72qDNqdD4oFXbNOiu81DMpSQD2M1tY0fSFw%3D"
#league = League(Z_LEAGUE_ID,year,Z_LEAGUE_espn_s2,Z_LEAGUE_SWID)


#testing trophies
MVP = get_MVP(league.box_scores(12))
print(MVP.name)
print(MVP.points)
LVP = get_LVP(league.box_scores(12))
print(LVP.name)
print(LVP.points)
print(get_hue_jackson(league.box_scores(5),league))
print(get_sith_lord(league.box_scores(5),league))