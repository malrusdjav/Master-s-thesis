import pytablewriter

data = [
    [0, 0.1, "hoge", True, 0, "2017-01-01 03:04:05+0900"],
    [2, "-2.23", "foo", False, None, "2017-12-23 12:34:51+0900"],
    [3, 0, "bar", "true", "inf", "2017-03-03 22:44:55+0900"],
    [-10, -9.9, "", "FALSE", "nan", "2017-01-01 00:00:00+0900"],
]

headers = ["int", "float", "str", "bool", "mix", "time"]

writer = pytablewriter.LatexTableWriter()
writer.headers = headers
writer.value_matrix = data

file = open('output.txt', 'w')

file.write(writer.dumps())

file.close()
