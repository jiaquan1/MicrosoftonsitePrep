
class Solution:
    def employfreetime(self,schedule):
        schedule.sort(key = lambda x:x[0])
        busytime = []
        freetime = []
        if not schedule:
            return []
        busytime.append(schedule[0])
        for item in schedule[1:]:
            if item[0]>busytime[-1][1]:
                freetime.append([busytime[-1][1],item[0]])
                busytime.append(item)
            else:
                busytime[-1][1]=max(busytime[-1][1],item[1])
        return freetime

b= Solution()
schedule = [[1,2],[5,6],[1,3],[4,10]]
print(b.employfreetime(schedule))
schedule = [[1,3],[6,7],[2,4],[2,5],[9,12]]
print(b.employfreetime(schedule))




