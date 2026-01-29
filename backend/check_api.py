import requests
import time
import sys

url_root = 'http://127.0.0.1:5000/'
url_translate = 'http://127.0.0.1:5000/translate'

for i in range(20):
    try:
        r = requests.get(url_root, timeout=1)
        print('GET / ->', r.status_code)
        break
    except Exception as e:
        time.sleep(0.5)
else:
    print('Failed to connect to', url_root)
    sys.exit(1)

try:
    r = requests.post(url_translate, json={'text':'hello','source_lang':'en','target_lang':'kn'}, timeout=5)
    print('POST /translate ->', r.status_code, r.json())
except Exception as e:
    print('POST /translate error:', e)
    sys.exit(1)
