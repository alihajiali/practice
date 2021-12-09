List = [(19542209, "New York"), (4887871, "Alabama"), (5462579, "Tokyo"), (8563259, "Tehran"), (45756325, "Seol"), (58693218, "Pekan")]
revers_lst=[elm for elm in reversed(List)]
sorted_by_second = sorted(List, key=lambda tup:list(tup[1])[-1],reverse=True)
print(revers_lst)
print(sorted_by_second)


