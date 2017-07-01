# hugotools
Some tools I have created to use hugo.
If you need help building your hugo site, you can find out more about me here:  http://noahgift.com/

My stack for these scripts was:

### Conversion from Wordpress

I went the old school way and simply dumped the tables via SQL to CSV format, then converted them to JSON.  I then wrote a python script to create markdown files you can see here: 

  https://github.com/noahgift/hugotools/blob/master/wordpress_conversions/make_products.py.

### Sync to S3 Via Makefile and aws s3 command

You can see my Makefile here:

  https://github.com/noahgift/hugotools/blob/master/Makefile#L19

### Automatic Deploy via Wercker

I had a few issues here, but one thing that really helped was to make sure empty folders had a .gitignore.  You can see an example here:

  https://github.com/noahgift/hugotools/blob/master/wercker/wercker.yml

### Creating real-time search with algolia

I used algolia for a search engine:  
  
  https://www.algolia.com/doc/api-client/python/getting-started.  

You can see how I both created a simple index here:  
  
  https://github.com/noahgift/hugotools/blob/master/algolia/make_algolia_index.py

You can see the update of the index here:
  
  https://github.com/noahgift/hugotools/blob/master/algolia/sync_algolia_index.py
