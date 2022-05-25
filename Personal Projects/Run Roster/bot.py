# libraires
import discord
from keep_alive import keep_alive

#start webserver (to host on replit)
keep_alive()

# bot info
TOKEN = 'OTU4MDc5NjIwODAzMDkyNTEx.G1Xo-K.o7P5_ZgnmIg14cyVONb2K7RJKZE11_g7W4Kj20'
GUILDS = [843601559262986270, 937351484796968991]

# emojis
tank = '<:Tank:958144873402368000>'
heal = '<:Heal:958144828242288650>'
damage = '<:Damage:958144784298561556>'
remove = '<:Remove:958180465989287936>'
general = '<:Add:959545085610045440>'
expand = '<:AddExpand:959549351380799498>'
delete = '\N{CROSS MARK}'
acknowledge = '✅'

# lookup lists
dungeonNames = [
					['AC', 'Arx Corninum'],
					['BCI' , 'Banished Cells I'],
					['BCII' , 'Banished Cells II'],
					['BDC' , 'Blessed Crucible'],
					['BDV' , 'Black Drake Villa'],
					['BH' , 'Blackheart Haven'],
					['BRF' , 'Bloodroot Forge'],
					['CA' , 'The Coral Aerie'],
					['COAI' , 'City of Ash I'],
					['COAII' , 'City of Ash II'],
					['COHI' , 'Crypt of Hearts I'],
					['COHII' , 'Crypt of Hearts II'],
					['COS' , 'Cradle of Shadows'],
					['CU' , 'The Cauldron'],
					['CT' , 'Castle Thorn'],
					['DSCI' , 'Darkshade Cavers I'],
					['DSCII' , 'Darkshade Cavers II'],
					['DC' , 'The Dread Cellar'],
					['DK' , 'Direfrost Keep'],
					['DOM' , 'Depths of Malatar'],
					['EHI' , 'Elden Hollow I'],
					['EHII' , 'Elden Hollow II'],
					['FGI' , 'Fungal Grotto I'],
					['FGII' , 'Fungal Grotto II'],
					['FH' , 'Falkreath Hold'],
					['FL' , 'Fang Lair'],
					['Fv' , 'Frostvault'],
					['ICP' , 'Imperial City Prison'],
					['IR' , 'Icereach'],
					['LOM' , 'Lair of Maarselok'],
					['MGF' , 'Moongrave Fane'],
					['MHK' , 'Moon Hunter Keep'],
					['MOS' , 'March of Sacrifices'],
					['ROM' , 'Ruins of Mazzatun'],
					['RPB' , 'Red Petal Bastion'],
					['SW' , 'Selene\'s Web'],
					['SCI' , 'Spindleclutch I'],
					['SCII' , 'Spindleclutch II'],
					['SCP' , 'Scalecaller Peak'],
					['SG' , 'Stone Garden'],
					['SR' , 'Shipwright\'s Regret'],
					['TI' , 'Tempest Island'],
					['UHG' , 'Unhallowed Grave'],
					['VOM' , 'Vaults of Madness'],
					['VF' , 'Volenfell'],
					['WGT' , 'White-Gold Tower'],
					['WSI' , 'Wayrest Sewers I'],
					['WSII' , 'Wayrest Sewers II']
				]
trialNames = [	
				['AA' , 'Aetherian Archive'],
				['HRC' , 'hel Ra Citadel'],
				['SO' , 'Sanctum Ophidia'],
				['MOL' , 'Maw of Lorkhaj'],
				['HOF' , 'Halls of Fabrication'],
				['AS' , 'Asylum Sanctorium'],
				['CR' , 'Cloudrest'],
				['SS' , 'Sunspire'],
				['KA' , 'Kyne\'s Aegis'],
				['RG' , 'Rockgrove'],
				['DR' , 'Dreadsail Reef']
			]
arenaNames = [
				['DA' , 'Dragonstar Arena'],
				['BRP' , 'Blackrose Prison']
			]
activityTitles = []
for item in dungeonNames:
	activityTitles.append(item[1])
for item in trialNames:
	activityTitles.append(item[1])
for item in arenaNames:
	activityTitles.append(item[1])


bot = discord.Bot()

async def get_activity(ctx: discord.AutocompleteContext):
    return [activity for activity in activityTitles if activity.lower().startswith(ctx.value.lower())]



