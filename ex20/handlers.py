class Handler:
    """
    对Parser发起的方法调用进行处理的对象

    Parser将对每个文本块调用start()和end(),并将合适
    的文本块名称作为参数。方法sub()将用于正则表达式替换，
    使用诸如'emphasis'等名称调用时，这个方法将返回相应的
    替换函数
    """
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)
        if callable(method):
            return method(*args)

    def start(self, name):
        self.callback('start_',name)
    def end(self, name):
        self.callback('end_', name)
    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_',name, match)
            if result is None: match.group(0)
            return result
        return substitution


class HTMLRenderer(Handler):
    def start_paragraph(self):
        print('<p>')
    def end_paragraph(self):
        print('</p>')
    def sub_emphasis(self, match):
        return '<em>{}</em>'.format(match.group(1))
    def feed(self,data):
        print(data)
