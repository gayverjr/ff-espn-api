from espn_api.football import League
from espn_api.football.trophies import *
from espn_api.football.power_rankings import *
from scipy import stats
import numpy as np

best_player_line = "best player"
worst_player_line = "worst player"

Z_league = True
Z_LEAGUE_ID = 1185741
Z_LEAGUE_SWID = "{AC702CB3-C59E-4EAD-A273-47C8EFA3B5E8}"
Z_LEAGUE_espn_s2 = "AEBrtMduGrOeFF0Yai%2Bh2gIu9%2FTDbj9xCuxORMm6IrSe%2FBjFvTaWjgRFmxl3aJkmw%2FpOJ9NjQidKJZ%2FXaLFPb1kD4766ARu6JjylBALPKZQJAW%2FhumRiGzf3Nnk%2BkTLda1n3ssM3oqJsM7%2Bl1udELfYaHomSyLrMgkkf%2FjbbY6kiy3oQNoO3PUpwMnE5Ng5bq9UoJVQ9RcDGNmlMKiUnjfGowZ5emx5m72qDNqdD4oFXbNOiu81DMpSQD2M1tY0fSFw%3D"

year = 2020
league = League(Z_LEAGUE_ID,year,Z_LEAGUE_espn_s2,Z_LEAGUE_SWID)
week = 1

print("[u] Weekly trophies [/u]")
print()
print("MVP:"+str(get_MVP(league.box_scores(week),league)))
print("[b] MVP [/b]")
player,pts,team = get_MVP(league.box_scores(week),league)
print(str(player)+ "("+str(team)+"): " + '{0:.3g}'.format(pts) + " points")
print("[b] LVP [/b]")
player,pts,team = get_LVP(league.box_scores(week),league)
print(str(player)+ "("+str(team)+"): " + '{0:.3g}'.format(-1*pts) + " points below projection")
print("[b] Benchwarmer [/b]")
player,team = get_bwotw(league.box_scores(week),league)
print(str(player.name)+ "("+str(team)+"): " + '{0:.3g}'.format(player.points) + " points")
print("[b] Defensive Player of the week [/b]")
player,pts,team = get_DPOTW(league.box_scores(week),league)
print(str(player)+ "("+str(team)+"): " + '{0:.3g}'.format(pts) + " points")
print("[b] Adam Gase [/b]")
team,points=get_hue_jackson(league.box_scores(week),league,Zleague=Z_league)
print(team.team_name + ": " + '{0:.3g}'.format(points) + " points left on the bench.")
print("[b] Hoodie [/b]")
team,points=get_sith_lord(league.box_scores(week),league,Zleague=Z_league)
print(team.team_name + ": " + '{0:.3g}'.format(points) + " points better than ESPN suggested lineup.")
print("[b] Top defense [/b]")
team,points=get_top_defense(league.box_scores(week),league)
print(team.team_name + ": " + '{0:.3g}'.format(points) + " points scored by defensive players.")
print("[b] Biggest L [/b]")
winner,loser,diff = get_biggest_L(league.box_scores(week))
print(winner.team_name + " over " + loser.team_name + ": " + '{0:.3g}'.format(diff) +" point margin of victory.")
worst,wst_pts,best,bst_pts = get_best_and_worst(league,week)
print("[b] Hottest in the office [/b]")
print(best.team_name + ": " + '{0:.3g}'.format(bst_pts)+" points")
print("[b] Weenie Hut Jr. [/b]")
print(worst.team_name + ": " + '{0:.3g}'.format(wst_pts)+" points")
print()
print("[u] Season long trophies [/u]")
print()
print("[b] Defense wins championships [/b]")
team,dpts = get_top_defense_season(league,week)
print(team.team_name + " leads the league with " '{0:.3g}'.format(dpts) + " points scored by defensive players.")
print("[b] Best Gameday Coach [/b]")
team,pts = best_coach(league,week,Z=True)
print(team.team_name + " has picked up " + '{0:.3g}'.format(pts) + " points with wise lineup decisions on the year.")
print("[b] Should fire himself [/b]")
team,pts = worst_coach(league,week,Z=True)
print(team.team_name + " has left " + '{0:.3g}'.format(-1*pts) + " points on the bench on the year.")
print("[b] Luckiest lad [/b]")
pts_against = sorted(league.teams,key=lambda x: x.points_against)
print(pts_against[0].team_name + " with only " + '{0:.3g}'.format(pts_against[0].points_against) + " points against.")
print("[b] I can't believe this is happening to me [/b]")
print(pts_against[-1].team_name + " with an unfortunate " + '{0:.3g}'.format(pts_against[-1].points_against) + " points against.")
pts_for = sorted(league.teams,key=lambda x: x.points_for)
print("[b]" + best_player_line + "[/b]")
print(pts_for[-1].team_name + " with a mighty " + '{0:.3g}'.format(pts_for[-1].points_for) + " points scored.")
print("[b]" + worst_player_line + "[/b]")
print(pts_for[0].team_name + " with a pitiful " + '{0:.3g}'.format(pts_for[0].points_for) + " points scored.")
