import pickle
import json

import re
import shapely.geometry


def get_location(lst):
    try:
        # lst.reverse()
        point = shapely.geometry.Point(lst)
        for i in location:
            polygon = shapely.geometry.Polygon(location[i]['geometries'][0]['coordinates'][0][0])
            if point.within(polygon):
                return i
    except:
        return None


if __name__ == "__main__":
    print(get_location([144.997, -37.8028]))
