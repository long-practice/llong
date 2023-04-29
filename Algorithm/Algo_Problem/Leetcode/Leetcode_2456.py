class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        creator_idx, i = {}, 0
        for creator in creators:
            if creator not in creator_idx:
                creator_idx[creator] = i
                i += 1
        inv_creator_idx = {v: k for k, v in creator_idx.items()}

        total_views = [0 for _ in range(len(creator_idx))]
        total_create = [[] for _ in range(len(creator_idx))]

        for creator, id_, view in zip(creators, ids, views):
            idx = creator_idx[creator]
            total_views[idx] += view
            heapq.heappush(total_create[idx], (-view, id_))

        max_view = max(total_views)
        max_idx = [i for i in range(len(total_views)) if total_views[i] == max_view]

        answer = []
        for M_idx in max_idx:
            who, what = inv_creator_idx[M_idx], total_create[M_idx][0][1]
            answer.append((who, what))
        return answer