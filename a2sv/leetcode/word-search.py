class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        my_set = set()

        def find(x, y, i):
            if i == len(word):
                return True

            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                return False

            if board[x][y] != word[i] or (x, y) in my_set:
                return False

            my_set.add((x, y))

            result = (
                find(x - 1, y, i + 1)
                or find(x + 1, y, i + 1)
                or find(x, y - 1, i + 1)
                or find(x, y + 1, i + 1)
            )

            my_set.remove((x, y))

            return result

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    my_set.clear()
                    if find(x, y, 0):
                        return True

        return False