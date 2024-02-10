# LectureTubeClicker
If you are also a student of TU Wien and don't want to click through the 400 Pages to find your lecture, here is a little script that does it automatically for you (it's still a little buggy)

## How it works
Install selenium and webdriver by using pip3 install selenium and pip3 install webdriver (if you are still missing some package, your console will tell you)

Open up the program in any editor of your choice and type in the professor of your choice in the variable prof as well as the year the lecture was held in into the variable year. You can be more specific if you want but I can't guarantee that it will work.

You also need to add in your TUWEL login credentials in the variables username and password. (The program is very short so u can easily check for yourself that i'm not stealing any data)

Then simply start the program and watch the magic happen. (It's not very fast but it saves u some time hopefully)

## Potential bugs
You may run into timeouts. Just restart the program. If it happens too often, increaste the button_wait value in 0.1 increments. My personal recommendation is 0.5.
Sometimes it doesn't exactly stop where u want it to stop, I couldn't figure out why. The if condition, that checks if prof and year is in page source stops, as soon as it finds the year (?). Potential bugfix coming soon.
