# libraires
import discord
from discord.ui import Select, View
from discord.utils import get
from keep_alive import keep_alive

#start webserver (to host on replit)
keep_alive()

# bot info
TOKEN = 'OTY0NzE2NzE5MTIzODU3NDM4.GkC27u.mBcMSi136Fd6SHOFTWn0XvuV7NMM4jbeKEyZfg'
GUILDS = [430111187288457226]

bot = discord.Bot()
category_roles = ['FPS', 'MOBA', 'PainGaming', 'PartyPack', 'RIOT', 'RPG', 'RTS'] # 7 roles
community_roles = ['D&DCommunity', 'PingMe,YouWon\'t', 'TheaterKids'] # 3 roles
league_roles = ['Clash', 'Customs', 'League', 'tft'] # 4 roles
game_roles = ['AmongUs', 'Apex', 'Baulder\'sGate', 'BloonsTD', 'Breakpoint', 'Civs', 'DeadByDaylight', 'GenshinImpact', 'Minecraft', 'NewWorld', 'PokemonMMO', 'Valorant', 'Warframe'] # 13 roles


@bot.slash_command(guild_ids = GUILDS, name = 'get_roles', description = 'recive the role selection menu')
async def get_roles(ctx):
  id = get(ctx.guild.roles, name='SomstraSociety')
  user = ctx.user
  if id in user.roles:
    category_select = Select(placeholder = 'Select Category Role(s)', min_values = 1, max_values = 7)
    community_select = Select(placeholder = 'Select Community Role(s)', min_values=1, max_values=3)
    league_select = Select(placeholder = 'Select League Role(s)', min_values = 1, max_values = 4)
    game_select = Select(placeholder = 'Select Game Role(s)', min_values = 1, max_values = 13)
  
    for role in category_roles:
      category_select.append_option(discord.SelectOption(label = role))
    for role in community_roles:
      community_select.append_option(discord.SelectOption(label = role))
    for role in league_roles:
      league_select.append_option(discord.SelectOption(label = role))
    for role in game_roles:
      game_select.append_option(discord.SelectOption(label = role))
  
    async def category_callback(interaction):
      user = interaction.user
      guild = interaction.guild
      message = ''
      
      for role in category_select.values:
        id = get(guild.roles, name=role)
        if id == None:
          message += '\n' + role + ' has failed to add.'
        else:
          if id not in user.roles:
            await user.add_roles(id)
            message += '\n' + role + ' has been added.'
          else:
            await user.remove_roles(id)
            message += '\n' + role + ' has been removed.'
      await interaction.response.send_message(content = message, ephemeral = True)
  
    async def community_callback(interaction):
      user = interaction.user
      guild = interaction.guild
      message = ''
    
      for role in community_select.values:
        id = get(guild.roles, name=role)
        if id == None:
          message += '\n' + role + ' has failed to add.'
        else:
          if id not in user.roles:
            await user.add_roles(id)
            message += '\n' + role + ' has been added.'
          else:
            await user.remove_roles(id)
            message += '\n' + role + ' has been removed.'
      await interaction.response.send_message(content = message, ephemeral = True)
      
    
    async def league_callback(interaction):
      user = interaction.user
      guild = interaction.guild
      message = ''
      
      for role in league_select.values:
        id = get(guild.roles, name=role)
        if id == None:
          message += '\n' + role + ' has failed to add.'
        else:
          if id not in user.roles:
            await user.add_roles(id)
            message += '\n' + role + ' has been added.'
          else:
            await user.remove_roles(id)
            message += '\n' + role + ' has been removed.'
      await interaction.response.send_message(content = message, ephemeral = True)
    async def game_callback(interaction):
      user = interaction.user
      guild = interaction.guild
      message = ''
      
      for role in game_select.values:
        id = get(guild.roles, name=role)
        if id == None:
          message += '\n' + role + ' has failed to add.'
        else:
          if id not in user.roles:
            await user.add_roles(id)
            message += '\n' + role + ' has been added.'
          else:
            await user.remove_roles(id)
            message += '\n' + role + ' has been removed.'
      await interaction.response.send_message(content = message, ephemeral = True)
    
   
    category_select.callback = category_callback
    community_select.callback = community_callback
    league_select.callback = league_callback
    game_select.callback = game_callback
    
    view = View(category_select, community_select, league_select, game_select)
    await ctx.respond(content = '-\nSelect your roles below.\nPress "Dismiss message" when you are finished.',view = view, ephemeral = True)

  else:
    await ctx.respond(content = 'You do not have permission to use this command. Please read and accept the rules then try again.', ephemeral = True)
@bot.slash_command(guild_ids = GUILDS, name = 'accept_rules', desciption = 'accept the rules as written in #somstra-rules')
async def accept_rules(ctx):
  id = get(ctx.guild.roles, name='SomstraSociety')
  await ctx.user.add_roles(id)
  await ctx.respond(content = 'thank you for accepting the rules', ephemeral = True)
bot.run(TOKEN)
