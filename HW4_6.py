from itertools import count, cycle

start_iterator = 3

for el in count(start_iterator):
     if el > 10:
         break

     print(el)

print ("Second iterator")
cycling_list = [1, 2, 16, 33, 22]
max_iterations = 10
iteration_count = 0

for el in cycle(cycling_list):
     print(el)
     iteration_count += 1

     if iteration_count >= max_iterations:
         break