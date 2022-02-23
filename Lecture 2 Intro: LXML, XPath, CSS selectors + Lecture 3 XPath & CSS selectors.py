from lxml import etree

# ########################################################### 2. Intro: LXML, XPath, CSS selectors #########################################################################

print('#'*10, '2. Intro: LXML, XPath, CSS selectors', '#'*10)

# etree.parse เป็นการดึงข้อมูลจากเว็บ 
tree = etree.parse(" **อย่าลืมเปลี่ยน Path เป็น web_page.html ** ") 
#print(tree) # จะ print ได้ <lxml.etree._ElementTree object at 0x0000023640310540>


# ==================================== LXML ==================================== 
print('='*20, '2.1 LXML', '='*20)

# ------- เกี่ยวกับ find() ------- 
# จะได้ 1 คำตอบ ข้อเสียคือดึงได้เฉพาะอันแรกที่เจอ

# ต้องการดึงชื่อ <title>
title_element = tree.find('head/title')
#print(title_element)  # จะ print ได้ <Element title at 0x1534b8eaac0>
print('LXML title element: ',title_element.text) # ใส่ .text เพื่อจะได้แสดงเป็น text ออกมา


# ต้องการดึง <p> 
body_element = tree.find('body/p')
print('LXML body element: ',body_element.text)


# ------- เกี่ยวกับ findall() ------- 
# จะได้ทุกคำตอบ 

list_item = tree.findall("body/ul/li")
# print(list_item.text) ใช้งานไม่ได้เนื่องจากเป็น list 
# ต้องใช้ for 
for li in list_item:
    a = li.find('a')

    if a is not None:
        # print อีกแบบที่อ. ใช้
        # print('LXML list item: ', f"{li.text.strip()} {a.text}")  
        # .strip() เป็นการตัดช่องว่างทั้งหมด
        print('LXML list item: ', li.text.strip(), a.text)

    else:
        print('LXML list item: ',li.text)


print('')

# ==================================== Intro: XPath ==================================== 
# มีจุดเด่นคือช่วยย่อ Code ได้

print('='*20, '2.2 Intro: LXML & XPath', '='*20)

# การใช้ //
title_element = tree.find('//title')
print('XPath title element: ',title_element.text)


body_element = tree.find('//p')
print('XPath body element: ',body_element.text)


# การใช้ text() ทำให้ไม่ต้องใส่.text ใน print
body_element = tree.xpath('//p/text()')[0]  # [0] คือ list index ที่ 0 ถ้าเอาออกจะได้ ['FutureSkill']
print('XPath body element: ',body_element)


list_item = tree.xpath("//li")
#print('XPath list item: ',list_item)
for li in list_item:
    # map() เป็นการ map ก้อน str.strip เข้ากับ li.xpath('.//text()')
    # .//text() โดย . เป็นการทำให้path ต่อเนื่องขึ้น มีการค้นหาไปข้างใน
    #text = map(str.strip, li.xpath('.//text()'))  
    
    # ใช้ list() เพราะต้องการรองรับค่าที่ออกมากจาก map() โดย map() จะ return เป็นobj
    #print('XPath list item: ',list(text)) 

    # แบบ .join() 
    text = ''.join(map(str.strip, li.xpath('.//text()')))
    print('XPath list item: ',text) # ใส่แบบนี้ได้เลย เพราะ .join() จะ return เป็นtext


print('')

# ==================================== Intro: CSS selectors ==================================== 
# ไม่ต้อง import เพราะ CSS selectors ทำงานร่วมกับ LXML อยู่แล้ว (แต่ไม่ได้อยู่ใน LXML)

print('='*20, '2.3 Intro: LXML & CSS selectors', '='*20)

tree = etree.parse("D:\_Mill\Works_education\Higher\_Workshop\FutureSkill\PythonWebScraping\CODE\src\web_page.html")

