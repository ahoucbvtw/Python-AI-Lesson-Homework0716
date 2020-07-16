from tkinter import *
import tkinter.font as tkfont
from tkinter import messagebox
from tkinter import filedialog
import csv

class Main(object):

	def __init__(self):

		self.window = Tk()
		self.window.title("Homework") #視窗名稱
		self.window.config(background = "#f0f0f0")#更該視窗背景顏色
		self.window.geometry("450x360+600+250") #視窗解析度 (x*y+視窗欲固定的畫面位置X+視窗欲固定的畫面位置Y)
		self.window.resizable(0,0) #不可以更改大⼩
		Font_Title = tkfont.Font(family = "Arial", size = 25, weight = "bold")
		Font = tkfont.Font(family = "新細明體", size = 13)
		Font_Button = tkfont.Font(family = "新細明體", size = 10, weight = "bold")
		Font_Answer = tkfont.Font(family = "新細明體", size = 13, weight = "bold", underline= True)

		def Start():
			fristagency = {}
			data = []
			searchagency = Agencyinput.get()
			if searchagency == "":
				messagebox.showwarning("Error","請輸入欲查詢的政府機關單位！！")
			else:
				with open ("./data/opendata_requests.csv",mode="r",encoding = "UTF-8") as file:
					a = csv.reader(file)
					for i, row in enumerate(a):
						if i == 0:
							pass
						else:
							#檢查字典中是否有一筆一筆row[0]的機關名稱，沒有就給1
							if fristagency.get(row[0]) == None:
								fristagency[row[0]] = 1
							#如果字典中有row[0]的機關名稱，則用原來的數值+1
							else:
								fristagency[row[0]] = fristagency[row[0]] + 1

							if row[0] == searchagency:
								#按照rawdata格式輸入至data的List中
								data.append(f"{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}")

					maxopendata = max(fristagency, key = fristagency.get)
					Advanced_Answer.config(text = f"『{maxopendata}』貢獻 {fristagency[maxopendata]} 筆 OpenData 為最多筆")
					print(f"『{maxopendata}』貢獻 {fristagency[maxopendata]} 筆 OpenData 為最多筆")

					if data == []:
						messagebox.showinfo(title = "Notice", message = "您輸入的政府單位並位上傳任何資料集！！")
						print("您輸入的政府單位並位上傳任何資料集")
					else:
						#將按照rawdata格式輸入的Data寫入新的自定義檔名並按照rawdata格式中先新增第一列內部各項資料的敘述
						with open(searchagency + "_output.csv", "w", encoding = "UTF-8") as outputfile:
							outputfile.write("提供機關名稱,資料集名稱,瀏覽次數,下載次數,資料集評分,上架日期\n")
							for i, text in enumerate(data):
								# print(text)
								if i == len(data) - 1:
									outputfile.write(text)
								else:
									outputfile.write(text + "\n")
							messagebox.showinfo(title = "Notice", message = f"總共{len(data)}筆數據已輸出成 『{searchagency}_output.csv』 ！！")
							print(f"總共{len(data)}筆數據已輸出成 『{searchagency}_output.csv』 ！！")

#####################################################################################################################################################
		TFrame = Frame(self.window)
		TFrame.grid(row = 0, padx = 10, pady = 10)

############################################################################################################################################
		Title = Label(TFrame, font = Font_Title, text = "Homework")
		Title.grid(row = 0, columnspan = 2, padx = 2, pady = 10)

		Emptylabel = Label(TFrame)
		Emptylabel.grid(row = 1, column = 0, padx = 5, pady = 10)

		Agencyinput_Title = Label(TFrame, font = Font, text = "欲查詢的政府機關單位：")
		Agencyinput_Title.grid(row = 2, column = 0, padx = 5, pady = 10)

		Agencyinput = Entry(TFrame, font = Font, width = 25)
		Agencyinput.grid(row = 2, column = 1, padx = 5, pady = 10)

###########################################################################################################################################
		Search = Button(TFrame, text = "查詢", font = Font_Button, bg = "skyblue", width = 10, height = 1, command = Start)
		Search.grid(row = 3, columnspan = 2, padx = 5, pady = 10)

		Emptylabel01 = Label(TFrame)
		Emptylabel01.grid(row = 4, column = 0, padx = 5, pady = 10)

###########################################################################################################################################
		TFrame1 = Frame(self.window)
		TFrame1.grid(row = 1, padx = 10, pady = 10)

		Advanced_Title = Label(TFrame1, font = Font, text = "[進階Q]：哪一個部門貢獻最多筆 OpenData")
		Advanced_Title.grid(row = 0, column = 0, padx = 5, pady = 10)

		Advanced_Answer = Label(TFrame1, font = Font_Answer)
		Advanced_Answer.grid(row = 1, column = 0, padx = 5, pady = 10)


		self.window.mainloop()

if __name__ == '__main__':
	Main()