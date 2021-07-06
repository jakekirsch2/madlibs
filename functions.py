import aiohttp

class madlibs:
    # def main():
    #     url = 'https://reminiscent-steady-albertosaurus.glitch.me/'


    #     adjective = requests.get(url=url + 'adjective').text.replace('"','')
    #     verb = requests.get(url=url + 'verb').text.replace('"','')
    #     noun = requests.get(url=url + 'noun').text.replace('"','')

    #     sentence = 'The elephant tried to ' + verb + ' the ' + noun + ', but it was too ' + adjective + '.'

    #     return sentence
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

# print(asyncio.run(madlibs.main()))
