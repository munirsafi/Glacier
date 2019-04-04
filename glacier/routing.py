routes = {}


class Router():

    def add(self, path, function, method):
        routes[path] = function
