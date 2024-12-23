import requests

# بيانات البطاقة
card_data = {
    "card_number": "4111111111111111",
    "expiry_month": "12",
    "expiry_year": "2024",
    "cvv": "123"
}

# بوابة دفع وهمية
url = "https://checkout.stripe.com/c/pay/ppage_1QZJrbDOVUu6yhjNz3qN7Gt4#fidkdWxOYHwnPyd1blppbHNgWjAwdGNSNnNKMGo1SHZqalNGX2JQYjdpSzU1dXFoM2tQVEInKSdobGF2Jz9%2BJ2hwbGEnPydLRCcpJ3ZsYSc%2FJ0tEJyknYnBsYSc%2FJ0tEJ3gpJ2dgcWR2Jz9eWCknaWR8anBxUXx1YCc%2FJ3Zsa2JpYFpscWBoJyknd2BjYHd3YHdKd2xibGsnPydtcXF1dj8qKm5qYWwrcXMnKSdpamZkaWAnP2twaWl4JSUl"

# إرسال الطلب
response = requests.post(url, data=card_data)

# التحقق من النتيجة
if response.status_code == 200 and "valid" in response.text.lower():
    print("البطاقة صالحة")
else:
    print("البطاقة غير صالحة")
