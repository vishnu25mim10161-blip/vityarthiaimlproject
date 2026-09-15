import pandas as pd
from sklearn.linear_model import LinearRegression
import tkinter as tk
from tkinter import messagebox

df = pd.read_csv("housing_dataset_large_with_year.csv")
X = df[['Bedrooms','Bathrooms','Size_sqft','Parking_space','Condition','Year']]
y = df['Price_INR']
model = LinearRegression()
model.fit(X, y)

def predict():
    try:
        b = int(bed.get())
        ba = int(bath.get())
        s = float(size.get())
        p = int(park.get())
        c = int(cond.get())
        yr = int(year.get())
        features = [[b, ba, s, p, c, yr]]
        price = model.predict(features)[0]
        messagebox.showinfo("Result", f"🏡 Estimated Price: ₹{price:,.0f}")
    except Exception as e:
        messagebox.showerror("Error", "Fill all fields correctly!")

root = tk.Tk()
root.title("🏠 House Price Predictor (ML Model)")
root.geometry("360x430")
root.config(bg="#709D9B")

fields = [
    ("Bedrooms",1),
    ("Bathrooms",2),
    ("Size (sqft)",3),
    ("Parking (0/1)",4),
    ("Condition (1-5)",5),
    ("Construction Year",6)
]

vars = [tk.Entry(root, width=10, bd=2, justify='center') for _ in fields]

for i, (label_text, _) in enumerate(fields):
    tk.Label(root, text=label_text, bg="#DCE6F1", fg="#130F54",
             font=("Segoe UI", 10, "bold")).place(x=40, y=60 + i * 50)

for i, entry in enumerate(vars):
    entry.place(x=220, y=60 + i * 50)

bed, bath, size, park, cond, year = vars

tk.Button(root, text="Predict Price 💰", bg="#2563EB", fg="white",
          font=("Segoe UI", 11, "bold"), activebackground="#1D4ED8",
          width=20, command=predict).place(x=80, y=370)

root.mainloop()