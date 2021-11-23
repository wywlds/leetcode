class Node():
    def __init__(self, name):
        self.name = name
        self.children = []

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = Node(kingName)
        self.index = {kingName: self.root}
        self.death_set = {""}

    def birth(self, parentName: str, childName: str) -> None:
        new_node = Node(childName)
        self.index[parentName].children.append(new_node)
        self.index[childName] = new_node

    def death(self, name: str) -> None:
        self.death_set.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        def dfs(n):
            if n.name not in self.death_set:
                ans.append(n.name)
            for c in n.children:
                dfs(c)
        dfs(self.root)
        return ans