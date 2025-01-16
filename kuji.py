import random as r
import time
kaisu = 0
while True:
     time.sleep(1)
     num = r.randint(1,5)
     if num < 5:
          print("はずれ")
          kaisu +=1
          continue
     else:
          print("あたり")
          kaisu +=1
          print(f"{kaisu*100}円使いました。")
          break