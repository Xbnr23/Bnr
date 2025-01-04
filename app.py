import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime, timedelta


# إضافة مشترك جديد
def add_subscriber():
    name = name_entry.get()
    surname = surname_entry.get()
    phone = phone_entry.get()
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    alert_days = alert_days_entry.get()

    if not (name and surname and phone and start_date and end_date and alert_days):
        messagebox.showerror("خطأ", "يرجى تعبئة جميع الحقول!")
        return

    # إضافة البيانات إلى الجدول
    subscriber_list.insert("", "end", values=(name, surname, phone, start_date, end_date, "نشط"))

    # تنبيه إن وجد مشترك قريب من انتهاء اشتراكه
    days_to_alert = int(alert_days)
    end_date_obj = datetime.strptime(end_date, "%d/%m/%Y")
    if (end_date_obj - datetime.now()).days <= days_to_alert:
        messagebox.showwarning("تنبيه", f"المشترك {name} قريب من انتهاء اشتراكه!")

    # إعادة تعيين الحقول
    clear_fields()


# إعادة تعيين الحقول
def clear_fields():
    name_entry.delete(0, tk.END)
    surname_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    start_date_entry.delete(0, tk.END)
    end_date_entry.delete(0, tk.END)
    alert_days_entry.delete(0, tk.END)


# إعداد نافذة التطبيق
root = tk.Tk()
root.title("إدارة المشتركين")
root.geometry("800x600")

# التعليمات
tk.Label(root, text="إدارة المشتركين", font=("Arial", 16, "bold")).pack(pady=10)

# إدخال البيانات
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="الاسم:").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="اللقب:").grid(row=1, column=0, padx=5, pady=5)
surname_entry = tk.Entry(frame, width=30)
surname_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="رقم الهاتف:").grid(row=2, column=0, padx=5, pady=5)
phone_entry = tk.Entry(frame, width=30)
phone_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="تاريخ بدء الاشتراك (DD/MM/YYYY):").grid(row=3, column=0, padx=5, pady=5)
start_date_entry = tk.Entry(frame, width=30)
start_date_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame, text="تاريخ نهاية الاشتراك (DD/MM/YYYY):").grid(row=4, column=0, padx=5, pady=5)
end_date_entry = tk.Entry(frame, width=30)
end_date_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(frame, text="تنبيه قبل انتهاء الاشتراك (بالأيام):").grid(row=5, column=0, padx=5, pady=5)
alert_days_entry = tk.Entry(frame, width=30)
alert_days_entry.grid(row=5, column=1, padx=5, pady=5)

# أزرار
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="إضافة مشترك", command=add_subscriber, bg="green", fg="white")
add_button.grid(row=0, column=0, padx=10)

cancel_button = tk.Button(button_frame, text="إلغاء", command=clear_fields, bg="red", fg="white")
cancel_button.grid(row=0, column=1, padx=10)

# جدول عرض المشتركين
table_frame = tk.Frame(root)
table_frame.pack(pady=10)

columns = ("الاسم", "اللقب", "رقم الهاتف", "تاريخ بدء الاشتراك", "تاريخ نهاية الاشتراك", "الحالة")
subscriber_list = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)

for col in columns:
    subscriber_list.heading(col, text=col)
    subscriber_list.column(col, width=120)

subscriber_list.pack()

# رسالة تنبيه
tk.Label(root, text="⚠️ تنبيه: لديك مشتركين قريبين من انتهاء اشتراكهم!", fg="red").pack(pady=10)

# تشغيل التطبيق
root.mainloop()
