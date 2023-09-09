import  requests
from bs4 import BeautifulSoup
import smtplib
import time

while True:
    re = requests.get("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
    res = re.content
    # print(res)
    soup = BeautifulSoup(res,features='html.parser')
    # print(soup.prettify())
    price = float(soup.find('p', class_ = 'price_color').text[1:])
    # **Note:** The `class_` attribute is used to specify the CSS classes of an element in
    # print(price)

    if price < 60:
        smt = smtplib.SMTP('smtp.gmail.com', 587)
        smt.ehlo()
        smt.starttls()
        smt.login('vdarshan859@gmail.com', 'evlmkwabhynegivo')
        smt.sendmail('vdrashan859@gmail.com',
                    'darshanvyas410@gmail.com',
                    f"Subject: Headphoen price drop notifier\n\nHii, price has dropped to {price}.\nBUY IT.")
        smt.quit()
    time.sleep(2)