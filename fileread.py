
import random
import time
import os
import json

answers = []
with open(r"C:\Users\svenk\PycharmProjects\pythonProject\questions.text", 'r') as f:
    question = f.readlines()
for i in range(0,10):
    word = random.choice(question)[:-1]
    print("========================")
    print("Question")
    print(word)
    print(" ")
    print("========================")
    tic = time.perf_counter()
    g = input()
    toc = time.perf_counter()
    print(f"you answered  in {toc - tic:0.2f} seconds")
    answers.append(g)

print(answers)
