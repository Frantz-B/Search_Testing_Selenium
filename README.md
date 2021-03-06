# Search_Testing_Selenium
###Testing search functionality using Selenium framework

**FrantzMoatTest.py** and **MoatPage.py** are the two Python scripts that needs to be downloaded in order to run.  I wrote them in a matter where you will not need to download other libraries but I do assume you have Python 3.5 installed.  This was a solution I created in response to the challenge/test I was given below.

Once you have both files, **FrantzMoatTest.py** is the script that needs to executed.  You can execute with the following command : 
```
python FrantzMoatTest.py -v
```

---

###Challenge Issued:

  The site under test is `www.moat.com`.  I was tasked to write a small handful of Selenium tests in Python to satisfy the following:
* Verify that the _"Try These"_ links are random and that they work.
* Verify that the _"Recently Seen Ads"_ are no more than half an hour old.
* Verify the ad count on the search results page is correct, even if there are multiple pages in the results set.
* Verify the _"Share this Ad"_  feature.

---

###Difficulties I overcame:

* Finding the Right library/class that gave accurate Passes and Fails for a given url.  Originally, I used _'HTTP.client'_ class but the _'urllib'_ class was more effective.
* Dealing with the dynamic grid and not being able to easily find the location of the creatives on said grid was quite challenging. This is because when the mouse cursor goes over a creative, it quickly & automatically displays a popup.  However, after asking for help of which didn't pan out, I did eventually figure it out.  Yea, I was proud...
* After dealing with the 3rd question, the 4th question was rather quick & easy to solve :smirk:.

---
###Manual_Section: :file_folder: contents

Inside this folder are sample test cases based on my exploratory testing of the search section.  This is in the file:

**Sample Test Cases - Search functionality - Moat.txt**

There are a number of bugs I found and I added some personal notes in the file:

**Bugs found, Search Terms, etc.txt**