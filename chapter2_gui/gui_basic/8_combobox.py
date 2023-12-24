import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

values = [f"{i}일" for i in range(1, 32)] # 1 ~ 31 가지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드결제일") # 최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height=5, values=values, state="readonly")
readonly_combobox.current(0) # 0번재 인덱스 값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get()) #  선택된 값 표시
    print(readonly_combobox.get())

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()