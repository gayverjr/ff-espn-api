from espn_api.football import League
from espn_api.football.trophies import *
from espn_api.football.power_rankings import *
from espn_api.football.team_report import *
from scipy import stats
import numpy as np


##for the league
THE_LEAGUE_SWID = "{AC702CB3-C59E-4EAD-A273-47C8EFA3B5E8}"
THE_LEAGUE_espn_s2 = "AEBrtMduGrOeFF0Yai%2Bh2gIu9%2FTDbj9xCuxORMm6IrSe%2FBjFvTaWjgRFmxl3aJkmw%2FpOJ9NjQidKJZ%2FXaLFPb1kD4766ARu6JjylBALPKZQJAW%2FhumRiGzf3Nnk%2BkTLda1n3ssM3oqJsM7%2Bl1udELfYaHomSyLrMgkkf%2FjbbY6kiy3oQNoO3PUpwMnE5Ng5bq9UoJVQ9RcDGNmlMKiUnjfGowZ5emx5m72qDNqdD4oFXbNOiu81DMpSQD2M1tY0fSFw%3D"
THE_LEAGUE_ID = 893209
year = 2020
league = League(THE_LEAGUE_ID,year,THE_LEAGUE_espn_s2,THE_LEAGUE_SWID)
#for Z league
Z_LEAGUE_ID = 1185741
Z_LEAGUE_SWID = "{AC702CB3-C59E-4EAD-A273-47C8EFA3B5E8}"
Z_LEAGUE_espn_s2 = "AEBrtMduGrOeFF0Yai%2Bh2gIu9%2FTDbj9xCuxORMm6IrSe%2FBjFvTaWjgRFmxl3aJkmw%2FpOJ9NjQidKJZ%2FXaLFPb1kD4766ARu6JjylBALPKZQJAW%2FhumRiGzf3Nnk%2BkTLda1n3ssM3oqJsM7%2Bl1udELfYaHomSyLrMgkkf%2FjbbY6kiy3oQNoO3PUpwMnE5Ng5bq9UoJVQ9RcDGNmlMKiUnjfGowZ5emx5m72qDNqdD4oFXbNOiu81DMpSQD2M1tY0fSFw%3D"


league = League(Z_LEAGUE_ID,year,Z_LEAGUE_espn_s2,Z_LEAGUE_SWID)
pos = ["QB","RB","WR","TE","K","D/ST"]
pos =["QB","RB","WR","TE","K", "DE","S","CB","DT","LB"]
D_pos = ["DE","S","CB","DT","LB"]
#Z_bool=False
Z_bool=True
week = 1
# generate all of the points once
for team in league.teams:
    team.reports={}
    for position in pos:
        position_analysis(team,week,league,position)
# second pass through so we can have rankings
for team in league.teams:
    print(team)
    print("Points lost from lineup decisions:"+'{0:.4g}'.format(-1*coach_rating(team,week,league,Z=Z_bool)))
    trades,add_drops = get_activity(league,team)
    print("Add/drops:" + str(add_drops))
    print("Team stud:" + str(team_stud(team,week,league)[0]))
    print("Team dud:" + str(team_dud(team,week,league)[0]))
    print("Most underutilized:" + str(team_bw(team,week,league)[:4]))

    #print("Points lost from lineup decisions:"+str(coach_rating(team,week,league,Z=True)))
    d_points =0
    d_bench =0
    team_points = np.sum(team.scores[:week])
    for position in pos:
        rank= position_rank(team,league,position)+1
        if position in D_pos:
            d_points += team.reports[position][1]
        else:
            print(position + "\t" + "Avg starter PPG: " + '{0:.3g}'.format(team.reports[position][0]) + "\t" +" Avg bench PPG:" +  '{0:.3g}'.format(team.reports[position][2]) + "\t Percentage of total points:" +  '{0:.4g}'.format(team.reports[position][1]/team_points*100) +"%" + "\t" + "Rank:" + str(rank)  )
    if d_points > 0:
        print("Total Defense" + "\t" + "PPG: " + '{0:.3g}'.format(d_points/week) + "\t Point share:" +  '{0:.3g}'.format(d_points/team_points*100) +"%" )
    print("\n")
'''
for team in league.teams:
    print(team)
    print("Team stud:" + str(team_stud(team,5,league)[0]))
    print("Team dud:" + str(team_dud(team,5,league)[0]))
    print("Team bw:" + str(team_bw(team,5,league)[:4]))
    print("RB:"+str(position_report(team,5,league,"RB")))
    print("WR:"+str(position_report(team,5,league,"WR")))
    print("QB:"+str(position_report(team,5,league,"QB")))
    print("TE:"+str(position_report(team,5,league,"TE")))
    print("K:"+str(position_report(team,5,league,"K")))
    print("D/ST:"+str(position_report(team,5,league,"D/ST")))
    print("Points lost:"+str(coach_rating(team,5,league)))
'''
