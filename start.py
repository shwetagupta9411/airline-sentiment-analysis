from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from airline_test import TestAirlineSentiment

"""
sample request
http://localhost:6543?review=@AIRLINE $ % StAff I hate the services http://www.google.com

"""
def airline_sentiment_prediction(request):
    print("test")
    model_name = "airline_sentiment_model_20201123025610.sav"
    review = request.GET.get('review')
    res = TestAirlineSentiment(model_name, review).test()
    return Response(res)


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('airline', '/')
        config.add_view(airline_sentiment_prediction, route_name='airline')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
