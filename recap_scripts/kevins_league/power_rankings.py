from espn_api.football import League
from espn_api.football.trophies import *
from espn_api.football.power_rankings import *
from scipy import stats
import numpy as np


##for the league
THE_LEAGUE_SWID = "{AC702CB3-C59E-4EAD-A273-47C8EFA3B5E8}"
THE_LEAGUE_espn_s2 = "AEBrtMduGrOeFF0Yai%2Bh2gIu9%2FTDbj9xCuxORMm6IrSe%2FBjFvTaWjgRFmxl3aJkmw%2FpOJ9NjQidKJZ%2FXaLFPb1kD4766ARu6JjylBALPKZQJAW%2FhumRiGzf3Nnk%2BkTLda1n3ssM3oqJsM7%2Bl1udELfYaHomSyLrMgkkf%2FjbbY6kiy3oQNoO3PUpwMnE5Ng5bq9UoJVQ9RcDGNmlMKiUnjfGowZ5emx5m72qDNqdD4oFXbNOiu81DMpSQD2M1tY0fSFw%3D"
THE_LEAGUE_ID = 893209
year = 2020
league = League(THE_LEAGUE_ID,year,THE_LEAGUE_espn_s2,THE_LEAGUE_SWID)
week = 1


rankings = power_rankings(league,week)
print("Rank\tTeam\tW/L\tPoints\tOverall\tBench\tPWR")
for i in range(0,len(rankings)):
    team = rankings[i]
    print("[b]" + str(i+1)+ ":[/b] "+ team.team_name +str("(")+ str(team.wins) + "-" + str(team.losses) + str(")"))
    print("Points:" + '{0:.4g}'.format(np.sum(team.scores[:week])) + "(" + str(team.pts_rank)+ ")"+ " OVR:" +
          str(team.ovw)+ "-" + str(team.ovl) + "(" + str(team.ovr_rank) + ")" + " Bench:" + '{0:.4g}'.format(team.bench_points) + "(" + str(team.bnch_rank) + ")" + " PWR:" + '{0:.2g}'.format(team.power_score) )

