import requests, json, urllib.request
from flask import render_template
from bs4 import BeautifulSoup


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

def createPage(databaseId, headers, titleInput, ingredientsInput, urlInput):
    createUrl = 'https://api.notion.com/v1/pages'

    newPageData = {
        "parent": {"database_id": databaseId},
        "properties": {
            "Name": {
                "title": [
                    {
                        "type": "text",
                        "text": {
                            "content": titleInput
                        }
                    }
                ]
            },
            "Ingredients": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": ingredientsInput
                        }
                    },
                ]
            },
            "Link": {
                "url": urlInput
            }
        }
    }

    data = json.dumps(newPageData)

    res = requests.request("POST", createUrl, headers=headers, data=data)
    return res.status_code

def getImage (urlInput):
    page = urllib.request.urlopen(urlInput)
    soup = BeautifulSoup(page, features="html.parser")

    image = soup.find_all('img')
    img = image[2]['src']
    return img
