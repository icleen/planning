import os
import numpy as np


def run_simulation(dice_probs, ladder_spots, snake_spots, num_sims=1):
    if not np.isarray(dice_probs):
        dice_probs = np.array(dice_probs)
    dice_values = np.arange(len(dice_probs)) + 1
    if not np.isarray(ladder_spots):
        ladder_spots = np.array(ladder_spots)
    if not np.isarray(snake_spots):
        snake_spots = np.array(snake_spots)

    players = np.ones((num_sims, 1))
    ladder_starts = ladder_spots[:, 0].reshape(1, -1).repeat(num_sims)
    ladder_ends = ladder_spots[:, 0].reshape(1, -1).repeat(num_sims)
    snake_starts = snake_spots[:, 0].reshape(1, -1).repeat(num_sims)
    snake_ends = snake_spots[:, 0].reshape(1, -1).repeat(num_sims)

    turns = np.zeros(num_sims)

    while not np.all(players == 100):
        roll = np.random.choice(dice_values, size=players.shape, p=dice_probs)
        new_loc = players + roll
        roll_idx = new_loc <= 100
        players[roll_idx] = new_loc[roll_idx]
        ladder_idx = players == ladder_starts
        players[ladder_idx.any(-1)] = ladder_ends[ladder_idx]
        snake_idx = players == snake_starts
        players[snake_idx.any(-1)] = snake_ends[snake_idx]
        turns[players < 100] += 1
        if (turns >= 1000).any():
            import pdb; pdb.set_trace()
    return


def run_test(dice_probs, ladder_spots, snake_spots):
    pass


def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_tests = int(input().strip())

    tests = []

    for ti in range(num_tests):
        dice_probs = [float(val) for val in input().strip().split(',')]
        num_ladders, num_snakes = [int(val) for val in input().strip().split(',')]
        ladder_spots = [[float(val) for val in pair.strip().split(',')] for pair in input().strip().split(' ')]
        snake_spots = [[float(val) for val in pair.strip().split(',')] for pair in input().strip().split(' ')]
        assert len(ladder_spots) == num_ladders
        assert len(snake_spots) == num_snakes
        
        tests.append({
            'dice_probs': dice_probs,
            'ladder_spots': ladder_spots,
            'snake_spots': snake_spots,
        })

    for test in tests:
        result = run_test(**test)

        fptr.write(str(result) + '\n')

    fptr.close()


if __name__ == '__main__':
    main()
