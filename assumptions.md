## Assumptions and thought process for elevator challenge

The first attempt for this challenge was completed on a Jupyter notebook with the individual processes being separated out. The first process to be nailed down was extracting the difference between floors. This was accomplished by utilizing the `diff()` function of the `numpy` libraray, which returned a list object of the integer difference between each desired floor.
```
import numpy
nums = [2,9,1,32]
v = numpy.diff(nums)
```

After the process for finding the difference between floors had been established, the next step was two-fold, wherein the starting floor needed to be added to the list of floors being visited and the difference between floors needing to be changed to absolute values. The addition of the starting floor was accomplished by utilizing the built in `insert()` function to add the starting floor to the beginning of the provided list. The absolute values were similarily obtained by running the built in `abs()` function on the newly modified list.
```
starting = 12
nums.insert(0, starting)
abs_value = abs(nums)
```

Once the list of floors had been fully transformed to include the starting floor and the absolute value between each floor, the next process was to determine how long it would take the elevator to travel the full amount of floors given. This was accomplished using simple multiplication and list comprehension on the list of floors against the time constant. The return of this multiplication gave a list of the time intervals that would happen between each desired floor. The total time was then determined by utilizing the `sum()` function on this list.
```
time = 10
math = [i*time for i in abs_value]
total_time = sum(math)
```

After determining each process was working as intended, joining them all into a function was a simple matter of organizing the processes and getting rid of redunancies.
```
def elevator(starting_floor, floors_visited):
    time = 10
    floors_visited.insert(0, starting_floor)
    floors = abs(numpy.diff(floors_visited))
    travel_time = [i*time for i in floors]
    total_time = sum(travel_time)
    return total_time, floors_visited
```

From here, the notebook was returning the desired outputs, and it was time to harden the function. The function was moved over to a scratch file in PyCharm for further testing and addtions. The first step taken was to add a docstring to the function for ease of use. The second update was a simple string modifier to return a message including the desired data so that the return was easier to read and decipher what each variable or variables represent. The final step in hardening was to sanitize the inputs for the function so that other variable types could be entered without breaking the functionality. This was accomplished by type comparison and try and except logic to alter the inputs to the desired object type.
```
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
```

The `main` function houses the varriables given in the example, but these can be changed out for further testing as deemed necessary.
```
if __name__ == '__main__':
    starting_floor_main = 12
    floors_visited_main = [2, 9, 1, 32]
    print(elevator(starting_floor_main, floors_visited_main))
```

No additional features were tried and left out. There was some testing and renaming of variables done on the function, but no additional functionality that isn't already in the function was attempted/given up.
