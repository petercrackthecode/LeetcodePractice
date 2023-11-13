# https://leetcode.com/problems/minimum-number-of-refueling-stops/
from heapq import heappop, heappush
from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """
        target = 100
        startFuel = 10 
                      0.      1.      2       3
        stations = [[10,60],[20,30],[30,30],[60,40]]
        output = 2

        fuel = 20 + 50 + 30 = 100
             = 30 + 40 + 30 = 100
             = 60 + 0  + 40 = 100

        Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.


        - Track the furthest distance we can reach so far curr_max_distance
        - Go through the stations: for each station:
            - if its position <= curr_max_distance, that means we could stop and pump gas at that station => Push that station's gas to our max-heap (remember to revert the value of the gas since heapq in python only supports min heap).
            - else: we know that we need to pump gas at at least one previous station that we have passed => pop the heap and add the value of the gas to our curr_max_distance, and increment the stations_count by 1
        - Repeat the above steps until curr_max_distance >= target or we have traversed through all the station
        - By the end of the loop, while curr_max_distance is smaller than target and while we still have unused stations (len(unused_stations) > 0): keep popping the heap and add the value of the gas to our curr_max_distance, , and increment the stations_count by 1

        Return -1 if curr_max_distance < target else stations_count
        """
        # [[10,60],[20,30],[30,30],[60,40]]
        if startFuel >= target:
            return 0
        passed_stations = []
        curr_max_distance = startFuel

        i = 0
        stations_count = 0

        while curr_max_distance <= target and i < len(stations):
            [station_pos, station_gas] = stations[i]
            if curr_max_distance >= station_pos:
                heappush(passed_stations, -station_gas)
                i += 1
            else:  # curr_max_distance < station_pos
                # already pumped all the prev station
                if len(passed_stations) == 0:
                    return -1

                station_gas = -heappop(passed_stations)
                curr_max_distance += station_gas
                stations_count += 1

        while curr_max_distance < target and len(passed_stations) > 0:
            station_gas = -heappop(passed_stations)
            curr_max_distance += station_gas
            stations_count += 1

        return stations_count if curr_max_distance >= target else -1
