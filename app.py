import curses
from datetime import datetime, timedelta


# إعداد البيانات
subscribers = []


# إضافة مشترك جديد
def add_subscriber(name, surname, phone, start_date, end_date, alert_days):
    end_date_obj = datetime.strptime(end_date, "%d/%m/%Y")
    days_remaining = (end_date_obj - datetime.now()).days

    # تحديد الحالة
    if days_remaining <= 0:
        status = "منتهي"
    elif days_remaining <= alert_days:
        status = "قريب من الانتهاء"
    else:
        status = "نشط"

    # إضافة المشترك إلى القائمة
    subscribers.append({
        "name": name,
        "surname": surname,
        "phone": phone,
        "start_date": start_date,
        "end_date": end_date,
        "status": status
    })


# عرض واجهة القائمة
def display_subscribers(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "إدارة المشتركين", curses.A_BOLD)
    stdscr.addstr(2, 0, "الاسم      اللقب     رقم الهاتف     تاريخ البدء   تاريخ النهاية   الحالة")
    stdscr.addstr(3, 0, "-" * 60)

    # عرض المشتركين
    for idx, sub in enumerate(subscribers, start=4):
        line = f"{sub['name']:10}{sub['surname']:10}{sub['phone']:15}{sub['start_date']:15}{sub['end_date']:15}{sub['status']:10}"
        stdscr.addstr(idx, 0, line)

    stdscr.addstr(len(subscribers) + 5, 0, "اضغط 'a' لإضافة مشترك جديد، أو 'q' للخروج.")
    stdscr.refresh()


# نموذج لإضافة مشترك
def add_subscriber_form(stdscr):
    curses.echo()

    stdscr.clear()
    stdscr.addstr(0, 0, "إضافة مشترك جديد", curses.A_BOLD)
    stdscr.addstr(2, 0, "الاسم: ")
    name = stdscr.getstr(2, 10).decode("utf-8")
    stdscr.addstr(3, 0, "اللقب: ")
    surname = stdscr.getstr(3, 10).decode("utf-8")
    stdscr.addstr(4, 0, "رقم الهاتف: ")
    phone = stdscr.getstr(4, 15).decode("utf-8")
    stdscr.addstr(5, 0, "تاريخ البدء (DD/MM/YYYY): ")
    start_date = stdscr.getstr(5, 25).decode("utf-8")
    stdscr.addstr(6, 0, "تاريخ النهاية (DD/MM/YYYY): ")
    end_date = stdscr.getstr(6, 27).decode("utf-8")
    stdscr.addstr(7, 0, "عدد أيام التنبيه قبل الانتهاء: ")
    alert_days = int(stdscr.getstr(7, 35).decode("utf-8"))

    add_subscriber(name, surname, phone, start_date, end_date, alert_days)
    curses.noecho()


# البرنامج الرئيسي
def main(stdscr):
    curses.curs_set(0)

    while True:
        display_subscribers(stdscr)
        key = stdscr.getch()

        if key == ord('a'):
            add_subscriber_form(stdscr)
        elif key == ord('q'):
            break


# تشغيل التطبيق
curses.wrapper(main)
