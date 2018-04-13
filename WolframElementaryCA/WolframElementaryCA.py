import copy
import matplotlib.pyplot as plt
import numpy as np

space = 128

state = []
for s1 in range(space):
    state.append(0)
state.append(1)
for s2 in range(space):
    state.append(0)

# state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

rule_set_binary = [0, 0, 0, 1, 1, 1, 1, 0]

iterations = int(len(state)/2)

basic_rules = [[1, 1, 1],
               [1, 1, 0],
               [1, 0, 1],
               [1, 0, 0],
               [0, 1, 1],
               [0, 1, 0],
               [0, 0, 1],
               [0, 0, 0]]


def lookup_neighbors(old_state, position):

    # Determine length of basic rules.
    neighbors = len(basic_rules[0])

    # Look up the neighbors from the previous state, based on basic rule
    # length.
    neighborhood = []
    for neighbor in range(neighbors):
        prev_pos = (neighbor - 1) + position
        # Take the first value if position value exceeds the list length.
        if prev_pos >= len(old_state):
            prev_pos = 0

        # Create neighborhood from previous state.
        # print(prev_pos)
        # print("Previous position: {}".format(prev_pos))
        neighborhood.append(old_state[prev_pos])

    return neighborhood

    #     # Fill positions of new state based on neighborhood of previous state.
    #     for br in range(len(basic_rules)):
    #         if basic_rules[br] is neighborhood:
    #             new_state.append(rule_set[br])
    #
    # return new_state


def advance_state(start_state, iterations, rule_set):

    state_collection = []
    state_collection.append(copy.deepcopy(start_state))

    # Iterate the state for the specified number of steps.
    for step in range(iterations):
        # print("* Step: {}".format(step))
        # print("------")

        # Look at the positions of the new state.
        new_state = []
        for new_position in range(len(start_state)):
            # print("Position: {}".format(new_position))
            # print("Previous state: {}".format(state_collection[-1]))

            neighborhood = lookup_neighbors(state_collection[-1], new_position)
            # print("Neighborhood: {}".format(neighborhood))

            for br in range(len(basic_rules)):
                # print("Basic rule: {}".format(basic_rules[br]))
                if basic_rules[br] == neighborhood:
                    new_state.append(rule_set[br])
                    # print("*TRUE*")
                # else:
                    # print("False")

        # print("New state: {}".format(new_state))
        state_collection.append(new_state)

    return state_collection


states = advance_state(state, iterations, rule_set_binary)

# for i in states:
#     print(i)


# data = np.random.random(size=(6, 6))

data = np.array(states)
plt.imshow(data, interpolation='nearest', cmap='binary')

plt.show()
