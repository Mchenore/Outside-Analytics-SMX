import numpy


def elevator(starting_floor: int, floors_visited: list):
    """
    Calculate the time it takes an elevator to travel a given number of floors given a constant
    time variable
    Args:
        starting_floor (int) = Starting floor number
        floors_visited (list) = Floors to be visited
    Returns:
        String message listing the total travel time and floors visited
    """

    if type(starting_floor) == list:
        try:
            starting_floor = [int(i) for i in starting_floor][0]
        except ValueError:
            pass
    if type(starting_floor) != int:
        try:
            starting_floor = int(starting_floor)
        except ValueError:
            pass
    if type(floors_visited) != list:
        try:
            floors_visited = [int(i) for i in floors_visited]
        except ValueError:
            pass
    if type(floors_visited) == str:
        try:
            floors_visited = [int(i) for i in floors_visited.split(",")]
        except ValueError:
            pass
    else:
        for floor in floors_visited:
            if type(floor) != int:
                floors_visited = [int(i) for i in floors_visited]
    int_time = 10
    floors_visited.insert(0, starting_floor)
    floors = abs(numpy.diff(floors_visited))
    travel_time = sum([i*int_time for i in floors])
    return (f"The elevator took a time of {travel_time} to visit the following floors: "
            f"{floors_visited}")


if __name__ == '__main__':
    starting_floor_main = 12
    floors_visited_main = [2, 9, 1, 32]
    print(elevator(starting_floor_main, floors_visited_main))
