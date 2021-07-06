import aiohttp

class madlibs:
    async def main():

        data = {}

        types = ['adjective', 'verb', 'noun']

        url = 'https://reminiscent-steady-albertosaurus.glitch.me/'

        async with aiohttp.ClientSession() as session:

            for type in types:
                tempUrl = url + type
                async with session.get(tempUrl) as resp:
                    data[type] = await resp.json()

        sentence = 'The ' + data['noun'] + ' tried to ' + data['verb'] + ', but it was too ' + data['adjective'] + '.'

        return sentence
