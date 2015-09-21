from Tkinter import *
import sys
commands = []

#open the input file for reading
inputFile = open("searches.txt", "r")
allSearches = inputFile.readlines()

for search in allSearches:
	commands.append(search.strip())

    
inputFile.close()

#define the actual function to correct the word
def closest(u):
	return min(commands, key=lambda v: len(set(u) ^ set(v)))
#define the autocorrect function to use the closest function to get the closest word in commands
def autocorrect(word):
	similar = closest(word)
	return similar
#function that completes the word, with the word displayed in the autoCorrectBox 
def correction():
	textBoxValue = str(textCap.get())
	textBox.delete(0, END)
	
	correctWord = autocorrect(textBoxValue)
	textBox.insert(INSERT, str(correctWord))
def completion(event):
	textBoxValue = str(textCap.get())
	textBox.delete(0, END)
	
	correctWord = autocorrect(textBoxValue)
	textBox.insert(INSERT, str(correctWord))
#the function which acts upon a keypress that utilizes the autocorrect function
def onKeyPress(event):
	autoCorrectBox.delete(0.0, END)
	currentValueInTextBox = str(textCap.get())
	
	autoCorrectValue = autocorrect(currentValueInTextBox)
	autoCorrectBox.insert(INSERT, str(autoCorrectValue))
#a function to write new values out to the searches file
def searchButton():
	valueInTextBox = str(textCap.get())
	if valueInTextBox in commands:
		global errorLabel
		errorLabel = Label(root, text='Already know it')
		errorLabel.config(bg='light green')
		errorLabel.grid(row=5, column=4)
	else:
		outFile = open("searches.txt", "a")
		outFile.write("\n" + valueInTextBox)
		outFile.close()
	#initialize the GUI window
if __name__ == "__main__":
	root = Tk()
	root.geometry("400x300+100+150")	
	root.title("Auto-complete")
	#pack(fill=BOTH, expand=1)
	root.config(bg='light blue')
	root.bind("<KeyPress>", onKeyPress)
	root.bind("<space>", completion)
	
	textCap = StringVar()
	firstLabel = Label(root, text='Enter a word to search:')
	firstLabel.config(bg='white')
	textBox = Entry(root, textvariable=textCap)
	textBox.grid(row=0,column=3)
	autoCorrectBox = Text(root, width=20, height=1)
	autoCorrectBox.place(x=120, y=50)
	correctLabel = Label(root, text='Did you mean?: ')
	correctLabel.place(x=5, y=50)
	correctLabel.config(bg='white')
	firstLabel.grid(row=0,column=0)
	
	sButton = Button(root, text='Search', command=searchButton)
	sButton.place(x=50, y=23)
	qButton = Button(root, text='Quit', command=root.quit)
	qButton.place(x=215, y=23)
	aButton = Button(root, text='Auto-Complete', command=correction)
	aButton.place(x=120, y=23)


	root.mainloop()