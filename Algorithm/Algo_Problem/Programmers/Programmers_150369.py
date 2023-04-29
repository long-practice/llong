def solution(cap, n, deliveries, pickups):
    answer = 0

    deliveries_ls = [(i, d) for i, d in enumerate(deliveries, start=1) if d]
    pickups_ls = [(i, p) for i, p in enumerate(pickups, start=1) if p]

    while deliveries_ls or pickups_ls:
        p = d = 0
        can_deliveries = cap
        while deliveries_ls and can_deliveries:
            d_, count = deliveries_ls.pop()
            can_deliveries -= count
            d = max(d, d_)
            if can_deliveries < 0:
                deliveries_ls.append((d_, -can_deliveries))
                can_deliveries = 0

        can_pickups = cap
        while pickups_ls and can_pickups:
            p_, count = pickups_ls.pop()
            p = max(p, p_)
            can_pickups -= count
            if can_pickups < 0:
                pickups_ls.append((p_, -can_pickups))
                can_pickups = 0

        answer += max(d, p) * 2

    return answer