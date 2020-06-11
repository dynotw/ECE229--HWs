def get_prob(seq, dic):
    n = len(seq)
    prob = 1
    dp = [False] * (n + 1)
    dp[0] = True
    pro_list = [1] * (n + 1)
    for i in range(n):
        for j in range(i + 1, n + 1):
            if (dp[i] and (seq[i:j] in dic)):
                dp[j] = True
                if pro_list[j] == 1:
                    pro_list[j] = pro_list[i] * dic[seq[i:j]]
                else:
                    pro_list[j] = max(pro_list[j], pro_list[i] * dic[seq[i:j]])

    return pro_list[-1] if pro_list[-1] != 1 else 0