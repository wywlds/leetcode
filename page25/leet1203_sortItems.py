from typing import List


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        groups = [[] for _ in range(m)]
        group_dic = {}
        for i, g in enumerate(group):
            if g > -1:
                groups[g].append(i)
                group_dic[i] = g
            else:
                groups.append([i])
                group_dic[i] = len(groups) - 1

        group_external_input_edges = [0 for _ in range(len(groups))]
        group_external_output_edges = [set() for _ in range(len(groups))]
        item_internal_input_edges = [0 for _ in range(n)]
        item_internal_output_edges = [[] for _ in range(n)]
        for i, beforeItem in enumerate(beforeItems):
            group_i = group_dic[i]
            for j in beforeItem:
                group_j = group_dic[j]
                if group_i == group_j:
                    item_internal_input_edges[i] += 1
                    item_internal_output_edges[j].append(i)
                else:
                    if group_i not in group_external_output_edges[group_j]:
                        group_external_input_edges[group_i] += 1
                        group_external_output_edges[group_j].add(group_i)
        def unzip(g):
            group_items = groups[g]
            if len(group_items) == 0:
                return []
            ans = []
            zero_input_items = [i for i in group_items if item_internal_input_edges[i] == 0]
            while len(zero_input_items) != 0:
                cur_item = zero_input_items.pop(0)
                ans.append(cur_item)
                for next_item in item_internal_output_edges[cur_item]:
                    item_internal_input_edges[next_item] -= 1
                    if item_internal_input_edges[next_item] == 0:
                        zero_input_items.append(next_item)
            return None if len(ans) != len(group_items) else ans

        ans = []
        zero_input_groups = [i for i in range(len(groups)) if group_external_input_edges[i] == 0]
        while len(zero_input_groups) != 0:
            cur_group = zero_input_groups.pop(0)
            group_list = unzip(cur_group)
            if group_list is None:
                return []
            ans.extend(group_list)
            for next_group in group_external_output_edges[cur_group]:
                group_external_input_edges[next_group] -= 1
                if group_external_input_edges[next_group] == 0:
                    zero_input_groups.append(next_group)
        return [] if len(ans) != n else ans


if __name__=="__main__":
    n = 8
    m = 2
    group = [-1,-1,1,0,0,1,0,-1]
    beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
    solution = Solution()
    print(solution.sortItems(n, m, group, beforeItems))
