import asyncio
from unittest import result

async def sum(a, b):
    return a + b

async def print_sum(a, b):
    result = await sum(a, b)
    print(f'O resultado da soma é: {result}')

asyncio.run(print_sum(3, 5))