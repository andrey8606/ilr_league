from django.shortcuts import render, redirect

from .models import Result

CURR_YEAR = '2022'
CURR_DISTANCE = '1000'
CITIES = {
    'Moscow': 'Москва',
    'Rostov-on-Don': 'Ростов-на-Дону',
    'Saint-Petersburg': 'Санкт-Петербург',
    'Sevastopol': 'Севастополь',
    'Kemerovo': 'Кемерово',
    'Kazan': 'Казань',
}
MONTHS = ['jan', 'feb', 'mar', 'apr', 'may',
          'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']


def index(request):
    gender_dropdown_value = ''
    city_dropdown_value = ''
    distance_dropdown_value = ''
    gender_query = request.GET.get('gender')
    city_query = request.GET.get('city')
    year_query = request.GET.get('year')
    distance_query = request.GET.get('distance')
    clear_filter = request.GET.get('clear_filter')
    if (clear_filter != ''
            and clear_filter is not None
            and clear_filter == 'True'):
        return redirect('index')
    if year_query != '' and year_query is not None:
        all_results = Result.objects.all().filter(year=year_query)
    else:
        all_results = Result.objects.all().filter(year=CURR_YEAR)

    if (distance_query != ''
            and distance_query is not None):
        all_results = all_results.filter(distance=distance_query)
        distance_dropdown_value = distance_query
    else:
        all_results = all_results.filter(distance=CURR_DISTANCE)
        distance_dropdown_value = CURR_DISTANCE

    if (gender_query != ''
            and gender_query is not None
            and gender_query != 'All'):
        if gender_query == 'Male':
            all_results = all_results.filter(gender='М')
        else:
            all_results = all_results.filter(gender='Ж')
        gender_dropdown_value = gender_query
    if (city_query != ''
            and city_query is not None
            and city_query != 'All'):
        all_results = all_results.filter(city=CITIES[city_query])
        city_dropdown_value = city_query

    if year_query != '' and year_query is not None:
        all_results = all_results.filter(year=year_query)
        year_dropdown_value = year_query
    else:
        all_results = all_results.filter(year=CURR_YEAR)
        year_dropdown_value = CURR_YEAR
    month_visible = {}

    for month in MONTHS:
        val = month + '_result__exact'
        month_visible[month] = str(all_results
                                   .exclude(**{val: '0'})
                                   .count() > 0).lower()
    context = {'all_results': all_results,
               'gender_dropdown_value': gender_dropdown_value,
               'city_dropdown_value': city_dropdown_value,
               'year_dropdown_value': year_dropdown_value,
               'month_visible': month_visible,
               'distance_dropdown_value': distance_dropdown_value}
    return render(request, 'index.html', context)
