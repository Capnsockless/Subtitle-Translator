import pysrt
import yaml
from translatepy import Translator
import os

#Open config file
with open('config.yaml', 'r') as file:
    subParams = yaml.safe_load(file)

filename = subParams['inputSubs']
#Load subtitles
subs = pysrt.open('Subtitles/' + filename, encoding='UTF-8')

#Initialize the translator
translator = Translator()

inLang = subParams['inputLang']
outLang = subParams['outputLang']
for i in subs:
    currSub = i.text
    translation = translator.translate(text=currSub, source_language=inLang, destination_language=outLang)
    i.text = translation

#Add the result language name onto the filename and save it
outputFile = filename
outputFile = outputFile[:max([idx for idx, x in enumerate(outputFile) if x == '.'])]

outputFileName = outputFile + outLang + '.srt'

subs.save('Subtitles/' + outputFileName, encoding='UTF-8')
