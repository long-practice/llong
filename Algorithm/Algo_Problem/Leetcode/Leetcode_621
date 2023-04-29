class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count, cool_q = {}, collections.deque(['idle' for _ in range(n)])
        total_task = 0
        for t in tasks:
            task_count[t] = task_count.get(t, 0) + 1
            total_task += 1

        h1 = []
        for task, count in task_count.items():
            heapq.heappush(h1, (-count, task))

        time = 0
        while total_task:
            if h1:
                c, t = heapq.heappop(h1)
                total_task -= 1
                cool_q.append((c + 1, t))
            else:
                cool_q.append('idle')

            e = cool_q.popleft()
            if e != 'idle' and e[0]:
                heapq.heappush(h1, e)
            time += 1

        return time