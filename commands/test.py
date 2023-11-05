# commands/test.py

import discord
from discord.ext import commands

async def common_test_logic(ctx, number: int, slash: bool = False):
    response = f'Vous avez demandé à tester le numéro {number}!'
    if slash:
        await ctx.respond(response)
    else:
        await ctx.send(response)

def setup(bot):
    @bot.command(name='test')
    async def test(ctx, number: int):
        await common_test_logic(ctx, number)

    @bot.slash_command(name='test')
    async def test_slash(ctx, number: int):
        await common_test_logic(ctx, number, slash=True)
