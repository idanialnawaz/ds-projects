import tkinter
from tkinter import *  # import all the library of the tkinter module
from tkinter import messagebox, filedialog
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs  # importing BeautifulSoup
import instaloader
from linkedin_api import Linkedin
import pandas as pd
import snscrape.modules.twitter as sntwitter
from facebook_scraper import *


def facebook_interface():
    # facebook_photo = PhotoImage(file='facebook.png')
    profile_username = StringVar()
    Facebook_Profile = Entry(container_window,
                             font=("Agency FB", 15),
                             width=35,
                             textvariable=profile_username,
                             )
    Facebook_Profile.insert(0, 'Enter Profile username here')
    Facebook_Profile.place(x=220, y=120)

    # Facebook's data scraping function
    def Facebook():
        print(profile_username.get())
        list = str([get_profile(f"{profile_username.get()}")]).split(",")
        for elements in list:
            print(elements)

    download_button = Button(container_window,
                             command=Facebook,
                             font=('Agency FB', 20, 'bold'),
                             background='#3b5998',
                             text='Download',
                             foreground='white',
                             state=ACTIVE,
                             width=15,

                             )
    download_button.place(x=250, y=280)

    def clear():
        Facebook_Profile.delete(0, END)

    facebook_label = Label(container_window,
                           text="facebook.com",  # text for label
                           font=('Agency FB', 20, 'bold'),  # styling the font

                           fg="#3b5998",  # foreground color for label
                           width=20,
                           bg="white",  # background color for label
                           relief=RAISED,  # border type for the label
                           bd=10,  # border thickness for the label
                           # image=facebook_photo,
                           # compound='left'
                           )

    facebook_label.place(x=200, y=40)  # placement of label inside the container window

    VideoLink_label = Label(container_window,
                            text="Profile Name",  # text for label
                            fg="#3b5998",  # foreground color for label
                            font=('Agency FB', 15, 'bold'),  # styling the font
                            bg="white",  # background color for label
                            width=15,
                            relief=RAISED,  # border type for the label

                            # compound='left'
                            )
    VideoLink_label.place(x=80, y=120)

    def display():
        if x.get() == 1:
            print("you agree")
        else:
            print("you don't agree")

    x = IntVar()

    check_button = Checkbutton(container_window, text='''Agree to 'terms and conditions' ''',
                               variable=x,
                               onvalue='1',
                               offvalue='0',
                               command=display,
                               font=('Agency FB', 10, 'bold'),
                               fg='black',
                               bg='#3b5998',
                               activebackground='#3b5998',
                               activeforeground='black',
                               pady=10,
                               padx=5,
                               image=photo2,
                               compound=LEFT,

                               )
    check_button.place(x=250, y=220)


