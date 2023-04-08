# nice -n -10 python3.9 nice_test.py or python3.9 nice_test.py
# calculate the elapsed time between tests(lower priority vs normal priority)
import datetime

start_time = datetime.datetime.now()
print(f"start : {start_time}")
sum = 0
for i in range(1, 50000000):
    sum = sum + i
print(sum)

end_time = datetime.datetime.now()
print(f"end : {end_time}")
elapsed_time = end_time - start_time
print(f"elapsed : {str(elapsed_time)}")