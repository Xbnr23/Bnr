import requests

# قائمة البطاقات
cards = [
    {"card_number": "4111111111111111", "expiry_month": "12", "expiry_year": "2024", "cvv": "123"},
    {"card_number": "5500000000000004", "expiry_month": "06", "expiry_year": "2025", "cvv": "456"},
    {"card_number": "340000000000009", "expiry_month": "09", "expiry_year": "2026", "cvv": "789"}
]

# بوابة دفع وهمية
url = "https://example-payment-gateway.com/validate_card"

# التحقق من كل بطاقة
for card in cards:
    response = requests.post(url, data=card)
    if response.status_code == 200 and "valid" in response.text.lower():
        print(f"البطاقة صالحة: {card['card_number']}")
    else:
        print(f"البطاقة غير صالحة: {card['card_number']}")
