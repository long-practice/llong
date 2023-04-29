def solution(nodeinfo):
    answer = []

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)
    nodeinfo.sort()
    nodey = [y for _, y, _ in nodeinfo]
    preorder, postorder = [], []

    def order(nodeinfoseg, nodeyseg):
        if len(nodeyseg) == 1:
            preorder.append(nodeinfoseg[0][2])
            postorder.append(nodeinfoseg[0][2])
            return

        if nodeyseg:
            mid = nodeyseg.index(max(nodeyseg))
            preorder.append(nodeinfoseg[mid][2])
            order(nodeinfoseg[:mid], nodeyseg[:mid])
            order(nodeinfoseg[mid + 1:], nodeyseg[mid + 1:])
            postorder.append(nodeinfoseg[mid][2])

    order(nodeinfo, nodey)
    answer.append(preorder)
    answer.append(postorder)
    return answer