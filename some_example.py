import random
import time

lst = [random.random() for _ in range(10000)]
t0 = time.time()
lst.sort() # in-place
t1 = time.time()

another_list = [random.random() for _ in range(10000)]
t2 = time.time()
new_lst = sorted(another_list) # out-of-place
t3 = time.time()

print(f"In-place sort time: {t1-t0}")
print(f"Out-of-place sort time: {t3-t2}")
