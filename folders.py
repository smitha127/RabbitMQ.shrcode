import os



#def createfolder():

#change directory
os.chdir('C:\\Users\\1023528\\Desktop\\OpenFolder')

#print current working directory
print(os.getcwd())

#create directory
os.mkdir("data1")
print(os.listdir(os.getcwd()))

os.rename("data1","SCU")
print(os.listdir(os.getcwd()))

print(os.getcwd())

os.mkdir("ENGINE")
print(os.listdir(os.getcwd()))

os.mkdir("PartNumber")
print(os.listdir(os.getcwd()))

os.mkdir("Concession")
subfolder_names = ['Input','WIP','TecnicalReview','Deliverables']
for subfolder_name in subfolder_names:
    os.makedirs(os.path.join('Concession', subfolder_name))
    print(os.listdir(os.getcwd()))
