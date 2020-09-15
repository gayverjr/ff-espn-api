from espn_api.football import League
from espn_api.football.trophies import *
from espn_api.football.power_rankings import *
from scipy import stats
import numpy as np



year = 2020
Z_LEAGUE_ID = 1185741
Z_LEAGUE_SWID = "{AC702CB3-C59E-4EAD-A273-47C8EFA3B5E8}"
Z_LEAGUE_espn_s2 = "AEBrtMduGrOeFF0Yai%2Bh2gIu9%2FTDbj9xCuxORMm6IrSe%2FBjFvTaWjgRFmxl3aJkmw%2FpOJ9NjQidKJZ%2FXaLFPb1kD4766ARu6JjylBALPKZQJAW%2FhumRiGzf3Nnk%2BkTLda1n3ssM3oqJsM7%2Bl1udELfYaHomSyLrMgkkf%2FjbbY6kiy3oQNoO3PUpwMnE5Ng5bq9UoJVQ9RcDGNmlMKiUnjfGowZ5emx5m72qDNqdD4oFXbNOiu81DMpSQD2M1tY0fSFw%3D"


league = League(Z_LEAGUE_ID,year,Z_LEAGUE_espn_s2,Z_LEAGUE_SWID)

Z_league = True
week = 1
print(league.box_scores(16)[0].home_team)
print(get_projected_score(league.box_scores(16)[0].home_lineup))
print(get_optimal_score(league.box_scores(16)[0].home_lineup))

print(league.box_scores(16)[0].away_team)
print(get_projected_score(league.box_scores(16)[0].away_lineup))
print(get_optimal_score(league.box_scores(16)[0].away_lineup))


print(league.box_scores(16)[4].home_team)
print(get_projected_score_Z(league.box_scores(16)[4].home_lineup))
print(get_optimal_score_Z(league.box_scores(16)[4].home_lineup))

print(league.box_scores(16)[4].away_team)
print(get_projected_score_Z(league.box_scores(16)[4].away_lineup))
print(get_optimal_score_Z(league.box_scores(16)[4].away_lineup))

