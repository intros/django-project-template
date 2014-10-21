#!/bin/bash

CLOUDFRONT_HOSTNAME=d18rm8cl8msm70.cloudfront.net
ALL_LINKS=""
newline=$'\n'

pushd javascripts
for each in `ls |grep -v min`; do 
    uglifyjs -mc -o min/$each.min.js $each/*.js; 
done

pushd min
for each in *.min.js; do
    MD5STRING=`md5 -q $each | awk '{ print substr($1,0,9)}'`
    NEWFILENAME=${each%%.js}.$MD5STRING.js
    mv $each $NEWFILENAME
    s3cmd --no-progress -c ~/.s3cfg-intros put --acl-public $NEWFILENAME s3://static_intros/eagle/javascripts/min/$NEWFILENAME
    echo "<script src=\"//$CLOUDFRONT_HOSTNAME/eagle/javascripts/min/$NEWFILENAME\"></script>"
    ALL_LINKS+="${newline}<script src=\"//$CLOUDFRONT_HOSTNAME/eagle/javascripts/min/$NEWFILENAME\"></script>"
done

popd;
popd;

compass compile -s compressed --no-line-comments --force
MD5STRING=`md5 -q stylesheets/app.css | awk '{ print substr($1,0,9)}'`
NEWFILENAME=stylesheets/app.$MD5STRING.css
cp stylesheets/app.css $NEWFILENAME
s3cmd --no-progress -c ~/.s3cfg-intros put --acl-public $NEWFILENAME s3://static_intros/eagle/$NEWFILENAME
echo "<link rel=\"stylesheet\" href=\"//$CLOUDFRONT_HOSTNAME/eagle/$NEWFILENAME\">"
ALL_LINKS+="${newline}<link rel=\"stylesheet\" href=\"//$CLOUDFRONT_HOSTNAME/eagle/$NEWFILENAME\">"

echo "$ALL_LINKS"


