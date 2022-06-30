import sys

#受け取るデータのクラス
class Data:
    def __init__ (self,name):
        self.name = name
    list = []

#inputを受け取る関数
def get_input(question_count):
    input_sys = sys.stdin.readline
    input_lists = []
    for i in range(question_count):
        input_len = str(input_sys().rstrip())
        input_lists.append(input_len)
    return input_lists

#main関数
def main():
    input_sys = sys.stdin.readline
    question_count = int(input_sys().rstrip())
    list = get_input(question_count)
    data_class = Data("Question")
    data_class.list = list
    for i in data_class.list:
        output = "Hello," + i
        print(output)

if __name__ == "__main__":
    main()