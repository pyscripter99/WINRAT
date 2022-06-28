# WINRAT #

## DISCALMER ##
DO NOT USE FOR ANYTHING BAD!!!

## ABOUT ##
When you run the dropper executable or python file it loads the sandbox detector or stage2 form the web.
Stage 2 only has the code for sandbox detection, if all checks pass it loads stage3, Stage 3 main goal is to look at the modules configuration file and automatically import and call their run function. This can be confgured that each module run in a new thread.

The staging means that every time the dropper is executed it repeats the prosess meaning a file is saved to the hard drive.

The final stage (stage 3) will add itself to startup, execute the new file and delete the original ( executed self )

## HOW TO USE ##
Run
```
$ python generator.py --help
```

Examples

```
$ python generator.py
$ python generator.py --help
$ python generator.py --exe true --name paylaod.exe
```