#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    r_numerals = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
    }
    r_list = list(reversed(roman_string))
    prev = 0
    final = 0
    for letter in r_list:
        if letter in r_numerals:
            num_value = r_numerals[letter]
            if num_value < prev:
                num_value = prev - num_value
                final -= prev
            final += num_value
            prev = num_value
    return final


# roman_number = "X"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# roman_number = "VII"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# roman_number = "IX"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# roman_number = "LXXXVII"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# roman_number = "DCCVII"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))
