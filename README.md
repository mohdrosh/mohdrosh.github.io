# Digital Valentines Day Card
> They say the pen is mightier than the sword. But you're a developer, and you build empires with just a keyboard and mouse.
> Why give money to hallmark so they can chop down trees to make cards.
> Show her you love her in a way that's more "you".

Displays a message for your valentine, with custom images in the shape of a heart.
Moving your mouse over the heart shaped images causes them to move.

## Files and Folders:
* images folder
  - Place the images you want to use for the card
  > Note: does not support .heic files on firefox, or edge. I have not tested on safari, or other browsers. 
  > It's best to use universally supported formats like jpeg or png.
* message.txt
  - Leave a note, or a poem for your valentine
  - For the best results, try to have 1 image for each line in your message
* valentine.html
  - This is the card itself.
* generate.py
  - a simple python file that takes your images, and your message, and populates data.js, which valentine.html loads to get your images and message.
  - takes a boolean argument (scatter: default=False)
* data.json
  - valentine.html has some javascript functions that use this data. You can modify it using the templated structure, but it's automatically populated and overwritten if you run generate.py


## Instructions
1. Add a message for your valentine in message.txt
2. Add the images you want to use in your card
   > Again, for best results, try to have 1 image for each line in your message
3. run `python generate.py`
4. Open valentine.html in your browser.


## Remarks
I wrote this because I didn't have a card, but wanted to do something special for my wife.
I only spent a few hours writing this, so I don't expect it to be perfect.
In my case, the order of the images didn't really matter, so I did not spend time ensuring
that they appear in the proper order.

I suspect that they will appear in order the order they are placed in the images directory.
Or alphabetically. I'm not sure to be honest.
If this repo gets attention, I'm open to maintaining it and adding features by request.

I might put this in a docker container sometime in the near future (probably just an httpd service) so you can host it somewhere, rather than just providing an html file.