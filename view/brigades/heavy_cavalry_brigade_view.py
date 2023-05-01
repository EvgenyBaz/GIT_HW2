def h_cvlry_brigade_bttln_Lists(heavy_cvlr_brigade_number, presenter, HeavyCvlrBrgdCmndr, HeavyCvlrBrgdFirstBattalion,
                              HeavyCvlrBrgdSecondBattalion, HeavyCvlrBrgdThirdBattalion):
    # задаем возможны варианты имен командиров

    cmndrs_list = presenter.BrigadeCmndrsNamesList(heavy_cvlr_brigade_number)
    for cmndrName in cmndrs_list:
        HeavyCvlrBrgdCmndr.addItem(cmndrName)

    # задаем возможные варианты для первого батальона
    bttln_list = presenter.BrigadeBttlnList(0, heavy_cvlr_brigade_number)
    for bttlnName in bttln_list:
        HeavyCvlrBrgdFirstBattalion.addItem(bttlnName)
    # задаем возможные варианты для второго батальона
    bttln_list = presenter.BrigadeBttlnList(1, heavy_cvlr_brigade_number)
    for bttlnName in bttln_list:
        HeavyCvlrBrgdSecondBattalion.addItem(bttlnName)
    # задаем возможные варианты для третьего батальона
    bttln_list = presenter.BrigadeBttlnList(2, heavy_cvlr_brigade_number)
    for bttlnName in bttln_list:
        HeavyCvlrBrgdThirdBattalion.addItem(bttlnName)
