import re
from re import compile, findall


class YoutubeUrlValidate:

    def validate(url):
        patern = re.compile("(http(s)?://)?(www.)?youtube.com(.br)?")
        result = patern.findall(url)
        return result
