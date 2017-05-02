Code for thesis project, 2016-2017.

## Components
Core components:
* `OpenWPM/` - Web crawler, built on [OpenWPM](https://github.com/citp/OpenWPM).
* `mailserver/` - Mail server.

Other tools:
* `alexa-scraper/` - For scraping [Alexa Top Sites by Category](http://www.alexa.com/topsites/category).
* `GoogleScraper/` - For generating lists of shady sites to crawl, using [GoogleScraper](https://github.com/NikolaiT/GoogleScraper).
* `WebCensusNotebook/` - For pulling data from the [Princeton Web Census](https://webtransparency.cs.princeton.edu/webcensus/).

## Usage
### System Requirements
* The framework is fully tested only on Ubuntu 16.04, and requires Java and
  Python runtime environments.
* The processes (described below) can be run on separate machines. The mail
  server is OS-independent, but the web crawler only runs on Linux.
* Depending on the number of registered sites, the mail server might store
  anywhere from a few hundred megabytes to tens of gigabytes of data on disk
  per month.

### Processes
The system consists of three long-running processes:
* The mail server, which receives, stores, and analyzes incoming mail.
  ```
  $ cd mailsever
  $ mvn clean package
  $ java -jar target/mailserver.jar
  ```
* The web crawler, which crawls a list of input sites.
  ```
  $ cd OpenWPM
  $ python crawl.py
  ```
* An OpenWPM script, which polls the mail server for links in emails to visit.
  ```
  $ cd OpenWPM
  $ python visit.py
  ```
Multiple instances of the web crawler and OpenWPM script can be run in parallel
to speed up execution.

### SMTP Configuration
Running the mail server requires a domain name with MX records pointing to the
server. Additionally, if running the web crawler or OpenWPM script from machines
other than the mail server's machine, host records (A, CNAME) must also be set.

### Input Sites
Some input site lists are included in `OpenWPM/data/`. To crawl other lists,
either generate them with the provided tools or supply your own, then edit
`OpenWPM/crawl.py` to have the web crawler read the new files.
