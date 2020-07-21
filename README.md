# minecraft-modpack-search-tools
This is a very work-in-progress, alpha version of a set of tools I'm developing for working with data about Minecraft mods and modpacks webscraped from Curseforge. Currently, it is only set up to take in a particular mod you want to play with and find a modpack that includes that mod. Then, you can filter and sort that list of modpacks by any metric that is collected by your webscraping.

In its current stage, to use it, you will need to actually alter the code until I eventually get it working with command-line arguments, and maybe eventually a graphical user interface, if I take it that far.

Below, is a gif showing an example of how it should look when it's set up as expected.

## Demo
![](demo1.gif)

## Instructions
```
pip3 install beautifulsoup4
pip3 install selenium
pip3 install lxml
```
Make sure that Google Chrome is installed in the default location it picks on your PC.

Download and install ChromeDriver into a folder of your choosing.
https://chromedriver.chromium.org/downloads

Add the path to your ChromeDriver folder to your Windows path by doing the following:
- Open any File Explorer window.
- Right-click "This PC"
- Click "Properties"
- Click "Advanced system settings"
- Click the "Advanced" tab.
- Click "Environment Variables..."
- In the "System variables" pane, click the "Path" row.
- In the "System variables" pane, click the "Edit..." button.
- Click the "New" button.
- Type or paste the path you chose for your ChromeDriver location.
- Click "OK" when you are finished.

Note: ChromeDriver does not need to be already running in order for the script to work. The script will do that automatically.


```
python3 ./script.py
```
