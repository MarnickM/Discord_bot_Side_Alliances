import os, json, time, threading
import discord
from discord import channel
from discord.ui import Button
from discord.ext import commands
from datetime import datetime, timedelta
from itertools import islice
import requests
# from discord_slash.utils.manage_components import create_button, create_actionrow
# from discord_slash.model import ButtonStyle
# pm2 list => to view processes
# pm2 start main.py 
# pm2 logs id
# pm2 stop id
# pm2 restart id

intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix="-", intents=intents)

captain_role_id = 1303332767462985809
garyID = 781062676557594625
evoID = 196032505940279296
evelinID = 754149390809038939
decoyID = 92745784511991808
pawelID = 347291231396691978
koyaID = 327758753518845953
MohamedrID = 1060559440346099834

async def loadJson(fileName):
  with open(fileName, 'r') as file:
    data = json.load(file)
    return data


async def saveJson(fileName, data):
  with open(fileName, 'w') as file:
    json.dump(data, file, indent=4)


@bot.event
async def on_ready():
  print("bot ready")

@bot.command()
async def addmember(ctx):
  
  name = ctx.author.name
  members = await loadJson("./members.json")
  if members[name] is not None:
    ctx.send(f"{name} is already in the members list!")
    return
  
  members["members"][name] = {"points": "0", "totalpoints": "0"}
  await saveJson("./members.json", members)
  await ctx.send(f"{name} has been added!")


@bot.command()
async def delmember(ctx, member=None):
  if ctx.author.id != garyID and ctx.author.id != evoID:
      await ctx.send("you can't use this command")
      return
  if member is None:
    await ctx.send("Please write the member name")
    return
  members = await loadJson("./members.json")
  if member not in members["members"]:
    await ctx.send("This member does not exist!")
    await ctx.send(":information_source: Don't forget use the real discord name of the user you want to delete.")
  else:
    del members["members"][member]
    await saveJson("./members.json", members)
    await ctx.send("Member has been removed!")


# @bot.command()
# async def score(ctx):
#   members = await loadJson("./members.json")
#   war = await loadJson("./war_info.json")
#   enemy_name = war["name"]
#   total_war_score = 0
#   for member, values in members["members"].items():
#     total_war_score += int(values["points"])

#   # Iterate through each member and get the 5 highest points
#   for member, values in members["members"].items():
#       points_list = [(key, value["points"]) for key, value in members["members"].items()]
#       points_list.sort(key=lambda x: x[1], reverse=True)
      
#       # Get the top 5 points for the current member
#       top_5_points = points_list[:5]

#   file = discord.File("./1_5_1_1.png", filename="1_5_1_1.png")

#   embed = discord.Embed(
#     title="Scoreboard",
#     description=f"Galactic Empire II VS {enemy_name}",
#     color=discord.Colour.from_rgb(255, 191, 0)
#   )
#   embed.set_thumbnail(url="attachment://1_5_1_1.png")

  
#   embed.add_field(name=f":first_place: {top_5_points[0][0]}",value=f"Total score: {top_5_points[0][1]}",inline=False)
#   embed.add_field(name=f":second_place: {top_5_points[1][0]}",value=f"Total score: {top_5_points[1][1]}",inline=False)
#   embed.add_field(name=f":third_place: {top_5_points[2][0]}",value=f"Total score: {top_5_points[2][1]}",inline=False)
#   embed.add_field(name=f"#4 {top_5_points[3][0]}",value=f"Total score: {top_5_points[3][1]}",inline=False)
#   embed.add_field(name=f"#5 {top_5_points[4][0]}",value=f"Total score: {top_5_points[4][1]}",inline=False)
#   embed.set_footer(text="doesn't regard wp reductions")

#   # row = discord.create_actionrow(*[
#   #   discord.create_button(style=discord.ButtonStyle.secondary, label="War Scoreboard", custom_id="War Scoreboard"),
#   #   discord.create_button(style=discord.ButtonStyle.secondary, label="Alliance Scoreboard", custom_id="Alliance Scoreboard")])
    
#   #   # Send the message with buttons
#   await ctx.send(file=file, embed=embed) # , components=[row]


