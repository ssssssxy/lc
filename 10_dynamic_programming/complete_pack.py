def complete_pack_1(weight, value, bag_weight):
    dp = [0] * (bag_weight + 1)
    for i in range(len(value)):
        for j in range(weight[i], bag_weight+1):
            dp[j] = max(dp[j], dp[j-weight[i]]+value[i])
    return dp[-1]


print(complete_pack_1(weight = [1, 3, 4], value = [15, 20, 30], bag_weight = 4))
