import csv


# all the lists for the  app
tittle =[]
html =[]
css =[]
javascript =[]

# plening for all a the data tis is very ineficent fix later
with open('tittle.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        for x in row:
            tittle.append(x)
        
        
with open('html.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        for x in row:
            html.append(x)
            
with open('css.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        for x in row:
            css.append(x)
        
with open('javascript.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        for x in row:
            javascript.append(x)
            
# the function on entering the values
# int the oder tittle,html,css,javscript
def enter():
    askvariable =input("tittle>> ")
    tittle.append(askvariable.upper())
    askvariable =input("html>> ")
    html.append(askvariable)
    askvariable =input("css>> ")
    css.append(askvariable)
    askvariable =input("javascript>> ")
    javascript.append(askvariable)

# function to view everythng in this format:
# TITTLE
# html
# css
# javascript
def showlist():
     for x in range (len(tittle)):
        print(tittle[x])
        print(html[x])
        print(css[x])
        print(javascript[x])



while 1==1:
    option = input("add 1 view 2 quit 3: ")
    if option == "1":
        enter()
    elif option == "2":
        showlist()
    elif option == "3":
#         save all the data in csv files
        with open('tittle.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for item in tittle:
                writer.writerow([item])
        with open('html.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for item in html:
                writer.writerow([item])
        with open('css.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for item in css:
                writer.writerow([item])
        with open('javascript.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for item in javascript:
                writer.writerow([item])
        break
