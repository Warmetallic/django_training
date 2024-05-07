from django.http import HttpRequest

def setup_useragent_on_request_middleware(get_response):
    print("Initial call")

    def middleware(request: HttpRequest):
        print("before get response")

        request.user_agent = request.META["HTTP_USER_AGENT"]

        response = get_response(request)

        print("after get response")
       
        return response
    
    return middleware


class CountRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.request_count = 0
        self.response_count = 0
        self.exceptions_count = 0

    def __call__(self, request: HttpRequest):
        self.request_count += 1
        print("request_count", self.request_count)
        response = self.get_response(request)
        self.response_count += 1
        print("response_count", self.response_count)
        return response
    
    def process_exception(self, request: HttpRequest, exception: Exception):
        self.exceptions_count += 1
        print("got", self.exceptions_count, "exceptions so far")