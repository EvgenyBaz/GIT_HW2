def grndr_brigade_bttln_Lists(grndr_brigade_number, presenter, GrndrBrgdCmndr, GrndrBrgdFirstBattalion,
                              GrndrBrgdSecondBattalion, GrndrBrgdThirdBattalion, GrndrBrgdFourthBattalion):
    # задаем возможны варианты имен командиров

    cmndrs_list = presenter.BrigadeCmndrsNamesList(grndr_brigade_number)
    for cmndrName in cmndrs_list:
        GrndrBrgdCmndr.addItem(cmndrName)

    # задаем возможные варианты для первого батальона
    bttln_list = presenter.BrigadeBttlnList(0, grndr_brigade_number)
    for bttlnName in bttln_list:
        GrndrBrgdFirstBattalion.addItem(bttlnName)
    # задаем возможные варианты для второго батальона
    bttln_list = presenter.BrigadeBttlnList(1, grndr_brigade_number)
    for bttlnName in bttln_list:
        GrndrBrgdSecondBattalion.addItem(bttlnName)
    # задаем возможные варианты для третьего батальона
    bttln_list = presenter.BrigadeBttlnList(2, grndr_brigade_number)
    for bttlnName in bttln_list:
        GrndrBrgdThirdBattalion.addItem(bttlnName)
    # задаем возможные варианты для четвертого батальона
    bttln_list = presenter.BrigadeBttlnList(3, grndr_brigade_number)
    for bttlnName in bttln_list:
        GrndrBrgdFourthBattalion.addItem(bttlnName)

