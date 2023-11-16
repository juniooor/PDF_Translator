from pypdf import PdfReader
from translate import Translator
translator = Translator(to_lang='pt')

reader = PdfReader("In The Night.pdf")

for page in reader.pages:
    text = page.extract_text()
    linhas = text.splitlines()
    for linha in linhas:
        print(linha)
        traducao = translator.translate(linha)
        print(traducao, '\n')
 
   
