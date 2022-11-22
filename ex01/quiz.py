import random

def shutudai():
    que_dct = {"サザエの旦那の名前は？" : ("マスオ", "ますお"),
                "カツオの妹の名前は？" : ("ワカメ", "わかめ"),
                "タラオはカツオから見てどんな関係？" : ("甥", "おい", "甥っ子", "おいっこ")}
    que = random.choice(["サザエの旦那の名前は？", "カツオの妹の名前は？", "タラオはカツオから見てどんな関係？"])
    print(que)
    return que_dct[que]



def kaitou(anss, usr):
    if usr in anss:
        print("正解!!!")
    else:
        print("出直してこい")



if __name__ == "__main__":
    kaitou(shutudai(), input("答えるんだ："))
    # anss = shutudai()
    # usr = input("答えるんだ：")
    # kaitou(anss, usr)
