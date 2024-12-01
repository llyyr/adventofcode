#!/usr/bin/env python3.11

from aochelper import *

inp = tuple(map(ints, open('19.txt').read().strip().splitlines()))

def solve(ore_r_c, clay_r_c, obs_r_co, obs_r_cc, geo_r_co, geo_r_cobs, T):
    max_o_cost = max(ore_r_c, clay_r_c, obs_r_co, geo_r_co)
    S = [(1, 0, 0, 0, 0, 0, 0, 0, T)]
    seen = set()
    best = 0
    while S:
        state = S.pop()
        r1_cnt, r2_cnt, r3_cnt, r4_cnt, ore, clay, obs, geo, t = state
        best = max(best, geo)
        if t == 0:
            continue
        ore = min(ore, t * max_o_cost - r1_cnt * (t - 1))
        clay = min(clay, t * obs_r_cc - r2_cnt * (t - 1))
        obs = min(obs, t * geo_r_cobs - r3_cnt * (t - 1))
        state = (r1_cnt, r2_cnt, r3_cnt, r4_cnt, ore, clay, obs, geo, t)
        if state in seen:
            continue
        seen.add(state)
        S.append((r1_cnt, r2_cnt, r3_cnt, r4_cnt,
                  ore + r1_cnt, clay + r2_cnt, obs + r3_cnt, geo + r4_cnt,
                  t - 1))
        if ore >= geo_r_co and obs >= geo_r_cobs:
            S.append((r1_cnt, r2_cnt, r3_cnt, r4_cnt + 1,
                      ore - geo_r_co + r1_cnt, clay + r2_cnt, obs - geo_r_cobs + r3_cnt, geo + r4_cnt,
                      t - 1))
        elif ore >= obs_r_co and clay >= obs_r_cc and r3_cnt < geo_r_cobs:
            S.append((r1_cnt, r2_cnt, r3_cnt + 1, r4_cnt,
                      ore - obs_r_co + r1_cnt, clay - obs_r_cc + r2_cnt, obs + r3_cnt, geo + r4_cnt,
                      t - 1))
        elif ore >= clay_r_c and r2_cnt < obs_r_cc:
            S.append((r1_cnt, r2_cnt + 1, r3_cnt, r4_cnt,
                      ore - clay_r_c + r1_cnt, clay + r2_cnt, obs + r3_cnt, geo + r4_cnt,
                      t - 1))
        if ore >= ore_r_c and r1_cnt < max_o_cost:
            S.append((r1_cnt + 1, r2_cnt, r3_cnt, r4_cnt,
                      ore - ore_r_c + r1_cnt, clay + r2_cnt, obs + r3_cnt, geo + r4_cnt,
                      t - 1))
    return best

print(sum(i * solve(*nums, 24) for i, *nums in inp))
print(solve(*inp[0][1:], 32) * solve(*inp[1][1:], 32) * solve(*inp[2][1:], 32))

