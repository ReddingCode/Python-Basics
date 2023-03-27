
# Table de multiplication

def multiply(n, min=1, max=10):
    if min <= max:
        print("Vous devez rentrer un nombre max qui est superieur a min")
    for i in range(min, max+1):
        print(f"{i} x {n} = {i*n}")


multiply(2, 10, 5)

# for i in range(0, 10):

#     print(f"{i+1} x {table} = {(i+1)*table}")
