def rec_fun(number):
    if number == 0:
        return
    rec_fun(number - 1)
    print(number)



rec_fun(10)
