class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


def seek_goal(map_data, start, goal):
    """
    Algorithm seekGoal

    Determines the path to a desired goal.

    Pre:
        map_data contains the path information.

    Post:
        The path to the goal is printed.
    """

    # Create stack
    stack = Stack()

    # Set current point to starting point
    current = start

    goal_not_found = True

    # Loop while current point exists
    # and goal has not been found
    while current is not None and goal_not_found:

        # If current point is the goal
        if current == goal:

            goal_not_found = False

        else:

            # Push current point onto stack
            stack.push(current)

            # Get next point
            if current in map_data and len(map_data[current]) > 0:

                # Check for branch points
                branch_points = map_data[current]

                # Push branch points onto stack
                for branch_point in branch_points[1:]:
                    stack.push(branch_point)

                # Advance to next node
                current = branch_points[0]

            else:

                current = None

    # Check whether path was found
    if stack.is_empty() and goal_not_found:

        print("There is no path to your goal.")

    else:

        print("The path to your goal is:")

        # Pop stack and print path
        while not stack.is_empty():

            point = stack.pop()

            print(point)

        print("End of Path")


def main():

    # Example map
    map_data = {
        "A": ["B"],
        "B": ["C"],
        "C": ["D"],
        "D": ["E"],
        "E": []
    }

    start = "A"
    goal = "E"

    print("Goal Seeking Algorithm")
    print("----------------------")

    seek_goal(map_data, start, goal)


if __name__ == "__main__":
    main()