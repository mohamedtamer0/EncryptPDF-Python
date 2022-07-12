from os import listdir
from random import choice
import pikepdf
from pikepdf import Pdf
Data=[]
path="D:\Attchment"
OutputFolder="D:\Attchment"
pdfs=[ filename for filename in listdir(path) if filename.endswith(".pdf") ]
for pdf in pdfs:
    temppassword=''.join([choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for i in range(10)])
    with Pdf.open(f"{path}/{pdf}") as pdffile:
        pdffile.save(f"{OutputFolder}/{pdf[:-4]}_encrypted.pdf",encryption=pikepdf.Encryption(owner=temppassword, user=temppassword, R=4))
    Data.append(f"{pdf},{temppassword}")
open("credentials.csv","a").writelines(s + '\n' for s in Data)