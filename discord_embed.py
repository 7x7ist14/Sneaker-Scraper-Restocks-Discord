import discord
import datetime
import restocks_main
from config import TOKEN, CHANNEL_NAME, COMMAND_PREFIX
from discord.ext import commands

restocks_url = restocks_main.restocks_url
restocks_sizes = restocks_main.restocks_stock
restocks_pic = restocks_main.restocks_product_img
restocks_title = restocks_main.product_title
stockx_url = restocks_main.stockx_url
hypeboost_url = restocks_main.hypeboost_product_url
goat_url = restocks_main.product_goat
sneakit_url = restocks_main.sneakit_product_url

if not TOKEN:
    raise ValueError("The Bot-Token was not included in the config.py file")

if not CHANNEL_NAME:
    raise ValueError("The Channel-Name was not included in the config.py file")

if not COMMAND_PREFIX:
    raise ValueError("The Command-Prefix was not included in the config.py file")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Scraping! (Restocks)'))
    print("Bot logged in!")


@bot.event
async def on_message(message):
  if message.author == bot.user:
      return
  message_content = message.content.lower()

  if message.channel.name == CHANNEL_NAME:
    if message.content.startswith(COMMAND_PREFIX): #(Prefix "$") SKU for scraping

      if COMMAND_PREFIX in message_content:
          await message.channel.send("Scraping...")
          SKU_raw = message_content.replace(COMMAND_PREFIX, '') # everything after prefix is the search (SKU)
          SKU = SKU_raw.replace(" ", "")
          restocks_sizes_output = restocks_sizes(SKU)
          restocks_product_output = restocks_url(SKU)
          restocks_image_output = restocks_pic(SKU,restocks_url)
          restocks_title_output = restocks_title(SKU)
          stockx_url_output = stockx_url(SKU)
          hypeboost_url_output = hypeboost_url(SKU)
          goat_url_output = goat_url(SKU)
          sneakit_url_output = sneakit_url(SKU)

          embed = discord.Embed(
            title=restocks_title_output,
            url=restocks_product_output,
            color=0x607d8b
          )
          embed.set_author(
            name="Restocks Scraper",
            url="https://twitter.com/jakobaio",
            icon_url= "https://www.reklamation24.de/img/content/marken/original_6710_1.gif"
            )
          embed.set_thumbnail(
            url=restocks_image_output
          )
          embed.add_field(
            name="Prices:",
            value=restocks_sizes_output
          )
          embed.add_field(
          name="Open Product on:",
          value=f"[[StockX]]({stockx_url_output})      " f"[[Restocks]]({restocks_product_output})      " f"[[Hypeboost]]({hypeboost_url_output})      " f"[[GOAT]]({goat_url_output})      " f"[[Sneakit]]({sneakit_url_output})      ",
          inline=False
          )
          embed.set_footer(
            text=f"Developed by JakobAIO      |      Restocks-Scraper      |      {datetime.datetime.now().strftime('%H:%M:%S')}"
          )

          await message.channel.send(embed=embed) #sends sizes in discord chat
          print('Scraping Successful!')

    else:
      await message.channel.send("***Wrong command used!***")

bot.run(TOKEN)
