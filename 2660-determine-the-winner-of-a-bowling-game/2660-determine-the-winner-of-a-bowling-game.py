class Solution(object):
    def isWinner(self, player1, player2):
        sum1 = 0
        sum2 = 0

        for i in range(len(player1)):
            if (i > 0 and player1[i - 1] == 10) or (i > 1 and player1[i - 2] == 10):
                sum1 += 2 * player1[i]
            else:
                sum1 += player1[i]

        for i in range(len(player2)):
            if (i > 0 and player2[i - 1] == 10) or (i > 1 and player2[i - 2] == 10):
                sum2 += 2 * player2[i]
            else:
                sum2 += player2[i]

        if sum1 > sum2:
            return 1
        elif sum2 > sum1:
            return 2
        else:
            return 0