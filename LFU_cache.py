class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.buffer = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.buffer



        # Your LFUCache object will be instantiated and called as such:
        # obj = LFUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)