from typing import List



def list_avg(sequence: List) -> float:  # This will tell python that sequence should be a list
                                        # and should return a float
    return sum(sequence) / len(sequence)


# This is useful to tell you if you are passing the wrong thing

print(list_avg((1, 2, 3, 4)))
