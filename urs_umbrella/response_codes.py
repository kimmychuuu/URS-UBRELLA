'''
API Response Codes
'''

class ResponseCodes:

    @staticmethod
    def get_message(response_code: str) -> str:
        # Response codes from API
        RESPONSE_CODES = {
            'URS-0101': 'AUTHENTICATION_FAILED',

            'URS-0201': 'PARAMETERS_MISSING',

            'URS-0301': 'USER_NOT_FOUND',
            'URS-0302': 'PENDING_TRANSACTION_FOUND',
            'URS-0303': 'PENDING_TRANSACTION_NOT_FOUND',
            'URS-0304': 'UMBRELLA_NOT_FOUND',
            
            'URS-0404': 'UNKNOWN ERROR'
        }

        if response_code in RESPONSE_CODES:
            return RESPONSE_CODES[response_code]
        else:
            return RESPONSE_CODES['URS-0404']
        

    
    @property
    def UNKNOWN_ERROR():
        UNKNOWN_ERROR = 'URS-0404 - UNKNOWN ERROR'
        return UNKNOWN_ERROR
