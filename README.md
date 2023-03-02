# Sneaker-Scraper-Restocks-Discord
A Scraper for all prices and sizes of a sneaker on the reselling website Restocks.
The scraper will return a message in your Discord chanel with a list of all sizes and prices + the product url for Restocks, StockX and Hypeboost.

# Requirements:
1. Check if you have all the needed Python libraries.

+ requests (pip install requests)
+ json (pip install json)
+ BeautifulSoup (pip install beautifulsoup4)
+ Discord (pip install discord.py)
+ selenium (pip install selenium)

--> to install them just write the pip install... command in your Terminal.


# Chrome Driver
Please Check that you have the same version of the chrome driver in the folder with the scraper files as your main chrome is!
To check that go to "chrome://settings/help" and click on "About Chrome".
After that go to https://chromedriver.chromium.org/downloads and download the right version.
If your version isn't the same as in the Folder, just download your version and replace the chrome-driver file.
In the folder is the version: ChromeDriver 110.0.5481.77

2. Open "Config" file and input your Discord Bot Token.

3. Open and run the "discord_embed" file. (best for this is VS-Code in my opinion)

4. Write the keyword ($restocks) + SKU in your discord server.
   format: $restocks SKU --> (example: $scrape CW1590-100)


The Scraper will now send you all listed sizes and their prices in the discord channel.
Also the Restocks Product URL is in the blue title.
At the bottom of the discord message you can also find the StockX and Restocks Product URL to the Scraped Product.

# Return Message Example:
The return message looks like this:

![Restocks-message-github](https://user-images.githubusercontent.com/103487648/221952547-676ef432-cced-4e03-9970-c0ac6a80f4c8.png)