# ต้องมีตัวแปรแบบนี้(ไม่แน่ใจว่า.getroot() คืออะไร) มารับ ถึงจะใช้ CSS selectors ได้
html = tree.getroot()


title_element = html.cssselect("title")[0] # [0] คือ list index ที่ 0
print('CSS selectors title element: ', title_element.text)


list_item = html.cssselect("li")
#print('CSS selectors list item: ', list_item.text)
for li in list_item:
    a = li.cssselect('a')

    if len(a) == 0: # len(a) == 0 แปลว่า ไม่มี a ก็ได้ เพราะความยาว = 0
        print('CSS selectors list item: ', li.text)
    
    else: # มี a 
        print('CSS selectors list item: ', li.text.strip(), a[0].text)


print('')

# ########################################################### 3. XPath & CSS selectors #########################################################################

print('#'*10, '3. XPath & CSS selectors', '#'*10)

# ==================================== 3.1 CSS selectors ==================================== 
print('='*20, '3.1 CSS selectors', '='*20)

# ใช้เว็บ https://try.jsoup.org/
# โดยใช้ไฟล์ตัวอย่างจาก src/CSS_Selectors_simplified.html

print('คำสั่ง Select ') 

# การค้นหาสามารถใส่แค่ชื่อ tag หรือ element ก็ได้เลย เช่น p, div, span

# การค้นหาเจาะจง class จะใช้ .ชื่อclass
# การค้นหาเจาะจง id จะใช้ #ชื่อid

# a[href^='http']                      // ^ เป็น search ที่ระบุจากตัวแรก ว่า http  
# a[href$='fr']                        // $ เป็น search ที่ระบุจากตัวท้าย ว่า fr
# a[href*='google']                    // * เป็น search ที่ระบุจากตรงไหนก็ได้ ว่า google

# div.into p                           // จะแสดงข้อมูลแต่ละ p ออกมา
# div.into p, span#location            // จะแสดงข้อมูลแต่ละ p และแสดงspan id = location ออกมา 
#                                         โดยในที่นี้การแสดง 2 อย่างร่วมกันจะต้องอยู่ใน parent เดียวกันเท่านั้น ซึ่งก็คือ div.into

# div.into > p                         // จะแสดงข้อมูลแค่ p ออกมา

# div.into + p                         // จะแสดงข้อมูล p ที่ติดอยู่ข้าง ๆ div.into ออกมา

# li:nth-child(1)                      // จะแสดงข้อมูล li ตัวที่ 1 ออกมา    ---- เพิ่มเติม: index ของ css select จะเริ่มที่ 1
# li:nth-child(1), li:nth-child(2)     // จะแสดงข้อมูล li ตัวที่ 1 และ 2 ออกมา
# li:nth-child(even)                   // จะแสดงข้อมูล li ลำดับเลขคู่ ออกมา
# li:nth-child(odd)                    // จะแสดงข้อมูล li ลำดับเลขคี่ ออกมา

print('')

# ==================================== 3.2 XPath ==================================== 
print('='*20, '3.2 XPath', '='*20)

# ใช้เว็บ https://scrapinghub.github.io/xpath-playground/
# โดยใช้ไฟล์ตัวอย่างจาก src/XPath_Selectors_simplified.html

print('คำสั่ง') 

# เนื่องจากจะ return ออกมาเป็น ele จึงต้องใส่ text() ไปทำให้เป็นtext

# //div[@class = "intro"]                                       -- เจาะจงไปที่ class="intro"
# //div[@class = "intro"]/p                                     -- เจาะจงไปที่ class="intro" และเข้าถึง p ที่อยู่ในclassนี้

# //div[@class = "intro" or @class = "outro"]/p/text()          -- เจาะจงไปที่ class="intro" และ class = "outro" และเข้าถึง p ที่อยู่ในทั้ง 2 class นี้
 
