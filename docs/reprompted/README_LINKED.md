# Reprompted for Stable Diffusion
Supercharge your prompt workflow with this powerful templating/scripting language. 

## Introduction

**Reprompted** is the refactored, and revitalized child of the highly modular addon for [AUTOMATIC1111's Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui), [Reprompted](https://github.com/ThereforeGames/reprompted). This templating language allows you to include various shortcodes in your prompts. You can pull text from files, declare variables, process text through conditional functions, and so much more. Think Wildcards on Steroids. 

The engine is flexible enough to serve as an **all-purpose text generator**.

Under active development and revitalized with some updates leveraging AI, LLMs and other advancements in the ML field. 

> Reprompted is built on top of Darren Mulholland's execellent [Python Shortcodes](https://www.dmulholl.com/dev/shortcodes.html) library.

## Installation
Simply clone or download this repo and place the files in the base of the extension directory of webUI (A1111,Forge, or Reforge).

You can alternatively run the included `reprompted_dry.py` to generate text in Command Prompt or Terminal without needing Stable Diffusion.

## Basic Usage

From txt2img or img2img select Reprompted as your active script: 

Now, shortcodes in your prompt will be processed through Reprompted to assemble the final string for image generation. 

### Try out the included demo

Enter the following as your prompt

`[file human/main]`

>> TIP: It is a simple human generator that will choose hair color, race and posture. 

The `[file]` shortcode looks in `reprompted/templates` for the specified text file (`reprompted/templates/human/main.txt`). You do not need to ttype the file extension.

## More to Explore

There are countless possibilities that you have to explore and create new ones yourself. 

To learn more about Remprompted and its capabilities, check out the following resources:
- [Starter Guide](GUIDE.md)
- [Full Documentation](DOCUMENTATION.md)
- [Changelog](CHANGELOG.md)

> Feel free to [open an issue](https://github.com/BenjaMITM/Reprompted/issues) if you run into a problem

> For general discussion and template sharing, use the [Discussions board](https://github.com/BenjaMITM/Reprompted/discussions)