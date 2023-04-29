class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks).values()
        max_task = max(task_count)
        max_count = sum(1 for c in task_count if c == max_task)
        return max((n + 1) * (max_task - 1) + max_count, len(tasks))