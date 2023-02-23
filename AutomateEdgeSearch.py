# workable solution to open and search 10 different times
import webbrowser
import time
import pyautogui
# set browser path to be edge
webbrowser.register('edge', None, webbrowser.BackgroundBrowser("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"))
# Get the search term from the user
search_terms = range(15)

# Open the browser and search for the search term
openBrowser = False
for search_term in search_terms:
    if (openBrowser == False):
        webbrowser.get("edge").open("https://www.bing.com/search?q=" + str(search_term))
        openBrowser = True
    else:
        webbrowser.get("edge").open("https://www.bing.com/search?q=" + str(search_term))
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'w')