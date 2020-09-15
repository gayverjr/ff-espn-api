import numpy as np
from .trophies import *

def get_activity(league,team):
    trades=0
    add_drops=1
    activity=league.recent_activity(200)
    for act in activity:
        for action in act.actions:
            if team in action:
                if "TRADED" in action:
                    trades+=1
                else:
                    add_drops+=1
                break
    return(trades,add_drops)

def get_team_lineup(team,box_scores):
    for matchup in box_scores:
        if matchup.home_team == team:
            return matchup.home_lineup
        elif matchup.away_team == team:
            return matchup.away_lineup
    return None

def team_stud(team,week,league):
    players_and_scores = {}
    for i in range(1,week+1):
        box_scores = league.box_scores(i)
        lineup = get_team_lineup(team,box_scores)
        for player in lineup:
            if player.slot_position != "BE":
                if player.name not in players_and_scores:
                    players_and_scores[player.name]= player.points
                else:
                    players_and_scores[player.name] = players_and_scores[player.name] + player.points
    players_and_scores = players_and_scores.items()
    players_and_scores = sorted(players_and_scores, key=lambda x: x[1],reverse=True )
    return players_and_scores

def team_dud(team,week,league):
    players_and_scores = {}
    for i in range(1,week+1):
        box_scores = league.box_scores(i)
        lineup = get_team_lineup(team,box_scores)
        for player in lineup:
            if player.slot_position != "BE":
                if player.name not in players_and_scores:
                    players_and_scores[player.name]= player.points-player.projected_points
                else:
                    players_and_scores[player.name] = players_and_scores[player.name] + player.points -player.projected_points
    players_and_scores = players_and_scores.items()
    players_and_scores = sorted(players_and_scores, key=lambda x: x[1])
    return players_and_scores

def team_bw(team,week,league):
    players_and_scores = {}
    for i in range(1,week+1):
        box_scores = league.box_scores(i)
        lineup = get_team_lineup(team,box_scores)
        for player in lineup:
            if player.slot_position == "BE":
                if player.name not in players_and_scores:
                    players_and_scores[player.name]= player.points
                else:
                    players_and_scores[player.name] = players_and_scores[player.name] + player.points
    players_and_scores = players_and_scores.items()
    players_and_scores = sorted(players_and_scores, key=lambda x: x[1],reverse=True )
    return players_and_scores


def position_rank(team,league,pos):
    l1=league.teams
    l1= sorted(l1,key=lambda x: x.reports[pos][0],reverse=True)
    rank = l1.index(team)
    return rank

def position_analysis(team,week,league,pos):
    pos_points = 0
    bench_points = 0
    num_started=0
    bench_players = 0
    for i in range(1,week+1):
        box_scores = league.box_scores(i)
        lineup = get_team_lineup(team,box_scores)
        for player in lineup:
            if player.slot_position == pos:
                pos_points += player.points
                num_started+=1
            elif player.slot_position=="RB/WR/TE" and pos in player.eligibleSlots:
                pos_points += player.points
                num_started+=1
            elif pos in player.eligibleSlots:
                if player.pro_opponent!=None:
                    bench_points += player.points
                    bench_players+=1
    if bench_players==0:
        bench_players=1
    team.reports[pos]=(pos_points/num_started,pos_points,bench_points/bench_players)

def coach_rating(team,week,league,Z=False):
    points_lost = 0
    for i in range(1,week+1):
        box_scores = league.box_scores(i)
        lineup = get_team_lineup(team,box_scores)
        if Z:
            points_lost += team.scores[i-1]-get_optimal_score_Z(lineup)
        else:
            points_lost += team.scores[i-1]-get_optimal_score(lineup)
    return points_lost
