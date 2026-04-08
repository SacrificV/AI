def even_nums(n):
    for i in range(1, n+1):
        yield i * 2
for num in even_nums(10):
    print(num)