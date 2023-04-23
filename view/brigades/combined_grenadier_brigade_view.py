def comb_grndr_brigade_bttln_Lists(comb_grndr_brigade_number, presenter, CombGrndrBrgdCmndr, CombGrndrBrgdFirstBattalion,
                              CombGrndrBrgdSecondBattalion, CombGrndrBrgdThirdBattalion, CombGrndrBrgdFourthBattalion,
                              CombGrndrBrgdFifthBattalion, CombGrndrBrgdSixthBattalion, CombGrndrBrgdSeventhBattalion):
    # задаем возможны варианты имен командиров

    cmndrs_list = presenter.BrigadeCmndrsNamesList(comb_grndr_brigade_number)
    for cmndrName in cmndrs_list:
        CombGrndrBrgdCmndr.addItem(cmndrName)

    # задаем возможные варианты для первого батальона
    bttln_list = presenter.BrigadeBttlnList(0, comb_grndr_brigade_number)
    for bttlnName in bttln_list:
        CombGrndrBrgdFirstBattalion.addItem(bttlnName)

    # задаем возможные варианты для второго батальона
    bttln_list = presenter.BrigadeBttlnList(1, comb_grndr_brigade_number)
    for bttlnName in bttln_list:
        CombGrndrBrgdSecondBattalion.addItem(bttlnName)
    # задаем возможные варианты для третьего батальона
    bttln_list = presenter.BrigadeBttlnList(2, comb_grndr_brigade_number)
    for bttlnName in bttln_list:
        CombGrndrBrgdThirdBattalion.addItem(bttlnName)
    # задаем возможные варианты для четвертого батальона
    bttln_list = presenter.BrigadeBttlnList(3, comb_grndr_brigade_number)
    for bttlnName in bttln_list:
        CombGrndrBrgdFourthBattalion.addItem(bttlnName)
    # задаем возможные варианты для пятого батальона
    bttln_list = presenter.BrigadeBttlnList(4, comb_grndr_brigade_number)
    for bttlnName in bttln_list:
        CombGrndrBrgdFifthBattalion.addItem(bttlnName)
    # задаем возможные варианты для шестого батальона
    bttln_list = presenter.BrigadeBttlnList(5, comb_grndr_brigade_number)
    for bttlnName in bttln_list:
        CombGrndrBrgdSixthBattalion.addItem(bttlnName)
    # задаем возможные варианты для шестого батальона
    bttln_list = presenter.BrigadeBttlnList(6, comb_grndr_brigade_number)
    for bttlnName in bttln_list:
        CombGrndrBrgdSeventhBattalion.addItem(bttlnName)
