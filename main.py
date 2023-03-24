
print("""                                             >>>WELCOME TO PDF<<< MERGER                                    """)


from PyPDF2 import PdfWriter
import os


merge=PdfWriter()

files=[file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merge.append(pdf)

name=input("Enter the name by which you want to save the Merged PDF file:")
merge.write(f"{name}.pdf")
merge.close()    

print(f'''                           Your merged PDF named {name}.pdf is ready. Thankyou for visiting!
      ''')