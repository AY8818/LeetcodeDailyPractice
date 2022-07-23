# 657. Robot Return to Origin
def judgeCircle(moves):
    return moves.count('U') - moves.count('D') == 0 and moves.count('L') - moves.count('R') == 0


moves = "UD"

print(judgeCircle(moves))
