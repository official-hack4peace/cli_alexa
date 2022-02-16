print("           ____")
print("          (____)  <[Hello!]"
print("          |    |")
print("          |____|")

import webbrowser
name = input("Enter your name please: ")
print ("Hello! it's Alexa How can I help you?")
reply = input("Enter: ")
if reply==("Alexa open instagram"): 
	print(webbrowser.open("https://www.instagram.com")) 
if reply==("Alexa open twitter"):
	print(webbrowser.open("https://mobile.twitter.com/?lang=en"))
if reply==("Alexa open google"):
	print(webbrowser.open("https://www.google.com"))
if reply==("Alexa open youtube"):
	print(webbrowser.open("https://www.youtube.com"))
if reply==("Alexa open whatsapp"):
	print(webbrowser.open("https://www.whatsapp.com"))

# asking quetions with Alexa
if reply==("Alexa how are you?"):
	print("Fine!")
if reply==("Alexa what things you can do?"):
	print("Lot's of things for example you can say like this 'Alexa open youtube' or something else.")
if reply==("Alexa what is your age?")
# reply from alexa
if reply==("Alexa hello"):
	print("Hello", name, "\U0001F917")
if reply==("Alexa hi"):
	print("hi", name, "\U0001F917")
if reply==("Alexa good morning"):
	print("good morning", name, "\U0001F917")
if reply==("Alexa good afternoon"):
	print("good afternoon", name)
if reply==("Alexa good night"):
	print("good night", name, "\U0001F62A")
if reply==("Alexa today is my birthday"):
	print("happy birthday", name)
if reply==("Alexa i love you"):
        print("Sorry I am program")
