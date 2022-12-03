import sys
import re
import time


class elf:
    with open('input.txt', 'r') as f:
        inp = f.read().splitlines()
        f.close()

    def part_1():
        item_list = []

        for backpack in elf.inp:
            compartment_1 = backpack[:int(len(backpack)/2)]
            compartment_2 = backpack[int(len(backpack)/2):]

            item_list.append((set(compartment_1) & set(compartment_2)).pop())

        ucase_letters = list(filter(lambda x: 64 < ord(x) < 97, item_list))
        ucase_values = list(map(lambda x: ord(x)-38, ucase_letters))
        lcase_letters = list(
            filter(lambda x: 96 < ord(x) < 123, item_list))
        lcase_values = list(map(lambda x: ord(x)-96, lcase_letters))

        return sum(ucase_values) + sum(lcase_values)

    def part_2():
        temp_list = []
        current_group = 0
        item_list = []

        for i in range(len(elf.inp)):
            if int((i - (i % 3))/3) == current_group:
                temp_list.append(elf.inp[i])
            else:
                item_list.append((set(temp_list[0]) & set(
                    temp_list[1]) & set(temp_list[2])).pop())
                temp_list = []
                temp_list.append(elf.inp[i])
                current_group = int((i - (i % 3))/3)

        item_list.append((set(temp_list[0]) & set(
            temp_list[1]) & set(temp_list[2])).pop())

        ucase_letters = list(filter(lambda x: 64 < ord(x) < 97, item_list))
        ucase_values = list(map(lambda x: ord(x)-38, ucase_letters))
        lcase_letters = list(
            filter(lambda x: 96 < ord(x) < 123, item_list))
        lcase_values = list(map(lambda x: ord(x)-96, lcase_letters))

        return sum(ucase_values) + sum(lcase_values)


if __name__ == "__main__":
    t0 = time.time()
    part = sys.argv[1]

    if part == '1':
        print(elf.part_1())
    elif part == '2':
        print(elf.part_2())
    t1 = time.time()

    print(f'{str(round((t1-t0)*1000,3))} ms för del {part}')
