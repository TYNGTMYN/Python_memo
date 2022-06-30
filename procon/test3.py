import sys

#inputを受け取る関数
def get_input():
    input_sys = sys.stdin.readline
    input_lists = []
    len_count = int(input_sys().rstrip())
    for i in range(len_count):
        input_len = list(map(str,input_sys().rstrip().split()))
        input_lists.append(input_len)
    return input_lists

def main():
    input_lists = get_input()
    for i in input_lists:
        print(i)

if __name__ == "__main__":
    main()