def build_collector_url(webmap=None, portal_url=None, url_type="Web", referenceContext=None, center=None, search=None, featureSourceURL=None, featureAttributes=None, callback=None, callbackPrompt=None):
        if url_type == "Web":
            url = "https://collector.arcgis.app"
        else:
            url = "arcgis-collector://"
        item_id = webmap
        params = []
        if webmap is not None:
            if isinstance(webmap, arcgis.mapping.WebMap):
                item_id = webmap.item.id
            elif isinstance(webmap, arcgis.gis.Item):
                item_id = webmap.id
            params.append("itemID=" + item_id)
        if portal_url:
            params.append("portalURL="+portal_url)

        params.append("referenceContext="+referenceContext)
        if referenceContext == "open":
            pass
        elif referenceContext == "center" and item_id:
            if center is None:
                raise ValueError("Invalid parameters -- Must specify a center parameter if reference context = center")
            else:
                params.append("center="+center)
        elif referenceContext == "search" and item_id:
            if search is None:
                raise ValueError("Invalid parameters -- Must specify a search parameter if reference context = search")
            else:
                params.append("search="+search)
        elif referenceContext == "addFeature" and item_id:
            if featureSourceURL is None:
                raise ValueError("Invalid parameters -- Must specify a featureSourceURL parameter if reference context = addFeature")
            else:
                params.append("featureSourceURL="+featureSourceURL)
            if featureAttributes is not None:
                params.append("featureAttributes="+featureAttributes)
            if callback is not None:
                params.append("callback="+callback)
            if callbackPrompt is not None:
                params.append("callbackPrompt="+callbackPrompt)
        else:
            raise ValueError("Invalid parameters -- Must specify a reference context (addFeature, center, open, search)")


        if params:
            url += "?" + "&".join(params)
        return url
