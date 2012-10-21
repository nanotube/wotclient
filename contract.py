from xml.etree.ElementTree import Element, SubElement, Comment, tostring

class contract:    
    entityname = ""
    targetkeyfingerprint = ""
    rating = ""
    propagationrating = ""
    comment = ""
    validation = ""
    description = ""
    liability = ""
    
    def __init__(self, pEntityName, pTargetkeyfingerprint, pRating, pPropagationrating, pComment, pValidation, pDescription, pLiability ):
        entityname = pEntityName
        targetkeyfingerprint = pTargetkeyfingerprint
        rating = pRating
        propagationrating = pPropagationrating
        comment = pComment
        validation = pValidation
        description = pDescription
        liability = pLiability
        
    def GeneratePacket(self, entity,email, defname, deftype):
        top = Element('OTCTrustContract')
        entity = SubElement(top, 'entity',{'Name':entity,'E-Mail':email})
        definition = SubElement(top, 'definiition',{'Name':defname,'Type':deftype})
        
        print tostring(top)
