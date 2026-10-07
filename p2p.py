import tkinter as tk

window = tk.Tk()
window.title("RANDOM")
window.geometry("1920x1080")

def login():
    if name.get():
        login_frame.pack_forget()
        catalog_frame.pack(pady=50)

def perehod():
    catalog_frame.pack_forget()
    order_frame.pack(pady=50)

login_frame = tk.Frame(window)
login_frame.pack(pady=100)
tk.Label(login_frame, text="Логин", font=("Arial Bold", 20)).pack(pady=20)

name = tk.Entry(login_frame, text="Логин", font=("Arial Bold", 16))
name.pack(pady=20)

tk.Button (login_frame,text="Войти", command=login).pack(pady=10)

order_frame = tk.Frame(window)
tk.Label(order_frame, text="Корзина", font=("Arial Bold", 20)).pack(pady=20)

catalog_frame = tk.Frame(window)
tk.Label(catalog_frame, text="Каталог товаров", font=("Arial Bold", 20)).pack(pady=20)
tk.Button (catalog_frame,text="Корзина", command=perehod).pack(pady=10)




window.mainloop()



