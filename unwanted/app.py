import datetime
import time 
import webbrowser 
def search():
    print("Choose what you want to do? ")
    print("1. Open You Tube")
    print("2. Open Gmail")
    print("3. Open Chat GPT")
    print("4. Google Home Page ")
    ch=input("enter your choice")
    if ch=='1': 
        query=input("Enter the topic your want to see in youtube")
        webbrowser.open(f"https://www.youtube.com/search?q={query}")

    if ch=='2':
        webbrowser.open(f"https://www.gmail.com")
    
    if ch=='3':
        query=input("enter the content for chat gpt")
        webbrowser.open(f"https://www/chatgpt.com/?q={query}")
    
    if ch=='4':
        query=input("What you want to search in google")
        webbrowser.open(f"https://www/google.com/search?q={query}")
    else: 
        print("Invladi Choice")
        
    
r
search() 
