#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# 近似算法的应用 => 集合覆盖问题
#
# tip: 场景和题目描述件ppt
#######################################################################################

if __name__ == '__main__':
    states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
    stations = {}
    stations["knoe"] = set(["id", "nv", "ut"])
    stations["ktwo"] = set(["wa", "id", "mt"])
    stations["kthree"] = set(["or", "nv", "ca"])
    stations["kfour"] = set(["nv", "ut"])
    stations["kfive"] = set(["ca", "az"])

    final_stations = set()

    while states_needed:
        best_station = None
        states_covered = set()
        for station, states in stations.items():
            covered = states_needed & states
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        states_needed -= states_covered
        final_stations.add(best_station)


    print(final_stations)
