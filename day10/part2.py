from collections import defaultdict

lines = [l.strip() for l in open('input.txt').readlines()]

outputs = defaultdict(list)
bots = defaultdict(list)
instructions = []
bot_instructions = []


for line in lines:
    if line.startswith('value'):
        chip, _, bot_num = line.partition(' goes to bot ')
        _, _, chip = chip.partition(' ')
        bots[bot_num].append(int(chip))
    else:
        instructions.append(line)

for instruction in instructions:
    bot_num, _, rest = instruction.partition(' gives low to ')
    _, _, bot_num = bot_num.partition(' ')
    low_to, _, high_to = rest.partition(' and high to ')
    bot_instructions.append({
        'bot_num': bot_num,
        'low': low_to,
        'high': high_to
    })

while True:
    found = False
    for i in bot_instructions:
        if len(bots[i['bot_num']]) > 1:
            found = True
            if i['low'].startswith('bot'):
                bots[i['low'].split(' ')[-1]].append(min(*bots[i['bot_num']]))
            else:
                outputs[i['low'].split(' ')[-1]].append(min(*bots[i['bot_num']]))

            if i['high'].startswith('bot'):
                bots[i['high'].split(' ')[-1]].append(max(*bots[i['bot_num']]))
            else:
                outputs[i['high'].split(' ')[-1]].append(max(*bots[i['bot_num']]))

            bots[i['bot_num']] = []
    if not found:
        print outputs['0'][0] * outputs['1'][0] * outputs['2'][0]
        exit()

