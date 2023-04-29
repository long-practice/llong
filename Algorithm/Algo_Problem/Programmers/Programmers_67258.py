def solution(gems):
    answer = (1, len(gems))

    unique_count = len(set(gems))
    gem_dict = {}
    curr_gems = set()

    left, right = 0, 0
    while right <= len(gems):
        while len(curr_gems) == unique_count:
            answer = min(answer, (left + 1, right), key=lambda x: x[1] - x[0])
            gem_dict[gems[left]] -= 1
            if not gem_dict[gems[left]]:
                curr_gems.remove(gems[left])
            left += 1

        try:
            gem_dict[gems[right]] = gem_dict.get(gems[right], 0)
            if not gem_dict[gems[right]]:
                curr_gems.add(gems[right])
            gem_dict[gems[right]] += 1
            right += 1
        except IndexError:
            break

    return answer