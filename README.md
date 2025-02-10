# درگاه پرداخت Seppy

Seppy یک پکیج پایتون برای ادغام با **درگاه پرداخت سامان (SEP)** است. این پکیج توابعی ساده برای تولید لینک پرداخت، تایید تراکنش و بازگرداندن تراکنش فراهم می‌کند.

## ویژگی‌ها
- تولید لینک پرداخت برای کاربران.
- بررسی وضعیت تراکنش.
- بازگردانی تراکنش در صورت لزوم.

## نصب

برای نصب این پکیج از pip استفاده کنید:
```bash
pip install seppy
```

## تنظیمات
قبل از استفاده از این پکیج، مقادیر زیر را در فایل تنظیمات Django (`settings.py`) اضافه کنید:

```python
SEPPY_TERMINAL_ID = "your_terminal_id"
SEPPY_PRIVATE_KEY_ADDRESS = "./private_key.pem"
# SEPPY_BASE_DOMAIN = "proxy.doamin.com"  # اختیاری، برای ارسال پیام‌ها به سرور واسط استفاده می‌شود
```

## استفاده

ابتدا توابع مورد نیاز را وارد کنید:

```python
from seppy import get_payment_link, verify_transaction, reverse_transaction
```

### 1. دریافت لینک پرداخت
از این تابع برای تولید لینک پرداخت و هدایت کاربران به درگاه بانک سامان استفاده کنید:

```python
payment_data = get_payment_link(
    amount=100000,  # مبلغ به ریال
    redirect_url="https://yourwebsite.com/payment/callback",
    phone_number="09123456789",
    res_number="123456"
)

if payment_data["status"] == 1:
    print("آدرس پرداخت:", payment_data["url"])
else:
    print("خطا:", payment_data["errorDesc"])
```

### 2. تایید تراکنش
پس از انجام پرداخت، می‌توانید وضعیت تراکنش را با شماره مرجع بررسی کنید:

```python
success, message = verify_transaction("REF123456")
if success:
    print("تراکنش با موفقیت تایید شد")
else:
    print("خطای تایید:", message)
```

### 3. بازگردانی تراکنش
در صورت نیاز، می‌توانید تراکنش را با شماره مرجع بازگردانی کنید:

```python
success, message = reverse_transaction("REF123456")
if success:
    print("تراکنش با موفقیت بازگردانی شد")
else:
    print("خطای بازگردانی:", message)
```

## مدیریت خطاها
هر تابع پیام‌های خطای دقیقی را برای کمک به اشکال‌زدایی ارائه می‌دهد. حتماً خطاها را به درستی مدیریت کنید.

## مجوز
این پکیج تحت مجوز MIT منتشر شده است.

## مشارکت
پیشنهادات و درخواست‌های اصلاحی استقبال می‌شود. لطفاً قبل از ایجاد تغییرات عمده، یک Issue باز کنید.

## تماس
برای پشتیبانی با ایمیل [freecyberhawk@gmail.com](mailto:freecyberhawk@gmail.com) تماس بگیرید.


---

# Seppy Payment Gateway

Seppy is a Python package for integrating with **Saman Bank (SEP) Payment Gateway**. It provides easy-to-use functions for generating payment links, verifying transactions, and reversing transactions.

## Features
- Generate a payment link for users to complete their payment.
- Verify a transaction status.
- Reverse a transaction when necessary.

## Installation

Install the package using pip:
```bash
pip install seppy
```

## Configuration
Before using the package, add the following settings to your Django settings file (`settings.py`):

```python
SEPPY_TERMINAL_ID = "your_terminal_id"
SEPPY_PRIVATE_KEY_ADDRESS = "./private_key.pem"
# SEPPY_BASE_DOMAIN = "proxy.doamin.com"  # Optional, used for sending messages to an intermediary server
```

## Usage

First, import the required functions:

```python
from seppy import get_payment_link, verify_transaction, reverse_transaction
```

### 1. Get Payment Link
Use this function to generate a payment link that redirects users to the Saman Bank payment gateway.

```python
payment_data = get_payment_link(
    amount=100000,  # Amount in Rials
    redirect_url="https://yourwebsite.com/payment/callback",
    phone_number="09123456789",
    res_number="123456"
)

if payment_data["status"] == 1:
    print("Payment URL:", payment_data["url"])
else:
    print("Error:", payment_data["errorDesc"])
```

### 2. Verify a Transaction
After the payment is completed, you can verify the transaction using the reference number.

```python
success, message = verify_transaction("REF123456")
if success:
    print("Transaction Verified Successfully")
else:
    print("Verification Failed:", message)
```

### 3. Reverse a Transaction
If necessary, you can reverse a transaction using its reference number.

```python
success, message = reverse_transaction("REF123456")
if success:
    print("Transaction Reversed Successfully")
else:
    print("Reversal Failed:", message)
```

## Error Handling
Each function returns meaningful error messages to help with debugging. Make sure to handle exceptions properly.

## License
This package is released under the MIT License.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss your ideas.

## Contact
For support, contact [freecyberhawk@gmail.com](mailto:freecyberhawk@gmail.com).

