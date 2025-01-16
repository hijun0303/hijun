ja = int(input("国語の通知表評定を入力\n"))
ma = int(input("数学の通知表評定を入力\n"))
en = int(input("英語の通知表評定を入力\n"))
hyoutei = ja+ma+en
if ja==1 or ma==1 or en==1:
     print("推薦は受けられません")
elif hyoutei>=12:
     print("特進クラス")
elif hyoutei>=10:
     print("総合進学クラス")
elif hyoutei>=8:
     print("一般クラス")
else:
     print("推薦は受けられません")