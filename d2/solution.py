ROCK = 1
PAPER = 2
SCISSORS = 3
LOSE = 0
DRAW = 3
WIN = 6

def parse(data):
    f = open(data).read()
    return [line.split(' ') for line in f.splitlines()]

def part1(data):
    key = {'A': ROCK, 'B': PAPER, 'C': SCISSORS, 'X': ROCK, 'Y': PAPER, 'Z': SCISSORS}
    score = 0
    for opp, me in data:
        opp_move, my_move = key[opp], key[me]
        score += my_move
        if opp_move == my_move:
            score += DRAW
        elif (opp_move == ROCK and my_move == PAPER) or (opp_move == PAPER and my_move == SCISSORS) or (opp_move == SCISSORS and my_move == ROCK):
            score += WIN
    return score

def part2(data):
    moves = {'A': ROCK, 'B': PAPER, 'C': SCISSORS}
    outcomes = {'X': LOSE, 'Y': DRAW, 'Z': WIN}
    score = 0
    for opp, outcome in data:
        opp_move, outcome = moves[opp], outcomes[outcome]
        score += outcome
        if outcome == DRAW:
            score += opp_move
        elif outcome == WIN:
            if opp_move == ROCK:
                score += PAPER
            elif opp_move == SCISSORS:
                score += ROCK
            else: 
                score += SCISSORS
        else:
            if opp_move == ROCK:
                score += SCISSORS
            elif opp_move == SCISSORS:
                score += PAPER
            else: 
                score += ROCK
    return score
data = parse('input')
print(part1(data))
print(part2(data))
