[![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Assets/1.png?raw=true "Bi0s")](https://tasks.bi0s.in/home)

# ❌Buggy PHP❌

### Description : 

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Assets/15.jpeg?raw=true)

### Category : 
- **WEB**
### Challenge Link :

- [Mirror](http://168.119.123.141:9898/)

### Initial Analysis :

- Just click on the link http://168.119.123.141:9898/.
- My guess is that there will be some **Bug** with the php of the webpage.
- So If we find the bug then we will get the flag.
1. Analyse the **PHP** of the web page.
2. Find the Bug
3. Rectify it and capture the Flag.

### Steps To Be followed :
- To find the **PHP** of the web page **?source** command is used.

```
http://168.119.123.141:9898/?source
```
![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Assets/17.jpeg?raw=true)

- You will be able to see the **PHP** now.
- Try to analyse it.
- Then you you will come to know that **IF** conditions given there should satisfy to get the **FLAG**.
- We need to **PASS** the **VARIABLES** so that it collects the data that we provide.

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Assets/18.jpeg?raw=true)

- Pass the variable value such that it satisfies all **IF** conditions.

```
http://168.119.123.141:9898/?variable_name1=value1 & variable_name2=value2
```
```
http://168.119.123.141:9898/?B=5E9
```
- Here **B='5E9'** is provided because it should be **Greater than 10000** and **Length < 4** and should be **NUMERIC**.
- **"&"** is used to **PASS MULTIPLE VARIABLE** at same time.
- Next is to pass the **"A"**.
- From the Hint given its clear that it is an **UNICODE**;
- Then Copy the **"A"** **ERROR** from the Previous Bug Page.

```
http://168.119.123.141:9898/?B=5E9&A
```

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Assets/23.jpeg?raw=true)

- Finally flag will be shown in the Page.

![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Assets/19.jpeg?raw=true)
![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Assets/20.jpeg?raw=true)
![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Assets/21.jpeg?raw=true)
![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Assets/22.jpeg?raw=true)
![Bi0s](https://github.com/abhishekabi2002/Bi0s/blob/master/Assets/16.jpeg?raw=true)

### Flag 🏴 : 
> **inctfj{l1f3_1s_e4sy_w1th_PHP}**





