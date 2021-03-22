def solution(bridge_length, weight, truck_weights):
    answer = 1
    moving, pos = [truck_weights.pop(0)], [1]
    cur = sum(moving)
    while len(moving) > 0:
        answer += 1
        pos = [v + 1 for v in pos]

        if pos[0] > bridge_length:
            pos.pop(0)
            cur -= moving.pop(0)

        if len(truck_weights) > 0 and cur + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            moving.append(truck)
            pos.append(1)
            cur += truck

    return answer