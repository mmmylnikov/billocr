import easyocr
from datetime import datetime
import time
start_time = time.time()

FOLDER_OCR = '/Users/mylnikov/Documents/GitHub/billocr/'+\
             'testfile/article/ '
FILE_OCR = '4.jpeg'

reader = easyocr.Reader(['uk', 'ru', 'en'])
result = reader.readtext(FOLDER_OCR + FILE_OCR)
precSUM = 0

f = open('exportOCR.txt', 'w')
f.close
f = open('exportOCR.txt', 'a')
f.write('Файл: {}\n'.format(FILE_OCR))
f.write('Текст OCR:\n')
f.write('====================================\n')

for text in result:
    print(text[1])
    f.write(text[1] + '\n')
    precSUM += text[2]

precAVG = round(precSUM/len(result)*100, 2)

f.write('====================================\n')
finish_time = round(time.time() - start_time, 2)
f.write('Текст распознан за {} сек\n'.format(finish_time))
f.write('Усредненная точность распознавания {} %\n'.format(precAVG))
f.close

print(result)