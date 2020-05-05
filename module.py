from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import random
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Bot() :

    def __init__(self,username,password) :

        options = webdriver.ChromeOptions()
        options.add_argument("--lang=en")
        options.add_argument("user-data-dir=C:/Users/yuszi/AppData/Local/Google/Chrome/User Data/Default")
        self.chrome = webdriver.Chrome(chrome_options=options)
        self.action = webdriver.ActionChains(self.chrome)
        self.chrome.get("https://instagram.com/accounts/login")

        self.username = username
        self.password = password

        self.print = "[InstagramPy]:"

        self.chrome.maximize_window()

        print("\n")

    def login(self) :
        searchInput = self.chrome.find_elements_by_css_selector("input[placeholder='Search']")
        if  (bool(searchInput) == False) :
            self.chrome.implicitly_wait(5)
            sleep(1)

            usernameInput = self.chrome.find_elements_by_name("username")[0]
            passwordInput = self.chrome.find_elements_by_name("password")[0]
            login = self.chrome.find_elements_by_css_selector("button[type='submit']")[0]

            sleep(2)

            usernameInput.send_keys(self.username)
            passwordInput.send_keys(self.password)

            login.click()

            sleep(1)
            self.closenotf()
            print("Hello Adamım")

    def closenotf(self) :

        buton = self.chrome.find_elements_by_css_selector(".HoLwm")
        if buton :
            self.chrome.implicitly_wait(5)
            sleep(1)
            buton[0].click()

    def follow_user(self,*args) :
        for arg in args :
            sleep(1)

            link = arg
            self.find_user(link)

            sleep(1)

            buton = self.chrome.find_elements_by_css_selector("button._5f5mN")[0]
            buton.click()


            sleep(3)
        self.chrome.get("https://www.instagram.com")

    def unfollow_user(self,*args) :
        for arg in args :
            sleep(1)

            link = arg
            self.find_user(link)

            sleep(1)
            buton = self.chrome.find_elements_by_css_selector("button.-fzfL")
            if (buton) :
                buton = buton[0]
                buton.click()
                verifyButton = self.chrome.find_elements_by_css_selector("button.aOOlW")[0]
                verifyButton.click()
                sleep(3)

        self.chrome.get("https://www.instagram.com")

    def like(self) :
        likebtn = self.chrome.find_element_by_css_selector(".fr66n")
        if likebtn != "null" :
            likebtn.click()

    def save_to_archive(self,post) :
        sleep(1)
        if self.chrome.find_element_by_css_selector(".wpO6b > svg[aria-label='Save']") :
            self.chrome.find_element_by_css_selector(".wpO6b").click()
            sleep(1)

    def like_by_user(self,*args) :

        for arg in args :

            sleep(1)
            self.find_user(arg)

            linkList = []

            sleep(1)

            postNumber = self.chrome.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[1]/span/span").get_attribute("innerHTML")
            while True :
                parent = self.chrome.find_elements_by_css_selector(".Nnq7C")[i]
                if (len(linkList) >= postNumber) :
                    print(self.print,"All Links were Pulled")
                    break
                for z in range(3) :
                    linkElem = parent.find_elements_by_css_selector(".v1Nh3 > a")[z]
                    link = linkElem.get_attribute("href")
                    if linkList.count(link) == 0 :
                        linkList.append(link)
                    else :
                        i+=1
                        break
                self.chrome.execute_script("window.scrollTo(0,window.pageYOffset+321)")

                sleep(1)

            sleep(1)

            for post in linkList :
                self.chrome.get(post)
                sleep(3)
                self.like()
                sleep(1)

    def find_user(self,isim) :

        sleep(1)

        input = self.chrome.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
        input.send_keys(isim)
        sleep(1)

        box = self.chrome.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[not(contains(@href,"/explore"))]')
        box.click()

    def find_tag(self,tag) :

        sleep(1)

        input = self.chrome.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
        input.send_keys(tag)
        sleep(1)

        box = self.chrome.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[contains(@href,"/explore/tags")]')
        box.click()

    def find_location(self,location) :

        sleep(1)

        input = self.chrome.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
        input.send_keys(location)
        sleep(1)

        box = self.chrome.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[contains(@href,"/explore/locations")]')
        box.click()

    def like_by_tag(self,amount,*args) :
        for arg in args :

            self.find_tag(arg)
            sleep(1)
            self.chrome.execute_script("window.scrollTo(0,0)")
            clickedImageCount=0
            sleep(1)

            while (int(amount)*100) > self.chrome.execute_script("return document.body.scrollHeight") :
                self.chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            self.chrome.execute_script("window.scrollTo(0,0)")

            sleep(1)

            parent = self.chrome.find_elements_by_css_selector("div.Nnq7C")
            satırS = len(parent)
            for i in range(satırS) :
                satır = parent[i]
                images = satır.find_elements_by_css_selector(".v1Nh3")
                imageSayi = len(images)
                for z in range(imageSayi) :
                    if (clickedImageCount > int(amount) or clickedImageCount == int(amount)) :
                        break
                    image = images[z]   
                    image.click()
                    clickedImageCount+=1
                    
                    sleep(2)
                    closebtn = self.chrome.find_element_by_xpath("/html/body/div[4]/div[3]")
                    closebtn.click()
                    sleep(1)
    
    def get_followers(self,hesap,yer) :

        if os.path.exists(yer) :
            os.remove(yer)

        self.find_user(hesap)
        sleep(1)

        takipci = self.chrome.find_elements_by_css_selector(".g47SY")[1]
        takipciSayisi = takipci.get_attribute("title")
        followerCount = int(str(takipciSayisi).replace(",",""))
        
        sleep(1)
        takipci.click()

        sleep(1)
        #box = self.chrome.find_elements_by_css_selector(".isgrP")
        self.chrome.execute_script("elem = document.getElementsByClassName('isgrP')[0]")
        while (followerCount*40) + 100 > int(self.chrome.execute_script("return elem.scrollHeight")) :
            sleep(1)
            self.chrome.execute_script("elem.scrollTo(0,elem.scrollHeight)")
        sleep(1)
        self.chrome.execute_script("elem.scrollTo(0,0)")

        followerBox = self.chrome.find_elements_by_css_selector(".d7ByH > .FPmhX")
        followerDescriptionBox = self.chrome.find_elements_by_css_selector(".wFPL8")
        len(followerDescriptionBox)
        self.chrome.implicitly_wait(15)
        f = open(yer,"w+",encoding="utf-8")
        number = len(followerBox)
        lineCount = 0
        for i in range(number) :
            follower = followerBox[i]
            followerDes = followerDescriptionBox[i]
            followerName = follower.get_attribute("innerHTML")
            followerLink = follower.get_attribute("href")
            followerDescription = followerDes.get_attribute("innerHTML")
            if followerDescription == "" :
                followerDescription = self.print + " Empty"
            self.chrome.implicitly_wait(3)
            f.write("\nFollower Name: " + followerName)
            f.write("\nFollower Description: " + followerDescription)
            f.write("\nFollower Link: " + followerLink)
            f.write("\n")
            lineCount+=1


        f.write("\n" + self.print + " Follower Count : "+str(followerCount))
        f.write("\n" + self.print +" Follower Name Pulled : "+str(lineCount))

        f.close()

        closebtn = self.chrome.find_elements_by_css_selector("body > div.RnEpo.Yx5HN > div > div:nth-child(1) > div > div:nth-child(3) > button")[0]
        self.chrome.implicitly_wait(5)
        self.chrome.implicitly_wait(2)
        sleep(1)
        closebtn.click()

        sleep(3)

        self.chrome.get("https://www.instagram.com")
    
    def read_stories(self) :
        
        sleep(1)

        firstStory = self.chrome.find_elements_by_css_selector("button.jZyv1")[0]
        self.chrome.implicitly_wait(5)
        firstStory.click()

        sleep(1)

        while True :
            sleep(1)
            next = self.chrome.find_elements_by_css_selector(".coreSpriteRightChevron")
            if (next) :
                next[0].click()
                print(self.print,"Next Story")
            else :
                print(self.print,"All Stories was readed")
                break

        self.chrome.get("https://www.instagram.com")

    def comment(self,*args) :
        
        if self.chrome.find_elements_by_css_selector("textarea.Ypffh") :
            comment = random.choice(args)[0]
            #Selecting 2 times is working
            commentArea = self.chrome.find_element_by_class_name('Ypffh')
            commentArea.click()
            commentArea = self.chrome.find_element_by_class_name('Ypffh')
            commentArea.send_keys(comment)

            sleep(1)

            btnelement = self.chrome.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[3]/div/form/button')
            self.chrome.implicitly_wait(5)
            btnelement.click()

            sleep(1)

    def users_all_posts(self,users,**seçimler) :

        amount = seçimler.get("amount")
        comment = seçimler.get("comment")
        like = seçimler.get("like")
        commentOptions = seçimler.get("comment_options")
        save = seçimler.get("save")

        for user in users :

            linkList = []
            sleep(1)

            self.find_user(user)
            sleep(2)

            postCount = int(str(self.chrome.find_elements_by_css_selector(".g47SY")[0].get_attribute("innerHTML")).replace(",",""))
            i=0

            if (amount == "all") :
                amount = postCount
            
            if (amount > postCount) :
                amount = postCount
            #uzunluk = (amount*100)+500

            postRendered = 0

            while True :
                parent = self.chrome.find_elements_by_css_selector(".Nnq7C")[i]
                if (len(linkList) >= amount) :
                    print(self.print,"All Links were Pulled")
                    break
                for z in range(3) :
                    if amount <= postRendered :
                        break
                    linkElem = parent.find_elements_by_css_selector(".v1Nh3 > a")[z]
                    link = linkElem.get_attribute("href")
                    if linkList.count(link) == 0 :
                        linkList.append(link)
                    else :
                        i+=1
                        break
                    postRendered+=1
                self.chrome.execute_script("window.scrollTo(0,window.pageYOffset+321)")

                sleep(1)

            sleep(1)

            self.chrome.execute_script("window.open('','_blank');")
            self.chrome.switch_to.window(self.chrome.window_handles[1])

            sleep(1)

            for post in linkList :
                self.chrome.get(post)
                sleep(1)
                if like :
                    self.like()
                    print(self.print,"Post Liked")
                    sleep(1)
                if comment :
                    self.comment(commentOptions)
                    print(self.print,"Post Commented")
                    sleep(1)
                if save :
                    self.save_to_archive(post)
                    print(self.print,"Post Saved on Archive")
                    sleep(1)
            sleep(1)


    def quit_browser(self) :
        print(self.print,"Quiting Browser")
        self.chrome.quit()