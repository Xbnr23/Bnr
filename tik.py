import requests
import time
import random

# تنبيه توعوي
print("=" * 60)
print("🚨 هذا السكريبت تعليمي فقط. لا تستخدمه في تطبيقات حقيقية!")
print("❌ المتابعات الوهمية تنتهك سياسات المنصات وقد تؤدي إلى حظر حسابك.")
print("=" * 60)

# إدخال معرف الحساب الهدف
target_user_id = input("🎯 أدخل معرف الحساب الهدف (User ID): ")

# تعريف واجهة API وهمية (تعليمية فقط)
fake_api_url = "https://hoti6.free.beeceptor.com"

# إعدادات الطلب
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Content-Type": "application/json",
}

# عدد المتابعات الوهمية المراد تنفيذها
target_follows = int(input("🎯 أدخل عدد المتابعات الوهمية المطلوب تنفيذها: "))
fake_follows_count = 0

print("\n🔄 بدء إرسال الطلبات الوهمية...\n")

# تنفيذ العملية
while fake_follows_count < target_follows:
    try:
        # إرسال طلب متابعة وهمي
        response = requests.post(
            fake_api_url,
            headers=headers,
            json={"user_id": target_user_id, "follower_id": random.randint(10000, 99999)},
        )

        # التحقق من نجاح الطلب
        if response.status_code == 200:
            fake_follows_count += 1
            print(f"✅ متابعة وهمية تمت إضافتها ({fake_follows_count}/{target_follows})")
        else:
            print(f"❌ فشل في الإرسال. كود الخطأ: {response.status_code}")

        # تأخير عشوائي لمحاكاة النشاط البشري
        time.sleep(random.uniform(0.5, 2.0))

    except Exception as e:
        print(f"⚠️ حدث خطأ: {e}")
        break

print("\n⚠️ انتهت العملية! هذه المتابعات غير حقيقية ولا تضيف قيمة حقيقية للحساب.\n")
