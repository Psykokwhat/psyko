import discord
from discord.ext import commands
import asyncio
from asyncio import *
import random
from random import randint
import os

bot = commands.Bot(description='Psykose', command_prefix='h!')

@bot.event
async def on_member_join(member):
	my_guild = bot.get_guild(457198861635813386)
	join = my_guild.get_channel(457199084269338634)
	await join.send(f"**Bienv'nue dans l'Hôpital Psykotrique, {member.mention}. Va donc lire les <#457200817888559104> avant tout chose si tu ne veux pas finir en quarantaine mon salaud.**")

@bot.event
async def on_member_remove(member):
	my_guild = bot.get_guild(457198861635813386)
	join = my_guild.get_channel(457199084269338634)
	await join.send(f"**{member.display_name} nous a quittés, il est desormais libre et sain d'esprit ! Félicitons-le.**")

@bot.command()
async def gay(ctx):
	"""A quel pourcentage suis-je gay ?"""
	a = randint(0,100)
	msg = await ctx.send('**Activation en cours... Veuillez ne pas éteindre le patient.** <a:psygif_loading:511175795192889344>')
	await asyncio.sleep(1.5)
	if a<6:
		await msg.edit(content=(f"**Vous êtes gay à seulement {a}%, il semble que vous soyez atteint d'hétérosexualité aigue ! On va devoir vous mettre en quarantaine. Dieu vous garde..."))
	elif a<26:
		await msg.edit(content=(f"**{a}% ? Hm, il semble que vous ayez été infecté d'hétérosexualité de manière assez conséquente... Nous allons devoir procéder à un toucher rectal pour finaliser l'analyse. Restez en place, s'il-vous-plaît !**"))
	elif a<51:
		await msg.edit(content=(f"**Vous semblez ne porter en vous que {100-a}% d'hétérosexualité, c'est plutôt bon signe. On vous laisse partir ~**"))
	else:
		await msg.edit(content=(f"**Waow ! {a}% ! Vous semblez être épargné de cette saloperie d'hétérosexualité, c'est tout bon pour vous.**"))


bot.run(bot.run(os.environ['TOKEN']))