# @bot.event
# async def on_button_click(interaction):
#     if interaction.custom_id == "War Scoreboard":
#         await show_alliance_scoreboard(interaction, alliance_id=1)
#     elif interaction.custom_id == "Alliance Scoreboard":
#         await show_alliance_scoreboard(interaction, alliance_id=2)

# async def show_alliance_scoreboard(interaction, alliance_id):
#     members = await loadJson("C:\\Users\\Marni\\Desktop\\Games\\Galaxy_life\\Bot\\GalaxyLifeBot\\members.json")

#     for member, values in members["members"].items():
#       points_list = [(key, value["totalpoints"]) for key, value in members["members"].items()]
#       points_list.sort(key=lambda x: x[1], reverse=True)
      
#       # Get the top 5 points for the current member
#       top_5_points = points_list[:5]
    
#     # Implement logic to fetch and display the scoreboard for the selected alliance
#     # Modify the logic based on your requirements
    
#     file = discord.File("C:\\Users\\Marni\\Desktop\\Games\\Galaxy_life\\Bot\\GalaxyLifeBot\\1_5_1_1.png", filename="1_5_1_1.png")

#     embed = discord.Embed(
#         title=f"Top 5 highest warpoints in Galactic Empire II",
#         description=f"Total points",
#         color=discord.Colour.from_rgb(255, 191, 0)
#     )
#     embed.set_thumbnail(url="attachment://1_5_1_1.png")

#     embed.add_field(name=f":first_place: {top_5_points[0][0]}",value=f"Total score: {top_5_points[0][1]}",inline=False)
#     embed.add_field(name=f":second_place: {top_5_points[1][0]}",value=f"Total score: {top_5_points[1][1]}",inline=False)
#     embed.add_field(name=f":third_place: {top_5_points[2][0]}",value=f"Total score: {top_5_points[2][1]}",inline=False)
#     embed.add_field(name=f"#4 {top_5_points[3][0]}",value=f"Total score: {top_5_points[3][1]}",inline=False)
#     embed.add_field(name=f"#5 {top_5_points[4][0]}",value=f"Total score: {top_5_points[4][1]}",inline=False)
#     embed.set_footer(text="Might be inaccurate due to wp reductions for attacking low lvl players.")
#     await interaction.message.edit(embed=embed, file=file)


@bot.command()
async def save(ctx):

  war = await loadJson("./war_info.json")
  alliance_name = war["name"]
  archive = await loadJson("./war_archive.json")

  if alliance_name in archive and archive[alliance_name] is not None:
    temporary_save = archive[alliance_name]
    await saveJson("./backup.json", temporary_save)
    await ctx.send("This alliance already existed in archive, overwriting...")
    archive[alliance_name] = {}

  archive[alliance_name] = war
  await saveJson("./war_archive.json", archive)
  await ctx.send("Saved!")


@bot.command()
async def createwar(ctx, enemyAlliance=None):
  if captain_role_id not in [role.id for role in ctx.author.roles]:
    await ctx.send("you can't use this command")
    return
  if enemyAlliance is None:
    await ctx.send("Please write the enemy alliance name!")
    return
  
  global regentime
  regentime = 0
  
  archive = await loadJson("./war_archive.json")
  war = await loadJson("./war_info.json")

  if enemyAlliance in archive and archive[enemyAlliance] is not None:
    war = archive[enemyAlliance]
  else:
    war["name"] = enemyAlliance
    war["members"] = {}

        # Update downtimes with "unknown" to "0"
  for member in war["members"].values():
      for colony, details in member.items():
          if details[0] == "unknown":
              details[0] = "0"

  await saveJson("./war_info.json", war)
  await ctx.send("War has been created")


@bot.command()
async def addenemy(ctx, enemy=None, starbaseLVL=None):
  # added starbaseLVL none check
  if enemy is None or starbaseLVL is None:
    await ctx.send("Please write the enemy name and starbase lvl!")
    return
  # added error check for starbase lvl
  if int(starbaseLVL) < 1 or int(starbaseLVL) > 9:
    await ctx.send("There can only be starbases between 1 and 9")
    return

  # create starbase lvl template
  starbasetemp = "SB" + starbaseLVL

  war = await loadJson("./war_info.json")
  lower_case_members = {
      key.lower(): value
      for key, value in war["members"].items()
  }

  if enemy.lower() in lower_case_members:
    lower_enemy = enemy.lower()
    for key, value in war["members"].items():
      if key.lower() == lower_enemy:
        enemy = key
        break

  if enemy in war["members"]:
    await ctx.send("The enemy is already registered!")
    return
  # added the starbase to the list
  war["members"][enemy] = {"C0": ["0", "0", starbasetemp]}
  await saveJson("./war_info.json", war)
  await ctx.send("Added enemy **" + enemy + "** !")