def Instagram_interface():
    container_window.config(background="#3f729b")  # sets the background color
    # insta_photo = PhotoImage(file='instagram.png')
    username = StringVar()
    insta_user = Entry(container_window,
                       font=("Agency FB", 15),
                       width=35,
                       textvariable=username
                       )
    insta_user.insert(0, 'Enter username here')
    insta_user.place(x=220, y=120)

    # Instagram data scraping function
    def Instagram():
        print(username.get())
        # Creating an instance of the Instaloader class
        bot = instaloader.Instaloader()

        # Loading a profile from an Instagram handle
        profile = instaloader.Profile.from_username(bot.context, username.get())
        # file = open("Output.txt", "w")
        output = f"is verified: {str(profile.is_verified)}\nName: {str(profile.full_name)}\nBiography: {str(profile.biography)}\nprofile picture: {str(profile.get_profile_pic_url())}\n Username: {str(profile.username)}\nUser ID:{str(profile.userid)}\nNumber of Posts: {str(profile.mediacount)}\nFollowers Count: {str(profile.followers)}\nFollowing Count: {str(profile.followees)}\nExternal URL: {str(profile.external_url)}"
        print(output)
    download_button = Button(container_window,
                             command=Instagram,
                             font=('Agency FB', 20, 'bold'),
                             background='#3f729b',
                             text='Download',
                             foreground='white',
                             state=ACTIVE,
                             width=15
                             )
    download_button.place(x=250, y=280)

    def clear():
        insta_user.delete(0, END)

    insta_label = Label(container_window,
                        text="Instagram.com",  # text for label
                        font=('Agency FB', 20, 'bold'),  # styling the font
                        fg="#3f729b",  # foreground color for label
                        width=20,
                        bg="white",  # background color for label
                        relief=RAISED,  # border type for the label
                        bd=10,  # border thickness for the label
                        # image=insta_photo,
                        # compound='left'
                        )

    insta_label.place(x=200, y=40)  # placement of label inside the container window

    VideoLink_label = Label(container_window,
                            text="Username",  # text for label
                            font=('Agency FB', 15, 'bold'),  # styling the font
                            fg="#3f729b",  # foreground color for label
                            bg="white",  # background color for label
                            width=15,
                            relief=RAISED
                            )
    VideoLink_label.place(x=80, y=120)

    def display():
        if x.get() == 1:
            print("you agree")
        else:
            print("you don't agree")

    x = IntVar()

    check_button = Checkbutton(container_window, text='''Agree to 'terms and conditions' ''',
                               variable=x,
                               onvalue='1',
                               offvalue='0',
                               command=display,
                               font=('Agency FB', 10, 'bold'),
                               fg='black',
                               bg='#3f729b',
                               activebackground='#3f729b',
                               activeforeground='black',
                               pady=10,
                               relief=RAISED,
                               padx=5,
                               image=photo2,
                               compound=LEFT,

                               )
    check_button.place(x=250, y=220)


def Youtube_interface():
    container_window.config(background="red")  # sets the background color

    video_link = StringVar()

    youtube_link = Entry(container_window,
                         font=('Agency FB', 15),
                         width=35,
                         textvariable=video_link,
                         )
    youtube_link.insert(0, "Enter link here")
    youtube_link.place(x=220, y=120)

    # YouTube's data scraping function
    def Youtube():
        print(video_link.get())
        # copy YouTube url from YouTube website
        # init an HTML Session
        session = HTMLSession()
        # get the html content
        response = session.get(f"{video_link.get()}")
        # execute Java-script, timeout is necessary pass otherwise it will through error
        response.html.render(timeout=20)
        # create bs object to parse HTML
        soup = bs(response.html.html, "html.parser")

        output = f"{str(soup.find_all('meta'))}\nTitle of the Video:{str(soup.find('meta', itemprop='name')['content'])}" \
                 f"\nViews on the Video: {str(soup.find('meta', itemprop='interactionCount')['content'])} "

        print(output)

    download_button = Button(container_window,
                             command=Youtube,
                             background='#c4302b',
                             font=("Agency FB", 20, "bold"),
                             text='Download',
                             foreground='white',
                             state=ACTIVE,
                             width=15,
                             )
    download_button.place(x=250, y=280)

    youtube_label = Label(container_window,
                          text="Youtube.com",  # text for label
                          font=('Agency FB', 20, 'bold'),  # styling the font
                          fg="red",  # foreground color for label
                          width=20,
                          bg="white",  # background color for label
                          relief=RAISED,  # border type for the label
                          bd=10,  # border thickness for the label
                          )

    youtube_label.place(x=200, y=40)  # placement of label inside the container window

    def clear():
        youtube_link.delete(0, END)

    VideoLink_label = Label(container_window,
                            text="Video Link",  # text for label
                            font=('Agency FB', 15, 'bold'),  # styling the font
                            fg="#c4302b",  # foreground color for label
                            # font=('Agency FB', 15, 'bold'),  # styling the font
                            bg="white",  # background color for label
                            width=15,
                            relief=RAISED,

                            # compound='left'
                            )
    VideoLink_label.place(x=80, y=120)

    def display():
        if x.get() == 1:
            print("you agree")
        else:
            print("you don't agree")

    x = IntVar()

    check_button = Checkbutton(container_window, text='''Agree to 'terms and conditions' ''',
                               variable=x,
                               onvalue='1',
                               offvalue='0',
                               command=display,
                               font=('Agency FB', 10, 'bold'),
                               fg='black',
                               bg='#c4302b',
                               activebackground='red',
                               activeforeground='black',
                               pady=10,
                               padx=5,
                               image=photo2,
                               compound=LEFT,

                               )
    check_button.place(x=250, y=220)


