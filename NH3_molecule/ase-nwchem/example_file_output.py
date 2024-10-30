## Python program to print the data
'''res: dict[int, list[str]] = {1: ["Python", '33.2', 'UP'], 2: ["Java", '23.54', 'DOWN'], 3: ["Ruby", '17.22', 'UP']}

file = open('example_file_output.txt', 'w')

file.write("Pos \t, Lang\t, Percent \t, Change\n")
for k, v in res.items():
    lang, perc, change = v
    file.write(f'{k} {lang} {perc} {change}\n')'''

from tabulate import tabulate

file = open('example_file_output.txt', 'w')

data: list[list[str]] = [['1', 'Liquid', '24', '12'],
[2, 'Virtus.pro', 19, 14],
[3, 'PSG.LGD', 15, 19],
[4,'Team Secret', 10, 20]]
file.write(tabulate(data, headers=["Pos", "Team", "Win", "Lose"]))
