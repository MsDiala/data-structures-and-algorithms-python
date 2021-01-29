def bfs(start, goal, dictionary):
    """
    #######################################
    #       Breadth-first Search BFS      #
    #            Data Structure           #
    #              Coded By.              #
    #             Ashraf Amer             #
    #            Jan,14 2020              #
    #            AI workshop              #
    #######################################
    """
    
    openNode = [(start,[start])]
    closed = []
    solutions = []

    while openNode != []:
        (node,path) = openNode.pop(0)

        if node == goal:
            solutions.append(path)

        allChilds = dictionary[node]

        if node not in closed:
            closed.append(node)

        testPath = []
        selectedPath = []

        for i in allChilds:
            testPath = path + [i]
            if len(testPath) == len(set(testPath)):
                selectedPath.append((i,testPath))

        openNode = selectedPath + openNode

    return solutions


def closedDfs(start, goal, dictionary):
    openNode = [(start,[start])]
    closed = []
    solutions = []

    while openNode != []:

        if openNode != []:
            (node,path) = openNode.pop(0)

        if node == goal:
            solutions.append(path)

        allChilds = dictionary[node]

        if node not in closed:
            closed.append(node)

            testPath = []
            selectedPath = []

            for i in allChilds:
                testPath = path + [i]
                if len(testPath) == len(set(testPath)):
                    selectedPath.append((i,testPath))

            openNode = openNode + selectedPath

    return solutions


if __name__ == "__main__":

    graph = {
        'A' : ['B', 'C'],
        'B' : ['A', 'G', 'D'],
        'C' : ['A', 'D', 'F'],
        'D' : ['C', 'B', 'E'],
        'E' : ['D', 'F', 'K'],
        'F' : ['C', 'E', 'G'],
        'G' : ['B', 'F', 'H'],
        'H' : ['G', 'K', 'M'],
        'K' : ['H', 'E', 'M'],
        'M' : ['H', 'K']
        }


    bfsAM = bfs('A', 'M', graph)
    print ("BFS Paths: [A -> M] ==>", bfsAM, "\n length:" ,len(bfsAM), "\n")
