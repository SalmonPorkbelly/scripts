# Cpu Bound
test = 0
while True:
    test = test + 1

# I/O Bound
while True:
    f = open("./io_test.txt", 'w')
    f.write("test")
    f.close()

