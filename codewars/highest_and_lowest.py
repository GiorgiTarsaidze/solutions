def high_and_low(numbers):
    # ...
    lst_nums = [int(i) for i in numbers.split(" ")]
    return f"{max(lst_nums)} {min(lst_nums)}"