import os

from blue_options.help.functions import get_help
from blue_objects import file, README

from blue_flie import NAME, VERSION, ICON, REPO_NAME
from blue_flie.help.functions import help_functions


items = README.Items(
    [
        {
            "name": "swarm simulation",
            "marquee": "https://github.com/kamangir/assets/raw/main/blue-plugin/marquee.png?raw=true",
            "description": "Simulating harm/cost for swarms of AI IEDs.",
            "url": "./blue_flie/sim/docs",
        },
        {
            "name": "blue-flie",
            "marquee": "https://www.bitcraze.io/images/documentation/overview/system_overview.jpg",
            "description": "[Crazyflie 2.1 Brushless](https://www.bitcraze.io/products/crazyflie-2-1-brushless/)",
            "url": "./blue_flie/docs",
        },
    ]
)


def build():
    return all(
        README.build(
            items=readme.get("items", []),
            path=os.path.join(file.path(__file__), readme["path"]),
            ICON=ICON,
            NAME=NAME,
            VERSION=VERSION,
            REPO_NAME=REPO_NAME,
            help_function=lambda tokens: get_help(
                tokens,
                help_functions,
                mono=True,
            ),
        )
        for readme in [
            {
                "items": items,
                "path": "..",
            },
            {
                "path": "docs",
            },
            {
                "path": "sim/docs",
            },
        ]
    )
