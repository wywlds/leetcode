from typing import List
import collections
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ans = []
        email_to_index_dict = {}
        index_to_email_dict = {}
        email_to_name_dict = {}
        count = 0
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email_to_index_dict:
                    email_to_index_dict[email] = count
                    index_to_email_dict[count] = email
                    email_to_name_dict[email] = name
                    count += 1

        parents = [-1] * count
        def find(x):
            if parents[x] < 0:
                return x
            parents[x] = find(parents[x])
            return parents[x]
        def union(x, y):
            parent_x = find(x)
            parent_y = find(y)
            if parent_x != parent_y:
                parents[parent_y] = parent_x

        for account in accounts:
            email_0 = account[1]
            for email_1 in account[2:]:
                union(email_to_index_dict[email_0], email_to_index_dict[email_1])

        set_dic = collections.defaultdict(list)
        for i, email in index_to_email_dict.items():
            parent = find(i)
            set_dic[index_to_email_dict[parent]].append(email)
        for parent_email, emails in set_dic.items():
            ans.append([email_to_name_dict[parent_email]] + sorted(emails))
        return ans