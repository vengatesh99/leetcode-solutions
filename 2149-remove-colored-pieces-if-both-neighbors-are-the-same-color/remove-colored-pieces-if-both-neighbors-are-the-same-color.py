class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice,bob = 0,0
        prev = colors[0]
        c = 1
        for i in range(1,len(colors)):
            if prev == colors[i]:
                c+=1
            else:
                if prev == "A":
                    alice+=max(0,c-2)
                else:
                    bob+=max(0,c-2)
                c = 1
            prev = colors[i]
        if colors[-1] == "A":
            alice+=max(0,c-2)
        else:
            bob+=max(0,c-2)
        print(alice,bob)
        return True if alice>bob else False

