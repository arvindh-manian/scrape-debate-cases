# What is this for?

This program is supposed to be used to quickly scrape a lot of cases from the wikis (LD/PF/Policy).

# How do I use this?

First, install [python](https://www.python.org/). Next, download everything in the Github repository. Next, open your command line. Navigate to where you downloaded the repository, and run `$ pip install -r requirements.txt`

This will install all of the dependencies needed for the Python script.


Now, you're ready to scrape cases. Open the wiki, go to the page index, go to attachments, and set the parameters however they suit you. Copy the URL, and run `python3 scrapecases.py [url]` without the brackets. Then, open Google Chrome and install the extension [Tab Save](https://chrome.google.com/webstore/detail/tab-save/lkngoeaeclaebmpkgapchgjdbaekacki). Click the extension, and paste in your list of URLs. This will allow chrome to download all of the links at the same time.

# How can I contribute to this project?

This probably won't be maintained tbh. This was just an attempt to get more familiar with web scraping. If you're actually interested in helping, though, open Issues and PRs and I'll try to deal with them.