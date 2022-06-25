# WINRAT #

## DISCALMER ##
DO NOT USE FOR ANYTHING BAD!!!

## ABOUT ##
When you run the dropper executable or python file it loads the sandbox detector or stage2 form the web.
Stage 2 only has the code for sandbox detection, if all checks pass it loads stage3, Stage 3 main goal is to look at the modules configuration file and automatically import and call their run function. This can be confgured that each module run in a new thread.

## HOW TO USE ##
Run
```
python generator.py --help
```

Examples

```
python generator.py
python generator.py --debug
```