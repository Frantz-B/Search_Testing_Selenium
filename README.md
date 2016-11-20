# Search_Testing_Selenium
###Testing search functionality using Selenium framework

**FrantzMoatTest.py** and **MoatPage.py** are the two Python scripts that are needs to be downloaded in order to run.  I wrote them in a matter where you will not need to download other libraries but I do assume you have Python 3.5 installed.  This was a solution I created in response to the challenge/test I was given below.

Once you have both files, **FrantzMoatTest.py** is the script that needs to executed.  You can execute with the following command :
`python FrantzMoatTest.py -v`

---

####Challenge Issued:

  The site under test is `www.moat.com`.  I was to write a small handful of Selenium tests in Python to satisfy the following:
* Verify that the "Try These" links are random and that they work.
* Verify that the "Recently Seen Ads" are no more than half an hour old.
* Verify the ad count on the search results page is correct, even if there are multiple pages in the results set.
* Verify the "Share this Ad"  feature.

---

####Difficulties I overcame:

* Finding the Right library/class that gave accurate Passes and Fails for a given url.  Originally was using 'HTTP.client' but 'urllib' was more effective.
* Dealing with the dynamic grid and not being able to easily find the location of the creatives on said grid because when the mouse went on a creative, it quickly & automatically displayed a popup..  But after asking for help, of which didn't pan out, I did eventually figure it out.  Yea, I was proud..
* After dealing with the 3rd question, 4 question was rather easy to solve and quick :)

---
####Manual_Section: contents

Inside this folder are sample test cases based on my exploratory testing of the search section.  This is in the file **Sample Test Cases - Search functionality - Moat.txt**.  There are a number of bugs I found and added some personal notes in file **Bugs found, Search Terms, etc.txt**.