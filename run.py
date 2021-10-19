import urllib.request 
from fpdf import FPDF
from os import listdir

print('Start Download') 

path = "C:/Users/yaros/Downloads/prez2/" # Путь к скачанным картинкам

pdfFileName = "file.pdf" # Имя будущего PDF файла

n = 1
try:
    while (n < 5):
        # Указать ссылку на картинку. У меня картинка с "удоными" названиями, поэтому беру все циклом по имени
        url = f'https://webkim.online/presentation/9f30223aa5c65ac9ca033d82f2851be2cf38a6cc-1634619619386/presentation/b947139544c61d1367ce10265a5dc62a8be9855d-1634619866221/slide-{n}.png'
        urllib.request.urlretrieve(url, f'{path}'+f'{n}.png')
        print(f'{n}.png download')
        n+=1
except:
    print('File downloaded')

imagelist = listdir(path) # получение списка изображений

pdf = FPDF('L','mm','my') # Создание документа с форматами страниц 1900*600

x,y,w,h = 0,0,0,0 # Значения для размещения картинок

for image in imagelist:

    pdf.add_page()
    pdf.image(path+image,x,y,w,h)

pdf.output(pdfFileName,"F") #ывгрузка pdf файла на рабочий стол
print('PDF convert done')

