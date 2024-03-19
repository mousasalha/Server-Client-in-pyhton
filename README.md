# Server-Client-in-pyhton
Server - Client web server using socket programming 
# Birzeit University -Palestine-

Part 1 :
Using socket programming, implement TCP client and server applications in go, python, java or C. The server should listen on port 9955. The server waits for a message from a client.
 If the message is with one of the students ID, the sever should do the following:

1.display a message on the server side that the OS will lock screen after 10 seconds
2.send a message to the client that the sever will lock screen after 10 seconds
3.then wait 10 seconds
4.then call a function lock the screen of the operating system (windows or Linux or MAC). 

Any student ID of the group member should work. Any other student number or any text should display an error message on the server side and no lock screen should be done. 


files : 
server.py
client.py

Part 2 : 


Using socket programming, implement a simple but a complete web server in python that is listening on port 9966.
Have a look also on rfc2616 (https://datatracker.ietf.org/doc/html/rfc2616 )
0-from rfce2616, what is Content-Type in the HTTP request and why do we need it?
 The user types in the browser something like http://localhost:9966/ar or http://localhost:9966/en 
The program should check 
1-if the request is / or /index.html or /main_en.html or /en (for example localhost:9966/ or localhost:9966/en) then the server should send main_en.html file with Content-Type: text/html. 
The main_en.html file should contain 
HTML webpage that contains 
a.“ENCS3320-My Tiny Webserver 23/24” in the title
b.“Welcome to our course Computer Networks, This is a tiny webserver” (part of the phrase is in Blue)
c.Use CSS to make the page looks nice
d.Divide the page in different boxes and put student’s information in the different boxes
e.Include CSS as a separate file 
f.Summarize point 0 above in a box
g.Group members names and IDs (each one in a box)
h.Some information about the group members. For instance, projects you have done during different course (programming, electrical, math, etc), skills, hobbies, etc.
i.The page should contain at least an image with extention.jpg and an image with extension .png
j.A link to a local html file (an html file) 
k.a link to https://www.w3schools.com/python/python_strings.asp

2-If the request is /ar then the server response with main_ar.html which is an Arabic version of main_en.html 
3 -------- if the request is an .html file then the server should send the requested html file with Content-Type: text/html. You can use any html file.
3-if the request is a .css file then the server should send the requested css file with Content-Type: text/css. You can use any CSS file
4-if the request is a .png then the server should send the png image with Content-Type: image/png. You can use any image.
5-if the request is a .jpg then the server should send the jpg image with Content-Type: image/jpeg. You can use any image.
6-Use  the status code 307 Temporary Redirect to redirect the following
a.If the request is /cr then redirect to cornell.edu website
b.If the request is /so then redirect to stackoverflow.com website
c.If the request is /rt then redirect to ritaj website

7-If the request is wrong or the file doesn’t exist the server should return a simple HTML webpage that contains (Content-Type: text/html)
1- “HTTP/1.1 404 Not Found” in the response status
2-“Error 404” in the title
3-“The file is not found” in the body in red
4-Your names and IDs in Bold
5-The IP and port number of the client
8-The program should print the HTTP requests on the terminal window (command line window).


file : web-server.py
