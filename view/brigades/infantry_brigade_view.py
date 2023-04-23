
def inf_brigade_bttln_Lists(brigade_number, presenter, brgdCmndr, brgdFirstBattalion, brgdSecondBattalion,
                          brgdThirdBattalion, brgdFourthBattalion, brgdAdditionalBattalion, brgdAdditionalJgrBattalion):
    # задаем возможны варианты имен командиров

    cmndrs_list = presenter.BrigadeCmndrsNamesList(brigade_number)
    for cmndrName in cmndrs_list:
        brgdCmndr.addItem(cmndrName)
    # задаем возможные варианты для первого батальона

    bttln_list = presenter.BrigadeBttlnList(0, brigade_number)

    for bttlnName in bttln_list:
        brgdFirstBattalion.addItem(bttlnName)
    # задаем возможные варианты для второго батальона
    bttln_list = presenter.BrigadeBttlnList(1, brigade_number)
    for bttlnName in bttln_list:
        brgdSecondBattalion.addItem(bttlnName)
    # задаем возможные варианты для третьего батальона
    bttln_list = presenter.BrigadeBttlnList(2, brigade_number)
    for bttlnName in bttln_list:
        brgdThirdBattalion.addItem(bttlnName)
    # задаем возможные варианты для четвертого батальона
    bttln_list = presenter.BrigadeBttlnList(3, brigade_number)
    for bttlnName in bttln_list:
        brgdFourthBattalion.addItem(bttlnName)
    # задаем возможные варианты для дополнительного батальона
    bttln_list = presenter.BrigadeBttlnList(4, brigade_number)
    for bttlnName in bttln_list:
        brgdAdditionalBattalion.addItem(bttlnName)
    # задаем возможные варианты для дополнительного батальона егерей
    bttln_list = presenter.BrigadeBttlnList(5, brigade_number)
    for bttlnName in bttln_list:
        brgdAdditionalJgrBattalion.addItem(bttlnName)



