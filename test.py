import random

# 2021-07-18 19:17:04
# 文字の分割＆return それぞれの要素が入ったリスト。
def moji_split(zenbun_str):
  moji_list = zenbun_str.split(',')
  for moji in moji_list:
    print(moji)
  return moji_list


# 2021-07-19 10:14:19
# main
# zenbun_str = '野菜,根菜のラタトゥイユ,24'
# print(zenbun_str)
# moji_list = moji_split(zenbun_str)

# file_bistro = open('bistro.txt','r')
# file_staub  = open('staub.txt' ,'r')

with open("bistro.txt",'r',encoding="utf-8_sig") as file_bistro:
  list_bistro = file_bistro.readlines()
# print("len(list_bistro)="+str(len(list_bistro)))

with open("staub.txt" ,'r',encoding="utf-8_sig") as file_staub:
  list_staub  = file_staub.readlines()
# print("len(list_staub)="+str(len(list_staub)))

rand_bistro = random.randint(0,len(list_bistro)-1)
rand_staub  = random.randint(0,len(list_staub) -1)

print("ビストロ＝"+str(list_bistro[rand_bistro]))
print("ストウブ＝"+str(list_staub[ rand_staub] ))



