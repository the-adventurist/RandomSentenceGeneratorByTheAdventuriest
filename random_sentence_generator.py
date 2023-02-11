import random


def get_random_word(words):
    return random.choice(words)


names = ['Michelle', 'Beverly', 'Ice', 'Brian', 'George', 'Anthony', 'Giselle', 'Setfani', 'Philip']
places = ['the Moon', 'Sofia', 'Varna', 'Plovdiv', 'Istanbul', 'Wonderful world', 'overseas', 'Polyanci', 'Alexxandria']
verbs = ['gets rid of', 'eats', 'holds', 'builds', 'flies', 'sleeps', 'smokes', 'waters', 'looks', 'brinks', 'drinks', 'prays']
nouns = ['stone', 'rock', 'bike', 'road', 'bottle', 'leather', 'ladder', 'horse', 'plate', 'wine', 'jar', 'orange']
adverbs = ['diligently', 'slowly', 'hardly', 'warmly', 'coldly', 'toughly', 'permanently', 'violently', 'reliably']
details = ['along the river bank', 'at home', 'at work', 'in the office', 'of the peak of the bullshits',
           'somewhere in the middle of their nowhere', 'under the table of thier parent\'s house'
           'under the water', 'on the roof of the friend\'s house', 'under someone\'s vehicle']

print('Hello this is your first random sentence:')
while True:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_detail = get_random_word(details)

    print(f'{random_name} from {random_place} {random_adverb} {random_verb} {random_noun}')
    print(input('Click [Enter] to generate new one.'))
