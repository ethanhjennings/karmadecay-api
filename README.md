# karmadecay-api
Unofficial Python3 "API" for [karmadecay.com](http://karmadecay.com). This works by scraping the site's HTML.

## Usage
```python
import kdapi

for item in kdapi.check("imgur.com/ndDmnN4"):
    print(item.link)
```

You can use imgur urls, or reddit submission urls.

### Available data
| name        | description                                             |
| ------------|---------------------------------------------------------|
| title       | reddit submission title                                 |
| link        | reddit submission link                                  |
| imgur_link  | non-reddit link                                         |
| user        | submitter username                                      |
| subreddit   | submission subreddit                                    |
| similarity* | percentage similarity to link being checked             |
| time*       | how long ago the submission was made  (ex: "a day ago") |
| score*      | submission sore on reddit                               |
| comments*   | number of comments on submission                        |

*Not always available, will sometimes be set to None

If you really need these values to be guaranteed you can search for the link using [praw](https://github.com/praw-dev/praw).


## Installation
Clone this repo and copy the `kdapi` directory into your project. Make sure you have [lxml](http://lxml.de/) and [requests](http://docs.python-requests.org/en/latest/) installed.
