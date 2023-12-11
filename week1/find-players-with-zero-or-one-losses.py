from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = {}
        losses = {}

        for winner, loser in matches:
            wins[winner] = wins.get(winner, 0) + 1
            losses[loser] = losses.get(loser, 0) + 1

        no_loss = [player for player in wins if player not in losses]
        one_loss = [player for player in losses if losses[player] == 1]

        return [sorted(no_loss), sorted(one_loss)]