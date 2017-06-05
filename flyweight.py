import abc
"""
亨元模式
模式特点：运用共享技术有效地支持大量细粒度的对象。

程序实例：一个网站工厂，根据用户请求的类别返回相应类别的网站。如果这种类别的网站已经在服务器上，那么返回这种网站并加上不同用户的独特的数据；如果没有，那么生成一个。

代码特点：为了展示每种网站的由用户请求的次数，这里为它们建立了一个引用次数的字典。

　　　　　　之所以不用Python的sys模块中的sys.getrefcount()方法统计引用计数是因为有的对象可能在别处被隐式的引用，从而增加了引用计数。 
"""


class User:
    def __init__(self, n):
        self.name = n


class Website:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def use(self, u):
        """users use website"""


class ConcreteWebsite(Website):
    def __init__(self, wn):
        self.website_name = wn

    def use(self, u):
        print u.name + " use " + self.website_name


class WebsiteFactory:
    flyweights = {}

    def get_website_category(self, n):
        if self.flyweights.has_key(n) is False:
            self.flyweights[n] = ConcreteWebsite(n)
        return self.flyweights[n]

    def get_website_count(self):
        print len(self.flyweights.keys())


if __name__ == "__main__":
    website_factory = WebsiteFactory()
    alice = User("Alice")
    bob = User("Bob")

    website = website_factory.get_website_category("bbs")
    website.use(alice)
    website.use(bob)
    website_factory.get_website_count()

    website = website_factory.get_website_category("blog")
    website.use(alice)
    website.use(bob)
    website_factory.get_website_count()

    website = website_factory.get_website_category("bbs")
    website.use(alice)
    website.use(bob)
    website_factory.get_website_count()
