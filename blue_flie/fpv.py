list_of_builds = {
    "2in-100": {
        "url": "https://www.youtube.com/watch?v=MxG22nbBNvQ",
        "size_in": 2.0,
        "cost_dollar": 100.0,
        "marquee": "2-in-100-dollar",
    },
    "35in-160": {
        "url": "https://www.youtube.com/watch?v=aXrrg48auhU",
        "size_in": 3.5,
        "cost_dollar": 160.0,
        "weight_gr": 250.0,
        "marquee": "TBA",
    },
    "template": {
        "url": "TBA",
        "size_in": 0.0,
        "cost_dollar": 0.0,
        "weight_gr": 0.0,
        "marquee": "TBA",
    },
    "template": {
        "url": "TBA",
        "size_in": 0.0,
        "cost_dollar": 0.0,
        "weight_gr": 0.0,
        "marquee": "TBA",
    },
    "template": {
        "url": "TBA",
        "size_in": 0.0,
        "cost_dollar": 0.0,
        "weight_gr": 0.0,
        "marquee": "TBA",
    },
    "template": {
        "url": "TBA",
        "size_in": 0.0,
        "cost_dollar": 0.0,
        "weight_gr": 0.0,
        "marquee": "TBA",
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
            "size_in": "size (inches)",
            "cost_dollar": "cost ($",
            "weight_gr": "weight (g)",
            "comments": "",
        }[what]
    ]

    for build_name in list_of_builds:
        if build_name == "template":
            continue

        if what == "marquee":
            items += [""]
        elif what == "url":
            items += [""]
        elif what == "size_in":
            items += [""]
        elif what == "cost_dollar":
            items += [""]
        elif what == "weight_gr":
            items += [""]
        elif what == "comments":
            items += [""]
