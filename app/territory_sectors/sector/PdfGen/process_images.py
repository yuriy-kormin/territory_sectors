# flake8: noqa: E501

import io
import os
import requests
from PIL import Image
from django.urls import reverse_lazy
from qr_code.qrcode.maker import make_qr_code_image
from qr_code.qrcode.utils import QRCodeOptions
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from .utils import get_xy



def generate_qr(request, sector):
    url = request.build_absolute_uri(
        reverse_lazy('uuid', kwargs={'pk': sector.uuid_id}))
    return make_qr_code_image(
        url, qr_code_options=QRCodeOptions(image_format="png", size=2,
                                           error_correction='L')
    )


def generate_map(sector):
    token = os.environ.get('MAPBOX_API_KEY')
    # https: // api.mapbox.com / styles / v1 / yuriykormin / clgyzsbgn00gs01pg4gmabbng.html?title = view & access_token = pk.eyJ1IjoieXVyaXlrb3JtaW4iLCJhIjoiY2xjdTZjMm1jMHJwZTNvbXg1cm1xMGh5ciJ9.uHPoJEdjly2KUEmc8YEOkw & zoomwheel = true & fresh = true  # 17.93/41.631875/41.609534
    base_url = "https://api.mapbox.com/styles/v1/yuriykormin/clgyzsbgn00gs01pg4gmabbng/static/"
    # url = f"{base_url}geojson(%7B%22type%22%3A%22FeatureCollection%22%2C%22features%22%3A%5B%7B%22type%22%3A%22Feature%22%2C%22properties%22%3A%7B%22marker-color%22%3A%22%23462eff%22%2C%22marker-size%22%3A%22medium%22%2C%22marker-symbol%22%3A%22bus%22%7D%2C%22geometry%22%3A%7B%22type%22%3A%22Point%22%2C%22coordinates%22%3A%5B-122.25993633270264,37.80988566878777%5D%7D%7D%2C%7B%22type%22%3A%22Feature%22%2C%22properties%22%3A%7B%22marker-color%22%3A%22%23e99401%22%2C%22marker-size%22%3A%22medium%22%2C%22marker-symbol%22%3A%22park%22%7D%2C%22geometry%22%3A%7B%22type%22%3A%22Point%22%2C%22coordinates%22%3A%5B-122.25916385650635,37.80629162635318%5D%7D%7D%2C%7B%22type%22%3A%22Feature%22%2C%22properties%22%3A%7B%22marker-color%22%3A%22%23d505ff%22%2C%22marker-size%22%3A%22medium%22%2C%22marker-symbol%22%3A%22music%22%7D%2C%22geometry%22%3A%7B%22type%22%3A%22Point%22%2C%22coordinates%22%3A%5B-122.25650310516359,37.8063933469406%5D%7D%7D%5D%7D)
    # /-122.256654,37.804077,13/1000x714?access_token={ACCESS_TOKEN}"
    # {
    #     "id": "text",
    #     "type": "symbol",
    #     "source": "circles",
    #     "source-layer": "streets",
    # }
    # https: // api.mapbox.com / styles / v1 / mapbox / streets - v11 / static / geojson(
    #     {"type": "FeatureCollection", "features": [{"type": "Feature",
    #                                                 "geometry": {
    #                                                     "type": "Point",
    #                                                     "coordinates": [
    #                                                         -122.413682,
    #                                                         37.775408]},
    #                                                 "properties": {
    #                                                     "name": "Golden Gate Park",
    #                                                     "category": "Park"}},
    #                                                {"type": "Feature",
    #                                                 "geometry": {
    #                                                     "type": "Point",
    #                                                     "coordinates": [
    #                                                         -122.404556,
    #                                                         37.768242]},
    #                                                 "properties": {
    #                                                     "name": "Crissy Field",
    #                                                     "category": "Park"}}]}) / auto / 400
    # x300?access_token = YOUR_MAPBOX_ACCESS_TOKEN & addlayer = {
    #                                                               "id": "text-layer",
    #                                                               "type": "symbol",
    #                                                               "source": "geojson",
    #                                                               "layout": {
    #                                                                   "text-field": [
    #                                                                       "get",
    #                                                                       "name"],
    #                                                                   "text-size": 16,
    #                                                                   "text-font": [
    #                                                                       "Open Sans Regular"]}} & layer = labels

    # https: // api.mapbox.com / styles / v1 / mapbox / streets - v11 / static / geojson(



    #!!!!! working example from chatgpt
    # https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/pin-s+000(-74.0060,40.7128),pin-s+000(151.2093,-33.8688),pin-s+000(-0.1278,51.5074)/auto/800x600?access_token=pk.eyJ1IjoieXVyaXlrb3JtaW4iLCJhIjoiY2xjdTZjMm1jMHJwZTNvbXg1cm1xMGh5ciJ9.uHPoJEdjly2KUEmc8YEOkw&marker=label:A|color:white|40.7128,-74.0060|sdjfnskdjfn dsfjnsdkfnj&marker=label:B|color:white|-33.8688,151.2093


    center = sector.get_center_coords()
    # gjson =
    # layer = '''
    #         {
    #             "id":"text-layer",
    #             "type":"symbol",
    #             "source":{
    #                 "type":"geojson",
    #                 "data":"geojson"
    #             }
    #             "source-layer":"",
    #             "layout":{"text-field":["get","text"]},
    #             "paint":{"text-color":"#000000"}
    #         }
    #         '''
    # layer = quote(layer.replace('\n', '').replace(' ', '').replace("$$$geojson$$$",gjson))

    url = f"{base_url}geojson({sector.get_mapbox_json()})/" \
          f"{center[0]},{center[1]},17.5/1000x714" \
          f"?access_token={token}"
          # f"&addlayer={layer}"
    # print(f'{url=}')
    return requests.get(url).content


def print_image(pdf, obj, request, sector):
    if obj not in ('qr', 'map'):
        raise IOError('unrecognized object')
    elif obj == 'qr':
        coordinates = get_xy(13, 10)
        image_bytes = generate_qr(request, sector)
        dimensions = 1.5*cm, 1.5*cm
    elif obj == 'map':
        image_bytes = generate_map(sector)
        coordinates = get_xy(0, 22)
        dimensions = A4[1] / 2, A4[0]/2 + cm
    pdf.drawInlineImage(
        Image.open(
            io.BytesIO(image_bytes)
        ),
        *coordinates,
        *dimensions
    )