@bot.command()
async def addcolony(ctx,
                    enemy=None,
                    colony=None,
                    coordinates=None,
                    starbaseLVL=None):
  # added coordinates and starbase lvl
  if enemy is None or colony is None or coordinates is None or starbaseLVL is None:
    await ctx.send(
        "Please write the enemy name, colony number, coordinates and starbase lvl!!"
    )
    return
  if int(colony) < 1 or int(colony) > 11:
    await ctx.send("There can only be colonies between 1 and 11")
    return
  # added error check for starbase lvl
  if int(starbaseLVL) < 1 or int(starbaseLVL) > 9:
    await ctx.send("There can only be starbases between 1 and 9")
    return
  
  # create starbase lvl template
  starbasetemp = "SB" + starbaseLVL
  ctemp = "C" + colony
  war = await loadJson("./war_info.json")
  lower_case_members = {
      key.lower(): value
      for key, value in war["members"].items()
  }

  if enemy.lower() in lower_case_members:
    lower_enemy = enemy.lower()
    for key, value in war["members"].items():
      if key.lower() == lower_enemy:
        enemy = key
        break
  if enemy in war["members"]:
    if ctemp in war["members"][enemy]:
      await ctx.send("The colony is already registered!")
      return
  else:
    await ctx.send("The enemy does not exist!!")
    return
  # place after name Cx,coords,starbase in list
  war["members"][enemy][ctemp] = ["0", coordinates, starbasetemp]

  for member, colonies in war['members'].items():
    sorted_colonies = dict(
        sorted(colonies.items(), key=lambda x: int(x[0][1:])))
    war['members'][member] = sorted_colonies

  await saveJson("./war_info.json", war)
  await ctx.send("Added colony **" + colony + "** for **" + enemy + "** !")


@bot.command()
async def delenemy(ctx, enemy=None):
  if enemy is None:
    await ctx.send("Please write the enemy name!")
    return
  
  war = await loadJson("./war_info.json")

  lower_case_members = {
      key.lower(): value
      for key, value in war["members"].items()
  }

  if enemy.lower() in lower_case_members:
    lower_enemy = enemy.lower()
    for key, value in war["members"].items():
      if key.lower() == lower_enemy:
        enemy = key
        break

  
  if enemy in war["members"]:
    del war["members"][enemy]
    await saveJson("./war_info.json", war)
    await ctx.send("Enemy removed!")
  else:
    await ctx.send("The enemy does not exist!")


@bot.command()
async def delcolony(ctx, enemy=None, colony=None):
  if enemy is None or colony is None:
    await ctx.send("Please write the enemy name and colony number!")
    return
  if int(colony) < 1 or int(colony) > 11:
    await ctx.send("There can only be colonies between 1 and 11")
    return
  
  war = await loadJson("./war_info.json")
  lower_case_members = {
    key.lower(): value
    for key, value in war["members"].items()
  }

  if enemy.lower() in lower_case_members:
    lower_enemy = enemy.lower()
    for key, value in war["members"].items():
      if key.lower() == lower_enemy:
        enemy = key
        break
  ctemp = "C" + colony
  
  if enemy in war["members"]:
    if ctemp in war["members"][enemy]:
      del war["members"][enemy][ctemp]
      await saveJson("./war_info.json", war)
      await ctx.send("Enemy colony removed!")
    else:
      await ctx.send("This enemy colony does not exist!")
  else:
    await ctx.send("The enemy does not exist!!")


