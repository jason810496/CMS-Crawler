<div align="center">
<h1>CMS Crawler</h1>
<a href="https://github.com/jason810496/CMS-Crawler">English</a>
</div>

## Contest Management System Crawler

用來 **壓力測試** [CMS(Contest Management System)](https://github.com/cms-dev/cms) 線上競賽系統的 CLI 工具

## 套件需求
```
pip3 install requirements.txt
```
- `python-dotenv`
- `bs4`
- `requests`

## 使用方法
用預設的 `.env` 訂定:
```
python3 cms-crawler.py
```

用 command line 更改設置:
```
python3 cms-crawler.py --file data.csv -v
```

可用的參數:
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

## 測試資料
測試資料必須以該形式 : `USER, PASSWORD, QUESTION_NAME, SUBMIT_FILE` 存成 CSV 檔

## 範例

Command : 

```
python3 cms-crawler.py --file data.csv --host https://oj.cms.mywebsite.judge -v
```

CSV 檔 : 
```
user1,password1,PA,submission/a.cpp
user2,password2,PB,submission/while.cpp
user3,password3,PA,submission/a.cpp
jason,jasonIsMe,PC,submission/a.cpp
bob,yoyo,PA,submission/while.cpp
```