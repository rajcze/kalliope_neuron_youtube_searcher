import urllib
import re
from kalliope.core.NeuronModule import NeuronModule, InvalidParameterException
class Youtube_searcher(NeuronModule):
    def __init__(self, **kwargs):
        cache = kwargs.get('cache', None)
        if cache is None:
            cache = False
            kwargs["cache"] = cache

        super(Youtube_searcher, self).__init__(**kwargs)
        # the args from the neuron configuration
        self.channel = kwargs.get('channel', None)
        self.title = "None"
        # check if parameters have been provided
        if self._is_parameters_ok():
            self.html_content = urllib.urlopen("https://www.youtube.com/results?sp=EgIQAg%253D%253D&search_query=" + self.channel)
            self.html_R = self.html_content.read()
            self.search_results = re.findall(r'href=\"/(.*?)\" class=\" yt-uix-sessionlink', self.html_R)
            if len(self.search_results) == 0:
                self.returncode = "Nochannelfound"
            else:
                self.video_url = re.findall(r'<a href=\"/watch\?v=(.{11})', "https://www.youtube.com/" + search_results[0] + "/videos")
                if len(self.video_url) == 0:
                    self.returncode = "Novideofound"
                else:
                    self.search_results_title = re.findall(r'\"title\":\"(.*?)\",\"', self.video_url[0])
                    if len(self.search_results_title) == 0:
                        self.returncode = "Notitlefound"
                    else:
                        self.title = search_results_title[0]
        self.message = {
            "title": self.title,
            "returncode": self.returncode
        }
        self.say(self.message)

    def _is_parameters_ok(self):
        """
        Check if received parameters are ok to perform operations in the neuron
        :return: true if parameters are ok, raise an exception otherwise
        .. raises:: MissingParameterException
        """
        if self.channel is None:
            raise MissingParameterException("You must specify a channel")
        if not isinstance(self.channel, str):
            raise MissingParameterException("Channel name must be a string")
        return True