import discord
import asyncio
import datetime
import random
import os
intents = discord.Intents.all()
token = "Nzk0MDY5OTAwMDk2MTc2MTQ4.X-1dOQ.yBMhVk0zU-vPPp0NyY01dryV2dU"
client = discord.Client()

@client.event
async def on_ready(): 
    print("ready")
    print(client.user)
    print(client.user.id)
    print('====================================')

@client.event
async def on_message(message): 
    if message.content == '찌츄야 도움말':
        embed=discord.Embed(color=0xff00, title="찌츄봇 명령어", description="명령어를 사용해봐요!", timestamp=message.created_at)
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url) 
        embed.add_field(name = '서버 유저 불러와', value = '전체 유저 수') 
        embed.add_field(name = '유저 상태 불러와', value = '유저 상태 online, offline') 
        embed.add_field(name = '찌츄야 안녕', value = '안녕하세요!') 
        embed.add_field(name = '찌츄야 숫자 선택', value = '랜덤 1 ~ 10000') 
        embed.add_field(name = '찌츄야 타이머', value = '10초 타이머') 
        embed.add_field(name = '!청소', value = '관리자 이외에 사용 할 시 경고') 
        await message.channel.send(embed=embed)

    if message.content == "서버 유저 불러와":
        await message.channel.send(len(message.guild.members))

    if message.content == "유저 상태 불러와":
        await message.channel.send(message.author.status)

    if message.content.startswith('찌츄야 안녕'):
        channel = message.channel 
        await channel.send('안녕하세요!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))

    if message.content == "찌츄야 숫자 선택":
        await message.channel.send(random.randint(1, 10000))

    if message.content == "찌츄야 타이머":
        await asyncio.sleep(1800)
        await message.channel.send(f"{message.author.mention}님 1800초가 지났어요!")

    if message.content.startswith("!청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메시지가 삭제되었습니다!")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)


