while True:
     try:
          ja = int(input("国語の通知表評定を入力\n"))
          ma = int(input("数学の通知表評定を入力\n"))
          en = int(input("英語の通知表評定を入力\n"))
          if ja<0 or ma<0 or en<0 or ja>5 or ma>5 or en>5:
               print("1~5の数字で入力してください")
               continue
     except ValueError:
          print("半角数字で入力してください")
     hyoutei = ja+ma+en
     if ja==1 or ma==1 or en==1:
          print("推薦は受けられません")
          break
     elif hyoutei>=12:
          print("特進クラス")
          break
     elif hyoutei>=10:
          print("総合進学クラス")
          break
     elif hyoutei>=8:
          print("一般クラス")
          break
     else:
          print("推薦は受けられません")
          break