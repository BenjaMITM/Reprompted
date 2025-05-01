# Documentation

**Note:** This is a work in progress. May become a Wiki in the future. 
            _*ALL SHORTCODE SYNTAX IS SUBJECT TO CHANGE*_

## Adding New Shortcodes

Shortcodes are loaded as Python modules from `reprompted/shortcodes`. You can make your own shortcodes by creating files in the same folder. Best practice is to create within the `/custom` subdirectory but anywhere within the shortcodes folder will still register.

The shortcode name is defined by the filename. The filenames should be unique for every shortcode.
E.g. `overrides.py` will give you the ability to use `[override]` shortcode.

The structure of shortcodes is as follows:
```python
class Shortcode():
    """A description of the shortcode goes here."""
    def __init__(self,Reprompted):
        self.Reprompted = Reprompted

    def run_block(self, pargs, kwargs, context):

        return("")

    def cleanup(self):
        return("")
```

The `__init__` function gives the shortcode access to our main Reprompted object. This is where you should declare any unique variables for your shortcode. 

The `run_block` function contains the main logic for your shortcode. It has access to special variables (_*Documentation from [Python Shortcdes](https://www.dmulholl.com/dev/shortcodes.html) library.*_):

- `pargs`: a **list** of the shortcode's positional arguments.
- `kwargs`: a **dictionary** of the shortcode's keyword arguments.
- `context`: an _optional_ arbitrary **context object** subblied by the _caller_.
- `content`: the **string** within the shortcode tags, e.g. `[tag]content[/tag]`.

**Positional** and **Keyword** arguments are passed as **strings**. The function itself should _return a string_ which will _replace the shortcode_ in the parsed text.

The `cleanup` function runs at the end of the parsing process. It will free any unnecessary variables from memory here.

_For more examples and usage inspiration, please examine the code of the stock shortcodes._

## Atomic vs Block Shortcodes

Reprompted supports two types of shortcodes:

**Block shortcodes**: 
  - Require an end tag
  - `[set my_var]This is a block shortcode[/set]`

**Atomic shortcodes**:
  - They are self closing. 
  - These do not require an end tag
  - `[get my_var]`

The two are mutually exclusive. Shortcodes **MUST** be defined as an Atomic Shortcode, or a Block Shortcode. 
It can never be both.

The type is declared by including one of the following functions in your `.py` file:

```python
def run_block(self, pargs, kwargs, context):
```

```python
def run_atomic(self, pargs, kwargs, context):
```

Atomic shortcodes _DO NOT_ receive a `content` variable.

## Understanding the Processing Chain
The internal order of the shortcode processing is essential to understand

_**Innershortcodes are processed before outer shortcodes**_

They work from the inside out.

This has a number of advantages, but it does present an issue with _conditional functions_.

Consider the following example:
```python
[if my_var=1][set another_var]0[/set][/if]
```

~~If your familiar with programming, then you might take this to mean that `another_var` is set to `0` if my_var equals `1`.~~

That logic would be incorrect.

In Reprompted syntax, `another_var` will equal 0 regardless of the outcome of the `if` statement.
This is because the `[set]` shortcode is processed before the `[if]` shortcode.
This means that `another_var` will always be set to `0`.

### A Solution: Secondary Shortcode Tags
Reprompted allows you to write tags using `<>` instead of `[]` to defer processing.

Like in our last example, if you want to set `another_var` to `0` only if `my_var` equals `1`, you can use the following syntax:
```python
[if my_var=1]<set another_var>0</set>[/if]
```
This will ensure that `another_var` is set to `0` only if `my_var` equals `1`.

This way the inner shortcode is not processed until *after* it is returned by the outer `[if]` statement.

Secondary shortcode tags give us a couple additiional benefits:
  * If your shortcode is computationally expensive, you can avoid running it unless the outer shortcode succeeds. For performance reasons this gives us excellent control of our resource usage.
  * We can pass these secondary shortcodse **as arguments in other shortcodes (That support it).
    * Example: We want to run the `[chance]` shortcode with dynamic probability. We can accomplish that like this:
    ```python
   `[chance _probability="<get_my_var>"]content[/chance]`

---
## Basic Shortcodes
*This section describe all the included basic shortcodes and their functionality.*

### [#]
type: Atomic

Description: Use this to write comments in your templates. 
Comments are discarded by Unprompted. They will not affect the final output.

*Best used for short notes and iformation for the template.*
```
[# This is my comment.]
```

### [chance int]
type: Block

Description: Returns the content if the integer you passed is greater than or equal to a randomly generated number between 1 and 100.

**Supports secondary shortcode tags**
- Optional Arguments: `_probability`
  - `[chance _probability="<get my_var>"]content[/chance]`

```
[chance 25]You will read this 25% of the time.[/chance]
```

### [choose]
type: Block
description: Returns one of multiple options. Delimited by the vertical pipe or newline character. `|`.

```python
[choose]red|yellow|blue|green[/choose]
```

### [else]
type: Block
descriptiion: Returns content if a previous *conditional* shortcode failed it's check. Otherwise discard. 
*Conditional shortcodes like `[if]` and `[chance]`*

**Note**: Currently `[else]` should appear immediately after the conditional shortcode - don't try to get too crazy with nesting or delayed statements or it will probably fail.

```python
[if my_var=0]Print something[/if][else]It turns out my_var did not equal 0.[/else]
```

### [eval]
Type: Block
Description: Uses python's `eval()` function to parse the content and return the result. Particularly useful for arithmetic operations.
```python
[eval]5 + 5[/eval]
```

### [file path(str)]
Type: Atomic
Description: Process the content of `path` (including any shortcodes therein) and return the result.

`reprompted/templates` is the base directory for this shortcode, e.g. `[file example/main]` will target `reprompted/templates/example.main.txt`.

Do not enter a file extension, `.txt` is assumed.

Supports relative paths by starting the `path` with `./`, e.g. `[file ./main]` will target the folder that the previously-called `[file]` resides in.

If the given `path` is a directory as opposed to a file, `[file]` will return the contents of a random file in that directory. 

```python
[file my_template/common/adjective]
```

### [get variable]
Type: Atomic
Description: Returns the value of `variable`.

Supports secondary shortcode tags with the optional `_var` argument, 

```python
[get _var="<file example>"]
``` 

### [if variable {_not}]
Type: Block
Description: Checks whether `variable` is equal to the given value.
If `true`, returns the content. Otherwise, discards it.

Supports the testing of multiple variables.
```python
[if var_a=1 var_b=50 var_c="something"]
```
* If one or more variables return false, the content is discarded.

##### _not Argument
The optional `_not` argument allows you to test for false instead of true.
```python
[if _not my_variable=1]
```
This will return the content if `my_variable` does *not* equal 1.

### [override variable]
Type: Atomic
Description: Forces `variable` to equal the given value when attempting to `[set]` it.

Supports multiple variables.

In the example below, `my_variable` will equal "panda" after running the `[set]` shortcode.

```python
[override my_variable="panda"][set my_variable]fox[/set]
```

### [random {_min} {_max} {_float}]
Type: Atomic
Descriptiopn; Returns a random integer between 0 and the given integer, e.g. `[random 2]` will return 0, 1, or 2.

You can specify the lower and upper boundaries of the range with `_min` and `_max`, e.g. `[random _min=5 _max=10]`.

If you pass `_float` into this shortcode, it will support decimal numbers instead of integers.

### [set {_append} {_prepend}] 
Description: 
Sets a variable to the given content.

Arguments:
`_append` will instead add the content to the end of the variable's current value, 
e.g. if `my_var` equals "hello" then 
```python
[set my_var _append] world.[/set]
```
This will make it equal "hello world."

`_prepend` will instead add the content to the beginning of the variable's current value.

Supports all Stable Diffusion variables that are exposed via Automatic's Script system, 
```python
[set cfg_scale]5[/set]
```
This will force the CFG Scale to be 5 for the run.