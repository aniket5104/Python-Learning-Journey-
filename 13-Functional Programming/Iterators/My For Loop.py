def my_for_loop(iterable):
    iter_num= iter(iterable)

    while True:
        try:
            print(next(iter_num))
        except StopIteration:
            break
    
lst=[1,2,3,4,5]
my_for_loop(lst)

