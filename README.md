# imgur_fav_downloader
A python script that downloads the favorites on imgur

REQUIREMENTS
---
Python 3 (https://www.python.org/downloads)

You have to register an application on imgur to get access to the API.
https://api.imgur.com/oauth2/addclient
Select OAuth 2.0 with callback URL and fill the rest. 
then you will get the information via email.

INSTALLATION
---
```shell
git clone https://github.com/hahahannes/imgur_fav_downloader.git
cd imgur_fav_downloader
python3 setup.py develop 
```

USAGE
---
```shell
python3 main.py 
```

Type the client id and secret, that you get from imgur and your username.
Copy aqnd paste the url that shows up and login to imgur.
Copy and paste the PIN from the website, where you get redirected, to the script.
The images will be downloaded in the imgs folder.

TODOs
---
Using to download saved links on reddit

LICENSE
---
The MIT License (MIT)
Copyright (c) <2016>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.