def Twitter_interface():
    # this is a web-scraper
    container_window.config(background="#00acee")  # sets the background color
    query = StringVar()
    twitter_query = Entry(container_window,
                          font=('Agency FB', 15),
                          width=35,
                          textvariable=query
                          )
    twitter_query.insert(0, 'Insert your query here')
    twitter_query.place(x=220, y=120)

    # twitter data scraping function
    def Twitter():
        print(query.get())

        tweets = []
        limit = 100

        for tweet in sntwitter.TwitterSearchScraper(query.get()).get_items():
            vars(tweet)
            if len(tweets) == limit:
                break
            else:
                tweets.append([tweet.date, tweet.user.username, tweet.content])

        df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])

        print(df)


    download_button = Button(container_window,
                             text='Download',
                             command=Twitter,
                             font=('Agency FB', 20, 'bold'),
                             background='#00acee',
                             foreground='white',
                             state=ACTIVE,
                             width=15,

                             )
    download_button.place(x=250, y=280)

    def clear():
        twitter_query.delete(0, END)

    twitter_label = Label(container_window,
                          text="Twitter.com",  # text for label
                          font=('Agency FB', 20, 'bold'),  # styling the font
                          fg="#00acee",  # foreground color for label
                          width=20,
                          bg="white",  # background color for label
                          relief=RAISED,  # border type for the label
                          bd=10,  # border thickness for the label
                          # image=twitter_photo,
                          # compound='left'
                          )

    twitter_label.place(x=200, y=40)  # placement of label inside the container window

    Query_label = Label(container_window,
                        text="Query",  # text for label
                        # font=('Agency FB', 20, 'bold'),  # styling the font
                        fg="#00acee",  # foreground color for label
                        font=('Agency FB', 15, 'bold'),  # styling the font
                        bg="white",  # background color for label
                        width=15,
                        relief=RAISED,  # border type for the label
                        )
    Query_label.place(x=80, y=120)

    def display():
        if x.get() == 1:
            print("you agree")
        else:
            print("you don't agree")

    x = IntVar()

    check_button = Checkbutton(container_window, text='''Agree to 'terms and conditions' ''',
                               variable=x,
                               onvalue='1',
                               offvalue='0',
                               command=display,
                               font=('Agency FB', 10, 'bold'),
                               fg='black',
                               bg='#00acee',
                               activebackground='#00acee',
                               activeforeground='black',
                               pady=10,
                               padx=5,
                               image=photo2,
                               compound=LEFT,

                               )
    check_button.place(x=250, y=220)