@bot.command()
async def down(ctx, enemy=None, colony="0"):

  if enemy is None:
    await ctx.send("Please write the enemy name!")
    return

  if colony != "0":
    if int(colony) < 1 or int(colony) > 11:
      await ctx.send("There can only be colonies between 1 and 11")
      return
    
  warpoints = {
      "1": 100,
      "2": 200,
      "3": 300,
      "4": 400,
      "5": 600,
      "6": 1000,
      "7": 1500,
      "8": 2000,
      "9": 2500
  }

  ctemp = "C" + colony
  war = await loadJson("./war_info.json")
  members_list = await loadJson("./members.json")
 
  special_names = {
    "ming_miw":"miw",
    "kuxuku_":"kuxaku",
    "pawel5142":"pawelcio123",
    "_temucin_":"cerdukay",
    "TahiaDjazair213algerCentre#8475":"cornflekssz",
    "szalonylukaszek69":"bonvsko",
    "kexsik777_29868":"0770",
    "eovcom1x": "eovcomix",
    "MP furry#0675":"nigkiip",
    "ahmed_real.":"ahmedwaheed2002"
  }
  
  lower_case_members = {
      key.lower(): value
      for key, value in war["members"].items()
  }
  existance = True

  if enemy.lower() in lower_case_members:
    lower_enemy = enemy.lower()
    for key, value in war["members"].items():
      if key.lower() == lower_enemy:
        enemy = key
    
    if ctemp in war["members"][enemy]:
       war["members"][enemy][ctemp][0] = datetime.now().strftime(
          "%Y-%m-%d %H:%M:%S")
      
       await saveJson("./war_info.json", war)
       if colony == "0":
         await ctx.send("**" + enemy + "** **main** Down")
       else:
         await ctx.send("**" + enemy + "** **" + ctemp + "** Down")
    else:
       existance = False
       await ctx.send("The enemy colony does not exist!")

    #if existance == True: 
          # start of scores
          #planet = war["members"][enemy][ctemp][2]
          #SB_level = planet[2]
          #points = warpoints[SB_level]
          #name = ctx.author.name
  
          #for key,value in special_names.items():
            #if key == name:
              #name = value
  
          #for key, value in members_list["members"].items():
            #if key.lower() == name:
              #value["points"] += points
              #value["totalpoints"] += points
          #await saveJson("./members.json", members_list)
          # end of scores
            #break

  else:
    await ctx.send("The enemy does not exist!")

@bot.command()
async def unknown(ctx, enemy=None, colony="0"):
  '''
  if ctx.author.id != garyID and ctx.author.id != evoID and ctx.author.id != catID:
    await ctx.send("The command is under maintenance, notify the dev's")
    return
  '''
  if enemy is None:
    await ctx.send("Please write the enemy name!")
    return

  if colony != "0":
    if int(colony) < 1 or int(colony) > 11:
      await ctx.send("There can only be colonies between 1 and 11")
      return

  ctemp = "C" + colony
  war = await loadJson("./war_info.json")
  lower_case_members = {
      key.lower(): value
      for key, value in war["members"].items()
  }

  if enemy.lower() in lower_case_members:
    lower_enemy = enemy.lower()
    for key, value in war["members"].items():
      if key.lower() == lower_enemy:
        enemy = key
        break

    if ctemp in war["members"][enemy]:
      war["members"][enemy][ctemp][0] = "unknown"
      
      
      await saveJson("./war_info.json", war)
      if colony == "0":
        await ctx.send("**" + enemy + "** **main** down time unkown")
      else:
        await ctx.send("**" + enemy + "** **" + ctemp + "** down time unknown")
    else:
      await ctx.send("The enemy colony does not exist!")
  else:
    await ctx.send("The enemy does not exist!")


@bot.command()
async def up(ctx, enemy=None, colony="0"):
  if enemy is None:
    await ctx.send("Please write the enemy name!")
    return

  if colony != "0":
    if int(colony) < 1 or int(colony) > 11:
      await ctx.send("There can only be colonies between 1 and 11")
      return
    
  war = await loadJson("./war_info.json")
  lower_case_members = {
    key.lower(): value
    for key, value in war["members"].items()
  }

  if enemy.lower() in lower_case_members:
    lower_enemy = enemy.lower()
    for key, value in war["members"].items():
      if key.lower() == lower_enemy:
        enemy = key
        break  
  ctemp = "C" + colony
  
  if enemy in war["members"]:
    if ctemp in war["members"][enemy]:
      war["members"][enemy][ctemp][0] = "0"
      await saveJson("./war_info.json", war)
      if colony == "0":
        await ctx.send("**" + enemy + "** **main** Up")
      else:
        await ctx.send("**" + enemy + "** **" + ctemp + "** Up")
    else:
      await ctx.send("The enemy colony does not exist!")
  else:
    await ctx.send("The enemy does not exist!!")

