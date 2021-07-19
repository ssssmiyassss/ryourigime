import random
import tkinter # Tkinterモジュールのインポート

# # 2021-07-18 19:17:04
# # 文字の分割＆return それぞれの要素が入ったリスト。
# def moji_split(zenbun_str):
#   moji_list = zenbun_str.split(',')
#   for moji in moji_list:
#     print(moji)
#   return moji_list

#####################################################
# コンソールに"Button is clicked."を出力する関数
def clicked():
  print("Button is clicked.")

def showmenu_button(list1,list2):
# 0～len(list)までの乱数を決める。
  rand1 = random.randint(0,len(list2)-1)
  rand2 = random.randint(0,len(list1)-1)
  label1 = tkinter.Label(root, text=str(list1[rand1]))# ラベルの作成
  label2 = tkinter.Label(root, text=str(list2[rand2]))# ラベルの作成
  label1.grid()#ラベルの表示
  label2.grid()#ラベルの表示

######################################################


# テキストファイルをオープンして，list_bistroに格納。
with open("bistro.txt",'r',encoding="utf-8_sig") as file_bistro:
  list_bistro = file_bistro.readlines()
# print("len(list_bistro)="+str(len(list_bistro)))

# テキストファイルをオープンして，list_bistroに格納。
with open("staub.txt" ,'r',encoding="utf-8_sig") as file_staub:
  list_staub  = file_staub.readlines()
# print("len(list_staub)="+str(len(list_staub)))

def showmenu_button2():
# 0～len(list)までの乱数を決める。
  rand1 = random.randint(0,len(list_bistro)-1)
  rand2 = random.randint(0,len(list_staub)-1)
  label1.config(text="ビストロ="+str(list_bistro[rand1]))# ラベルの作成
  label2.config(text="ストウブ="+str(list_staub[ rand2]))# ラベルの作成
  label1.grid()#ラベルの表示
  label2.grid()#ラベルの表示

# ウィンドウ（フレーム）の作成
root = tkinter.Tk()

# ウィンドウの名前を設定
root.title(u"今日のメニュー")

# ウィンドウの大きさを設定
root.geometry("300x300")





# ボタンの作成（text=ボタンに表示されるテキスト, command=押下時に呼び出す関数）
button = tkinter.Button(root, text="メニューを決める",width=40, command=showmenu_button2)
# button = tkinter.Button(root, text="メニューを決める")
# button.bind("<Button-1>",showmenu_button(list_bistro,list_staub)) 


# ラベルの作成
label = tkinter.Label(root, text="今日のメニュー")

# ボタンの表示
button.grid()

label1 = tkinter.Label(root, text=" ")# ラベルの作成
label2 = tkinter.Label(root, text=" ")# ラベルの作成


# イベントループ（TK上のイベントを捕捉し、適切な処理を呼び出すイベントディスパッチャ）
root.mainloop()

#-------------------------------------------------------------



