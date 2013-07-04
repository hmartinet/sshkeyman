#/bin/sh

TARGET_DIR=target
#VERSION=$(git describe --abbrev=0 --tags)
VERSION='1.0-alpha1'

rm -Rf $TARGET_DIR/sshkeyman
mkdir -p $TARGET_DIR/sshkeyman
cp -R debian $TARGET_DIR/sshkeyman/
cp -R src/* $TARGET_DIR/sshkeyman/

cd $TARGET_DIR/sshkeyman
dch --create -v $VERSION --package sshkeyman
debuild -i -us -uc -b

