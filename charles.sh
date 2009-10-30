#!/bin/sh

# set $JAVACMD
. /usr/share/java-utils/java-functions
set_javacmd

CLASSPATH=$(build-classpath-directory /usr/share/java/charles)

$JAVACMD \
	-cp $CLASSPATH \
	-Dcharles.config="~/.charles.config" \
	-Djava.library.path=/usr/lib/charles \
	com.xk72.charles.gui.MainWithClassLoader
