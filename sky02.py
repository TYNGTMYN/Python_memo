def main():
    #標準入力でスペースで区切られた２つの整数を受け取る
    a, b = map(int, input().split())
    #cにaの三乗を代入
    c = a ** 3

    e = (b-1) * (b-2)
    f = int(e / 2)
    
    #分母をc分子をeとする分数を約分して出力
    for i in range(2,f):
        while((f%i == 0)&(c%i == 0)):
            f = f / i
            c = c / i
    print(str(int(f)) + "/" + str(int(c)))

main()