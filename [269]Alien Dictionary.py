class Node(object):
    def __init__(self):
        self.IN = set()
        self.OUT = set()


class Solution(object):
    def alienOrder(self, words):
        allnodes, graph, res = set("".join(words)), {}, ""

        for i in allnodes:
            graph[i] = Node()

        for i in range(len(words)-1):
            for j in zip(words[i], words[i+1]):
                if j[0] != j[1]:
                    graph[j[0]].OUT.add(j[1])
                    graph[j[1]].IN.add(j[0])
                    break

        while allnodes:
            buff = set(
                [i for i in allnodes if graph[i].OUT and not graph[i].IN])
            if not buff:
                return (res + "".join(allnodes)) if not [i for i in allnodes if graph[
                    i].IN] else ""
            res += "".join(buff)
            allnodes -= buff
            for i in allnodes:
                graph[i].IN -= buff
        return res
