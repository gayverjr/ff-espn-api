from espn_api.football import League
from espn_api.football.trophies import *
from espn_api.football.power_rankings import *
from scipy import stats
import numpy as np


Z_league = True
Z_LEAGUE_ID = 1185741
Z_LEAGUE_SWID = "{AC702CB3-C59E-4EAD-A273-47C8EFA3B5E8}"
Z_LEAGUE_espn_s2 = "AEBrtMduGrOeFF0Yai%2Bh2gIu9%2FTDbj9xCuxORMm6IrSe%2FBjFvTaWjgRFmxl3aJkmw%2FpOJ9NjQidKJZ%2FXaLFPb1kD4766ARu6JjylBALPKZQJAW%2FhumRiGzf3Nnk%2BkTLda1n3ssM3oqJsM7%2Bl1udELfYaHomSyLrMgkkf%2FjbbY6kiy3oQNoO3PUpwMnE5Ng5bq9UoJVQ9RcDGNmlMKiUnjfGowZ5emx5m72qDNqdD4oFXbNOiu81DMpSQD2M1tY0fSFw%3D"

year = 2020
league = League(Z_LEAGUE_ID,year,Z_LEAGUE_espn_s2,Z_LEAGUE_SWID)
week = 1
print("MVP:"+str(get_MVP(league.box_scores(week),league)))
print("LVP:"+str(get_LVP(league.box_scores(week),league)))
print("Benchwarmer:"+str(get_bwotw(league.box_scores(week),league)))
print("Adam Gase:"+str(get_hue_jackson(league.box_scores(week),league,Zleague=Z_league)))
print("Hoodie:"+str(get_sith_lord(league.box_scores(week),league,Zleague=Z_league)))
print("L:"+str(get_biggest_L(league.box_scores(week))))
print("Best and worst:"+str(get_best_and_worst(league,week)))
print("DPOTW:"+str(get_DPOTW(league.box_scores(week),league)))
print("Top defense:" +  str(get_top_defense(league.box_scores(week),league)))


