
from enum import Enum, unique
import folium
import pandas

GOOGLE_MAPS_QUERY = "https://www.google.com/maps?ll="


@unique
class OfficeType(Enum):
    MAJOR = "major"
    MINOR = "minor"


def get_icon_style(office_area, office_type: OfficeType):
    if office_area == "Tokyo":
        color = "darkred"
    elif office_area == "Yokohama":
        color = "darkblue"
    else:
        color = "gray"

    # https://fontawesome.com/icons?d=gallery
    if office_type is OfficeType.MAJOR:
        icon = "star"
    elif office_type is OfficeType.MINOR:
        icon = "question"

    return {
        "color"      : color,
        "icon_color" : "white",
        "icon"       : icon,
        "prefix"      : "fa"     # font-awesome
    }


def main():
    offices_map = folium.Map(
        tiles="OpenStreetMap",
        location=(35.652832, 139.839478),  # Tokyo
        min_zoom=5,
        max_zoom=18,
        zoom_start=10
    )

    major_offices = folium.FeatureGroup(name="Major Offices")
    major_offices_data = None
    with open("major_offices.csv", "r", encoding="utf-8") as offices_csv:
        major_offices_data = pandas.read_csv(offices_csv)
    for row in major_offices_data.itertuples(name="Locations"):
        popup_html = """
            <h4>{}</h4><br/>
            <b>Address</b><br/>{}<br/>
            <a href=\"{}{},{}\">Google Maps</a>
        """.format(
            row.NAME,
            row.ADDRESS,
            GOOGLE_MAPS_QUERY, row.LAT, row.LONG)
        popup = folium.Popup(html=popup_html, max_width=350)
        icon_style = get_icon_style(row.AREA, OfficeType.MAJOR)
        icon = folium.Icon(**icon_style)
        marker = folium.Marker(
            (float(row.LAT), float(row.LONG)),
            popup=popup,
            tooltip=folium.Tooltip(row.NAME),
            icon=icon
        )
        major_offices.add_child(marker)
    offices_map.add_child(major_offices)

    minor_offices = folium.FeatureGroup(name="Minor Offices")
    minor_offices_data = None
    with open("minor_offices.csv", "r", encoding="utf-8") as offices_csv:
        minor_offices_data = pandas.read_csv(offices_csv)
    for row in minor_offices_data.itertuples(name="Locations"):
        popup_html = """
            <h4>{}</h4><br/>
            <b>Address</b><br/>{}<br/>
            <a href=\"{}{},{}\">Google Maps</a>
        """.format(
            row.NAME,
            row.ADDRESS,
            GOOGLE_MAPS_QUERY, row.LAT, row.LONG)
        popup = folium.Popup(html=popup_html, max_width=350)
        icon_style = get_icon_style(row.AREA, OfficeType.MINOR)
        icon = folium.Icon(**icon_style)
        marker = folium.Marker(
            (float(row.LAT), float(row.LONG)),
            popup=popup,
            tooltip=folium.Tooltip(row.NAME),
            icon=icon
        )
        minor_offices.add_child(marker)
    offices_map.add_child(minor_offices)

    offices_map.add_child(folium.LayerControl(collapsed=False))
    offices_map.save("offices.html")


main()
