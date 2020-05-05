# instagrambot
Instagram Bot with Selenium Webdriver

# Installation
1.clone repostory with git or directly install instabot.py file
2.Move file to your project bin

`from instabot import *`

# docs

## Init of Bot

`instabot = Bot(<username>,<password>)`

## login

`instabot.login()`
This function automaticly logins with your username and password

## closenotf
Closes notification 
### This function automaticly runinng after login
`instabot.closenotf()`

## follow_user
Follows users in parameters

`instabot.follow_user(<user1>,<user2>,...)`

## unfollow_user
Unfollows users in parameters

`instabot.unfollow_user(<user1>,<user2>,...)`

## like 
Likes the post already opened

`instabot.like()`

## like_by_user
Likes all posts of user

`instabot.like_by_user(<user1>,<user2>,...)`

## like_by_tag
Likes posts of tag

`instabot.like_by_tag(amount,<user1>,<user2>,...)`

## get_followers
Write followers of user to file

`instabot.get_followers(<user>,file_adress)`

## read_stories 
Read all stories

`instabot.read_stories`

## quit_browser
Exits from browser

`instabot.quit_browser()`
