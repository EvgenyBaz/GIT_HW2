def l_cvlry_brigade_bttln_Lists(light_cvlr_brigade_number, presenter, LightCvlrBrgdCmndr, LightCvlrBrgdFirstBattalion,
                              LightCvlrBrgdSecondBattalion, LightCvlrBrgdThirdBattalion):
    # задаем возможны варианты имен командиров

    cmndrs_list = presenter.BrigadeCmndrsNamesList(light_cvlr_brigade_number)
    for cmndrName in cmndrs_list:
        LightCvlrBrgdCmndr.addItem(cmndrName)

    # задаем возможные варианты для первого батальона
    bttln_list = presenter.BrigadeBttlnList(0, light_cvlr_brigade_number)
    for bttlnName in bttln_list:
        LightCvlrBrgdFirstBattalion.addItem(bttlnName)
    # задаем возможные варианты для второго батальона
    bttln_list = presenter.BrigadeBttlnList(1, light_cvlr_brigade_number)
    for bttlnName in bttln_list:
        LightCvlrBrgdSecondBattalion.addItem(bttlnName)
    # задаем возможные варианты для третьего батальона
    bttln_list = presenter.BrigadeBttlnList(2, light_cvlr_brigade_number)
    for bttlnName in bttln_list:
        LightCvlrBrgdThirdBattalion.addItem(bttlnName)
