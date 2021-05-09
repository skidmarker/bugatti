N, R = map(int, input().split())
all_cities = input().split()

M = int(input())
trip_cities = input().split()

K = int(input())
trans_data = [input().split() for _ in range(K)]

keys = {key: val for val, key in enumerate(all_cities)}
distance = [[float("inf")] * N for i in range(N)]
naeilro = [[float("inf")] * N for i in range(N)]
for i in range(N):
    distance[i][i] = 0
    naeilro[i][i] = 0

for t, s, e, c in trans_data:
    c = int(c)
    distance[keys[s]][keys[e]] = min(c, distance[keys[s]][keys[e]])
    distance[keys[e]][keys[s]] = min(c, distance[keys[e]][keys[s]])
    if t in ["Mugunghwa", "ITX-Saemaeul", "ITX-Cheongchun"]:
        naeilro[keys[s]][keys[e]], naeilro[keys[e]][keys[s]] = 0, 0
    elif t in ["S-Train", "V-Train"]:
        cost = c * 0.5
        naeilro[keys[s]][keys[e]] = min(cost, naeilro[keys[s]][keys[e]])
        naeilro[keys[e]][keys[s]] = min(cost, naeilro[keys[e]][keys[s]])
    else:
        naeilro[keys[s]][keys[e]] = min(c, naeilro[keys[s]][keys[e]])
        naeilro[keys[e]][keys[s]] = min(c, naeilro[keys[e]][keys[s]])

# k는 거쳐갈 점
# i는 시작점 j는 도착점
for k in range(N):
    for i in range(N):
        for j in range(N):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
            naeilro[i][j] = min(naeilro[i][j], naeilro[i][k] + naeilro[k][j])

total, total_naeilro = 0, 0
for i in range(len(trip_cities) - 1):
    s, e = trip_cities[i], trip_cities[i + 1]
    total += distance[keys[s]][keys[e]]
    total_naeilro += naeilro[keys[s]][keys[e]]

result = "Yes" if total > total_naeilro + R else "No"
print(result)
