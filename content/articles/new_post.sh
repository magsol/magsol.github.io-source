#!/bin/bash

if [[ $# != 1 ]]; then echo "$0 <article-slug>"; exit 1; fi

article_slug=$1
article_file=${article_slug}.md
touch ${article_file}

echo "Title: " > ${article_file}
echo "Category: " >> ${article_file}
#echo "Category:" $(grep -h "Category:" *.md | sed -r -e s,"Category: ",, -e s/", "/","/g | xargs -d "," -n1 | grep -Ev "^$" | sort | uniq | paste -d"," -s | sed s/","/", "/g
#) >> ${article_file}
echo "Tags: " >> ${article_file}
#echo "Tags:" $(grep -h Tags *.md | sed -r -e s,"Tags: ",, -e s/", "/","/g | xargs -d "," -n1 | grep -Ev "^$" | sort | uniq | paste -d"," -s | sed s/","/", "/g
#) >> ${article_file}
echo "Comments: true" >> ${article_file}
echo "Authors: Shannon Quinn" >> ${article_file}
echo "Slug: ${article_slug}" >> ${article_file}
echo "Date: $(date +"%Y-%m-%d %H:%M:%S")" >> ${article_file}
#echo "Summary: " >> ${article_file}

echo "Created pelican/content/${article_file}"
