from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

driveroptions = Options()
driveroptions.use_chromium = True
driveroptions.add_argument("--headless")
driveroptions.binary_location = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

service = Service("c:\\drivers\\msedgedriver.exe")
driver = webdriver.Edge(options=driveroptions, service=service)

url = "https://bing.com"
driver.get(url)

wait = WebDriverWait(driver, 10)
men_menu = wait.until(ec.visibility_of_element_located((By.XPATH, 
"/html/body/div[7]/div[2]/div/div[1]/div[3]/div/div/section[2]/div/div[2]/div/div/blockquote"))).text

# I modified the text here to allow for testing the email. Remove "not" to match the current text.
textToChange = "Vaccination appointments are not currently FULL"

if textToChange in men_menu:
    print("Found it. Not able to get an appointment yet.")
else: 
    emailText = "You can make an appt now."
    emailHTML = "Here is the <a href='foo.htm'>link</a>."

    emailFrom = "johnjansen@live.com"
    emailTo = "jncjansen@msn.com"

    msg = MIMEMultipart('alternative')
    msg.attach(MIMEText(emailText, 'plain'))
    msg.attach(MIMEText(emailHTML, 'html'))
    
    msg['From'] = emailFrom
    msg['To'] = emailTo
    msg['Subject'] = "Testing things"

    s = smtplib.SMTP("smtp.live.com",587)
    s.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
    s.starttls() #Puts connection to SMTP server in TLS mode
    s.ehlo()
    # for this, you'll want to use your real password
    # when I did that, I got a prompt from Authenticator on my phone with an "App" password to use
    # so I entered that here
    pword = "GET YOUR PASSWORD"

    s.login(emailFrom, pword)

    s.sendmail(emailFrom, emailTo, msg.as_string())

    s.quit()

driver.quit()

