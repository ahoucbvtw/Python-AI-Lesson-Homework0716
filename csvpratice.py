import csv


maxdownloadcount = 0
max_download_database = ""
fristagency = {}
data = []
# searchagancy = input("請輸入欲查詢的政府機關單位：")
searchagancy = "原住民族委員會"
with open ("./data/opendata_requests.csv",mode="r",encoding = "UTF-8") as file:
	a = csv.reader(file)
	for i, row in enumerate(a):
		if i == 0:
			pass
		else:
			#將row[3]下載次數12,455這種型式轉換成純數字型式
			if "," in row[3]:
				row[3] = row[3].replace(",","")
			row[3] = int(row[3])

			#依依判斷row[3]下載次數是否有大於前一筆，有就覆寫並列出其row[1]資料集名稱
			if row[3] > maxdownloadcount:
				maxdownloadcount = row[3]
				max_download_database = row[1]

			#檢查字典中是否有一筆一筆row[0]的機關名稱，沒有就給1
			if fristagency.get(row[0]) == None:
				fristagency[row[0]] = 1
			#如果字典中有row[0]的機關名稱，則用原來的數值+1
			else:
				fristagency[row[0]] = fristagency[row[0]] + 1

			if row[0] == searchagancy:
				#按照rawdata格式輸入至data的List中
				data.append(f"{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}")


	print(f"{max_download_database}：{maxdownloadcount}")
	print(max(fristagency, key = fristagency.get))
	print(fristagency[max(fristagency, key = fristagency.get)])
	# print(fristagency)
	print(f"{searchagancy}總共有{len(data)}筆數據")

	if data == []:
		print("您輸入的政府單位並位上傳任何資料集")
	else:
		#將按照rawdata格式輸入的Data寫入新的自定義檔名並按照rawdata格式中先新增第一列內部各項資料的敘述
		with open(searchagancy + "output.csv", "w", encoding = "UTF-8") as outputfile:
			outputfile.write("提供機關名稱,資料集名稱,瀏覽次數,下載次數,資料集評分,上架日期\n")
			for i, text in enumerate(data):
				# print(text)
				if i == len(data) - 1:
					outputfile.write(text)
				else:
					outputfile.write(text + "\n")
