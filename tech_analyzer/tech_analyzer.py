import requests
from bs4 import BeautifulSoup, Comment

target_url = "https://www.djangoproject.com/"

response=requests.get(target_url)
soup=BeautifulSoup(response.text, "lxml")

print(f'Анализ сайта: {target_url}')
print('-------------------------------------------')

print('[+] Анализ заголовков:')
if 'Server' in response.headers:
    print(f'- Server: {response.headers['Server']}')
else:
    print('- Server ...')
if 'X-Powered-By' in response.headers:
    print(f'- X-Powered-By: {response.headers['X-Powered-By']}')
else:
    print('- X-Powered-By ...')
if 'Set-Cookie' in response.headers:
    print(f'- Set-Cookie: {response.headers['Set-Cookie']}') 
else:
    print('- Set-Cookie ...') 
    
print('\n[+] Анализ HTML-кода:')

meta_tags = soup.find_all('meta')
scripts=soup.find_all('script', src=True)
links=soup.find_all('link')
comment=soup.find_all(string=lambda text: isinstance(text, Comment))

if meta_tags:
    print('\n- МЕТА ТЕГИ: \n')
    for meta_tag in meta_tags:
        print(meta_tag)
else:
    print('- ...')
if 'script' in response.text:
    print('\n- SCRIPTS: \n')
    for script in scripts:
        print(script)
else:
    print('- ...')
if 'link' in response.text:
    print('\n- LINKS: \n')
    for link in links:
        print(link)
else:
    print('- ...')
if  comment:
    print('\n- COMMENTS: \n')
    for com in comment:
        print(com)
else :
    print('- ...')


tech_signatures = {
    "WordPress": ["wp-content", "wordpress"],
    "Django": ["sessionid", "csrftoken", "django"],
    "Cloudflare": ["cloudflare"],
}
text_to_search = (response.text + str(response.headers)).lower()

detected_technologies=[]
for tech_name, keywords in tech_signatures.items():
    for keyword in keywords:
        if keyword in text_to_search:
            detected_technologies.append(tech_name)
            break
        
print("Найденные технологии:", detected_technologies)
    