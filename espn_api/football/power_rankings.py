import numpy as np

def get_all_overall_record(league,week=17):
    for team in league.teams:
        ovw = 0
        ovl = 0
        for team2 in league.teams:
            if team2 != team:
                for i in range(0,week):
                    if team.scores[i] > team2.scores[i]:
                        ovw +=1
                    else:
                        ovl += 1
        team.ovw = ovw
        team.ovl = ovl
    return sorted(league.teams,key=lambda x: x.ovw, reverse=True)

def get_overall_record(league,team,week=17):
    ovw = 0
    ovl = 0
    for team2 in league.teams:
        for i in range(0,week):
            if team.scores[i] > team2.scores[i]:
                ovw +=1
            else:
                ovl +=1
    return ovw,ovl

def get_all_points_scored(league,week=17):
    return sorted(league.teams,key=lambda x: np.sum(x.scores[:week]),reverse=True)

def get_team_lineup(team,box_scores):
    for matchup in box_scores:
        if matchup.home_team == team:
            return matchup.home_lineup
        elif matchup.away_team == team:
            return matchup.away_lineup
    return None

def get_all_bench_points(league,week=17):
    for team in league.teams:
        bench_points = 0
        for i in range(1,week+1):
            box_scores = league.box_scores(i)
            lineup = get_team_lineup(team,box_scores)
            for player in lineup:
                bench_points += player.points
        team.bench_points = bench_points
    return sorted(league.teams,key=lambda x: x.bench_points, reverse=True)

def assign_ranks(teams,ovr,points,bench,record,week):
    for team in teams:
        # ovr first
        for i in range(0,len(ovr)):
            if team.ovw == ovr[i].ovw:
                team.ovr_rank = i+1
                break
        # now pts
        for i in range(0,len(points)):
            if np.sum(team.scores[:week]) == np.sum(points[i].scores[:week]):
                team.pts_rank = i+1
                break

        # now bench
        for i in range(0,len(bench)):
            if team.bench_points == ovr[i].bench_points:
                team.bnch_rank = i
                break
        # now record
        for i in range(0,len(record)):
            if team.wins/(team.wins+team.losses) == record[i].wins/(record[i].wins+record[i].losses):
                team.record_rank = i+1
                break

def power_rankings(league,week):
    overall_records = get_all_overall_record(league,week=week)
    points_scored = get_all_points_scored(league,week)
    bench_points = get_all_bench_points(league,week)   
    records = sorted(league.teams,key=lambda x: x.wins/(x.wins+x.losses), reverse=True)
    assign_ranks(league.teams,overall_records,points_scored,bench_points,records,week)
    for team in league.teams:
        score = 0
        score += 0.3 * team.ovr_rank
        score += 0.3 * team.pts_rank
        score += 0.3 * team.record_rank
        score += 0.1 * team.bnch_rank
        team.power_score = score
        team.ovr_rank = overall_records.index(team)+1
        team.pts_rank = points_scored.index(team)+1
        team.bnch_rank = bench_points.index(team)+1
    return sorted(league.teams,key=lambda x: x.power_score)
