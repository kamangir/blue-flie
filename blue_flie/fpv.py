list_of_builds = {
    "2in-100": {
        "url": "https://www.youtube.com/watch?v=MxG22nbBNvQ",
        "size_in": 2.0,
        "cost_dollar": 100.0,
    },
    "3_5in-160": {
        "url": "https://www.youtube.com/watch?v=aXrrg48auhU",
        "size_in": 3.5,
        "cost_dollar": 160.0,
        "weight_gr": 250.0,
    },
    "5in": {
        "url": "https://www.youtube.com/watch?v=XB6b0HrDGeA",
        "size_in": 5.0,
        "build_year": 2023,
        "weight_gr": 767.0,
        "comments": "Amazon links ⚠️",
    },
    "5in-2": {
        "url": "https://www.youtube.com/watch?v=zj90LK8XR68",
        "size_in": 5.0,
        "cost_dollar": 816.38,
        "weight_gr": 426,
        "build_year": 2024,
        "purchase_link": "https://www.aliexpress.com/item/1005005105185798.html",
    },
    "7-in": {
        "url": "https://www.youtube.com/watch?v=0jOUTYBneVo",
        "size_in": 7.0,
        "cost_dollar": 150.0,
        "build_year": 2024,
    },
    "9-in": {
        "url": "https://www.youtube.com/watch?v=o8_5ppHROJ4",
        "size_in": 9.0,
        "build_year": 2025,
    },
    "template": {
        "url": "TBA",
        "size_in": 0.0,
        "cost_dollar": 0.0,
        "weight_gr": 0.0,
    },
    "template": {
        "url": "TBA",
        "size_in": 0.0,
        "cost_dollar": 0.0,
        "weight_gr": 0.0,
    },
    "template": {
        "url": "TBA",
        "size_in": 0.0,
        "cost_dollar": 0.0,
        "weight_gr": 0.0,
    },
}

build_count = len(
    [build_name for build_name in list_of_builds if build_name != "template"]
)

columns = {
    "marquee": "",
    "url": "",
    "size_in": "size",
    "cost_dollar": "cost",
    "weight_gr": "weight",
    "build_year": "build",
    "comments": "",
    "purchase_link": "🛒",
}
items = list(columns.values())
for build_name in list_of_builds:
    build = list_of_builds[build_name]
    if build_name == "template":
        continue

    for what in columns.keys():
        if what == "marquee":
            items += [
                "[![image](https://github.com/kamangir/assets/blob/main/blue-flie/fpv/{}.png?raw=true)]({})".format(
                    build_name,
                    build["url"],
                )
            ]
        elif what == "url":
            items += [build["url"]]
        elif what == "size_in":
            items += ['{:.1f}"'.format(build["size_in"])]
        elif what == "cost_dollar":
            items += [
                (
                    "${:.1f}".format(build["cost_dollar"])
                    if "cost_dollar" in build
                    else "?"
                )
            ]
        elif what == "weight_gr":
            items += [
                (
                    "{:.1f} gr".format(build["weight_gr"])
                    if "weight_gr" in build
                    else "?"
                )
            ]
        elif what == "build_year":
            items += [str(build.get("build_year", ""))]
        elif what == "purchase_link":
            items += [
                (
                    "[🛒]({})".format(build["purchase_link"])
                    if "purchase_link" in build
                    else ""
                )
            ]
        elif what == "comments":
            items += [build.get("comments", "")]
