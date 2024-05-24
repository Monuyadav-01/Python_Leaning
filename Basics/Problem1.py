movieCount = int(input("Enter movies cnt : "))
x = []
while movieCount != 0:
    movieName = input("Enter your movie name : ")
    x.append(movieName)
    movieCount = movieCount - 1
print(x)
