import PyPDF2
import pandas as pd
import os

column_names = ["Name", "Description"]
securityPatterns_df = pd.DataFrame(columns = column_names)

columns = list(securityPatterns_df)
data = []
# Folder Path
path = r"/Users/sayali/OneDrive - UW/Capstone/Code/PDFParsing/Data/secureDesignPatterns.pdf"

# creating a pdf file object 
pdfFileObj = open(path, 'rb') 
read_pdf = PyPDF2.PdfFileReader(pdfFileObj)

initialPages = 7
IndexPages = [6,9,16,26,29,38,48,57,69,75,82,90,94,96,102,106] # define variable for using in loop.

patternName = ['Distrustful Decomposition','PrivSep','Defer to Kernel','Secure Factory','Secure Strategy Factory',
               'Secure Builder Factory','Secure Chain of Responsibility','Secure State Machine','Secure Visitor',
              'Secure Logger','Clear Sensitive Information','Secure Directory','Pathname Canonicalization','Input Validation',
              'Resource Acquisition Is Initialization']

n = len(IndexPages)
for index, obj in enumerate(IndexPages):
    if index < (n-1):
        start = obj
        end = IndexPages[index + 1 ]
        number_of_pages = range(start+initialPages,end+initialPages)
        page_content=""
        #print(number_of_pages)
        for page_number in number_of_pages:
            page = read_pdf.getPage(page_number)
            page_content += page.extractText()     # concate reading pages.
        
        values =[patternName[index], page_content.replace('| CMU/SEI-2009-TR-010',' ')]
        zipped = zip(columns, values)
        a_dictionary = dict(zipped)
        data.append(a_dictionary)

securityPatterns_df = securityPatterns_df.append(data, True)
securityPatterns_df.to_csv("output/securityDesignPatternsBookData.csv", index=False)

securityPatterns_df = pd.read_csv("/Users/sayali/OneDrive - UW/Capstone/Code/PDFParsing/output/securityDesignPatternsBookData.csv", encoding="utf-8-sig")


os.chdir("/Users/sayali/OneDrive - UW/Capstone/Code/PDFParsing/output")
i = 0
for index, row in securityPatterns_df.iterrows():
    if i > len(securityPatterns_df):
       break
    else:
       f = open(row[0]+'.txt', 'w')
       f.write(row[1])
       f.close()
       i+=1