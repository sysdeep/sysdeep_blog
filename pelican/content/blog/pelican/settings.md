Title: Pelican settings
Date: 2014-06-16 10:20
Category: Development
Tags: pelican, settings
Summary: Short version for index and feeds


настройки пеликана


Metadata
========

Pelican tries to be smart enough to get the information it needs from the file system (for instance, about the category of your articles), but some information you need to provide in the form of metadata inside your files.

If you are writing your content in reStructuredText format, you can provide this metadata in text files via the following syntax (give your file the .rst extension):

	My super title
	##############

	:date: 2010-10-03 10:20
	:tags: thats, awesome
	:category: yeah
	:slug: my-super-post
	:author: Alexis Metaireau
	:summary: Short version for index and feeds


Pelican implements an extension to reStructuredText to enable support for the abbr HTML tag. To use it, write something like this in your post:

	This will be turned into :abbr:`HTML (HyperText Markup Language)`.

You can also use Markdown syntax (with a file ending in .md, .markdown, .mkd, or .mdown). Markdown generation requires that you first explicitly install the Markdown package, which can be done via pip install Markdown. Metadata syntax for Markdown posts should follow this pattern:


	Title: My super title
	Date: 2010-12-03 10:20
	Category: Python
	Tags: pelican, publishing
	Slug: my-super-post
	Author: Alexis Metaireau
	Summary: Short version for index and feeds



Conventions for AsciiDoc posts, which should have an .asc extension, can be found on the AsciiDoc site.

Pelican can also process HTML files ending in .html and .htm. Pelican interprets the HTML in a very straightforward manner, reading metadata from meta tags, the title from the title tag, and the body out from the body tag:

	<html>
	    <head>
	        <title>My super title</title>
	        <meta name="tags" content="thats, awesome" />
	        <meta name="date" content="2012-07-09 22:28" />
	        <meta name="category" content="yeah" />
	        <meta name="author" content="Alexis Métaireau" />
	        <meta name="summary" content="Short version for index and feeds" />
	    </head>
	    <body>
	        This is the content of my super blog post.
	    </body>
	</html>
With HTML, there is one simple exception to the standard metadata: tags can be specified either via the tags metadata, as is standard in Pelican, or via the keywords metadata, as is standard in HTML. The two can be used interchangeably.

Note that, aside from the title, none of this article metadata is mandatory: if the date is not specified and DEFAULT_DATE is set to fs, Pelican will rely on the file’s “mtime” timestamp, and the category can be determined by the directory in which the file resides. For example, a file located at python/foobar/myfoobar.rst will have a category of foobar. If you would like to organize your files in other ways where the name of the subfolder would not be a good category name, you can set the setting USE_FOLDER_AS_CATEGORY to False. When parsing dates given in the page metadata, Pelican supports the W3C’s suggested subset ISO 8601.

If you do not explicitly specify summary metadata for a given post, the SUMMARY_MAX_LENGTH setting can be used to specify how many words from the beginning of an article are used as the summary.

You can also extract any metadata from the filename through a regular expression to be set in the FILENAME_METADATA setting. All named groups that are matched will be set in the metadata object. The default value for the FILENAME_METADATA setting will only extract the date from the filename. For example, if you would like to extract both the date and the slug, you could set something like: '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

Please note that the metadata available inside your files takes precedence over the metadata extracted from the filename.