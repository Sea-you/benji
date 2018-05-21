import unittest

from . import DatabackendTestCase


class test_b2(DatabackendTestCase, unittest.TestCase):
    CONFIG = """
        configurationVersion: '1.0.0'
        logFile: /dev/stderr
        hashFunction: blake2b,digest_size=32
        dataBackend:
          type: b2
          b2:
             accountId: ********
             applicationKey: *******************************
             bucketName: backy2
             accountInfoFile: {testpath}/b2_account_info
             writeObjectAttempts: 1
             uploadAttempts: 5
                
          compression:
            - type: zstd
              materials:
                level: 1
              active: true
              
          encryption:
            - identifier: k1
              type: aes_256_gcm
              materials:
                masterKey: !!binary |
                  e/i1X4NsuT9k+FIVe2kd3vtHVkzZsbeYv35XQJeV8nA=
              active: true  
                
          consistencyCheckWrites: True
          simultaneousWrites: 5
          simultaneousReads: 5
          bandwidthRead: 0
          bandwidthWrite: 0
        """

if __name__ == '__main__':
    unittest.main()
