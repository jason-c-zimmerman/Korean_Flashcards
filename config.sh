bash=`which bash`
#!$bash

haveProg() {
	[ -x "$(which $1)" ]		
}

if haveProg apt-get; then pkgman="sudo apt-get"
elif haveProg yum; then pkgman="sudo yum"
elif haveProg pkg; then pkgman="pkg"
else
	echo 'No package manager found.'
	exit 2
fi

python=`which python`
if [ "$python" = "" ] 
then
	$pkgman install python
fi

pip=`which pip`
if [ "$pip" = "" ] 
then
	$pkgman install python-pip
fi

if [ $SHELL = "/data/data/com.termux/files/usr/bin/bash" ] 
then
	pkg install play-audio
fi

pip install readchar
pip install keyboard
pip install playsound

export PATH=$PATH:.
