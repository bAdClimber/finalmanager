import discord
import asyncio
from discord.ext import commands
from discord import Guild

client = commands.Bot(command_prefix='!!')


def is_not_pinned(mess):
    return not mess.pinned


@client.event
async def on_ready():
    print('wir sind eingeloogt als User {}'.format(client.user.name))
    client.loop.create_task(status_task())


async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('Event Manager'), status=discord.Status.online)
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game('evolved by Klausig,Climber'), status=discord.Status.online)
        await asyncio.sleep(3)


@client.command()
async def montag(ctx):
    guild: Guild = client.get_guild(545615291992768522)
    await ctx.send('!!clear 1')
    member = discord.utils.get(guild.roles, name="iOwNFAM")
    mess = await ctx.send(f'{member.mention}\r\n'
                          'Kommenden __**Montag - 20:00 Uhr**__ *T2*\r\n'
                          'PUBGM Romania Scrim - 4 Runden\r\n'
                          '---\r\n'
                          '__Alternativ:__\r\n'
                          'Europe Gaming League - 3 Runden\r\n'
                          'PUBGM Greece - 3 Runden')
    await mess.add_reaction(':Adobe_20200321_113931:698860021584494663')
    await mess.add_reaction(':Adobe_20200321_113804:698860007864664104')
    await mess.add_reaction(':Sub:698860033521352754')
    await asyncio.sleep(1)
    mess = await ctx.send(f'{member.mention}\r\n'
                          'Kommenden __**Montag - 20:20 Uhr**__ *FPP*\r\n'
                          'The Purge Scrim\r\n'
                          '3 Runden\r\n')
    await mess.add_reaction(':Adobe_20200321_113931:698860021584494663')
    await mess.add_reaction(':Adobe_20200321_113804:698860007864664104')
    await mess.add_reaction(':Sub:698860033521352754')
    await asyncio.sleep(1)


@client.command()
async def dienstag(message):
    guild: Guild = client.get_guild(545615291992768522)
    await message.channel.send('!!clear 1')
    member = discord.utils.get(guild.roles, name="iOwNFAM")
    mess = await message.channel.send(f'{member.mention}\r\n'
                                      'Kommenden __**Dienstag - 20:00 Uhr**__ *T1 Option*\r\n'
                                      'Brute Scrim - 3 Runden\r\n'
                                      '---\r\n'
                                      '__Alternativ:__\r\n'
                                      'EGL - 3 Runden\r\n'
                                      'NightCore - 3 Runden\r\n')
    await mess.add_reaction(':Adobe_20200321_113931:698860021584494663')
    await mess.add_reaction(':Adobe_20200321_113804:698860007864664104')
    await mess.add_reaction(':Sub:698860033521352754')
    await asyncio.sleep(1)
    mess = await message.channel.send(f'{member.mention}\r\n'
                                      'Kommenden __**Dienstag - 20:30 Uhr**__ *TPP <-> FPP*\r\n'
                                      'PUBGM France Scrim\r\n'
                                      '3 Runden\r\n')
    await mess.add_reaction(':Adobe_20200321_113931:698860021584494663')
    await mess.add_reaction(':Adobe_20200321_113804:698860007864664104')
    await mess.add_reaction(':Sub:698860033521352754')
    await asyncio.sleep(1)
    mess = await message.channel.send(f'{member.mention}\r\n'
                                      'Kommenden __**Dienstag - 21:00 Uhr**__ *TPP*\r\n'
                                      'Laughing Coffin Scrim\r\n'
                                      '3 Runden\r\n')
    await mess.add_reaction(':Adobe_20200321_113931:698860021584494663')
    await mess.add_reaction(':Adobe_20200321_113804:698860007864664104')
    await mess.add_reaction(':Sub:698860033521352754')
    await asyncio.sleep(1)


@client.command()
async def mittwoch(message):
    guild: Guild = client.get_guild(545615291992768522)
    await message.channel.send('!!clear 1')
    member = discord.utils.get(guild.roles, name="iOwNFAM")
    mess = await message.channel.send(f'{member.mention}\r\n'
                                      'Kommenden __**Mittwoch - 20:00 Uhr**__ *TPP*\r\n'
                                      'Endgegner Scrim - 3 Runden\r\n'
                                      '---\r\n'
                                      '__Alternativ:__\r\n'
                                      'EGL - 3 Runden\r\n')
    await mess.add_reaction(':Adobe_20200321_113931:698860021584494663')
    await mess.add_reaction(':Adobe_20200321_113804:698860007864664104')
    await mess.add_reaction(':Sub:698860033521352754')
    await asyncio.sleep(1)


