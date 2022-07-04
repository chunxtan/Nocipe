# Nocipe
A Notion-Bon Appetit recipe clipper, developed for my final project in CS50. 

![Demo GIF](https://github.com/chunxtan/Nocipe/blob/main/Screen%20Recording%202022-07-04%20at%2021.37.48.gif)

## Background
For my final project, I wanted to learn more about APIs and web scraping, while incorporating different topics from the various CS50 projects such as Flask. I also wanted to integrate my learning by developing something that would be useful to me. 

**Web scraping & its limitations**
Initially I had wanted to create a generate an app that would be able to scrape any recipe website that I entered as a value, to populate my notion database with the relevant fields. However, I learnt that web-scraping was not that simple as different websites have different HTML formats and the web app would have to cater to each specific’s website HTML format to function. Hence, I decided to focus on my favourite website, Bon Appetit, as the focus website of this project. 

**Potential trajectories**
I had also considered whether I should delve into Machine Learning for the web scraping portion or Natural Language Processing that would scan the contents of a recipe page & recgonise the required fields to scrape. After reading up on the basics, this proved to be a whole other ballgame and I decided to shelve it for another time.

**Web scraping**
I started off the project learning about basic web-scraping, and decided to go ahead with using Beautiful Soup as Bon Appetit’s website does not have an API. It was a generally smooth process save for the bit on scraping ingredients. Certain ingredients were listed in a descriptive way (e.g. “garlic, crushed or chopped”), which was not ideal for the format I was looking for in the Notion database. Hence, I developed a list of ingredients which I wanted to see, split each web-scraped ingredient string & scanned the latter to see if it appeared in the pre-generated list. At this time, I had also considered using a web-scraper to trawl through BA’s website to retrieve the most used words within the ingredients’ section but decided against it as I have a preferred list of “main” ingredients that I’d like to see in the Notion database as opposed to a general list of food. 

**Adding to Notion**
After cleaning up the results from the webscraper, I was figuring out how to fill up the required fields in the database. Thankfully, Notion has comprehensive documentation on their API though it was primarily in JS. As my app was in Python, I trawled through various tutorials to learn how to use Python to perform basic functionalities with the Notion API. The only frustrating bit of this aspect was that the “multi-select” field of Notion is unable to dynamically iterate over a list, & would instead require a manual input of all “tags” to be inputted. Hence, I decided on passing the ingredients in as a comma-separated list, which can be toggled back into multi-select as tags within Notion.


**Chrome extension**
Having completed the backend & basic front end of the app, I wanted to make the app more convenient to use by making it into a chrome extension. Alas, the same JS-based issue crops up again and I spent a good few weeks trying to figure it out but reaching an impasse in the understanding of modules and using webpack. It is still in the works and the updated code will be uploaded when that is complete. 

## Further development
- Chrome extension
- Notion login page
- Add instructions on readme
- NLP/ML for a more adaptive recipe clipper
