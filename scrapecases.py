from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import sys
import time
import requests
import pyperclip
import validators

# validating link
LINK = sys.argv[1]
while not (validators.url(LINK)):
    print("Invalid use")
    print("Correct format: $ python3 scrapecases.py https://hspf.debatecoaches.org/Main/AllDocs?view=attachments")
    LINK = input("Enter new link")


# change this if not on Mac - basically what Selenium uses to open webpage
BINARY = FirefoxBinary('/Applications/Firefox.app/Contents/MacOS/firefox-bin')


DRIVER = webdriver.Firefox(firefox_binary=BINARY)
DRIVER.get(LINK)


time.sleep(8)  # wait for load
print("Copying!")

# grabbing all links
LIST_LINKS = DRIVER.find_elements_by_tag_name('a')
docs = []
for link in LIST_LINKS:
    if str(link.get_attribute('href'))[-4:] == "docx":
        docs.append(str(link.get_attribute('href')))

# formatting links for Tab Save
docs = (str(docs)).replace("[", "")
docs = (str(docs)).replace("]", "")
docs = (str(docs)).replace("'", "")
docs = (str(docs)).replace(",", "\n")
pyperclip.copy(docs)
# for case in docs:
#     url = case

#     r = requests.get(url)

#     file_name = url[42:]
#     file_name = file_name.replace("%20", " ")
#     file_name = file_name.replace("/", " ")
#     print(f"downloading {file_name}")
#     with open(file_name, 'wb+') as f:

#         # write the contents of the response (r.content)
#         # to a new file in binary mode.
#         f.write(r.content)
DRIVER.quit()
print("Copied all links, now paste into Tab Save!")
