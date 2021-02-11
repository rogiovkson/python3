from python3.hw4.task1.lesson4_task1 import argv

time, hourly_rate, bonus = argv

try:
    time = int(time)
    hourly_rate = int(hourly_rate)
    bonus = int(bonus)
    salary = time * hourly_rate + bonus
    print(f'заработная плата сотрудника  {salary}')
except ValueError:
    print('Error')