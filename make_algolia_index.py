"""
Creates a very simple JSON index for Hugo to import into Algolia.  Easy to extend.

"""
import os
import json

CONTENT_ROOT = "../content/products"
CONFIG = "../config.toml"
INDEX_PATH = "../index.json"

def get_base_url():
    for line in open(CONFIG):
        if line.startswith("baseurl"):
            return line

def build_url(base_url, title):

    url = "<a href='%s'>%s</a>" % (base_url, title)
    return url

def build_index():
    baseurl = get_base_url()
    index =[]
    posts = os.listdir(CONTENT_ROOT)
    for line in posts:
        record = {}
        title = line.strip(".md")
        record['title'] = title
        record['url'] = build_url(baseurl, title)
        index.append(record)
    return index

def write_index():
    index = build_index()
    with open(INDEX_PATH, 'w') as outfile:
        json.dump(index,outfile)

if __name__ == '__main__':
    write_index()