@client.command()
async def donnerstag(message):
    guild: Guild = client.get_guild(545615291992768522)
    await message.channel.send('!!clear 1')
    member = discord.utils.get(guild.roles, name="iOwNFAM")
    mess = await message.channel.send(f'{member.mention}\r\n'
                                      'Kommenden __**Donnerstag - 20:00 Uhr**__ *T2*\r\n'
                                      'The Hate Scrim\r\n'
                                      '4 Runden PMCO settings\r\n'
                                      '---\r\n'
                                      'EGL - 3 Runden\r\n')
    await mess.add_reaction(':Adobe_20200321_113931:698860021584494663')
    await mess.add_reaction(':Adobe_20200321_113804:698860007864664104')
    await mess.add_reaction(':Sub:698860033521352754')
    await asyncio.sleep(1)
    mess = await message.channel.send(f'{member.mention}\r\n'
                                      'Kommenden __**Donnerstag - 21:00 Uhr**__ *TPP*\r\n'
                                      'Laughing Coffin Scrim\r\n'
                                      '3 Runden\r\n')
    await mess.add_reaction(':Adobe_20200321_113931:698860021584494663')
    await mess.add_reaction(':Adobe_20200321_113804:698860007864664104')
    await mess.add_reaction(':Sub:698860033521352754')
    await asyncio.sleep(1)


@client.command()
async def freitag(message):
    guild: Guild = client.get_guild(545615291992768522)
    await message.channel.send('!!clear 1')
    member = discord.utils.get(guild.roles, name="iOwNFAM")
    mess = await message.channel.send(f'{member.mention}\r\n'
                                      'Kommenden __**Freitag - 20:00 Uhr**__ *TPP*\r\n'
                                      'ULC-NEO scrim - 3 Runden\r\n'
                                      '---\r\n'
                                      '__Alternativ:__\r\n'
                                      'Sickology - 3 Runden\r\n'
                                      'EGL - 3 Runden\r\n')
    await mess.add_reaction(':Adobe_20200321_113931:698860021584494663')
    await mess.add_reaction(':Adobe_20200321_113804:698860007864664104')
    await mess.add_reaction(':Sub:698860033521352754')
    await asyncio.sleep(1)
    mess = await message.channel.send(f'{member.mention}\r\n'
                                      'Kommenden __**Freitag - 21:00 Uhr**__ *TPP*\r\n'
                                      '7Atoms scrim\r\n'
                                      '4 Runden\r\n')
    await mess.add_reaction(':Adobe_20200321_113931:698860021584494663')
    await mess.add_reaction(':Adobe_20200321_113804:698860007864664104')
    await mess.add_reaction(':Sub:698860033521352754')
    await asyncio.sleep(1)
    mess = await message.channel.send(f'{member.mention}\r\n'
                                      'Kommenden __**Freitag - 24:00 Uhr**__ *TPP*\r\n'
                                      '2 Runden\r\n')
    await mess.add_reaction(':Adobe_20200321_113931:698860021584494663')
    await mess.add_reaction(':Adobe_20200321_113804:698860007864664104')
    await mess.add_reaction(':Sub:698860033521352754')
    await asyncio.sleep(1)


@client.command()
async def samstag(message):
    guild: Guild = client.get_guild(545615291992768522)
    await message.channel.send('!!clear 1')
    member = discord.utils.get(guild.roles, name="iOwNFAM")
    mess = await message.channel.send(f'{member.mention}\r\n'
                                      'Kommenden __**Samstag - 20:00 Uhr**__ *TPP*\r\n'
                                      'Hyllos Scrim - 3 Runden\r\n'
                                      '---\r\n'
                                      '__Alternativ:__\r\n'
                                      'Anti Clan - 4 Runden\r\n')
    await mess.add_reaction(':Adobe_20200321_113931:698860021584494663')
    await mess.add_reaction(':Adobe_20200321_113804:698860007864664104')
    await mess.add_reaction(':Sub:698860033521352754')
    await asyncio.sleep(1)
    mess = await message.channel.send(f'{member.mention}\r\n'
                                      'Kommenden __**Samstag - 23:30 Uhr**__ *FPP*\r\n'
                                      'PDX Scrim\r\n'
                                      '2 Runden\r\n')
    await mess.add_reaction(':Adobe_20200321_113931:698860021584494663')
    await mess.add_reaction(':Adobe_20200321_113804:698860007864664104')
    await mess.add_reaction(':Sub:698860033521352754')
    await asyncio.sleep(1)


@client.command()
async def sonntag(message):
    guild: Guild = client.get_guild(545615291992768522)
    await message.channel.send('!!clear 1')
    member = discord.utils.get(guild.roles, name="iOwNFAM")
    mess = await message.channel.send(f'{member.mention}\r\n'
                                      'Kommenden __**Sonntag - 20:00 Uhr**__ *TPP*\r\n'
                                      'Owning Nation Scrim\r\n'
                                      '3 Runden\r\n')
    await mess.add_reaction(':Adobe_20200321_113931:698860021584494663')
    await mess.add_reaction(':Adobe_20200321_113804:698860007864664104')
    await mess.add_reaction(':Sub:698860033521352754')
    await asyncio.sleep(1)


