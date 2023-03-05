import discord
import restocks_main
from config import TOKEN
from discord.ext import commands

restocks_url = restocks_main.restocks_url
restocks_sizes = restocks_main.restocks_stock
restocks_pic = restocks_main.restocks_product_img
restocks_title = restocks_main.product_title
stockx_url = restocks_main.stockx_url
hypeboost_url = restocks_main.hypeboost_product_url

if not TOKEN:
    raise ValueError("The BOt-Token was not included in the config.py file")

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

  if message.content.startswith(f'$restocks'): #(Prefix "$") SKU for scraping

    if f'$restocks' in message_content:
        await message.channel.send("Scraping...")
        SKU = message_content.replace('$restocks ', '') # everything after prefix is the search (SKU)
        restocks_sizes_output = restocks_sizes(SKU)
        restocks_product_output = restocks_url(SKU)
        restocks_image_output = restocks_pic(SKU,restocks_url)
        restocks_title_output = restocks_title(SKU)
        stockx_url_output = stockx_url(SKU)
        hypeboost_url_output = hypeboost_url(SKU)

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
          name='Open Product on:',
          value=f"[StockX     ]({stockx_url_output})" f"[Hypeboost     ]({hypeboost_url_output})",
          inline=False
        )
        embed.set_footer(
          text="Developed by Jakob.AIO"
        )

        await message.channel.send(embed=embed) #sends sizes in discord chat
        print('Scraping Successful!')


bot.run(TOKEN)