@bot.slash_command(name = 'roster-activity', description = 'create a roster for a dungeon, trial, or arena')
@discord.option("activity_name", description="Choose your activity", autocomplete=get_activity)
@discord.option('level', description='Choose the level of the activity', choices = ['Normal', 'Veteran'])
async def activityRoster(ctx, activity_name, level, date, time, timezone, tank_count = 0, healer_count = 0, dps_count = 0):
	category = ctx.channel.category

	if level == 'Veteran':
		level_name = 'Veteran '
		level_abr = 'v'
	else:
		level_name = 'Normal '
		level_abr = 'n'

	eType, abr, activity_name = getType(activity_name)

	channel = await ctx.guild.create_text_channel(name = level_abr + abr + ' ' + date.replace('/','-'), category = category)

	seats = 0
	if eType == 'Trial':
		if tank_count == 0:
			tankNum = 2
		else:
			tankNum = tank_count
		if healer_count == 0:
			healerNum = 2
		else:
			healerNum = healer_count
		if dps_count == 0:
			dpsNum = 8
		else:
			dpsNum = dps_count
	elif eType == 'Dungeon':
		if tank_count == 0:
			tankNum = 1
		else:
			tanknum = tank_count
		if healer_count == 0:
			healerNum = 1
		else:
			healerNum = healer_count
		if dps_count == 0:
			dpsNum = 2
		else:
			dpsNum = dps_count
	else:
		tankNum = 0
		healerNum = 0
		dpsNum = 0
		seats = 4

	message = await channel.send(embed = createEmbed(ctx.author, eType, (level_name + activity_name), date, time, timezone, tankNum=tankNum, healerNum=healerNum, dpsNum=dpsNum, seats=seats))
	await addReactions(message, seats)
	await ctx.respond('created roster in ' + channel.mention, ephemeral = True)
	return channel



@bot.slash_command(name = 'roster-event', description = 'create a roster for an event - set seats to -1 to create an expandable roster')
async def eventRoster(ctx, event_name, date, time, timezone, seats):
	channel = ctx.channel
	category = channel.category
	channel = await ctx.guild.create_text_channel(name = event_name + ' ' + date.replace('/','-'), category = category)
	message = await channel.send(embed = createEmbed(ctx.author, 'Event', event_name, date, time, timezone, seats=int(seats)))
	await addReactions(message, int(seats))
	await ctx.respond('created roster in ' + channel.mention, ephemeral = True)



@bot.event
async def on_raw_reaction_add(payload):
	channel = bot.get_channel(payload.channel_id) # get channel from context
	user = payload.member # get user from context
	message = await channel.fetch_message(payload.message_id) # get message from channel + context
	embed = message.embeds[0]
	reaction = str(payload.emoji) # get emoji from context

	if user != bot.user: # ensure user who added the reaction is not the bot
		# delete message & channel (can only be done by original creator)
		if reaction == delete:
			for field in embed.fields:
				if str(user) in field.name:
					await channel.delete()
					return
		if reaction == remove:
			if any(str(reaction.emoji) == expand for reaction in message.reactions):
				await message.edit(embed = removeUser(user, embed, 1))
			else:
				await message.edit(embed = removeUser(user, embed, 0))
			await message.remove_reaction(reaction, user)
			return
		elif checkDuplicate(user, embed):
			pass
		else:
			if reaction == tank:
				await message.edit(embed = addTank(user, embed))
			elif reaction == heal:
				await message.edit(embed = addHealer(user, embed))
			elif reaction == damage:
				await message.edit(embed = addDPS(user, embed))
			elif reaction == general:
				await message.edit(embed = addGeneral(user, embed))
			elif reaction == expand:
				await message.edit(embed = addExpand(user, embed))
			else: # not a valid react for roseter signup
				return
		await verifyAddition(message, user, reaction)
		await message.remove_reaction(reaction, user) # remove reaction



async def verifyAddition(message, user, reaction):
	print('VERIFYING')
	embed = message.embeds[0]
	if not checkDuplicate(user, embed): # user not added to roster
		print('\tREDOING ADDDITION')
		if reaction == tank:
			await message.edit(embed = addTank(user, embed))
		elif reaction == heal:
			await message.edit(embed = addHealer(user, embed))
		elif reaction == damage:
			await message.edit(embed = addDPS(user, embed))
		elif reaction == general:
			await message.edit(embed = addGeneral(user, embed))
		elif reaction == expand:
			await message.edit(embed = addExpand(user, embed))
		verifyAddition(message, user, reaction)
	else:
		print('\tADDITION GOOD')
		return

def createEmbed(creator, eType, name, date, time, Timezone, seats = 0, tankNum = 2, healerNum = 2, dpsNum = 8):
	embed = discord.Embed(title = name, color = 0x55cc78)
	embed.add_field(inline = False, name = 'Creator: ' + str(creator), value = '\u200b')
	embed.add_field(inline = False, name = eType + ': ' + name, value = '\u200b')
	embed.add_field(inline = False, name = 'Date: ' + date, value = '\u200b')
	embed.add_field(inline = False, name = 'Time: ' + time + ' ' + Timezone, value = '\u200b')
	if eType == 'Event' or eType == 'Arena':
		peopleMessage = ''
		if int(seats) > 0:
			for i in range(int(seats)):
				peopleMessage += str(i+1) + ':\n'
		else:
			peopleMessage = '** **'
		embed.add_field(inline = False, name = 'People', value = peopleMessage)
	else:
		tankMessage = ''
		healerMessage = ''
		dpsMessage = ''
		for i in range(int(tankNum)):
			tankMessage += str(i+1) + ': \n'
		for i in range(int(healerNum)):
			healerMessage += str(i+1) + ': \n'
		for i in range(int(dpsNum)):
			dpsMessage += str(i+1) + ': \n'
		embed.add_field(inline = False, name = 'Tank ' + tank, value = tankMessage)
		embed.add_field(inline = False, name = '** **', value = '** **')
		embed.add_field(inline = False, name = 'Healer ' + heal, value = healerMessage)
		embed.add_field(inline = False, name = '** **', value = '** **')
		embed.add_field(inline = False, name = 'DPS ' + damage, value = dpsMessage)
		embed.add_field(inline = False, name = '\u200b', value = 'use the ractions below to sign up for the role you wish to fill\nuse ' + remove + ' to remove yourself from the roster\nuse ' + delete + ' to delete the roster (avaliabel only to the roster\'s creator)\nif you press a react and do not see your name appear on the list, please clear the react and try again\nif there are further problem please contact Hope4Worthy#1507 for further assistance')
	return embed




