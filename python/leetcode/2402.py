import heapq
import math
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # room_availability_time = [0] * n
        # meeting_count = [0] * n
        # for start, end in sorted(meetings):
        #     min_room_availability_time = math.inf
        #     min_available_time_room = 0
        #     found_unused_room = False
        #     for i in range(n):
        #         if room_availability_time[i] <= start:
        #             found_unused_room = True
        #             meeting_count[i] += 1
        #             room_availability_time[i] = end
        #             break
        #         if min_room_availability_time > room_availability_time[i]:
        #             min_room_availability_time = room_availability_time[i]
        #             min_available_time_room = i
        #     if not found_unused_room:
        #         room_availability_time[min_available_time_room] += end - start
        #         meeting_count[min_available_time_room] += 1

        # return meeting_count.index(max(meeting_count))
        unused_rooms, used_rooms = list(range(n)), []
        heapq.heapify(unused_rooms)
        meeting_counter = [0] * n # i-th -> # of meeting in room i-th
        max_ = -math.inf
        for start, end in sorted(meetings):
            # like in a simulation processing meetings i-th is like to say now we are at time start
            # so we can free the room in which there is a meeting that end before
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heapq.heappop(used_rooms)
                heapq.heappush(unused_rooms, room)
            if unused_rooms: # if there free rooms use the one with lowest index
                room = heapq.heappop(unused_rooms)
                heapq.heappush(used_rooms, [end,room])
            else:
                # if there are no free rooms check the room 
                meeting_end_room, room = heapq.heappop(used_rooms)
                heapq.heappush(used_rooms, [meeting_end_room + end - start, room])
            meeting_counter[room] += 1
            max_ = max(max_, meeting_counter[room])
        return meeting_counter.index(max_)
        