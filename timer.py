import time

"""Print the latest tutorial from Real Python"""
tic = time.perf_counter()
g = int(input())

toc = time.perf_counter()
print(f"Downloaded the tutorial in {toc - tic:0.2f} seconds")

