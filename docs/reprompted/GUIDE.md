# Starter Guide

## Creating Custom Templates
*The Fun and easy way*

We will tempalte a "human generator" similar to the one that is with the repo download. 

## 1) Create the entry point

In the root directory of the app, naviagate to `unprompted/templates`. This is where your templates live. You can organize the files here any way you like.

* Create a blank text file called `example.txt`. This will serve as the "entry point" for our new template.

* Open the new file and enter the following text:

```
Photo of a man
```

* Save the file and boot up the unprompted interface in Stable-Diffusion-WebUI-Forge. 
_This guide can be followed along with the standalone `unprompted_dry.py` if you prefer._

* Now enter the followiing as your promtp and press generate:

```
[file example]
```

Check the information underneath the resulting picture to confirm that Stable  Diffusion received the correct prompt ("Photo of a man")

* If it did, then let's  proceed to the good stuff...

## 2) Using the \[choose\] Shortcode

Now let's have Reprompted randomly choose between a man and a woman. 

```
Photo of a [choose]man|woman[/choose]
```

We use the vertical pipe (`|`) to separate our options and then Reprompted chooses one at random for us.

We can do the same thing with hair color for our subject.

`Photo of a [choose]red|blue|yellow|green|[/choose]-haired [choose]man|woman[/choose]`

> **TIP:** All of the code in this guide refers to our example.txt file unless otherwise noted. Remember to save your file with each change!

> **TIP:** You do NOT need to restart the WebUI when making changes to your templates (text files).


As you add more complex choices this list of options can get quite long. The longer it gets the more difficult it will be to manage. Instead of letting it get out of control, **We will create a separate file called `color.txt` and put our color choices in there.** 

> **TIP:** This is akin to 'object orientated approach' to programming.

Instead of using the vertical pipe in our `color.txt` file we can put our options on individual lines. 

Here is `color.txt`:
```
[choose]
red
blue
yellow
green
pink
[/choose]
```

We can always return to this file and add a bunch of other colors if we decide. Or we can repurpose this colors file for anything else. Let's make one that's more specific to hair colors.

`hair-colors.txt`
```
[choose]
brunette
blonde
platinum-blonde
chestnut
auburn
ginger
strawberry-blonde
grey
salt-n-pepper
black
[/choose]
```

Now we can reference our new fiels in `example.txt`:

`Photo of a [file hair-colors]-haired [choose]man|woman[/choose] wearing a [file color] hat.`

Notice how we can use our shortcodes inside of another template file. It's within that nesting that makes Reprompted so powerful.

Let's explore some other shortcodes.

### 3) Managing Stable Diffusion options with \[set\]

Reprompted allows us to manage variables using `[set]` and `[get]` shortcodes. You can create you rown variables or even adjust the system variables used by the image generator. 

At the bottom of `example.txt` let's declare a seed value of "1". This will help later debugging:
```
[set seed]1[/set]
```

For improved image quality, we can also set the CFG scale of 7 and turn on "Restore Faces" option:

```
[set cfg_scale]7[/set]
[set restore_faces]1[/set]
```

No matter how we change the UI, our template will **TAKE PRIORITY** over the options declared in the GUI and use our values we assigned here. 
*Provided we use them in the template we send through the pipeline, of course*

## 4) Overriding parts of the template

If you want the randomness a template offers, but you need to lock in a certain word or phrase of your choosing, you can accomplish this with the `[override]` shortcode.

In `example.txt`, say we need to generate a "panda" instead of a "man" or "woman". We would then need to wrap man/woman phrase with a variable that will act like a category: 

```
[set subject _out][choose]man|woman[/choose][/set]
```

We are calling the variable *`subject`* (you can name it whatever you want).

The `_out` argument indicates to Reprompted that we want to print this variable immediately for use in our prompt. This pushes it to priority level. 

* You sometimes will not want to do this. Like when we set the CFG scale and Restore Faces earlier. 

Now inside of the WebUI in the prompt section of Reprompted's accordian, we will change the prompt to this

```
[override subject="panda"][file example]
```

That’s all there is too it. 

So what we did is we created a variable called `subject`, this is so the choice of "man" or "woman" can be treated as a singular entity, as whatever choice it is would be the "subject" of our image. 

In doing so we can use the `[override]` shortcode to override the value of `subject` and force it to be a "panda" instead.

That way we don't need to change anything or add complex logic. We put the man woman choice in a container. Tell Reprompted Not to use that container, and instead use "panda" and then use the rest of `example.txt`. 

We shoul dnow have a an image of a panda with a certain colored hair wearing a certain colored hat. 

## 5) Conditional Shortcodes

Conditional shortcodes like `[if]` and `[chance]` will evaluate given variable(s) in their decision of what to output. 

For our purposes, we will run a check on the `subject` variable, and if it's set to `man`. If it is set to `man` we will make him wear a business suit 75% of the time.

On a new line write `wearing a business suit` inside of a conditional check in your example.txt file.

```
[if subject="man"]wearing a business suit[/if]
```

> **TIP:** Reprompted will automatically convert any linebreaks in our template to spaces, and will also remove unncessary/double spaces at the end of processing the chain.

Now to make it occur 75% of the time we introduce `[chance]` shortcode. 

```
[if subject="man"][chance 75]wearing a business suit[/chance][/if]
```

*Lets break down what all this template can do:*
Now we have it randomly choosing between a man and a woman.
It will randomly choose their hair color and hat color (separately with separate pools of choices).
And if it's a man, it will 75% of the time have them wearing a business suit
It will set our seed to 1
It will set our CFG scale to 7
And will turn on "Restore Faces" option in the web ui when it generates. 

**THAT IS AN INCREDIBLE AMOUNT OF VARIATION AND POWER ALL IN A SINGLE TEMPLATE FILE.**

Explore and get creative. Remember you can always return here if you want to take it step by step on creating more templates, but using different options. 

Have fun with it, we've only scratched the surface. Check out he full documentation

[Reprompted Documentation](DOCUMENTATION.md)

Good luck!