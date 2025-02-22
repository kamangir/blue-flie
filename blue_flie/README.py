import os

from blue_objects import file, README

from blue_flie import NAME, VERSION, ICON, REPO_NAME


items = README.Items(
    [
        {
            "name": "blue-flie",
            "marquee": "https://www.bitcraze.io/images/documentation/overview/system_overview.jpg",
            "description": "[Crazyflie 2.1 Brushless](https://www.bitcraze.io/products/crazyflie-2-1-brushless/)",
        },
    ]
)


def build():
    return README.build(
        items=items,
        path=os.path.join(file.path(__file__), ".."),
        ICON=ICON,
        NAME=NAME,
        VERSION=VERSION,
        REPO_NAME=REPO_NAME,
    )
