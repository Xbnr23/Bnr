import requests
import time
import random

# تنبيه توعوي
print("=" * 60)
print("🚨 هذا السكريبت تعليمي فقط ويُظهر كيفية عمل البوتات.")
print("❌ استخدامه على منصات حقيقية قد يؤدي إلى حظر حسابك!")
print("=" * 60)

# إدخال معرف الفيديو
target_video_id = input("🎯 أدخل معرف الفيديو الهدف (Video ID): ")

# تعريف عنوان الـ API الوهمي (تعليمي فقط)
fake_api_url = "https://x-bnr.free.beeceptor.com
Use this as base URL when making API calls.

"

# إعدادات الطلب
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Content-Type": "application/json",
}

# عدد المشاهدات المستهدفة
target_views = int(input("🎯 أدخل عدد المشاهدات الوهمية المطلوب إضافتها: "))
fake_views_count = 0

print("\n🔄 بدء إرسال الطلبات الوهمية...\n")

# تنفيذ العملية
while fake_views_count < target_views:
    try:
        # إرسال طلب وهمي
        response = requests.post(
            fake_api_url,
            headers=headers,
            json={"video_id": target_video_id, "user_id": random.randint(10000, 99999)},
        )

        # التحقق من نجاح الطلب
        if response.status_code == 200:
            fake_views_count += 1
            print(f"✅ مشاهدة وهمية تمت إضافتها ({fake_views_count}/{target_views})")
        else:
            print(f"❌ فشل في الإرسال. كود الخطأ: {response.status_code}")

        # تأخير عشوائي لمحاكاة النشاط البشري
        time.sleep(random.uniform(0.5, 2.0))

    except Exception as e:
        print(f"⚠️ حدث خطأ: {e}")
        break

print("\n⚠️ انتهت العملية! هذه الطلبات غير حقيقية ولا تضيف قيمة حقيقية للفيديو.\n")
