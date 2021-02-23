def get_params(priceMin=None, priceMax=None, areaMin=None,
                areaMax=None, newFlat=None, rgid=417899,
                roomsTotal=None, roomsTotal2=None, roomsTotal3=None,
                roomsTotal4=None, apartments=None, allNone=None,
                page=None):
    
#price params
    if priceMin == None:
        priceMin = ''
    else:
        priceMin = '&priceMin=' + str(priceMin)
    
    if priceMax == None:
        priceMax = ''
    else:
        priceMax = '&priceMax=' + str(priceMax)
#area params
    if areaMin == None:
        areaMin = ''
    else:
        areaMin = '&areaMin=' + str(areaMin)
    
    if areaMax == None:
        areaMax = ''
    else:
        areaMax = '&areaMax=' + str(areaMax)
#apartment type
    if newFlat == None:
        newFlat = ''
    else:
        newFlat = '&newFlat=' + str(newFlat).upper()
#rgid
    rgid = '&rgid=' + str(rgid)
#roomsTotal
    if roomsTotal == None:
        roomsTotal = ''
    else:
        roomsTotal = '&roomsTotal=' + str(roomsTotal).upper()
    
    if roomsTotal2 == None:
        roomsTotal2 = ''
    else:
        roomsTotal2 = '&roomsTotal=' + str(roomsTotal2).upper()

    if roomsTotal3 == None:
        roomsTotal3 = ''
    else:
        roomsTotal3 = '&roomsTotal=' + str(roomsTotal3).upper()

    if roomsTotal4 == None:
        roomsTotal4 = ''
    else:
        roomsTotal4 = '&roomsTotal=' + str(roomsTotal4).upper()
#apartments
    if apartments == None:
        apartments = ''
    else:
        apartments = '&apartments=' + str(apartments).upper()
#page
    if page == None:
        page = ''
    else:
        page = '&page=' + str(page)

#join params
    if allNone == None:
        params = 'isFastlink=true' + priceMin + priceMax + areaMin + areaMax + newFlat + rgid + roomsTotal \
                + roomsTotal2 + roomsTotal3 + roomsTotal4 + apartments + '&_pageType=search&_providers=seo&_' \
                + 'providers=queryId&_providers=forms&_providers=filters&_providers=filtersParams&_providers=awaps' \
                + '&_providers=direct&_providers=mapsPromo&_providers=newbuildingPromo&_providers=refinements&' \
                + '_providers=search&_providers=react-search-data&_providers=searchHistoryParams&_providers=searchParams' \
                + '&_providers=searchPresets&_providers=serpDirectPicType&_providers=showSurveyBanner&_providers=seo-data-offers-count' \
                + '&_providers=related-newbuildings&crc=u317c564d556bbadb8e2ed5ce115cec5f'
    elif allNone != None:
        params = 'isFastlink=true' + rgid + '&crc=u317c564d556bbadb8e2ed5ce115cec5f'

    return params

