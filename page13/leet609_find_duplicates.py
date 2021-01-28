# ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        value_dict = {}
        for file_info in paths:
            items =file_info.split(" ")
            parent = items[0]
            for file_detail_info in items[1:]:
                detail_items = file_detail_info.split("(")

                file_name = detail_items[0]
                content = detail_items[1].split(")")[0]
                if content in value_dict:
                    value_dict[content].append(parent + "/" + file_name)
                else:
                    value_dict[content] = [parent + "/" + file_name]
        return [file_list for file_list in value_dict.values() if len(file_list) > 1]