# GUSOMevals


INSTRUCTIONS

## USE AT YOUR OWN RISK....IT MAY NOT WORK AND IT MIGHT MESS THINGS UP.
## ALSO on a MAC, you have to run chromedriver once before running any script so that it isn't blocked by the security. Like double-click the chromedriver executable. If that gives an error message, ctrl-click the chromedriver.exe fiLe and click open from the menu. Then click open again in the pop-up. Chromedriver will then work for the script.

1. Install Python
2. Install Google Chrome if you don't already have it
2. Check version of chrome and download the correct “chromedriver” version. Check Chrome version by going to chrome settings then "About Chrome" at the bottom of the left side menu. Chromdriver download: (https://chromedriver.chromium.org/downloads). 
4. Install the “selenium” python module using either pip or conda, based on your python install
(ex. pip install -U selenium). Also install "webdriver manager" python module (ex. pip install webdriver-manager)
(might need to install Pip package manager first if you don't have it already)
5. Edit the script with the following (search for “ *** ” to find these lines):
	~~1. Filepath / location of chromedriver on your computer~~
	2. Your netID and password
	~~3. (Not necessary anymore) The last 9 digits of the long id number on the back of your gocard~~
6. Run the python script and just let it do its thing for a while.
7. When the 2FA screen shows up, approve the notification on your phone and then click "trust browser" in the chrome window. The script will give you 20 second to do this before it dies, so approve the 2FA and click "trust" quickly. The script will then continue to finish the evals.
