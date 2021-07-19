import random
import tkinter # Tkinterモジュールのインポート

# # 2021-07-18 19:17:04
# # 文字の分割＆return それぞれの要素が入ったリスト。
# def moji_split(zenbun_str):
#   moji_list = zenbun_str.split(',')
#   for moji in moji_list:
#     print(moji)
#   return moji_list

# テキストファイルをオープンして，list_bistroに格納。
with open("bistro.txt",'r',encoding="utf-8_sig") as file_bistro:
  list_bistro = file_bistro.readlines()
# print("len(list_bistro)="+str(len(list_bistro)))

# テキストファイルをオープンして，list_bistroに格納。
with open("staub.txt" ,'r',encoding="utf-8_sig") as file_staub:
  list_staub  = file_staub.readlines()
# print("len(list_staub)="+str(len(list_staub)))

#####################################################
# ビストロのボタンが押されたとき
def showmenu_button1():
  rand1 = random.randint(0,len(list_bistro)-1) # 0～len(list)までの乱数を決める。
  label1.config(text="ビストロ="+str(list_bistro[rand1]))# ラベルの更新
  label1.grid()#ラベルの表示

# ストウブのボタンが押されたとき
def showmenu_button2():
  rand2 = random.randint(0,len(list_staub)-1) # 0～len(list)までの乱数を決める。
  label2.config(text="ストウブ="+str(list_staub[ rand2]))# ラベルの更新
  label2.grid()#ラベルの表示
#####################################################

# ウィンドウ（フレーム）の作成
root = tkinter.Tk()

# ウィンドウの名前を設定
root.title(u"今日のメニュー")

# ウィンドウの大きさを設定
root.geometry("300x300")





# ボタンの作成（text=ボタンに表示されるテキスト, command=押下時に呼び出す関数）

# bistro.txt
button1 = tkinter.Button(root, text="ビストロのメニューを決める",width=40, command=showmenu_button1)
button1.grid() # ボタンの表示
label1 = tkinter.Label(root, text=" ")# ラベルの作成

# staub.txt
button2 = tkinter.Button(root, text="ストウブのメニューを決める",width=40, command=showmenu_button2)
button2.grid() # ボタンの表示
label2 = tkinter.Label(root, text=" ")# ラベルの作成


# イベントループ（TK上のイベントを捕捉し、適切な処理を呼び出すイベントディスパッチャ）
root.mainloop()

#-------------------------------------------------------------