async def addReactions(message, seats):
	if seats < 0: # expandable event roster
		await message.add_reaction(expand)
		await message.add_reaction(remove)
		await message.add_reaction(delete)
	elif(seats > 0): # fixed seating event roster or arena roster
		await message.add_reaction(general)
		await message.add_reaction(remove)
		await message.add_reaction(delete)
	else: # trial and dungeon rosters
		await message.add_reaction(tank)
		await message.add_reaction(heal)
		await message.add_reaction(damage)
		await message.add_reaction(remove)
		await message.add_reaction(delete)



def getType(eName):
	eType = 'Dungeon'
	length = len(eName)
	for abr, name in arenaNames:
		if abr in eName.upper() and length <= 4:
			return ['Arena', abr, name]
		elif name.upper() in eName.upper():
			return ['Arena', abr, name]
	for abr, name in trialNames:
		if abr in eName.upper() and length <= 4:
			return ['Trial', abr, name]
		elif name.upper() in eName.upper():
			return ['Trial', abr, name]
	for abr, name in dungeonNames:
		if abr in eName.upper() and length <= 4:
			return ['Dungeon', abr, name]
		elif name.upper() in eName.upper():
			return ['Dungeon', abr, name]
	return eType



def checkDuplicate(user, embed):
	for field in embed.fields:
		if user.mention in field.value:
			return True
	return False



def removeUser(user, embed, expandFlag):
	if expandFlag == 0:
		if user.mention in embed.fields[4].value:
			new = embed.fields[4].value.replace(user.mention, ' ')
			embed.set_field_at(index = 4, name = embed.fields[4].name, value = new)
		elif user.mention in embed.fields[6].value:
			new = embed.fields[6].value.replace(user.mention, ' ')
			embed.set_field_at(index = 6, name = embed.fields[6].name,value = new)
		elif user.mention in embed.fields[8].value:
			new = embed.fields[8].value.replace(user.mention, ' ')
			embed.set_field_at(index = 8, name = embed.fields[8].name, value = new)
		return embed
	else:
		field = embed.fields[4]
		for i in range(1, 9999):
			if str(i)+':<@' in field.value:
				new = field.value.replace(str(i) + ':' + user.mention, '')
				embed.set_field_at(index = 4, name = embed.fields[4].name, value = new)
				break
			elif not str(i) in field.value:
				break
			else:
				continue
		return embed
		


def addTank(user, embed):
	field = embed.fields[4]
	for i in range(1, 13):
		if str(i)+':<@' in field.value:
			continue
		elif str(i)+':' in field.value:
			new = field.value.replace(str(i) + ':', str(i) + ':' + user.mention)
			embed.set_field_at(index = 4, name = embed.fields[4].name, value = new)			
			break
		else:
			break
	return embed



def addHealer(user, embed):
	field = embed.fields[6]
	for i in range(1, 13):
		if str(i)+':<@' in field.value:
			continue
		elif str(i)+':' in field.value:
			new = field.value.replace(str(i) + ':', str(i) + ':' + user.mention)
			embed.set_field_at(index = 6, name = embed.fields[6].name, value = new)			
			break
		else:
			break
	return embed



def addDPS(user, embed):
	field = embed.fields[8]
	for i in range(1, 13):
		if str(i)+':<@' in field.value:
			continue
		elif str(i)+':' in field.value:
			new = field.value.replace(str(i) + ':', str(i) + ':' + user.mention)
			embed.set_field_at(index = 8, name = embed.fields[8].name, value = new)			
			break
		else:
			break
	return embed



def addGeneral(user, embed):
	field = embed.fields[4]
	for i in range(1, 13):
		if str(i)+':<@' in field.value:
			continue
		elif str(i)+':' in field.value:
			new = field.value.replace(str(i) + ':', str(i) + ':' + user.mention)
			embed.set_field_at(index = 4, name = embed.fields[4].name, value = new)	
			break
		else:
			break
	return embed



def addExpand(user, embed):
	field = embed.fields[4]
	for i in range(1, 9999):
		if str(i)+':<@' in field.value:
			continue
		else:
			new = field.value + '\n' + str(i) + ':' + user.mention
			embed.set_field_at(index = 4, name = embed.fields[4].name, value = new)
			break
	return embed



bot.run(TOKEN)
