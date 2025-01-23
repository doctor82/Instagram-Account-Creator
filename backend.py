from curl_cffi import requests
import time
import random

import names
import faker
import maillol as mailtm
from datetime import datetime
import sys
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
SUCCESS_LEVEL_NUM = 25  # A level between INFO (20) and WARNING (30)
logging.addLevelName(SUCCESS_LEVEL_NUM, "SUCCESS")

# Define a method to log at the SUCCESS level
def success(self, message, *args, **kwargs):
    if self.isEnabledFor(SUCCESS_LEVEL_NUM):
        self._log(SUCCESS_LEVEL_NUM, message, args, **kwargs)

logging.Logger.success = success
i = 36
j = 6
k = i ** j

def p():
    a = format(random.randint(0, k - 1), 'x')  
    # Ensure the result is exactly 6 characters long
    j = '0' * (6 - len(a)) + a  # Pad with leading zeros if the length is less than 6
    return j[-6:]  # Take exactly the last 6 characters


session = requests.Session(impersonate =None,
akamai = "1:65536;2:0;4:131072;6:262144|8290305|0|m,s,a,p",
extra_fp = {
                "tls_signature_algorithms": [
                    "ecdsa_secp256r1_sha256",
                    "rsa_pss_rsae_sha256",
                    "rsa_pkcs1_sha256",
                    "ecdsa_secp384r1_sha384",
                    "rsa_pss_rsae_sha384",
                    "rsa_pkcs1_sha384",
                    "rsa_pss_rsae_sha512",
                    "rsa_pkcs1_sha512"
                ],
                
}

)
web_dimensions = [
    "1920x1080", "1366x768", "1280x720", "1440x900", "1600x900", "1536x864", "1280x800", 
    "1024x768", "2560x1440", "3840x2160", "1680x1050", "1280x1024", "1360x768", "1440x1080", 
    "768x1024", "800x600", "1920x1200", "1360x1024", "2560x1600", "3200x1800", "1680x945", 
    "1024x576", "800x480", "1152x864", "2560x1080", "1280x854", "1440x1280", "1080x1920", 
    "1600x1200", "1024x600", "1280x480", "1400x1050", "1440x2560", "1440x720", "800x1280", 
    "1600x1200", "1600x768", "1280x960", "1360x768", "1920x1440", "1920x1600", "1680x1200", 
    "1440x768", "2048x1152", "1440x900", "1600x1024", "2560x1920", "1366x1024", "1024x800", 
    "2560x1080", "1400x900", "1920x1080", "1280x768", "1360x960", "1440x1280", "1024x768", 
    "1280x1024", "2048x1080", "2560x720", "1280x1024", "1024x768", "640x480", "320x240", 
    "1920x800", "1600x700", "1280x1024", "1200x800", "1600x768", "1680x720", "1280x640", 
    "800x640", "2560x1440", "1366x768", "1920x1440", "1440x800", "1600x800", "2560x1600", 
    "1440x960", "1280x1024", "1024x768", "1440x810", "1360x768", "1920x1080", "2560x1440", 
    "1600x1200", "1366x1024", "1920x1200", "1440x800", "1280x1024", "1024x768", "1600x1280", 
    "2560x1440", "1920x1080", "1600x1200", "1440x1050", "1920x1440", "1366x900", "1440x1600"
]
wd = random.choice(web_dimensions)

session.cookies['wd'] = wd
proxy = random.choice(open("proxy.txt", "r").readlines()).strip()
cookie_header = '; '.join([f"{key}={value}" for key, value in session.cookies.items()])
session.proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
session.headers =  {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'cookie':cookie_header ,
    'dpr': '1',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="131.0.6778.265", "Chromium";v="131.0.6778.265", "Not_A Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'viewport-width': wd.split('x')[0],
}
response = session.get('https://www.instagram.com/')

cookie_header = '; '.join([f"{key}={value}" for key, value in session.cookies.items()])
session.headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'cookie':cookie_header,
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/accounts/emailsignup/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="131.0.6778.265", "Chromium";v="131.0.6778.265", "Not_A Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-asbd-id': '129477',
    'x-csrftoken': session.cookies['csrftoken'],
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-kl-kfa-ajax-request': 'Ajax_Request',
    'x-requested-with': 'XMLHttpRequest',
    'x-web-device-id': session.cookies['ig_did'],
    'x-web-session-id':':'.join([p(), p(), p()])
}
response = session.get('https://www.instagram.com/api/v1/web/login_page/')


mailtmapi = mailtm.MailTmApi()
mail_details = mailtmapi.get_random_mail(mailtmapi.get_random_avaible_domain())
email = mail_details["email"]

email_password = mail_details["password"]
mail_token = mail_details["token"]
firstname=names.get_first_name()
UserName=firstname+email.split('@')[0]+wd
name_surname = faker.Faker().name()
nickname = name_surname.replace(" ", "").lower() + str(random.randint(100000, 999999))[:30]
logging.info(f'{nickname} | Email Generated: {email}')
data = {
    'enc_password':f'#PWD_INSTAGRAM_BROWSER:0:{int(datetime.now().timestamp())}:{email_password}',
    'email': email,
    'failed_birthday_year_count': '{}',
    'first_name': firstname,
    'username': nickname,
    'opt_into_one_tap': 'false',
    'seamless_login_enabled': '1',
    'use_new_suggested_user_name': 'false',
    'client_id' : session.cookies['mid']
}

response = session.post(
    'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/',

    data=data,
)


if 'fail' == response.json()['status']:
    flag = True
else:
 flag = False
bday = str(random.randint(1, 25))
bmonth = str(random.randint(1, 12))
byear = str(random.randint(1980, 2003))
data = {
            'day': bday,
            'month': bmonth,
            'year': byear, }
response = session.post(
            'https://www.instagram.com/api/v1/web/consent/check_age_eligibility/',
            data=data,
)
data = {
            'device_id': session.cookies['mid'],
            'email': email,
}

response = session.post(
            'https://www.instagram.com/api/v1/accounts/send_verify_email/',
            data=data,
)

logging.info(f'{nickname} | Email sent successfully : {email}')
while True:
        time.sleep(1)
        mails = mailtmapi.get_emails(mail_token)
        if mails != []:
                mail_code = mails[0]['subject'].split(" ")[0]
                break
data = {
            'code': mail_code,
            'device_id': session.cookies['mid'],
            'email': email,
}
logging.info(f'{nickname} | {email} - {mail_code}')
response = session.post(
            'https://www.instagram.com/api/v1/accounts/check_confirmation_code/',
            data=data,
)
signup_code = response.json()["signup_code"]
extra_session_id = ':'.join([p(), p(), p()])

data = {
            'enc_password':f'#PWD_INSTAGRAM_BROWSER:0:{int(datetime.now().timestamp())}:{email_password}',
            'day': bday,
            'email': email,
            'first_name': nickname,
            'month': bmonth,
            'username': nickname,
            'year': byear,
            'client_id':session.cookies['mid'],
            'seamless_login_enabled': "1",
            'tos_version': 'row',
            'force_sign_up_code': signup_code,
            "extra_session_id":extra_session_id
}

response = session.post(
            'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/',
            data=data,
)

if '"account_created":true' in response.text:
  logging.info(f'{nickname}:{email_password} Generated Successfully')

  with open('accounts.txt','a') as f:
        f.write(nickname+':'+email+':'+email_password+'|'+proxy+'\n')
