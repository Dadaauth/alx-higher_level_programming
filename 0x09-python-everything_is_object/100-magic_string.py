#!/usr/bin/pythoon3
def magic_string():
    magic_string.count += 1
    return "BestSchool" * magic_string.count

for _ in range(30):
    print(magic_string())