def linkedin_interface():
    container_window.config(background="#0072b1")  # sets the background color

    # linkedin_photo = PhotoImage(file='linkedin.png')
    useremail = StringVar()
    useremail = Entry(container_window,
                      font=('Agency FB', 15),
                      width=35,
                      textvariable=useremail,
                      )
    useremail.insert(0, 'Enter user email to login')
    useremail.place(x=220, y=120)

    password = StringVar()

    password_entry = Entry(container_window,
                           font=('Agency FB', 15),
                           width=35,
                           textvariable=password,
                           show="*"
                           )
    # password_entry.insert(0, 'Enter password')
    password_entry.place(x=200, y=170)

    # linkedin data scraping function
    def LinkedIn():
        print(useremail.get(), "\n", print(password.get()))
        # file = open("Linkedin.txt", "w")
        api = Linkedin(useremail.get(), password.get())
        decision = input(
            f"(A) Get profile from username\n(B) Search for School\n(C) Search for People \n(D) Search for Company\n")
        print(f"Your decision is {str(decision)}\n")
        if decision == 'A' or decision == 'a':
            username = input("Enter the username you want to get: ")

            print(api.get_profile(username))
        elif decision == 'B' or decision == 'b':
            school = input("Enter the school: ")
            print(api.get_school(school))
        elif decision == 'C' or decision == 'c':
            people = input("Enter the people: ")
            print(api.search_people(people))
        elif decision == 'D' or decision == 'd':
            company = input("Enter the company: ")
            print(api.get_company(company))

    submit_button = Button(container_window, text="Submit", font=('Agency FB', 20, 'bold'),
                           background='#0072b1',
                           foreground='white',
                           state=ACTIVE,
                           )
    submit_button.place(x=250, y=280)

    download_button = Button(container_window,
                             text='Download',
                             command=LinkedIn,
                             font=('Agency FB', 20, 'bold'),
                             background='#0072b1',
                             foreground='white',
                             state=ACTIVE,
                             width=15,

                             )
    download_button.place(x=250, y=280)

    linkedin_label = Label(container_window,
                           text="LinkedIn.com",  # text for label
                           font=('Agency FB', 20, 'bold'),  # styling the font
                           fg="#0072b1",  # foreground color for label
                           width=20,
                           bg="white",  # background color for label
                           relief=RAISED,  # border type for the label
                           bd=10,  # border thickness for the label
                           )

    linkedin_label.place(x=200, y=40)  # placement of label inside the container window

    password_label = Label(container_window,
                           text="Password",  # text for label
                           # font=('Agency FB', 20, 'bold'),  # styling the font
                           fg="#0072b1",  # foreground color for label
                           font=('Agency FB', 15, 'bold'),  # styling the font
                           bg="white",  # background color for label
                           width=15,
                           relief=RAISED,
                           )
    password_label.place(x=80, y=170)

    username_label = Label(container_window,
                           text="Usermail",  # text for label
                           # font=('Agency FB', 20, 'bold'),  # styling the font
                           fg="#0072b1",  # foreground color for label
                           font=('Agency FB', 15, 'bold'),  # styling the font
                           bg="white",  # background color for label
                           width=15,
                           relief=RAISED,

                           # compound='left'
                           )
    username_label.place(x=80, y=120)

    def display():
        if x.get() == 1:
            print("you agree")
        else:
            print("you don't agree")

    x = IntVar()

    check_button = Checkbutton(container_window, text='''Agree to 'terms and conditions' ''',
                               variable=x,
                               onvalue='1',
                               offvalue='0',
                               command=display,
                               font=('Agency FB', 10, 'bold'),
                               fg='black',
                               bg='#0072b1',
                               activebackground='red',
                               activeforeground='black',
                               pady=10,
                               padx=5,
                               image=photo2,
                               compound=LEFT,

                               )
    check_button.place(x=250, y=220)


container_window = tkinter.Tk()  # creates an instance of the window
container_window.geometry("720x350")  # sets the resolution (WxH)
container_window.title("Social Media Data Extracter")  # adds the title of window
container_window.config(background="#3b5998")  # sets the background color

photo1 = PhotoImage(file='neww.png')
photo2 = PhotoImage(file='img.png')

Facebook_button = Button(text='Facebook', font=('Agency FB', 10, 'bold'),
                         command=facebook_interface)
Facebook_button.place(x=0, y=0)
Instagram_button = Button(text='Instagram', font=('Agency FB', 10, 'bold'),
                          command=Instagram_interface)
Instagram_button.place(x=55, y=0)
Youtube_button = Button(text='Youtube', font=('Agency FB', 10, 'bold'), command=Youtube_interface)
Youtube_button.place(x=115, y=0)
Twitter_button = Button(text='Twitter', font=('Agency FB', 10, 'bold'), command=Twitter_interface)
Twitter_button.place(x=165, y=0)
Linkedin_button = Button(text='LinkedIn', font=('Agency FB', 10, 'bold'),
                         command=linkedin_interface)
Linkedin_button.place(x=210, y=0)

container_window.mainloop()
