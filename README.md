# XanglePython
`XanglePython` is Python code to use [XangleAPI](https://pro-api.xangle.io/).

## Prerequisites
You need to get an API key to use the XangleAPI. To get an API key, you need to do the following:

1. Fill in the form [Link](https://docs.google.com/forms/d/e/1FAIpQLSeysMAnTZmMdIpcuZSQ8nIzmTp0fj5MyNv2utvm5bQMSThIcA/viewform) for requesting API Key
2. After submitting the form, the review process might take serveral days
3. API Key will be issued and sent to the requested email address
4. Once you receive the API Key, attach the key in the header of each API request (X-XANGLE_API_KEY)

## How to use
Create an Xangle object.
```python
from xangle import Xangle

xangle = Xangle(api_key = "<YOUR_XANGLE_API_KEY>")
```

```json
{
  'data': {
    'projects': [
      {
        'name': 'EXPORT MOTORS PLATFORM',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '61244dff2aee1c486071a843',
        'status': 'active',
        'symbol': ' EMP'
      },
      {
        'name': 'QVING PLATFORM',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '608285c392266931a7ebbbe8',
        'status': 'active',
        'symbol': ' QVI '
      },
      {
        'name': 'sugarnetworks ',
        'onchain_ready': False,
        'onchain_type': None,
        'project_id': '61232f62e416678c99bb60f8',
        'status': 'active',
        'symbol': ' SNW'
      },
      {
        'name': '1337',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '604dd09dbb6c1bc6e2d2f162',
        'status': 'active',
        'symbol': '1337'
      },
      {
        'name': '1inch',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '5fe5a2e3025d18e1d625ea1b',
        'status': 'active',
        'symbol': '1INCH'
      },
      {
        'name': 'Triplant Dental Solution ',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '60655df85ff6c13271148306',
        'status': 'active',
        'symbol': '28VC'
      },
      {
        'name': '2Key',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '5d70ba174a708e8cd9077c7f',
        'status': 'active',
        'symbol': '2KEY'
      },
      {
        'name': '4ARTCoin',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '5ee185dcbb2b47ff7c0a3149',
        'status': 'active',
        'symbol': '4ART'
      },
      {
        'name': 'Alpha5',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '601b47a7dfde1943118b0336',
        'status': 'active',
        'symbol': 'A5T'
      },
      {
        'name': 'Arbitrage Analysis Beyond Commodity',
        'onchain_ready': False,
        'onchain_type': None,
        'project_id': '601b79f8a3049a62171fdc4e',
        'status': 'active',
        'symbol': 'AABC'
      },
      {
        'name': 'Acute Angle Cloud',
        'onchain_ready': True,
        'onchain_type': 'token',
        'project_id': '5de8bac850828f7b834288e3',
        'status': 'active',
        'symbol': 'AAC'
      },
      {
        'name': 'AAH',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '6055ab9450defbc9733e060e',
        'status': 'active',
        'symbol': 'AAH'
      },
      {
        'name': 'AMPnet APX Token',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '6047715e82a45cf890ca6973',
        'status': 'active',
        'symbol': 'AAPX'
      },
      {
        'name': 'Aave',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '5f7e6393cca364b463e4748a',
        'status': 'active',
        'symbol': 'AAVE'
      },
      {
        'name': 'ABBC Coin',
        'onchain_ready': False,
        'onchain_type': 'mainnet',
        'project_id': '5ce2697ebcd49728ab521902',
        'status': 'active',
        'symbol': 'ABBC'
      },
      {
        'name': 'Abel Network Token',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '603db84e78908242d8667049',
        'status': 'active',
        'symbol': 'ABEL'
      },
      {
        'name': 'ABEY',
        'onchain_ready': False,
        'onchain_type': None,
        'project_id': '6135561ca96cc37f89bb0452',
        'status': 'active',
        'symbol': 'ABEY'
      },
      {
        'name': 'Airbloc',
        'onchain_ready': True,
        'onchain_type': 'token',
        'project_id': '5cdbe3f619d48d574ef58d51',
        'status': 'active',
        'symbol': 'ABL'
      },
      {
        'name': 'ArcBlock',
        'onchain_ready': True,
        'onchain_type': 'token',
        'project_id': '5cadd0fc20e3f27b01a7fbd2',
        'status': 'active',
        'symbol': 'ABT'
      },
      {
        'name': 'Abyss Token',
        'onchain_ready': True,
        'onchain_type': 'token',
        'project_id': '5d5fa3a05965a519c0c3cd4a',
        'status': 'active',
        'symbol': 'ABYSS'
      },
      {
        'name': 'ACoconut',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '5fc439a78fa4707f0926e4a9',
        'status': 'active',
        'symbol': 'AC'
      },
      {
        'name': 'Acala Network',
        'onchain_ready': False,
        'onchain_type': None,
        'project_id': '5f48b25c7ba75eed6e478cf8',
        'status': 'active',
        'symbol': 'ACALA'
      },
      {
        'name': 'ACARZ',
        'onchain_ready': False,
        'onchain_type': None,
        'project_id': '607d2ba94c6dec27f488a083',
        'status': 'active',
        'symbol': 'ACARZ'
      },
      {
        'name': 'ACE Entertainment',
        'onchain_ready': False,
        'onchain_type': None,
        'project_id': '5dce4d66bc0f2de43fb68ad3',
        'status': 'active',
        'symbol': 'ACE'
      },
      {
        'name': 'ACENT',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '6063d2612932fa19a5ffadc8',
        'status': 'active',
        'symbol': 'ACE'
      },
      {
        'name': 'AceD',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '5ff5b46dda35811298ec9c37',
        'status': 'active',
        'symbol': 'AceD'
      },
      {
        'name': 'Alchemy Pay',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '5fd96ffb49284eaa794fb51b',
        'status': 'active',
        'symbol': 'ACH'
      },
      {
        'name': 'AC Milan Fan Token',
        'onchain_ready': False,
        'onchain_type': None,
        'project_id': '6035d37e9c1f4ea1328c2385',
        'status': 'active',
        'symbol': 'ACM'
      },
      {
        'name': 'Acorn Protocol',
        'onchain_ready': True,
        'onchain_type': 'token',
        'project_id': '5d9eeebb2ed0e2944763b33a',
        'status': 'active',
        'symbol': 'ACN'
      },
      {
        'name': 'Acreage',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '602ef17f98254546fe0ec337',
        'status': 'active',
        'symbol': 'ACR'
      },
      {
        'name': 'Achain',
        'onchain_ready': False,
        'onchain_type': None,
        'project_id': '5ce28557c899afcdae52199a',
        'status': 'active',
        'symbol': 'ACT'
      },
      {
        'name': 'Andre Cronje Index',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '5fd6489b22c3c6e8f52f0494',
        'status': 'active',
        'symbol': 'ACX'
      },
      {
        'name': 'ACDX Token',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '5fe1a1eaca4fb6febaeb05c2',
        'status': 'active',
        'symbol': 'ACXT'
      },
      {
        'name': 'Cardano',
        'onchain_ready': False,
        'onchain_type': 'mainnet',
        'project_id': '5ce25aed926c654a0e5cc19e',
        'status': 'active',
        'symbol': 'ADA'
      },
      {
        'name': 'ADD.xyz',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '6046f2cee9503f8f9ffe2fa8',
        'status': 'active',
        'symbol': 'ADD'
      },
      {
        'name': 'Akropolis Delphi',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '601dbff1668c189b8d877d1a',
        'status': 'active',
        'symbol': 'ADEL'
      },
      {
        'name': 'ADPlug',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '612fa6f7521ca5f20dca81d7',
        'status': 'active',
        'symbol': 'ADMON'
      },
      {
        'name': 'Adappter Token',
        'onchain_ready': True,
        'onchain_type': 'token',
        'project_id': '5fbc91814ea3c23b9f22c9bd',
        'status': 'active',
        'symbol': 'ADP'
      },
      {
        'name': 'adToken',
        'onchain_ready': True,
        'onchain_type': 'token',
        'project_id': '5de7118949efe67fd28b1b4c',
        'status': 'active',
        'symbol': 'ADT'
      },
      {
        'name': 'AdEx',
        'onchain_ready': True,
        'onchain_type': 'token',
        'project_id': '5d40fbb95d6fa3e7b641d867',
        'status': 'active',
        'symbol': 'ADX'
      },
      {
        'name': 'AdEx Loyalty',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '603a425ea5fe94bb29e5033e',
        'status': 'active',
        'symbol': 'ADXLOYALTY'
      },
      {
        'name': 'Aeternity',
        'onchain_ready': False,
        'onchain_type': 'mainnet',
        'project_id': '5ca5849720e3f224a3d09894',
        'status': 'active',
        'symbol': 'AE'
      },
      {
        'name': 'AEN Smart Token',
        'onchain_ready': True,
        'onchain_type': 'token',
        'project_id': '5dcb8881058493bcfa436cf8',
        'status': 'active',
        'symbol': 'AEN'
      },
      {
        'name': 'Aergo',
        'onchain_ready': False,
        'onchain_type': 'mainnet',
        'project_id': '5c6e562c20e3f23f0837cf53',
        'status': 'active',
        'symbol': 'AERGO'
      },
      {
        'name': 'Algoeuro',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '6048ed0e26bcd1ab679526f9',
        'status': 'active',
        'symbol': 'AEUR'
      },
      {
        'name': 'AfroDex Labs Token',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '5fdac981a54052d2aea929fb',
        'status': 'active',
        'symbol': 'AFDLT'
      },
      {
        'name': 'AGA Token',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '5ff3115ab620907685c09a6b',
        'status': 'active',
        'symbol': 'AGA'
      },
      {
        'name': 'AGA Rewards',
        'onchain_ready': False,
        'onchain_type': 'token',
        'project_id': '6042558edd43ff2ac12a5024',
        'status': 'active',
        'symbol': 'AGAr'
      },
      {
        'name': 'Agenor',
        'onchain_ready': False,
        'onchain_type': None,
        'project_id': '60a624fa0f1adf43ec0b6fa7',
        'status': 'active',
        'symbol': 'AGE'
      },
      {
        'name': 'SingularityNET',
        'onchain_ready': True,
        'onchain_type': 'token',
        'project_id': '5cadd0dc20e3f27b01a7fbc6',
        'status': 'active',
        'symbol': 'AGI'
      }
    ]
  },
  'status': {
    'credit': 1,
    'current_credit': 1999982,
    'error_code': 0,
    'error_message': None,
    'timestamp': '2021-11-09T00:58:19.934139'
  }
}
```
