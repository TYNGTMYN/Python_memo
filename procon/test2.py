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

#大文字に変換する関数
def upper_case_list(list):
    list_up = []
    #取得した文字列を大文字に変換
    for i in list:
        list_up_len =[]
        for j in i:
            list_up_len.append(j.upper())
        list_up.append(list_up_len)
    return list_up

#IDを更新する関数
def update_ID(ID_value):
    return str(int(ID_value) + int(100))

#新たなIDを与える関数
def get_new_ID(id_count):
    #ID付与数が10を超える場合
    if(int(id_count) > int(9) ):
        return "0" + str(id_count)
    else:
        return "00" + str(id_count)


#main関数
def main():
    list = get_input()
    
    list_up = upper_case_list(list)
    
    #各行に関して問題に答えていく
    for i in list_up:
        output = ""
        ID_count = 0
        ID_dict = {}
        #各文字列にIDを付与
        for j in i:
            #すでにIDが付与されている場合
            if(j in ID_dict.keys()):
                ID_dict[j] = update_ID(ID_dict[j])#IDを更新
                #IDが4桁を超えている場合
                if(int(ID_dict[j]) > int(999)):
                    ID_count += 1#IDのカウントを増やす
                    ID_dict[j] = get_new_ID(ID_count)#新たなIDを与える
                #IDが4桁を超えない場合
                else:
                    ID_dict[j] = update_ID(ID_dict[j])#IDを更新する
            #IDが付与されていない場合
            else:
                ID_count += 1#IDのカウントを増やす
                ID_dict[j] = get_new_ID(ID_count)#新IDの取得
            output += ID_dict[j] + " "
        print(output)#取得IDを出力
    
if __name__ == "__main__":
    main()