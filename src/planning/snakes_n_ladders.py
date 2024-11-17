import os
import numpy as np


def run_simulation(dice_probs, ladder_spots, snake_spots, num_sims=1):
    if not isinstance(dice_probs, np.ndarray):
        dice_probs = np.array(dice_probs)
    if not np.isclose(dice_probs.sum(), 1):
        dice_probs = dice_probs / np.sqrt((dice_probs**2).sum())
    dice_values = np.arange(len(dice_probs)) + 1
    if not isinstance(ladder_spots, np.ndarray):
        ladder_spots = np.array(ladder_spots)
    if not isinstance(snake_spots, np.ndarray):
        snake_spots = np.array(snake_spots)

    players = np.ones((num_sims, 1))
    # if len(ladder_spots) > 0:
    #     import pdb; pdb.set_trace()
    ladder_starts = np.tile(ladder_spots.reshape(-1, 2)[:, 0].reshape(1, -1), (num_sims, 1))
    ladder_ends = np.tile(ladder_spots.reshape(-1, 2)[:, 1].reshape(1, -1), (num_sims, 1))
    snake_starts = np.tile(snake_spots.reshape(-1, 2)[:, 0].reshape(1, -1), (num_sims, 1))
    snake_ends = np.tile(snake_spots.reshape(-1, 2)[:, 1].reshape(1, -1), (num_sims, 1))
    assert ladder_starts.shape[1] == ladder_spots.shape[0]

    turns = np.zeros(num_sims)

    while not np.all(players == 100):
        turns[players.reshape(-1) < 100] += 1
        roll = np.random.choice(dice_values, size=players.shape, p=dice_probs)
        new_loc = players + roll
        roll_idx = new_loc <= 100
        players[roll_idx] = new_loc[roll_idx]
        if ladder_starts.shape[1] > 0:
            ladder_idx = players == ladder_starts
            players[ladder_idx.any(-1)] = ladder_ends[ladder_idx].reshape(-1, 1)
        if snake_starts.shape[1] > 0:
            snake_idx = players == snake_starts
            players[snake_idx.any(-1)] = snake_ends[snake_idx].reshape(-1, 1)
        # if (turns >= 1000).any():
        #     import pdb; pdb.set_trace()
    return turns.mean().round(0)


def run_test(dice_probs, ladder_spots, snake_spots, turn_target):
    
    turn_est = run_simulation(dice_probs, ladder_spots, snake_spots, 5000)
    print('est, target:', turn_est, turn_target)

    return np.sqrt((turn_est - turn_target)**2)


def test_parser(tests):
    num_tests = len(tests)
    parsed_tests = []
    for ti in range(num_tests):
        dice_probs = [float(val) for val in tests[ti].strip().split(',')]
        num_ladders, num_snakes = [int(val) for val in tests[ti].strip().split(',')]
        ladder_spots = [[float(val) for val in pair.strip().split(',')] for pair in tests[ti].strip().split(' ')]
        snake_spots = [[float(val) for val in pair.strip().split(',')] for pair in tests[ti].strip().split(' ')]
        assert len(ladder_spots) == num_ladders
        assert len(snake_spots) == num_snakes
        
        parsed_tests.append({
            'dice_probs': dice_probs,
            'ladder_spots': ladder_spots,
            'snake_spots': snake_spots,
        })

    return parsed_tests


def main():

    if False:
        num_tests = int(input().strip())

        tests = []

        for ti in range(num_tests):
            new_test = []
            new_test.append(input())
            new_test.append(input())
            new_test.append(input())
            new_test.append(input())
            tests.append(new_test)

        tests = test_parser(tests)
    else:
        tests = [
            {
                'dice_probs': [1, 0, 0, 0, 0, 0],
                'ladder_spots': [],
                'snake_spots': [],
                'turn_target': 100,
            },
            {
                'dice_probs': [0.1, 0, 0, 0.1, 0.8, 0],
                'ladder_spots': [],
                'snake_spots': [],
                'turn_target': 20,
            },
            {
                'dice_probs': [0.25, 0.25, 0.25, 0.25, 0., 0.],
                'ladder_spots': [],
                'snake_spots': [],
                'turn_target': 40,
            },
            {
                'dice_probs': [0.32, 0.32, 0.12, 0.04, 0.07, 0.13],
                'ladder_spots': [[32, 62], [42, 68], [12, 98]],
                'snake_spots': [
                    [95, 13], [97, 25], [93, 37], [79, 27], [75, 19], [49, 47], [67, 17]
                ],
                'turn_target': 160,
            },
            {
                'dice_probs': [0.39, 0.05, 0.14, 0.05, 0.12, 0.25],
                'ladder_spots': [[32, 62], [44, 66], [22, 58], [34, 60], [2, 90]],
                'snake_spots': [
                    [85, 7], [63, 31], [87, 13], [75, 11], [89, 33], [57, 5], [71, 15], [55, 25]
                ],
                'turn_target': 95,
            },
            {
                'dice_probs': [0.54, 0.02, 0.02, 0.01, 0.3, 0.11],
                'ladder_spots': [[8, 52], [6, 80], [26 ,42], [2, 72]],
                'snake_spots': [
                    [51, 19], [39, 11], [37, 29], [81, 3], [59, 5], [79, 23], [53, 7], [43, 33], [77, 21]
                ],
                'turn_target': 162,
            },
        ]

    for test in tests:
        result = run_test(**test)
        print(str(result))


if __name__ == '__main__':
    main()
