#!/bin/sh
set -e

# set JAVA_HOME from jpackage-utils if available
if [ ! -f /usr/share/java-utils/java-functions ]; then
	echo >&2 "jpackage-utils not found."
	exit 1
fi
. /usr/share/java-utils/java-functions

MAIN_CLASS=com.xk72.charles.gui.MainWithClassLoader
LIBDIR=/usr/lib/charles
CLASSPATH=$(build-classpath-directory /usr/share/java/charles)

# activation: can't be added to classpath:
# Exception in thread "main" java.lang.SecurityException: Prohibited package name: java.lang
# but apparently not needed if part of jdk
for jar in oro; do
	jar=$(find-jar $jar)
	CLASSPATH=$CLASSPATH:$jar
done

# extra options
OPTIONS="\
	-Dcharles.config=~/.charles.config \
	-Djava.library.path=$LIBDIR
"

# this will call exec java
run "$@"
