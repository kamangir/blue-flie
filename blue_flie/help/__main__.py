from blueness import module
from blue_options.help.functions import help_main

from blue_flie import NAME
from blue_flie.help.functions import help_functions

NAME = module.name(__file__, NAME)


help_main(NAME, help_functions)







