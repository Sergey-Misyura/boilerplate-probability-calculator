import copy
import random
from collections import Counter     # for counting drawn balls
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        if not kwargs:
            self.contents = ['blue']    # if empty add 1 blue ball
        else:
            for color, num in kwargs.items():
                self.contents.extend([color for _ in range(num)])

    def draw(self, cnt):    # draw a balls
        self.selected = []  # list of selected balls
        if cnt < len(self.contents):
            for _ in range(cnt):
                self.selected.append(self.contents.pop(random.randrange(len(self.contents))))
        else:
            self.selected, self.contents = self.contents, []
        return self.selected


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    nums_success = 0    # number of successful
    for i in range(num_experiments):
        hat_exp = copy.deepcopy(hat)    # deepcopy of primary hat
        hat_exp.draw(num_balls_drawn)

        # result check
        if set(expected_balls.keys()) <= set(dict(Counter(hat_exp.selected)).keys()):
            for ball, nums in expected_balls.items():
                if nums > dict(Counter(hat_exp.selected))[ball]:
                    break
            else:
                nums_success += 1
    return (nums_success, nums_success/num_experiments)
