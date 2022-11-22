import random
import datetime

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
    print(f"回答時間：{(ed-st).seconds}秒")



if __name__ == "__main__":
    # kaitou(shutudai(), input("答えるんだ："))
    anss = shutudai()
    st = datetime.datetime.now()
    usr = input("答えるんだ：")
    ed = datetime.datetime.now()
    kaitou(anss, usr)
