#1/usr/bi/envpython3
from PIL import Image
import subprocess
import os, sys 

def get_all_pdf_files_as_list(path):
  pdfs={}
  for file in os.listdir(path):
    f,e=os.path.splitext(file)
    if e==".pdf":
      pdfs.append(file) 
      return pdfs

def main():
     running=True 

     while running: 
      print("select")
      option=input("Type for c for compression, m for merge and s for image to pdf and type q to exit")
      if option.lower()=="c":
        output_file="file.pdf"
        input_file="mpp.pdf"  
        compress_pdf(output_file,input_file) 
      if option.lower()=="s":
          convert_image_to_pdf('OIP.jpg')
      if option.lower()=='m':
        outfile="merge.pdf" 
        files=['OIP.pdf','mpp.pdf']
       # pdf_files= get_all_pdf_files_as_list(files) 
        print(files) 
        merge_pdf_files(outfile,files) 
        print('done')
           
      if option.lower()=="q": 
       print("Goodbye") 
       running=False 
       exit() 

def compress_pdf(output_file, file_to_compress): 
    script="gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -sNAME=setting -sOutputFile={} {}".format(output_file,file_to_compress)
    command = script.split(" ")
    print("This is the command that i will run{} ".format(command)) 
    subprocess.run(command) 
    
    src_file_size=os.path.getsize(file_to_compress) 
    out_file_size=os.path.getsize(output_file)
    print('!Done{}to{}'.format(src_file_size,out_file_size)) 

def convert_image_to_pdf(image_path:str):
     print('convert an image to pdf')
     with Image.open(image_path) as im:
          
       f,e=os.path.splitext(image_path)
       file_name="{}.pdf".format(f) 
       im.convert('RGB')
       im.save(file_name) 
       print('done')

def merge_pdf_files(output_file:str,files_to_merge: list): 
   files=" ".join(files_to_merge)
   print("the files to be merged{}".format(files))
   script="gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -dAutoRotatePages=/None -sOutputFile={} {}".format(output_file,files) 
   print("The script that I am going to run is: {}".format(script)) 
   command= script.split(" ") 
   print("The script that I am going to run is: {}".format(script)) 
   print(command) 
   print(script)
   subprocess.run("{}".format(command)) 
   return output_file

 

main() 
       
         




    
    
           

          
