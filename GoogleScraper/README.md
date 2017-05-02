Generating lists of shady sites for thesis project.

## Prerequisites
Uses [GoogleScraper](https://github.com/NikolaiT/GoogleScraper).

Installation on Ubuntu 14.04:
```
$ sudo apt-get install python3-dev libxml2-dev libxslt1-dev zlib1g-dev
$ virtualenv --python python3 env
$ source env/bin/activate
$ pip install GoogleScraper
```

Next, install the [Firefox driver](https://github.com/mozilla/geckodriver/releases/):
```
$ cd /usr/bin
$ sudo wget https://github.com/mozilla/geckodriver/releases/download/v0.14.0/geckodriver-v0.14.0-linux64.tar.gz
$ sudo tar -xvzf geckodriver-v0.14.0-linux64.tar.gz
$ sudo rm -f geckodriver-v0.14.0-linux64.tar.gz
$ sudo chmod +x geckodriver
```

## Usage
Reads line-separated keywords in `keywords.txt`:
```
$ source env/bin/activate
$ GoogleScraper --keyword-file keywords.txt --output-filename results.json --search-engine google --num-pages-for-keyword 10 --scrape-method selenium --sel-browser firefox
```

This outputs results to an SQLite3 database `google_scraper.db`.
To dump them (while filtering out some obvious non-results), use this query:
```
SELECT `link`
FROM `link`
WHERE (`domain` NOT LIKE '%ebay.%' AND `domain` NOT LIKE '%amazon.%' AND `domain` NOT LIKE '%google.%' AND `domain` NOT LIKE '%youtube.%' AND `domain` NOT LIKE '%reddit.%' AND `domain` NOT LIKE '%quora.%' AND `domain` NOT LIKE '%aliexpress.%' AND `domain` NOT LIKE '%overstock.%' AND `domain` NOT LIKE '%walmart.%' AND `domain` NOT LIKE '%vimeo.%' AND `domain` NOT LIKE '%dailymotion.%' AND `domain` NOT LIKE '%facebook.%' AND `domain` NOT LIKE '%wordpress.%' AND `domain` NOT LIKE '%pinterest.%' AND `domain` NOT LIKE '%yelp.%' AND `link` NOT LIKE '%wiki%' AND `link` NOT LIKE '%blog%' AND `link` NOT LIKE '%forum%')
GROUP BY `domain`;
```
