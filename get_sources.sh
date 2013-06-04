#!/bin/bash

ORIGNAME=inxi
VERSION=1.9.7
SVN_REVISION=2012
NAME=${ORIGNAME}-${VERSION}

rm -rf ${ORIGNAME}
svn co -r $SVN_REVISION http://inxi.googlecode.com/svn/trunk $NAME >/dev/null
find ${NAME} -name ".svn" -exec rm -rf {} \; 2>/dev/null
rm -rf $NAME/$ORIGNAME.1
rm -rf $NAME/$ORIGNAME.tar.gz
chmod -x $NAME/$ORIGNAME.changelog

tar cfJ ${NAME}.tar.xz ${NAME}
rm -rf ${NAME}
