
def brigade_bttln_Lists(brigade_number, presenter, brgdCmndr, brgdBattalionsList):
    # задаем возможны варианты имен командиров

    cmndrs_list = presenter.BrigadeCmndrsNamesList(brigade_number)
    for cmndrName in cmndrs_list:
        brgdCmndr.addItem(cmndrName)
    # задаем возможные варианты для батальона

    for i in range (0, len(brgdBattalionsList)):

        bttln_list = presenter.BrigadeBttlnList(i, brigade_number)
        for bttlnName in bttln_list:
            brgdBattalionsList[i].addItem(bttlnName)




