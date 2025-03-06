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
        "year": 2023,
        "weight_gr": 767.0,
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

items = (build_count + 1) * [""]
for what in ["marquee", "url", "size_in", "cost_dollar", "weight_gr", "comments"]:
    items += [
        {
            "marquee": "",
            "url": "",
            "size_in": "size",
            "cost_dollar": "cost",
            "weight_gr": "weight",
            "comments": "",
        }[what]
    ]

    for build_name in list_of_builds:
        if build_name == "template":
            continue

        if what == "marquee":
            items += [
                "[![image](https://github.com/kamangir/assets/blob/main/blue-flie/fpv/{}.png?raw=true)]({})".format(
                    build_name,
                    list_of_builds[build_name]["url"],
                )
            ]
        elif what == "url":
            items += [list_of_builds[build_name]["url"]]
        elif what == "size_in":
            items += ['{:.1f}"'.format(list_of_builds[build_name]["size_in"])]
        elif what == "cost_dollar":
            items += [
                (
                    "${:.1f}".format(list_of_builds[build_name]["cost_dollar"])
                    if "cost_dollar" in list_of_builds[build_name]
                    else "$?"
                )
            ]
        elif what == "weight_gr":
            items += [
                (
                    "{:.1f} gr".format(list_of_builds[build_name]["weight_gr"])
                    if "weight_gr" in list_of_builds[build_name]
                    else "?"
                )
            ]
        elif what == "comments":
            items += [""]
