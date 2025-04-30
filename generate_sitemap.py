#! /usr/bin/env python

import requests
import json
import os

URL = 'https://readthedocs.com/api/v3/projects/canonical-ubuntu-documentation-library/subprojects/?limit=50'
TOKEN = os.environ["TOKEN"]

def main():

    response = get_subprojects(URL, TOKEN)
    data = response.json()
    children = {}
    sitemap = open("sitemap.xml", "w")
    template_sitemap = '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'

    for item in data["results"]:
        children.update({item["child"]["urls"]["documentation"]: item["child"]["modified"]})

    for key, value in children.items():
        template_sitemap = "{}\n{}".format(template_sitemap, template_sitemap_section(key, value))

    sitemap.write(template_sitemap + "\n</urlset>")

def template_sitemap_section(loc, lastmod):
    template = "<url>\n<loc>{}</loc>\n<lastmod>{}</lastmod>\n</url>".format(loc, lastmod)
    return template

def get_subprojects(url, token):

    HEADERS = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=HEADERS)

    return response


if __name__ == "__main__":
    main()