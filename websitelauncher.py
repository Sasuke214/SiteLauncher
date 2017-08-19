import webbrowser
from tkinter import *
import os

class WebSiteLauncher:
         def __init__(self):
                  #initialize the sourceFile to the file containing urls
                  #if no list file is there create 1 giving default techsanjal.com
                  self.EntryVariable=StringVar()
                  self.InputUrlStore=[]
                  try:
                           sourceFile=open("input.txt","r+")                                   
                  except:
                           
                           sourceFile=open("input.txt",mode='w+')
                           sourceFile.write("www.techsanjal.com\n")
                           sourceFile.close()
                  
                  #Creating Frame for 3 different windows
                  self.Frame1=Frame(root)
                  self.Frame2=Frame(root)
                  self.Frame3=Frame(root)

                  self.SetMainGui()

                  
         #setting GUI for main window
         def SetMainGui(self):
                  try:
                           self.Frame2.destroy()
                  except:
                           print("")
                  try:
                           self.Frame3.destroy()
                  except:
                           print("")
                           
                  self.Frame1=Frame(root)
                  self.Frame1.grid()
                  
                  self.StartBtn=Button(self.Frame1,text="Launch",command=self.StartLaunch)
                  self.UrlInputBtn=Button(self.Frame1,text="InputUrl",command=self.SetInputGui)
                  self.DeleteUrlBtn=Button(self.Frame1,text="DeleteUrl",command=self.SetDeleteGui)
                  self.StartBtn.grid(row=0)
                  self.UrlInputBtn.grid(row=1)
                  self.DeleteUrlBtn.grid(row=2)

         ##InputStart
         #Setting GUI for input             
         def SetInputGui(self):
                  self.Frame1.destroy()
                  self.Frame2=Frame(root)
                  self.Frame2.grid()
                  
                  self.label=Label(self.Frame2,text="Enter your FileName:")
                  self.inputBox=Entry(self.Frame2,textvariable=self.EntryVariable)
                  self.nextbtn=Button(self.Frame2,text="Next",command=self.UrlInput)
                  self.MainMenu=Button(self.Frame2,text="MainMenu",command=self.LoadUrl)
                  self.label.grid()
                  self.inputBox.grid(row=1)
                  self.nextbtn.grid(row=2)
                  self.MainMenu.grid(row=3)
                  
         #Gettin url in entry box
         def UrlInput(self):
                  
                  inputUrl=str(self.inputBox.get())
                  self.EntryVariable.set("")
                  #checking if the given url is empty
                  if inputUrl=="":
                           #messagebox.showerror("Error","Please Assign the url")
                           return
                  #if not empty adding it to list
                  self.InputUrlStore.append(inputUrl)
                  
         #Loading url in database
         def LoadUrl(self):
                  self.UrlInput()
                  self.GetUrlList()
                  with open('input.txt','a+') as sourceFile:
                           counter=0
                           for s in self.InputUrlStore:
                                    counter+=1
                                    if not s in self.UrlList:
                                             if(counter==len(self.InputUrlStore)):
                                                      sourceFile.write(s)
                                             else:
                                                      sourceFile.write(s+'\n')
                  self.SetMainGui()
                  
         ##InputEnd
                  


         ##LaunchStart 
         #launch the url got as siteUrl argument         
         def Launch(self,siteUrl):    
                  webbrowser.open(siteUrl)
                  
         #Extracts all urls from url input file
         def GetUrlList(self):
                  with open('input.txt') as sourceFile:
                           self.UrlList=sourceFile.read().split('\n')
                  
         #start the siteLaunch
         def StartLaunch(self):
                  self.GetUrlList()
                  for s in self.UrlList:
                           if(str(s)!=""):
                                    self.Launch(str(s))
                  #To Exit The File 
                  root.destroy()
         ##LaunchEnd

         ##DeleteStart

         #delete completely
         def DeleteFile(self,urlindex,url):
                  self.listbox.delete(urlindex)
                  #getting the current item in file
                  self.GetUrlList()
                  #deleting content from  file
                  with open("input.txt","w+") as newfile:
                           counter=0
                           for s in self.UrlList:
                                    counter+=1
                                    if not s==url:
                                             if counter==len(self.UrlList): 
                                                      newfile.write(s)
                                             else:
                                                     newfile.write(s+'\n') 
                  
         #to choose whether to launch that or delete
         def ChooseByClick(self,clickedEvent):
                  #getting widget which send this event
                  try:
                           w=clickedEvent.widget
                           index=int(w.curselection()[0])
                           #getting link from listbox
                           urllink=w.get(index)
                           self.Launch(urllink)
                           self.DeleteFile(index,urllink)
                  except:
                           return

                  
                  
                  
         #setting GUI for delete
         def SetDeleteGui(self):
                  self.Frame1.destroy()
                  self.Frame3=Frame(root)
                  self.Frame3.pack()
                  
                  

                  self.MainMenu=Button(self.Frame3,text="MainMenu",command=self.SetMainGui)
                  
                  ##List to list all available links
                  self.GetUrlList()

                  ##list and scrollbar
                  self.lasFrame=Frame(self.Frame3)
                  self.lasFrame.pack()
                  ##
                  scrlbarV=Scrollbar(self.Frame3,orient=VERTICAL)
                  scrlbarH=Scrollbar(self.Frame3,orient=HORIZONTAL)

                  scrlbarV.pack(side=RIGHT,fill=Y)
                  scrlbarH.pack(side=BOTTOM,fill=X)

                  self.listbox=Listbox(self.Frame3,yscrollcommand=scrlbarV.set,xscrollcommand=scrlbarH.set)
                  self.listbox.pack(expand=YES,fill=BOTH)
                  #call the function choosebyclick when clicked in listbox
                  self.listbox.bind('<<ListboxSelect>>', self.ChooseByClick)
                  for i in range(0,len(self.UrlList)):
                           if self.UrlList[i]!="":
                                    self.listbox.insert(i,self.UrlList[i])
                  scrlbarV.config(command=self.listbox.yview)
                  scrlbarH.config(command=self.listbox.xview)
                  ##
                  self.MainMenu.pack()
                  
         ##DeleteEnd
         
root=Tk()
wlauncher=WebSiteLauncher()
root.mainloop()
