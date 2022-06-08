import sys
from time import perf_counter

Preamble_size = 25


def read_file(file):
    try:
        with open(file, 'r') as file:
            content = file.read().strip().split("\n")
            content = list(map(int, content))
            #print(content)

    except:
        print('Error to read file')
        sys.exit()

    return content


def is_sum_two_numbers(num: int, preamble: list):
    for i in range(len(preamble) - 1):
        for j in range(i + 1, len(preamble)):
            if preamble[i] + preamble[j] == num:
                return True
    return False


def part_one(data):
    for x in range(Preamble_size, len(data)):
        preamble = data[x - Preamble_size: x]
        if not is_sum_two_numbers(data[x], preamble):
            return data[x]


if __name__ == "__main__":
    start_timer = perf_counter()
    input_data = read_file("data.txt")
    print(part_one(input_data))
    end_timer = perf_counter()
    print(f'Time of execution {round(end_timer - start_timer, 5)} seconds')
    print('End of script')
    sys.exit(0)
