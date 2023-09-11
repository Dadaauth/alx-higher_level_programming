#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = ""
    prev = 0
    if not a_dictionary:
        return
    for key in a_dictionary:
        score = a_dictionary[key]
        if score > prev:
            best_key = key
            prev = score
    return best_key


# a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
# best_key = best_score(a_dictionary)
# print("Best score: {}".format(best_key))

# best_key = best_score(None)
# print("Best score: {}".format(best_key))
