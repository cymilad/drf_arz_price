from rest_framework.decorators import api_view
from rest_framework.response import Response
from .price import *


@api_view(['GET', 'POST'])
def index(request):
    data = {
        'Dollar': dollar(),
        'Canada Dollar': Canadian_dollar(),
        'Australia Dollar': Australian_dollar(),
        'New Zealand Dollar': NewZealand(),
        'Singapore Dollar': Singapore(),
        'Hong Kong Dollar': HongKong(),
        'Euro': euro(),
        'Dirham UAE': DirhamUAE(),
        'British Pound': GBP(),
        'Syrian Pound': Syria(),
        'Turkish Lira': TRY(),
        'Switzerland Franc': Switzerland(),
        'China Yuan': China(),
        'South Korea Won': South_Korea(),
        'Indian Rupee': India(),
        'Pakistan Rupee': Pakistan(),
        'Afghani': Afghanistan(),
        'Danish Crown': Denmark(),
        'Sweden Krona': Sweden(),
        'Norwegian Crown': Norway(),
        'Saudi Rial': Saudi_Arabia(),
        'Qatar Rial': Qatar(),
        'Oman Rial': Oman(),
        'Kuwait Dinar': Kuwait(),
        'Iraq Dinar': Iraq(),
        'Bahrain Dinar': Bahrain(),
        'Malaysian Ringgit': Malaysia(),
        'Thailand Baht': Thailand(),
        'Russian Ruble': Russian(),
        'Azerbaijan Manat': Azerbaijan(),
        'Armenian Dram': Armenian(),
        'Georgian Lari': Georgian(),
        'Kyrgystan Som': Kyrgystan(),
        'Tajikistan Somoni': Tajikistan(),
        'Turkmenistan Manat': Turkmenistan(),
    }
    return Response(data)