@bot.command()
async def upAll(ctx, enemy=None):
  if enemy is None:
    await ctx.send("Please write the enemy name!")
    return
    
  war = await loadJson("./war_info.json")
  lower_case_members = {
    key.lower(): value
    for key, value in war["members"].items()
  }

  if enemy.lower() in lower_case_members:
    lower_enemy = enemy.lower()
    for key, value in war["members"].items():
      if key.lower() == lower_enemy:
        enemy = key
        break  
  
  if enemy in war["members"]:
      for colony, values in war["members"][enemy].items():
            values[0] = "0"
      await saveJson("./war_info.json", war)
      await ctx.send(f"All planets of **{enemy}** are up!")
  else:
      await ctx.send("The enemy does not exist!")

@bot.command()
async def refreshMainWp(ctx):
    galacticEmpire_wp_sum = 0
    try:
      response = requests.get(f"https://api.galaxylifegame.net/Alliances/get?name=galactic%20empireIII")
      data = response.json()
      if 'Members' in data:
          members = data['Members']
          member_names = [member['Name'] for member in members]
          warpoints = {
                    1: 100,
                    2: 200,
                    3: 300,
                    4: 400,
                    5: 600,
                    6: 1000,
                    7: 1500,
                    8: 2000,
                    9: 2500
                }
          for member in member_names:
              response = requests.get(f"https://api.galaxylifegame.net/Users/name?name={member}")
              user_data = response.json()
              HQlevel = user_data['Planets'][0]["HQLevel"]
              if HQlevel in warpoints:
                  points = warpoints[HQlevel]
                  galacticEmpire_wp_sum += points
          main_wp = await loadJson("./total_wp.json")
          main_wp["total_wp"] = galacticEmpire_wp_sum
          await saveJson("./total_wp.json", main_wp)
        
      else:
          print("No member data found in the API response.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
# @bot.command()
# async def upgraded(ctx, starbaselvl=None):
#   if starbaselvl is None:
#     await ctx.send("Please write your new starbase level!")
#     return
#   if int(starbaselvl) < 1 or int(starbaselvl) > 9:
#     await ctx.send("There can only be starbases between 1 and 9")
#     return
#   points = await loadJson("./total_wp.json")
#   warpoints_added = {
#       "2": 100,
#       "3": 100,
#       "4": 100,
#       "5": 200,
#       "6": 400,
#       "7": 500,
#       "8": 500,
#       "9": 500
#   }
#   new_points = warpoints_added[starbaselvl]
#   points["total_wp"] += new_points
#   await ctx.send(f"Total warpoints of our alliance increased by {new_points}!")
#   await saveJson("./total_wp.json", points)


# @bot.command()
# async def add(ctx, starbaselvl=None):
#   if starbaselvl is None:
#     await ctx.send("Please write your new starbase level!")
#     return
#   if int(starbaselvl) < 1 or int(starbaselvl) > 9:
#     await ctx.send("There can only be starbases between 1 and 9")
#     return
#   points = await loadJson("./total_wp.json")
#   warpoints_added = {
#       "2": 200,
#       "3": 300,
#       "4": 400,
#       "5": 600,
#       "6": 1000,
#       "7": 1500,
#       "8": 2000,
#       "9": 2500
#   }
#   new_points = warpoints_added[starbaselvl]
#   points["total_wp"] += new_points
#   await ctx.send(f"Total warpoints of our alliance increased by {new_points}!")
#   await saveJson("./total_wp.json", points)

regentime = 0

@bot.command()
async def setTime(ctx, regenTime=None):
    if regenTime is None:
        await ctx.send("You must provide a rebuild time.")
        return

    try:
        regenTime = int(regenTime)
    except ValueError:
        await ctx.send("Rebuild time must be a number.")
        return

    if regenTime < 3 or regenTime > 7:
        await ctx.send("Rebuild time can be max 7 or min 3.")
        return

    global regentime
    regentime = regenTime
    await ctx.send(f"Rebuild time set to {regentime}")





@bot.command()
async def info(ctx):
  war = await loadJson("./war_info.json")
  points = await loadJson("./total_wp.json")
  # total sum of all our starbase levels combined
  GalacticEmpire_wp_sum = points["total_wp"]

  # total sum of all starbase levels combined of the enemy alliance
  EnemyAlliance_wp_sum = 0

  warpoints = {
      1: 100,
      2: 200,
      3: 300,
      4: 400,
      5: 600,
      6: 1000,
      7: 1500,
      8: 2000,
      9: 2500
  }
  counter = 0
  for player, player_data in war["members"].items():
    if "C0" in player_data:
      sb_value = int(player_data["C0"][2][2:])
      counter += 1
      EnemyAlliance_wp_sum += warpoints.get(sb_value, 0)

  regenTime = (3*EnemyAlliance_wp_sum)/GalacticEmpire_wp_sum
  # print(regenTime)
  base_value = int(regenTime)
  # print(base_value)
  border_for_rounding = base_value + 0.9
  # print(border_for_rounding)
  if regenTime < border_for_rounding:
    actualRegenTime = base_value
  else:
    actualRegenTime = base_value + 1
  # RegenFactor = EnemyAlliance_wp_sum / GalacticEmpire_wp_sum
  # # default regen time in wars is 3h
  # regenTime = 3
  # memberRatio = counter/18
  # memberTime = 3*memberRatio # respawn time based on members
  # if memberTime < 3:
  #   memberTime = 3
  # elif memberTime > 7:
  #   memberTime = 7
  # # calculate the actual regeneration time for a base
  # actualRegenTimeV1 = regenTime * RegenFactor # with no member consideration
  # actualRegenTime = round((actualRegenTimeV1 + memberTime)/2) # take average of both times
  # # actualRegenTime = round(regenTime * RegenFactor)
  if actualRegenTime < 3:
    actualRegenTime = 3
  elif actualRegenTime > 7:
    actualRegenTime = 7
  # actualRegenTime = 3

  global regentime
  if regentime != 0:
    actualRegenTime = regentime



  #actualRegenTime = 4
  embed = discord.Embed(
      title=war["name"],
      description=
      f"Total WP main:{EnemyAlliance_wp_sum}, Rebuild time:{actualRegenTime}",
      color=discord.Colour.from_rgb(0,0,0))
  currentTime = datetime.now()

  if len(war["members"]) <= 25:
    for member in war["members"]:
      text = ""
      for planet in war["members"][member]:

        # checking if time is unknown
        if war["members"][member][planet][0] == "unknown":
            starbaselvl = war["members"][member][planet][2]
            if planet== "C0":
              text += f":warning: main {starbaselvl}-> ????\n"
              continue
            else:
              coords = war["members"][member][planet][1]
              text += f":warning: {planet} {coords} {starbaselvl}-> ????\n"
              continue

        if war["members"][member][planet][0] == "0":
          # get the starbase lvl from position 2
          starbaselvl = war["members"][member][planet][2]
          if planet == "C0":
            text += f":white_check_mark: main  {starbaselvl}-> UP\n"
          else:
            coords = war["members"][member][planet][1]
            text += f":white_check_mark: {planet} {coords} {starbaselvl}-> UP\n"
          continue

        tempTime = war["members"][member][planet][0]
        tempTime = datetime.strptime(tempTime, "%Y-%m-%d %H:%M:%S")

        timeDifference = currentTime - tempTime
        # added the actualRegenTime instead of the hard coded 3h time
        if timeDifference >= timedelta(hours=actualRegenTime):
          war["members"][member][planet][0] = "0"
          # get the starbase lvl from position 2
          starbaselvl = war["members"][member][planet][2]
          if planet == "C0":
            text += f":white_check_mark: main {starbaselvl}-> UP\n"
          else:
            coords = war["members"][member][planet][1]
            # get the starbase lvl from position 2
            starbaselvl = war["members"][member][planet][2]
            # added the starbaselvl in the display
            text += f":white_check_mark: {planet} {coords} {starbaselvl}-> UP\n"
        else:
          # added the actualRegenTime instead of the hard coded 3h time
          timeLeft = timedelta(hours=actualRegenTime) - timeDifference
          hoursLeft = timeLeft.seconds // 3600
          minutesLeft = (timeLeft.seconds % 3600) // 60

          ptemp = ":octagonal_sign: " + planet
          coords = war["members"][member][planet][1]
          # get the starbase lvl from position 2
          starbaselvl = war["members"][member][planet][2]
          if planet == "C0":
            ptemp = ":octagonal_sign: main"
            coords = ""

          # added starbaselvl in the display
          text += f"{ptemp} {coords} {starbaselvl}-> {hoursLeft}h:{minutesLeft}m\n"

      embed.add_field(name=member, value=text, inline=True)

    embed.set_footer(text="Developed by Garybaldy16")
    await saveJson("./war_info.json", war)
    await ctx.send(embed=embed)

  else:
    max_members_per_embed = 25

    # Calculate the total number of members
    total_members = len(war["members"])

    # Iterate over members in chunks of max_members_per_embed
    for start_index in range(0, total_members, max_members_per_embed):
      end_index = start_index + max_members_per_embed
      current_members = list(war["members"].items())[start_index:end_index]

      embed = discord.Embed(
          title=war["name"],
          description=
          f"Total WP main:{EnemyAlliance_wp_sum}, Rebuild time:{actualRegenTime}",
          color=discord.Colour.from_rgb(0,0,0))

      for member, member_data in current_members:
        text = ""
        for planet in member_data:

            # checking if time is unknown
          if war["members"][member][planet][0] == "unknown":
              starbaselvl = war["members"][member][planet][2]
              if planet== "C0":
                text += f":warning: main {starbaselvl}-> ????\n"
                continue
              else:
                coords = war["members"][member][planet][1]
                text += f":warning: {planet} {coords} {starbaselvl}-> ????\n"
                continue

          if war["members"][member][planet][0] == "0":
            # get the starbase lvl from position 2
            starbaselvl = war["members"][member][planet][2]
            if planet == "C0":
              text += f":white_check_mark: main  {starbaselvl}-> UP\n"
            else:
              coords = war["members"][member][planet][1]
              text += f":white_check_mark: {planet} {coords} {starbaselvl}-> UP\n"
            continue

          tempTime = war["members"][member][planet][0]
          tempTime = datetime.strptime(tempTime, "%Y-%m-%d %H:%M:%S")

          timeDifference = currentTime - tempTime
          # added the actualRegenTime instead of the hard coded 3h time
          if timeDifference >= timedelta(hours=actualRegenTime):
            war["members"][member][planet][0] = "0"
            # get the starbase lvl from position 2
            starbaselvl = war["members"][member][planet][2]
            if planet == "C0":
              text += f":white_check_mark: main {starbaselvl}-> UP\n"
            else:
              coords = war["members"][member][planet][1]
              # get the starbase lvl from position 2
              starbaselvl = war["members"][member][planet][2]
              # added the starbaselvl in the display
              text += f":white_check_mark: {planet} {coords} {starbaselvl}-> UP\n"
          else:
            # added the actualRegenTime instead of the hard coded 3h time
            timeLeft = timedelta(hours=actualRegenTime) - timeDifference
            hoursLeft = timeLeft.seconds // 3600
            minutesLeft = (timeLeft.seconds % 3600) // 60

            ptemp = ":octagonal_sign: " + planet
            coords = war["members"][member][planet][1]
            # get the starbase lvl from position 2
            starbaselvl = war["members"][member][planet][2]
            if planet == "C0":
              ptemp = ":octagonal_sign: main"
              coords = ""

            # added starbaselvl in the display
            text += f"{ptemp} {coords} {starbaselvl}-> {hoursLeft}h:{minutesLeft}m\n"

        embed.add_field(name=member, value=text, inline=True)

      embed.set_footer(text="Developed by Garybaldy16")
      await saveJson("./war_info.json", war)
      await ctx.send(embed=embed)


# keep_alive.keep_alive()

# try:
#   bot.run(token)
# except Exception as e:
#   print(f"An error occurred: {type(e).__name__} - {e}")

#   # Create a dictionary with error information
#   error_data = {"error_type": type(e).__name__, "error_message": str(e)}

#   # Run the asynchronous task outside of an async function
#   bot.loop.run_until_complete(write_error_to_json(error_data))

#   asyncio.run(bot.close())  # Close the bot
#   # Add a delay before attempting to restart
#   asyncio.run(asyncio.sleep(5))
#   # Restart the bot
#   bot.loop.run_until_complete(bot.start(token))

