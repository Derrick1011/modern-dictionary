meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "CREEPY" : "Sesuatu hal yang menakutkan dan seram",
            "IYKYK" : "If you now you now",
            }

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    
    print("Makna kata dari",word,"adalah", meme_dict[word])
else:
    print("kata tidak ditemukan")
