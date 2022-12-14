import random

def getRandomMessage(txt):
    TextLib_array = txt.read().split(',')
    message = random.sample(TextLib_array, 1)
    return message[0]

def response(content):
    message = ''
    if (content == '哇靠'):
        with open('TextLib/哇靠.txt', 'r', encoding='utf-8') as txt:
            message = getRandomMessage(txt)

    elif (content == '哭阿') | (content == '哭啊'):
        with open('TextLib/哭阿.txt', 'r', encoding='utf-8') as txt:
            message = getRandomMessage(txt)

    elif (content == '真的假的') | (content == '真的假的拉'):
        with open('TextLib/真的假的.txt', 'r', encoding='utf-8') as txt:
            message = getRandomMessage(txt)

    elif (content == '真的欸') | (content == '真的ㄟ'):
        with open('TextLib/真的欸.txt', 'r', encoding='utf-8') as txt:
            message = getRandomMessage(txt)

    elif (content == '笑死') | (content == '校死') | (content == '笑die'):
        with open('TextLib/笑死.txt', 'r', encoding='utf-8') as txt:
            message = getRandomMessage(txt)

    elif (content == '讚喔') | (content == '讚哦') | (content == '讚ㄛ'):
        with open('TextLib/讚喔.txt', 'r', encoding='utf-8') as txt:
            message = getRandomMessage(txt)

    elif (content[:6] == '@ANGEL') | (content[:2] == '源昌') | (content[:2] == '元昌'):
        with open('TextLib/ANGEL.txt', 'r', encoding='utf-8') as txt:
            message = getRandomMessage(txt)

    return message