def minmeetingrooms(intervals):
    intervals.sort(key = lambda x: x.start)
    endtime = []
    count = 1
    for i in intervals:
        if endtime and i.start >=endtime[0]:
            heapq.heappop(endtime)
            heapq.heappush(i.end)
        else:
            count+=1
            heapq.heappush(i.end)
    return count
