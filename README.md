# kite-api-autologin

Single file python code to autologin into Kite/ Zerodha API with External TOTP enabled. 
  - This Auto-Logins to Zerodha's Kite Connect API in Pyhton without Selenium Webdriver.
  - It automatically creates the 6-digit 2FA authentication code using pyotp. 
  - You may have to reset your password/ 2FA in zerodha so that you can get your totp_key by clicking "Can’t scan? Copy key" when setting External 2FA TOTP.
  
These are the familiar authentication variables currently stored in keys.py file.
- api_key = ' '
- api_secret = ' '
- user_id = ' '
- user_password = ' '
- totp_key = ' '


Access the kiteconnect object in your strategy using:
- from login import *
- kite = login()
- print(kite.profile())
