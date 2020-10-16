"""
このファイルに解答コードを書いてください
"""

tmp_list = []
with open('./input.txt', 'r') as f:
    text = f.read()
    tmp_list = text.split('\n')

    tmp_dict = {}
    num = int(tmp_list[-2])
    for i in range(len(tmp_list) - 2):
        tmp_dict[(tmp_list[i].split(':'))[0]] = (tmp_list[i].split(':'))[1]
    sorted_dict = sorted(tmp_dict.items(), key=lambda x: int(x[0]))

    answer = ''
    for k in range(len(sorted_dict)):
        if num % int(sorted_dict[k][0]) == 0:
            answer += sorted_dict[k][1]

    if answer == '':
        print(num)
    else:
        print(answer)
