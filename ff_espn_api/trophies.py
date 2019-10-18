"""
How to import data from THE LEAGUE:
THE_LEAGUE_SWID = "{AC702CB3-C59E-4EAD-A273-47C8EFA3B5E8}"
THE_LEAGUE_espn_s2 = "AEBrtMduGrOeFF0Yai%2Bh2gIu9%2FTDbj9xCuxORMm6IrSe%2FBjFvTaWjgRFmxl3aJkmw%2FpOJ9NjQidKJZ%2FXaLFPb1kD4766ARu6JjylBALPKZQJAW%2FhumRiGzf3Nnk%2BkTLda1n3ssM3oqJsM7%2Bl1udELfYaHomSyLrMgkkf%2FjbbY6kiy3oQNoO3PUpwMnE5Ng5bq9UoJVQ9RcDGNmlMKiUnjfGowZ5emx5m72qDNqdD4oFXbNOiu81DMpSQD2M1tY0fSFw%3D"
THE_LEAGUE_ID = 893209
year = 2018
league = League(THE_LEAGUE_ID,year,THE_LEAGUE_espn_s2,THE_LEAGUE_SWID)

For Z League:
Z_LEAGUE_ID = 1185741
Z_LEAGUE_SWID = "{AC702CB3-C59E-4EAD-A273-47C8EFA3B5E8}"
Z_LEAGUE_espn_s2 = "AEBrtMduGrOeFF0Yai%2Bh2gIu9%2FTDbj9xCuxORMm6IrSe%2FBjFvTaWjgRFmxl3aJkmw%2FpOJ9NjQidKJZ%2FXaLFPb1kD4766ARu6JjylBALPKZQJAW%2FhumRiGzf3Nnk%2BkTLda1n3ssM3oqJsM7%2Bl1udELfYaHomSyLrMgkkf%2FjbbY6kiy3oQNoO3PUpwMnE5Ng5bq9UoJVQ9RcDGNmlMKiUnjfGowZ5emx5m72qDNqdD4oFXbNOiu81DMpSQD2M1tY0fSFw%3D"
#league = League(Z_LEAGUE_ID,year,Z_LEAGUE_espn_s2,Z_LEAGUE_SWID)

"""

def get_MVP(box_scores):
    '''Non-bench player w/ most points scored that week
    '''
    all_players = []
    for box_score in box_scores:
        all_players += box_score.home_lineup
        all_players += box_score.away_lineup
    all_players = sorted(all_players,key=lambda x: x.points, reverse=True)
    for player in all_players:
        if player.slot_position != "BE":
            return player,player.points

def get_LVP(box_scores):
    '''Non-bench player w/ fewest points relative to projection
    '''
    all_players = []
    for box_score in box_scores:
        all_players += box_score.home_lineup
        all_players += box_score.away_lineup
    all_players = sorted(all_players,key=lambda x: x.points-x.projected_points, reverse=False)
    worst_players = []
    for player in all_players:
        if player.slot_position != "BE":
            worst_players.append((player,player.points-player.projected_points))
    return worst_players

def get_bwotw(box_scores,league):
    '''Most points for bench player (benchwarmer of the week)
    '''
    all_players = []
    for box_score in box_scores:
        all_players += box_score.home_lineup
        all_players += box_score.away_lineup
    all_players = sorted(all_players,key=lambda x: x.points, reverse=True)
    best_benched_player = []
    i = 0
    while i<len(all_players) and not best_benched_player:
        player = all_players[i]
        if player.slot_position == "BE":
            best_benched_player = player
        i +=1
    for team in league.teams:
        if team.get_player_name(best_benched_player.playerId):
            return best_benched_player,team.team_name

def get_optimal_score(lineup):
    ''' Optimal score for a given lineup
    '''
    QBs=[]
    RBs=[]
    TE=[]
    Flex = []
    WRs = []
    D_ST = []
    K = []
    optimal_points = 0
    sorted_lineup = sorted(lineup,key=lambda x: x.points, reverse=True)
    for player in sorted_lineup:
        if "QB" in player.eligibleSlots and len(QBs)==0:
            QBs.append(player)
            optimal_points+=player.points
        elif "RB" in player.eligibleSlots and len(RBs)<2:
            RBs.append(player)
            optimal_points+=player.points
        elif "WR" in player.eligibleSlots and len(WRs)<2:
            WRs.append(player)
            optimal_points+=player.points
        elif "TE" in player.eligibleSlots and len(TE)==0:
            TE.append(player)
            optimal_points+=player.points
        elif "RB/WR/TE" in player.eligibleSlots and len(Flex)==0:
            Flex.append(player)
            optimal_points+=player.points
        elif "D/ST" in player.eligibleSlots and len(D_ST)==0:
            D_ST.append(player)
            optimal_points+=player.points
        elif "K" in player.eligibleSlots and len(K)==0:
            K.append(player)
            optimal_points+=player.points
    return optimal_points

