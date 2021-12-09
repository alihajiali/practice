def get_next_multiple(n):
    i = 1
    while True:
        if i % n == 0:
            yield i
        i += 1
    


gen_multiple_of_two = get_next_multiple(2)
print(next(gen_multiple_of_two))
print(next(gen_multiple_of_two))
print(next(gen_multiple_of_two))
print(next(gen_multiple_of_two))

print()

gen_multiple_of_two = get_next_multiple(13)
print(next(gen_multiple_of_two))
print(next(gen_multiple_of_two))
print(next(gen_multiple_of_two))
print(next(gen_multiple_of_two))