@client.command()
async def ares(message):
    guild: Guild = client.get_guild(545615291992768522)
    await message.channel.send('!!clear 1')
    member = discord.utils.get(guild.roles, name="iOwNFAM")
    mess = await message.channel.send(f'{member.mention}\r\n'
                                      'Kommenden __**Montag - 20:00 Uhr**__ *T2*\r\n'
                                      'PUBGM Romania Scrim - 4 Runden')
    await mess.add_reaction(':Adobe_20200321_113931:698860021584494663')
    await mess.add_reaction(':Adobe_20200321_113804:698860007864664104')
    await mess.add_reaction(':Sub:698860033521352754')
    await asyncio.sleep(1)
    mess = await message.channel.send(f'{member.mention}\r\n'
                                      'Kommenden __**Dienstag - 20:00 Uhr**__ *T1 Option*\r\n'
                                      'Brute Scrim - 3 Runden')
    await mess.add_reaction(':Adobe_20200321_113931:698860021584494663')
    await mess.add_reaction(':Adobe_20200321_113804:698860007864664104')
    await mess.add_reaction(':Sub:698860033521352754')
    await asyncio.sleep(1)
    mess = await message.channel.send(f'{member.mention}\r\n'
                                      'Kommenden __**Mittwoch - 20:00 Uhr**__ *TPP*\r\n'
                                      'Endgegner Scrim - 3 Runden\r\n'
                                      '---\r\n'
                                      '__Alternativ:__\r\n'
                                      'EGL - 3 Runden\r\n')
    await mess.add_reaction(':Adobe_20200321_113931:698860021584494663')
    await mess.add_reaction(':Adobe_20200321_113804:698860007864664104')
    await mess.add_reaction(':Sub:698860033521352754')
    await asyncio.sleep(1)
    mess = await message.channel.send(f'{member.mention}\r\n'
                                      'Kommenden __**Donnerstag - 20:00 Uhr**__ *T2*\r\n'
                                      'The Hate Scrim\r\n'
                                      '4 Runden PMCO settings\r\n'
                                      '---\r\n'
                                      'EGL - 3 Runden\r\n')
    await mess.add_reaction(':Adobe_20200321_113931:698860021584494663')
    await mess.add_reaction(':Adobe_20200321_113804:698860007864664104')
    await mess.add_reaction(':Sub:698860033521352754')
    await asyncio.sleep(1)
    mess = await message.channel.send(f'{member.mention}\r\n'
                                      'Kommenden __**Freitag - 21:00 Uhr**__ *TPP*\r\n'
                                      '7Atoms scrim\r\n'
                                      '4 Runden\r\n')
    await mess.add_reaction(':Adobe_20200321_113931:698860021584494663')
    await mess.add_reaction(':Adobe_20200321_113804:698860007864664104')
    await mess.add_reaction(':Sub:698860033521352754')
    await asyncio.sleep(1)
    mess = await message.channel.send(f'{member.mention}\r\n'
                                      'Kommenden __**Samstag - 20:00 Uhr**__ *TPP*\r\n'
                                      'Hyllos Scrim - 3 Runden\r\n'
                                      '---\r\n'
                                      '__Alternativ:__\r\n'
                                      'Anti Clan - 4 Runden\r\n')
    await mess.add_reaction(':Adobe_20200321_113931:698860021584494663')
    await mess.add_reaction(':Adobe_20200321_113804:698860007864664104')
    await mess.add_reaction(':Sub:698860033521352754')
    await asyncio.sleep(1)
    mess = await message.channel.send(f'{member.mention}\r\n'
                                      'Kommenden __**Sonntag - 20:00 Uhr**__ *TPP*\r\n'
                                      'Owning Nation Scrim\r\n'
                                      '3 Runden\r\n')
    await mess.add_reaction(':Adobe_20200321_113931:698860021584494663')
    await mess.add_reaction(':Adobe_20200321_113804:698860007864664104')
    await mess.add_reaction(':Sub:698860033521352754')
    await asyncio.sleep(1)


@client.command()
async def clear(ctx, amount=100):
    guild: Guild = client.get_guild(545615291992768522)
    if ctx.author.permissions_in(ctx.channel).manage_messages:
        await ctx.channel.purge(limit=amount, check=is_not_pinned)
        pruge = await ctx.channel.send(f'{amount} Nachichten wurden gelöscht!')
        await asyncio.sleep(5)
        await pruge.delete()
        return

    haha = await ctx.channel.send(f'{ctx.author.mention} du darfst das nicht!')
    await asyncio.sleep(5)
    await haha.delete()


client.run('NzA3ODU2MjI2NjgzMTkxMzI3.XrO4iA.lrrb79bo0KFA15eKrAiKSevcSqA')