# //a/@href                                                     -- จะแสดง www. ออกมา                       
# //a[starts-with(@href,'https')]                               -- ค้นหาใน a โดยอยู่ที่ @href ขึ้นต้นด้วย https  
# //a[ends-with(@href,'fr')]                                    -- ค้นหาใน a โดยอยู่ที่ @href ลงท้ายด้วย fr
# //a[contains(@href,'google')]                                 -- ค้นหาใน a โดยอยู่ที่ @href ตรงไหนก็ได้ด้วย google
# //a[contains(text(),'Google')]                                -- ค้นหาใน a โดยอยู่ที่ text() ตรงไหนก็ได้ด้วย google

# //ul[@id = "items"]                                           -- เข้าถึง list
# //ul[@id = "items"] / li[1]                                   -- เข้าถึง list ตัวที่ 1
# //ul[@id = "items"] / li[position() = 1 or position() = 4 ]   -- เข้าถึง list ตัวที่ 1 และ 4
# //ul[@id = "items"] / li[position() = last() ]                -- เข้าถึง list ตัวสุดท้าย
# //ul[@id = "items"] / li[position() > 1 ]                     -- เข้าถึง list ตัวที่มากกว่า 1
# //ul[@id = "items"] / li[position() < 2 ]                     -- เข้าถึง list ตัวที่มากกว่า 1

print('')

# ------------------ 3.2.1 Navigating using XPath (Going UP) ------------------------- 
print('-'*10, '3.2.1 Navigating using XPath (Going UP)', '-'*10)

# Navigating using XPath (Going UP) คือ การเริ่มจากข้างในออกมาข้างนอก   


print('คำสั่ง Navigating using XPath (Going UP)') 

# //p[@id = "outside"] /parent::div                             -- :: คือการระบุชนิดของtag  /parent::div เป็นการระบุเจาะจงไปที่ parent div
# //p[@id = "outside"] /parent::node()                          -- node() ใช้เมื่อไม่รู้ parent

# //p[@id = "unique"] /ancestor::node()                         -- /ancestor::node() จะมอง parent ของ parent ไปเรื่อย ๆ จนหมด ดังนี้ <p id="unique"> 
#                                                                   มีparent คือ <div class="outro"> ... <body> มี parent คือ <html lang="en">ฃ
# //p[@id = "unique"] /ancestor-or-self::node()                 -- -or-self ใส่เมื่อต้องการให้แสดงตัวเองด้วย

# //p[@id = "unique"] /preceding::node()                        -- preceding คล้าย ๆ ancestor แต่เป็นการระบุทั้งสิ่งที่อยู่ใน parent ด้วย (ญาติพี่น้อง)
# //p[@id = "unique"] /preceding::h1                            -- จะแสดง h1 ที่มาก่อนมัน
# //p[@id = "outside"] /preceding-siblings::node()              -- จะตัวที่มาก่อน p[@id = "outside"]

print('')


# ------------------ 3.2.2 Navigating using XPath (Going DOWN) ------------------------- 
print('-'*10, '3.2.2 Navigating using XPath (Going DOWN)', '-'*10)

# Navigating using XPath (Going DOWN) คือ การเริ่มจากข้างนอกมายังข้างใน   


print('คำสั่ง Navigating using XPath (Going DOWN)') 

# //div[@class = "intro"] /child::p                            -- มองลงมาใน p ที่เป็น child
# //div[@class = "intro"] /child::node()                       -- ใช้ node() เมื่อไม่รู้ว่ามี node() อะไรบ้าง

# //div[@class = "intro"] /following::node()                   -- /following จะแสดงหลังจากตัวมันเอง
# //div[@class = "intro"] /following-siblings::node()          -- จะแสดงตัวที่ติดกัน (อยู่ในระดับเดียวกัน)

# //div[@class = "intro"] /descendant::node()                  -- /descendant จะแสดงลูกของ@class = "intro" และลูกของลูก @class = "intro" ไปเรื่อย ๆ 


print('')
