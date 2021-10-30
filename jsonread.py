import time
import os
import json

data_size = 4
correct = 0
score = int(correct / data_size * 100)

with open(r"C:\Users\svenk\PycharmProjects\pythonProject\questionx.json") as f:
    data = json.load(f)
with open(r"C:\Users\svenk\PycharmProjects\pythonProject\answer.json") as f:
    ans = json.load(f)

options = (data['options'])
Question = (data['Question'])

answer = (data['answer'])

# print(data)

for i in range(4):

    print(Question[i])
    print("========================")
    print(options[i])
    tic = time.perf_counter()
    g = int(input())
    toc = time.perf_counter()
    tim = toc - tic
    print(f" Your answered the question  in {tim:0.2f} seconds")
    if g == answer[i]:
        print("your answer is correct")

        if 0 <= tim < 10:
            correct += 1
        elif 11 <= tim < 30:
            correct += .8
        elif 31 <= tim < 45:
            correct += .75
        else:
            correct += .65


    else:
        print("your answer is incorrect")
score = int((correct / data_size) * 100)

print(f" Your total score in this  {score} out of ")
