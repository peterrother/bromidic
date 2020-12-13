#!/bin/bash

BLOG_ROOT="./"
ENTRY_DIR=$BLOG_ROOT"/entries"

YEAR=`date "+%Y"`
MONTH=`date "+%m"`
DAY=`date "+%d"`

echo "Blog post title: "
read TITLE
echo "Url-friendly version: "
read URL_TITLE

mkdir -p $ENTRY_DIR/$YEAR/$MONTH/$DAY
touch $ENTRY_DIR/$YEAR/$MONTH/$DAY/$URL_TITLE".textile"
#open /Applications/TextEdit.app $ENTRY_DIR/$YEAR/$MONTH/$DAY/$URL_TITLE".textile"
#open /Applications/TextEdit.app $BLOG_ROOT"/pages/archive.textile"
vim $ENTRY_DIR/$YEAR/$MONTH/$DAY/$URL_TITLE".textile" $BLOG_ROOT"/pages/archive.textile"

echo "Would you like to publish this post?: "
read TO_PUBLISH

if [ $TO_PUBLISH == "y" ]
then
    cd $BLOG_ROOT
    make
    cd -
else
    exit 0
fi
