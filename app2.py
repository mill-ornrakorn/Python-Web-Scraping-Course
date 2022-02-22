

# ########################################################### 4. HTTP Request with Python #########################################################################
print('#'*10, '4. HTTP Request with Python', '#'*10)


# ใช้เว็บนี้
# http://books.toscrape.com/index.html

# การกด ctrl + u จะทำให้เห็น html ของเว็บ
# หรือพิมพ์ view-source: ไว้หน้า URL ก็ได้


# ==================================== 4.2 Python Requests ==================================== 
print('='*20, '4.2  Python Requests', '='*20)

# ใช้ library นี้
# https://docs.python-requests.org/en/latest/

import requests

r = requests.get('http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html') 

print(r) # จะได้ <Response [200]> ออกมา
# print(r.text) ในคลิปสอนไม่ error ระ แต่มา run เองขึ้น error

# ความมหายของ HTTP method (status)
#<Response [200]> : the request is successful
#<Response [404]> : the request is not found ไม่สมบูรณ์
# เพิ่มเติม https://www.geeksforgeeks.org/how-to-troubleshoot-common-http-error-codes/



print('')

# ==================================== 4.3  Requests/Response headers ==================================== 
print('='*20, '4.3 Requests/Response headers', '='*20)


#print(r.headers)

# การระบุ headers ไปจะทำให้เว็บคิดว่าเราใช้browser ในการค้นหา เว็บนั้นจึงจะยอมให้ข้อมูลกับเราครบ 
# ถ้าเราไม่ใส่ headers เว็บจะคิกว่าเรามีแนวโน้มแฮก จึงอาจไม่ให้ข้อมูลครบ

# headers เอามาจากการกด Inspect > Network > ctrl + r > index.html > Header > เลื่อนลงมาล่าง ๆ จะเจอคำว่า User-Agent:
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69'}

print('')



# ########################################################### 5. Web Scraping with Simple Scraping #########################################################################
print('#'*10, '5. Web Scraping with Simple Scraping', '#'*10)

import requests
from lxml import html


r = requests.get('http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html') 
print(r)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69'}

tree = html.fromstring(html=r.text)

title = tree.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/h1/text()')[0] # ใส่ [0] เพราะ return ออกมาเป็น list
print('title: ',title)  # จะได้ ['A Light in the Attic']

price = tree.xpath('//div[@id="content_inner"]/article/div[1]/div[2]/p[1]/text()')[0]
# print('price: ',price)  --- ใช้คำสั่งนี้ไม่มีมีปัญหา ทางแอดมินจึงให้ใช้code ล่างแทน 
# with open ('myfile.txt', 'w', encoding="utf-8") as f:
#     f.write(price) # ต้องไปเปิดไฟล์ FutureSkill\PythonWebScraping\myfile.txt ดู ถึงจะเห็นค่าที่ได้


availability = tree.xpath('//div[contains(@class,"col-sm-6 product_main")]/p[2]/text()')[1].strip( )  # เอาเว้นบรรทัดออก (เป็นการclean data อย่างนึง)
print('availability: ',availability)


description = tree.xpath('//*[@id="content_inner"]/article/p/text()')[0]
print('description: ',description)



print('')


# ==================================== 5.3 Cleaning Data ==================================== 
print('='*20, '5.3 Cleaning Data', '='*20)

# ใช้เว็บนี้
# https://regex101.com/


# เมื่อต้องการดึง ข้อมูลของ availability:  In stock (22 available) โดยจะเอาเฉพาะเลข 22 เท่านั้น สามารถทำได้โดย
# 1. เข้าเว็บ
# 2. ใส่ในช่อง test str. ว่า In stock (22 available)
# 3. ใส่คำสั่งในช่อง Regular expression ว่า \d+ ----------- \d = การดึงตัวเลข หรือ digit ส่วน + เป็นการดึง 2 หลัก

import re  # ย่อมาจาก Regular expression

in_stock = re.compile(r"\d+").findall(availability)[0] # r"\d+" โดย r เป็นการแสดงถึงข้อความที่เป็น Regular expression
print('In stock:' ,in_stock)


book_information = {
    'title': title,
    'price': price, 
    'availability': in_stock, #เปลี่ยนเป็น in_stock แทน availability
    'description': description
}

#print(book_information)  ขอไม่ print เพราะเหมือนจะerror ตรง price นะ ไว้อ่านทีเดียวตอน 5.4 เลย

print('')


# ==================================== 5.4 Json / CSV file ==================================== 
print('='*20, ' 5.4 Json / CSV file', '='*20)


# --------------------- json --------------------- 
print('-'*15, 'json', '-'*15)

import json 

def write_to_json(filename, data):
    f = open(filename, 'w') # เปิดไฟล์
    f.write(json.dumps(data))  # เขียนไฟล์
    f.close # ปิดไฟล์


write_to_json('book_information.json', book_information)
# ต้องไปเปิดไฟล์ FutureSkill\PythonWebScraping\book_information.json ดู ถึงจะเห็นค่าที่ได้


print('')

# --------------------- CSV --------------------- 
print('-'*15, 'CSV', '-'*15)

import csv

def write_to_csv(filename, data):
    headers = ['title','price','availability','description']
    with open(filename, 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f,headers) # จะเขียน headers เป็นส่วนแรก
        writer.writeheader() # เขียน headers
        writer.writerow(data) # เขียนข้อมูลในแนว row


write_to_csv('book_information.csv', book_information)
# ต้องไปเปิดไฟล์ FutureSkill\PythonWebScraping\book_information.csv ดู ถึงจะเห็นค่าที่ได้

print('')