def get_optimal_score_Z(lineup):
    ''' Optimal score for a given lineup
        '''
    QBs=[]
    RBs=[]
    TE=[]
    Flex = []
    WRs = []
    DT = []
    DE = []
    LB = []
    CB = []
    S = []
    K = []
    optimal_points = 0
    sorted_lineup = sorted(lineup,key=lambda x: x.points, reverse=True)
    for player in sorted_lineup:
        if "QB" in player.eligibleSlots and len(QBs)<2:
            QBs.append(player)
            optimal_points+=player.points
        elif "RB" in player.eligibleSlots and len(RBs)<2:
            RBs.append(player)
            optimal_points+=player.points
        elif "WR" in player.eligibleSlots and len(WRs)<2:
            WRs.append(player)
            optimal_points+=player.points
        elif "TE" in player.eligibleSlots and len(TE)==0:
            TE.append(player)
            optimal_points+=player.points
        elif "RB/WR/TE" in player.eligibleSlots and len(Flex)==0:
            Flex.append(player)
            optimal_points+=player.points
        elif "DT" in player.eligibleSlots and len(DT)==0:
            DT.append(player)
            optimal_points+=player.points
        elif "DE" in player.eligibleSlots and len(DE)==0:
            DE.append(player)
            optimal_points+=player.points
        elif "LB" in player.eligibleSlots and len(LB)==0:
            LB.append(player)
            optimal_points+=player.points
        elif "CB" in player.eligibleSlots and len(CB)==0:
            CB.append(player)
            optimal_points+=player.points
        elif "S" in player.eligibleSlots and len(S)==0:
            S.append(player)
            optimal_points+=player.points
        elif "K" in player.eligibleSlots and len(K)==0:
            K.append(player)
            optimal_points+=player.points
    return optimal_points

def get_hue_jackson(box_scores,league,Zleague=False):
    '''Worst team points relative to optimal points
    '''
    teams_and_differentials = []
    for box_score in box_scores:
        if Zleague:
            optimal_home = get_optimal_score_Z(box_score.home_lineup)
            optimal_away = get_optimal_score_Z(box_score.away_lineup)
        else:
            optimal_home = get_optimal_score(box_score.home_lineup)
            optimal_away = get_optimal_score(box_score.away_lineup)
        teams_and_differentials.append((box_score.home_team,optimal_home-box_score.home_score))
        teams_and_differentials.append((box_score.away_team,optimal_away-box_score.away_score))
    teams_and_differentials = sorted(teams_and_differentials,key=lambda x: x[1], reverse=True)
    return teams_and_differentials[:2]

def get_projected_score(lineup):
    '''Projected score of given lineup
    '''
    proj_score = 0
    for player in lineup:
        if player.slot_position != "BE":
            proj_score += player.projected_points
    return proj_score

def get_sith_lord(box_scores,league):
    ''' Most team points relative to projection
    '''
    teams_and_differentials = []
    for box_score in box_scores:
        proj_home = get_projected_score(box_score.home_lineup)
        teams_and_differentials.append((box_score.home_team,box_score.home_score-proj_home))
        proj_away = get_projected_score(box_score.away_lineup)
        teams_and_differentials.append((box_score.away_team,box_score.away_score-proj_away))
    teams_and_differentials = sorted(teams_and_differentials,key=lambda x: x[1], reverse=True)
    return teams_and_differentials[0]  

def get_biggest_L(box_scores):
    winner_loser_diff = []
    for box_score in box_scores:
        if box_score.home_score> box_score.away_score:
            winner_loser_diff.append((box_score.home_team,box_score.away_team,box_score.home_score-box_score.away_score))
        else:
            winner_loser_diff.append((box_score.away_team,box_score.home_team,box_score.away_score-box_score.home_score))
    winner_loser_diff = sorted(winner_loser_diff,key=lambda x: x[2], reverse=True)
    return winner_loser_diff[0]  
