import re

def parse(fileobj):
    line_nb = 0
    for line in fileobj:
        line_nb += 1
        m = re.match('.*<%=?\s+(?P<js>.*)\s+%>.*', line)
        if m:
            js = m.group('js')
            m = re.match('^\$\._\((?:[\'"])(?P<string>.*)(?:[\'"])\)$', js)
            if m:
                yield line_nb, 'gettext', m.group('string')
                continue

            m = re.match('^\$.*\.ngettext\((?:[\'"])(?P<string1>.*)(?:[\'"]), (?:[\'"])(?P<string2>.*)(?:[\'"]), .*\)$', js)
            if m:
                yield line_nb, 'ngettext', m.groups()
                continue

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
    fileobj = open('/home/jtrang/webapps/cloudui2/app/templates/test.html')
    for i in parse(fileobj):
        print i
