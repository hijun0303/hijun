import csv
import statistics as s
kekka = {}
with open("kekka2.csv","r") as f:
     kekka = {i[0]:[int(a) for a in i[1:]] for i in csv.reader(f) }

ja = [v[0] for k,v in kekka.items()]
ma = [v[1] for k,v in kekka.items()]
en = [v[2] for k,v in kekka.items()]
print(f"国語の平均点は{s.mean(ja)}点、数学は{s.mean(ma)}点、英語は{s.mean(en)}点です。")