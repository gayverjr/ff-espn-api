import numpy as np
from .trophies import *

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

'''
def position_report(team,week,league,pos):
    analyses = []
    for this_team in league.teams:
        analyses.append(position_analysis(this_team,week,league,pos))
    my_analysis = position_analysis(team,week,league,pos)
    analyses = sorted(analyses,key=lambda x: x[1],reverse=True)
    idx = analyses.index(my_analysis)
    return (my_analysis[1],my_analysis[2],my_analysis[3],idx+1)
'''

def position_rank(team,league,pos):
    l1=league.teams
    l1= sorted(l1,key=lambda x: x.reports[pos][0],reverse=True)
    rank = l1.index(team)
    return rank

def position_analysis(team,week,league,pos):
    pos_points = 0
    bench_points = 0
    for i in range(1,week+1):
        box_scores = league.box_scores(i)
        lineup = get_team_lineup(team,box_scores)
        for player in lineup:
            if player.slot_position == pos:
                pos_points += player.points
            elif player.slot_position=="RB/WR/TE" and pos in player.eligibleSlots:
                pos_points += player.points
            elif pos in player.eligibleSlots:
                bench_points += player.points
    team.reports[pos]=(pos_points,bench_points)
    #team_points = np.sum(team.scores[:week])
    '''
    if pos=="RB":
        team.rb_points=pos_points
        team.rb_bench=bench_points
    elif pos=="WR":
        team.wr_points=pos_points
        team.wr_bench=bench_points
    elif pos=="QB":
        team.qb_points=pos_points
        team.qb_bench=bench_points
    elif pos=="TE":
        team.te_points=pos_points
        team.te_bench=bench_points
    elif pos=="K":
        team.k_points=pos_points
        team.k_bench=bench_points
    else:
        if team.d_points:
            team.d_points+=pos_points
            team.d_bench+=bench_points
        else:
            team.d_points=pos_points
            team.d_bench=bench_points
#return (team,pos_points,bench_points,pos_points/team_points*100)
'''

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
