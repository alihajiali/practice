import module


person1 = module.Bank('ali', 50000)
person2 = module.Bank('ali2', 10000)

print(module.send_money(person1, 20000, person2))