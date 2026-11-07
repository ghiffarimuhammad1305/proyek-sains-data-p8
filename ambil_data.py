import urllib.request, csv, random, re

url = "https://raw.githubusercontent.com/indobenchmark/indonlu/master/dataset/smsa_doc-sentiment-prosa/train_preprocess.tsv"
lines = [l.decode('utf-8').strip() for l in urllib.request.urlopen(url).readlines() if l.strip()]
print("Total baris mentah:", len(lines))

random.seed(42)
sampled = random.sample(lines, 350)

with open("raw_20261107.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["teks_ulasan", "label_sentimen_asli", "teks_ulasan_bersih"])
    for l in sampled:
        p = l.split("\t")
        if len(p) >= 2:
            w.writerow([p[0], p[1], re.sub(r"@\w+", "[USER]", p[0])])

print("SUKSES: raw_20261107.csv (350 baris) berhasil dibuat!")
