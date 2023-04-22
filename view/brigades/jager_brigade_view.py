def jgr_brigade_bttln_Lists(jgr_brigade_number, presenter, JgrBrgdCmndr, JgrBrgdFirstBattalion,
                              JgrBrgdSecondBattalion, JgrBrgdThirdBattalion, JgrBrgdFourthBattalion,
                              JgrBrgdFifthBattalion, JgrBrgdSixthBattalion, JgrBrgdAdditional1Battalion,
                              JgrBrgdAdditional2Battalion):
    # задаем возможны варианты имен командиров

    cmndrs_list = presenter.BrigadeCmndrsNamesList(jgr_brigade_number)
    for cmndrName in cmndrs_list:
        JgrBrgdCmndr.addItem(cmndrName)

    # задаем возможные варианты для первого батальона
    bttln_list = presenter.BrigadeBttlnList(0, jgr_brigade_number)
    for bttlnName in bttln_list:
        JgrBrgdFirstBattalion.addItem(bttlnName)

    # задаем возможные варианты для второго батальона
    bttln_list = presenter.BrigadeBttlnList(1, jgr_brigade_number)
    for bttlnName in bttln_list:
        JgrBrgdSecondBattalion.addItem(bttlnName)
    # задаем возможные варианты для третьего батальона
    bttln_list = presenter.BrigadeBttlnList(2, jgr_brigade_number)
    for bttlnName in bttln_list:
        JgrBrgdThirdBattalion.addItem(bttlnName)
    # задаем возможные варианты для четвертого батальона
    bttln_list = presenter.BrigadeBttlnList(3, jgr_brigade_number)
    for bttlnName in bttln_list:
        JgrBrgdFourthBattalion.addItem(bttlnName)
    # задаем возможные варианты для пятого батальона
    bttln_list = presenter.BrigadeBttlnList(4, jgr_brigade_number)
    for bttlnName in bttln_list:
        JgrBrgdFifthBattalion.addItem(bttlnName)
    # задаем возможные варианты для шестого батальона
    bttln_list = presenter.BrigadeBttlnList(5, jgr_brigade_number)
    for bttlnName in bttln_list:
        JgrBrgdSixthBattalion.addItem(bttlnName)
    # задаем возможные варианты для дополнительного батальона
    bttln_list = presenter.BrigadeBttlnList(6, jgr_brigade_number)
    for bttlnName in bttln_list:
        JgrBrgdAdditional1Battalion.addItem(bttlnName)
    bttln_list = presenter.BrigadeBttlnList(7, jgr_brigade_number)
    for bttlnName in bttln_list:
        JgrBrgdAdditional2Battalion.addItem(bttlnName)