import glob;
import tesserocr
from PIL import Image
import datetime
import ImgProcess
import DateC
NewData = ImgProcess.ocr()
GetTodayDate = DateC.Date();
print(NewData.DateProd)
ProductDates = NewData.DateProd
NewData.GetDate(ProductDates)
ProductDays = ['-1']
ProductMonths = ['-1']
ProductYears = ['-1']
ProductDays.extend(NewData.Days)
ProductMonths.extend(NewData.Months)
ProductYears.extend(NewData.Years)
ProductDays.remove('-1')
ProductMonths.remove('-1')
ProductYears.remove('-1')
for idx in range(ProductDays.__len__()):
    ProductMonths[idx].strip('. ')
    ProductYears[idx].strip('. ')
    ProductDays[idx].strip('.')
print(ProductDays)
TodayDay = datetime.date.today().day
TodayMonth = datetime.date.today().month
TodayYear = datetime.date.today().year
# File to Write
fileExt = '.txt'
fileName = input('Indicate File Name : ')
f = open(fileName+fileExt,'a')
f.write('\nFile contains details about product codes regarding with the Product Dates\n')
f.write('Product Indexes are given by number on the Left before -(dash) symbol')
for i in range(ProductDates.__len__()):
    ProductDays[i].replace('.','');
    ProductMonths[i].replace('.','');
    ProductYears[i].replace('.','');
    #lineTowrite = [i,'- Product Date :',ProductDates[i]]
    f.write('\n')
    f.write(str(i));f.write('- Product Date :');f.write(ProductDates[i]);
f.close();
