from helpers import load_map
from shortest_path import shortest_path


MAP_40_ANSWERS = [
    (8, 24, [8, 14, 16, 37, 12, 31, 10, 24])
]


def test(shortest_path_function):
    map_40 = load_map('map-40.pickle')
    correct = 0
    for start, goal, answer_path in MAP_40_ANSWERS:
        path = shortest_path_function(map_40, start, goal)
        if path == answer_path:
            correct += 1
        else:
            print("For start:", start, 
                  "Goal:     ", goal,
                  "Your path:", path,
                  "Correct:  ", answer_path)
    if correct == len(MAP_40_ANSWERS):
        print("All tests pass! Congratulations!")
    else:
        print("You passed", correct, "/", len(MAP_40_ANSWERS), "test cases")
    

if __name__ == "__main__":
    test(shortest_path)


