 def fileOpenBox():
           nameOfFile = filedialog.askopenfilename(initialdir = "C:\\",title = "Select file",filetypes = ((".mp4","*.mp4"),("all files","*.*")))
      
 pickFile = tkinter.Button(w,text="Pick your video file", width=14, command=fileOpenBox).grid(row=4,column=2)