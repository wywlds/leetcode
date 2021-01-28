from typing import List
# n = 2
# logs =
# ["0:start:0",
#  "1:start:2",
#  "1:end:5",
#  "0:end:6"]

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        times = [0] * n
        s = []
        for log in logs:
            items = log.split(":")
            func_id = int(items[0])
            type = items[1]
            time_pos = int(items[2])
            if type == 'start':
                s.append((func_id, time_pos))
            else:
                inner_inclusive_time = 0
                poped = s.pop()
                if isinstance(poped, int):
                    inner_inclusive_time += poped
                    poped = s.pop()
                _, pos = poped
                inclusive_time = time_pos - pos + 1
                exclusive_time = inclusive_time - inner_inclusive_time
                times[func_id] += exclusive_time
                if s and isinstance(s[-1], int):
                    last_inclusive_time = s.pop()
                    s.append(last_inclusive_time + inclusive_time)
                else:
                    s.append(inclusive_time)
        return times

if __name__=="__main__":
    solution = Solution()
    result=solution.exclusiveTime(2, ["0:start:0","1:start:3","1:start:4","1:end:5","1:end:6","1:start:9","1:end:10"," \
                                                                                                           ""0:end:12"])
    print(result)
