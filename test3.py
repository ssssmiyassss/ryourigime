import random
import tkinter as tk # Tkinterモジュールのインポート

#####################################################
# 2021-07-19 16:57:06
# hoge
def hoge( number ) :
  print("hoge {:0=10}".format(number))


# 2021-07-18 19:17:04
# 文字の分割＆return それぞれの要素が入ったリスト。
def moji_split(zenbun_str):
  moji_list = []
  moji_list = zenbun_str.split(',')
  return moji_list
#####################################################



# テキストファイルをオープンして，list_bistroに格納。
list_bistro = []
with open("bistro.txt",'r',encoding="utf-8_sig") as file_bistro:
  list_bistro = file_bistro.readlines()

list_staub = []
# テキストファイルをオープンして，list_bistroに格納。
with open("staub.txt" ,'r',encoding="utf-8_sig") as file_staub:
  list_staub  = file_staub.readlines()

#####################################################

# ウィンドウ（フレーム）の作成
root = tk.Tk()

# ウィンドウの名前を設定
root.title(u"今日のメニュー")

# ウィンドウの大きさを設定
# root.geometry("800x300")
photownd_sizex = 600
photownd_sizey = 450
textwnd_sizex = 300
offset_sizey = 0
windsizex = photownd_sizex + textwnd_sizex
windsizey = offset_sizey + photownd_sizey
root.minsize(windsizex,windsizey)
canvas = tk.Canvas(root, width=photownd_sizex, height=photownd_sizey, bg="white")
canvas.place(x=textwnd_sizex, y=offset_sizey)
img0 = tk.PhotoImage(file="image_staub\\1.png")
image_on_canvas = canvas.create_image(0, 0, image=img0, anchor=tk.NW)
#####################################################
# ビストロのボタンが押されたとき
def showmenu_button1():
  rand1 = random.randint(0,len(list_bistro)-1) # 0～len(list)までの乱数を決める。
  moji1 = str(list_bistro[rand1]).replace('\n','')
  label1.config(text="ビストロ="+moji1)# ラベルの更新
  label1.grid()#ラベルの表示
  page1 = int( moji_split( str(list_bistro[rand1]) )[2] )
  print("bistro,page={}".format(page1))
  img1name = "image_bistro\\"+str(page1)+".png"
  print(img1name)
  img1 = tk.PhotoImage(file=img1name)
  canvas.itemconfig( image_on_canvas, image=img1)

# ストウブのボタンが押されたとき
def showmenu_button2():
  rand2 = random.randint(0,len(list_staub)-1) # 0～len(list)までの乱数を決める。
  label2.config(text="ストウブ="+str(list_staub[ rand2]))# ラベルの更新
  label2.grid()#ラベルの表示
  page2 = int( moji_split( str(list_staub[ rand2]) )[2] )
  print("staub,page={}".format(page2))
  img2name = "image_staub\\"+str(page2)+".png"
  print(img2name)
  img2 = tk.PhotoImage(file=img2name)
  canvas.itemconfig( image_on_canvas, image=img2)
#####################################################


# ボタンの作成（text=ボタンに表示されるテキスト, command=押下時に呼び出す関数）
# bistro.txt
button1 = tk.Button(root, text="ビストロのメニューを決める",width=40, command=showmenu_button1)
button1.grid() # ボタンの表示
label1 = tk.Label(root, text=" ")# ラベルの作成

# staub.txt
button2 = tk.Button(root, text="ストウブのメニューを決める",width=40, command=showmenu_button2)
button2.grid() # ボタンの表示
label2 = tk.Label(root, text=" ")# ラベルの作成



# イベントループ（TK上のイベントを捕捉し、適切な処理を呼び出すイベントディスパッチャ）
root.mainloop()

#-------------------------------------------------------------



