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
        
    def GeneratePacket(self, entity,email, kvpList):
        top = Element('OTCTrustContract')
        entity = SubElement(top, 'entity',{'Name':entity,'E-Mail':email})
		#definitions should be passed in as a list of key value pairs, allowing for more dynamic creation of packets
		for i in kvpList:
			for kvp in i:
				definition = SubElement(top, 'definiition',{'Name':kvp.key,'Type':kvp.value})
        
        
        print tostring(top)
