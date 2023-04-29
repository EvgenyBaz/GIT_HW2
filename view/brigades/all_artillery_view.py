def artillery_battery_Lists(art_battery_number, presenter, artLightBattery1, artLightBattery2, artLightBattery3,
                            artLightBattery4, artLightBattery5, artLightBattery6, artHeavyBattery1, artHeavyBattery2,
                            artHeavyBattery3, artHeavyBattery4, artUnicornBattery1, artUnicornBattery2,
                            artUnicornBattery3, artUnicornBattery4, artUnicornBattery5, artUnicornBattery6,
                            artHorseBattery1, artHorseBattery2, artHorseBattery3):
    # # задаем возможны варианты имен командиров
    #
    # cmndrs_list = presenter.BrigadeCmndrsNamesList(jgr_brigade_number)
    # for cmndrName in cmndrs_list:
    #     JgrBrgdCmndr.addItem(cmndrName)

    # задаем возможные варианты для первой легкой батареи
    bttln_list = presenter.BrigadeBttlnList(0, art_battery_number)
    for bttlnName in bttln_list:
        artLightBattery1.addItem(bttlnName)
    # задаем возможные варианты для второй легкой батареи
    bttln_list = presenter.BrigadeBttlnList(1, art_battery_number)
    for bttlnName in bttln_list:
        artLightBattery2.addItem(bttlnName)
    # задаем возможные варианты для третьей легкой батареи
    bttln_list = presenter.BrigadeBttlnList(2, art_battery_number)
    for bttlnName in bttln_list:
        artLightBattery3.addItem(bttlnName)
    # задаем возможные варианты для четвертой легкой батареи
    bttln_list = presenter.BrigadeBttlnList(3, art_battery_number)
    for bttlnName in bttln_list:
        artLightBattery4.addItem(bttlnName)
    # задаем возможные варианты для пятой легкой батареи
    bttln_list = presenter.BrigadeBttlnList(4, art_battery_number)
    for bttlnName in bttln_list:
        artLightBattery5.addItem(bttlnName)
    # задаем возможные варианты для шестой легкой батареи
    bttln_list = presenter.BrigadeBttlnList(5, art_battery_number)
    for bttlnName in bttln_list:
        artLightBattery6.addItem(bttlnName)
    # задаем возможные варианты для первой тяжелой батареи
    bttln_list = presenter.BrigadeBttlnList(6, art_battery_number)
    for bttlnName in bttln_list:
        artHeavyBattery1.addItem(bttlnName)
    # задаем возможные варианты для второй тяжелой батареи
    bttln_list = presenter.BrigadeBttlnList(7, art_battery_number)
    for bttlnName in bttln_list:
        artHeavyBattery2.addItem(bttlnName)
    # задаем возможные варианты для третьей тяжелой батареи
    bttln_list = presenter.BrigadeBttlnList(8, art_battery_number)
    for bttlnName in bttln_list:
        artHeavyBattery3.addItem(bttlnName)
    # задаем возможные варианты для четвертой тяжелой батареи
    bttln_list = presenter.BrigadeBttlnList(9, art_battery_number)
    for bttlnName in bttln_list:
        artHeavyBattery4.addItem(bttlnName)
    # задаем возможные варианты для первой батареи единорогов
    bttln_list = presenter.BrigadeBttlnList(10, art_battery_number)
    for bttlnName in bttln_list:
        artUnicornBattery1.addItem(bttlnName)
    # задаем возможные варианты для второй батареи единорогов
    bttln_list = presenter.BrigadeBttlnList(11, art_battery_number)
    for bttlnName in bttln_list:
        artUnicornBattery2.addItem(bttlnName)
    # задаем возможные варианты для третьей батареи единорогов
    bttln_list = presenter.BrigadeBttlnList(12, art_battery_number)
    for bttlnName in bttln_list:
        artUnicornBattery3.addItem(bttlnName)
    # задаем возможные варианты для четверой батареи единорогов
    bttln_list = presenter.BrigadeBttlnList(13, art_battery_number)
    for bttlnName in bttln_list:
        artUnicornBattery4.addItem(bttlnName)
    # задаем возможные варианты для пятой батареи единорогов
    bttln_list = presenter.BrigadeBttlnList(14, art_battery_number)
    for bttlnName in bttln_list:
        artUnicornBattery5.addItem(bttlnName)
    # задаем возможные варианты для шестой батареи единорогов
    bttln_list = presenter.BrigadeBttlnList(15, art_battery_number)
    for bttlnName in bttln_list:
        artUnicornBattery6.addItem(bttlnName)
    # задаем возможные варианты для первой конной батареи
    bttln_list = presenter.BrigadeBttlnList(16, art_battery_number)
    for bttlnName in bttln_list:
        artHorseBattery1.addItem(bttlnName)
    # задаем возможные варианты для второй конной батареи
    bttln_list = presenter.BrigadeBttlnList(17, art_battery_number)
    for bttlnName in bttln_list:
        artHorseBattery2.addItem(bttlnName)
    # задаем возможные варианты для третьей конной батареи
    bttln_list = presenter.BrigadeBttlnList(18, art_battery_number)
    for bttlnName in bttln_list:
        artHorseBattery3.addItem(bttlnName)