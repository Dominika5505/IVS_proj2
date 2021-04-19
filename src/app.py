# ======== Copyright (c) 2021, Vepro-knedlo-zelo s bryndzou, All rights reserved. ============ #
#
#  $Purpose:         Calculator - math library
#  
#  $University:      Brno University of Technology
#  $Faculty:         Faculty of Information Technology
#  $Programme:       Information Technology (Bachelor)
#  $Course:          Practical Aspects of Software Design (IVS)
#  $Academic year:   2020/2021 
#
#  $Authors:         Dominika Sedilekova    <xsedil00@stud.fit.vutbr.cz>  
#
# ======== Copyright (c) 2021, Vepro-knedlo-zelo s bryndzou, All rights reserved. ============ #

## 
#  @file app.py
# 
#  @author Dominika Sedilekova
#
#  @brief Start of the application
#

from gui import GUI

## starts gui of application
gui = GUI()
## creates app loop (app running)
gui.root.mainloop()