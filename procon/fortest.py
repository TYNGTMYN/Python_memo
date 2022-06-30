import sys
#受け取るデータのクラス
class Data:
    def __init__ (self,name):
        self.name = name
    list = []

#inputを受け取る関数
def get_input():
    input_sys = sys.stdin.readline
    input_lists = []
    len_count = int(input_sys())
    for i in range(len_count):
        input_len = list(map(int,input_sys().split()))
        input_lists.append(input_len)
    return input_lists

#main関数
def main():
    list = get_input()
    data_class = Data("data")
    data_class.list = list
    print(data_class.list)

if __name__ == "__main__":
    main()