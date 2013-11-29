import re

def parse(fileobj):
    line_nb = 0
    for line in fileobj:
        line_nb += 1

        m = re.findall('\$\._\([\'"](.*?)[\'"]\)', line)
        for res in m:
            yield line_nb, 'gettext', res

        m = re.search('\$.*\.ngettext\((?:[\'"])(?P<string1>.*)(?:[\'"]),[ ]*(?:[\'"])(?P<string2>.*)(?:[\'"]),.*\)', line)
        if m:
            yield line_nb, 'ngettext', m.groups()

def babel_extract(fileobj, keywords, comment_tags, options):
    """Extract messages from XXX files.
    :param fileobj: the file-like object the messages should be extracted
                    from
    :param keywords: a list of keywords (i.e. function names) that should
                     be recognized as translation functions
    :param comment_tags: a list of translator tags to search for and
                         include in the results
    :param options: a dictionary of additional options (optional)
    :return: an iterator over ``(lineno, funcname, message, comments)``
             tuples
    :rtype: ``iterator``
    """
    for i in parse(fileobj):
        yield i[0], i[1], i[2], []

if __name__ == '__main__':
    fileobj = open('./test.html')
    for i in parse(fileobj):
        print i
