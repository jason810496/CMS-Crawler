# CMS Crawler

[中文]()
## Contest Management System Crawler

A cli tool for **stress testing** [CMS(Contest Management System)](https://github.com/cms-dev/cms) Competitive Programming online judge.

## Requirements
```
pip3 install requirements.txt
```
- `python-dotenv`
- `bs4`
- `requests`

## Usage
use defult `.env` setting:
```
python3 cms-crawler.py
```

change setting by command line:
```
python3 cms-crawler.py --file data.csv -v
```

available arguments:
```
usage: cms-crawler.py [-h] [-v] [-f FILE] [-t THREAD_LIMIT] [--host HOST]

options:
  -h, --help            show this help message and exit
  -v, --verbose         increase output verbosity
  -f FILE, --file FILE  csv file with user,password,question,filename ( defult:
                        testing.csv )
  -t THREAD_LIMIT, --thread-limit THREAD_LIMIT
                        set thread limit ( defult 20 thread )
  --host HOST           set host ( Host also can be set in .env file )
```

## Testing Data
Testing data must be stored in a CSV file in the following format: `USER, PASSWORD, QUESTION_NAME, SUBMIT_FILE`.

## Example

Command : 

```
python3 cms-crawler.py --file data.csv --host https://oj.cms.mywebsite.judge -v
```

CSV file : 
```
user1,password1,PA,submission/a.cpp
user2,password2,PB,submission/while.cpp
user3,password3,PA,submission/a.cpp
jason,jasonIsMe,PC,submission/a.cpp
bob,yoyo,PA,submission/while.cpp
```