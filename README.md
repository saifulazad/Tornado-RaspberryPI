# Smart Home 
###Introduction 
This is a Simple project that assist to toggle RaspberryPI GPIO via web browser.

###How it works

* A python web server runs on Raspberry 
* There are as many clients as browsers 
* User interact with browser by toggling switches 
* The server reacts with user inputs
* server pass the value to Raspberry PI 
* Raspberry will response to server input 

###Technology use
* Tornado 
* Raspberry PI 2
* JavaScript 
* Python 
* HTML 
* CSS

###How to run this project 
####prerequisites
* Python 2.7.9 or higher 
* Raspberry PI 2
* 4 LEDs

###Steps

Open raspberry terminal

Type 

```
git clone https://github.com/saifulazad/Tornado-RaspberryPI.git
```
go to repo dir
then type 

```

python -m pip install -r requirements.txt
```
then type 

```

python app.py
```
