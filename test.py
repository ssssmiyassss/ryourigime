# 2021-07-18 19:17:04
# 文字の分割＆return それぞれの要素が入ったリスト。
def moji_split(zenbun_str):
  moji_list = zenbun_str.split(',')
  for moji in moji_list:
    print(moji)
  return moji_list


zenbun_str = '野菜,根菜のラタトゥイユ,24'
print(zenbun_str)
moji_list = moji_split(zenbun_str)