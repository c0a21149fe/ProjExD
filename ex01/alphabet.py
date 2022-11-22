import random
import datetime

len_all = 10
len_lost = 3
tried = 1

def start():
    global len_all, len_lost, tried
    def_lst = alph_list.copy()
    while(True):
        cur_lst = random.sample(def_lst, len(def_lst))
        alph = " ".join(cur_lst.copy())
        lost_lst = [""] * len_lost
        for i in range(len_lost):
            lost_lst[i] = cur_lst.pop(random.randint(0, len_all-1-i))
        cur = " ".join(cur_lst)
        lost = " ".join(lost_lst)
        print(f"対象文字：\n{alph}")
        print(f"欠損文字（デバッグ用）：\n{lost}")
        print(f"表示文字：\n{cur}")
        
        try:
            ans1 = int(input("欠損文字はいくつあるでしょうか？："))
        except ValueError:
            print("数字を入力してください.最初からやり直します")
            print("-"*40)
            continue
        if ans1 == len_lost:
            print("正解です。それでは, 具体的に欠損文字を１つずつ入力してください。")
            for i in range(len_lost):
                ans2 = input(f"{i+1}つ目の文字を入力してください：")
                if ans2 in lost_lst:
                    lost_lst.remove(ans2)
                else:
                    print("不正解です.また、チャレンジしてください")
                    break
            else:
                print("全問正解です")
                print(f"あなたは{tried}回挑戦しました。")
                break
        else:
            print("不正解です.また、チャレンジしてください")
        print("-" * 40)
        tried += 1

if __name__ == "__main__":
    st = datetime.datetime.now()
    alphabet = [chr(i) for i in range(65, 91)]  # AtoZ
    alph_list = random.sample(alphabet, len_all)
    start()
    print(f"実行時間：{(datetime.datetime.now()-st).seconds}秒")

