import tesserocr
from PIL import Image
import glob;

print(tesserocr.tesseract_version())  # print tesseract-ocr version
print(tesserocr.get_languages())  # prints tessdata path and list of available languages


####!!!!! Always Use Image.open in image_to_text to get better results
class ocr(object):
    def __init__(self):
        print("Consturctor Called\nIt does not store any data!");
        self.FilenameList = glob.glob("set1/*.bmp");
        self.ReadedText = [''];
        self.DateStart = [''];  # DateStart will be assigned to -5 of ReadedText
        self.DateProd = [''];
        self.ReadTxt();
        self.findDate();
        self.Days = ['']
        self.Months = ['']
        self.Years = ['']
        self.fixDates()
        print("Finished to Construct data!")
        return

    def ReadTxt(self):
        for x in range(self.FilenameList.__len__()):
            self.LineText = tesserocr.image_to_text(Image.open(self.FilenameList[x]), lang='ces');
            self.ReadedText.append(self.LineText)
        self.ReadedText.remove('');

    def findDate(self):
        for x in range(self.ReadedText.__len__()):
            chrIdx = (self.ReadedText[x].find('.20')) - 5  # Returns .20 index,Automatically Returns Beginning index
            # If Fails we will use other method
            if (chrIdx == -1):
                chrIdx = (self.ReadedText[x].find(' 20')) - 6  # Returns  20 index,Automatically Returns Beginning index
            # Now We have safe swith in the cases
            FoundDate = self.ReadedText[x][chrIdx:chrIdx + 11]  # Found Date;
            # Replace Errors With Proficent Numbers #
            FoundDate.replace(' ', '')
            FoundDate.replace('\n', '')
            # Replace Errors With Proficent Numbers
            self.DateProd.append(FoundDate)  # Add date to list
        self.DateProd.remove('')

    def fixDates(self):
        for x in range(self.DateProd.__len__()):
            self.DateProd[x].replace(" ", '');
            self.DateProd[x].replace("\n", '');

    def GetDate(self, List):
        for x in List:
            ProdDay = x[0:2]
            ProdMonth = x[3:5]
            ProdYear = x[6:10]
            self.Days.append(ProdDay)
            self.Months.append(ProdMonth)
            self.Years.append(ProdYear)
        self.Days.remove('')
        self.Months.remove('')
        self.Years.remove('')