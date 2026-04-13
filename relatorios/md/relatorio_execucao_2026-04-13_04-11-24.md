# Relatório de Testes de Criptografia

**Data da Execução:** 13/04/2026 04:11:24

## 1. Tabela de Desempenho Geral

| Arquivo | Alg | Modo | Tam (MB) | T. Cifrar (s) | T. Decifrar (s) | Throughput Cif. (MB/s) | Throughput Dec. (MB/s) | Entropia | Padrões |
|---------|-----|------|----------|---------------|-----------------|------------------------|------------------------|----------|---------|
| csv_categorico_100KB.csv | AES-128 | ECB | 0.0977 | 0.0008 | 0.0006 | 115.9223 | 158.3240 | 7.9976 | ✅ Não |
| csv_categorico_100KB.csv | AES-128 | CBC | 0.0977 | 0.0013 | 0.0026 | 77.4189 | 37.3127 | 7.9982 | ✅ Não |
| csv_categorico_100KB.csv | AES-128 | CFB | 0.0977 | 0.0026 | 0.0025 | 37.5783 | 39.4784 | 7.9981 | ✅ Não |
| csv_categorico_100KB.csv | AES-128 | OFB | 0.0977 | 0.0011 | 0.0010 | 91.1661 | 98.2513 | 7.9982 | ✅ Não |
| csv_categorico_100KB.csv | AES-128 | CTR | 0.0977 | 0.0009 | 0.0006 | 114.6119 | 152.4944 | 7.9983 | ✅ Não |
| csv_categorico_100KB.csv | AES-256 | ECB | 0.0977 | 0.0008 | 0.0008 | 120.2054 | 117.6234 | 7.9974 | ✅ Não |
| csv_categorico_100KB.csv | AES-256 | CBC | 0.0977 | 0.0010 | 0.0010 | 102.6875 | 97.3037 | 7.9983 | ✅ Não |
| csv_categorico_100KB.csv | AES-256 | CFB | 0.0977 | 0.0030 | 0.0026 | 32.6966 | 37.9045 | 7.9983 | ✅ Não |
| csv_categorico_100KB.csv | AES-256 | OFB | 0.0977 | 0.0008 | 0.0007 | 116.5690 | 131.6745 | 7.9983 | ✅ Não |
| csv_categorico_100KB.csv | AES-256 | CTR | 0.0977 | 0.0010 | 0.0010 | 102.6515 | 102.6335 | 7.9983 | ✅ Não |
| csv_categorico_100KB.csv | DES | ECB | 0.0977 | 0.0018 | 0.0016 | 53.1272 | 59.4571 | 7.9491 | ✅ Não |
| csv_categorico_100KB.csv | DES | CBC | 0.0977 | 0.0026 | 0.0019 | 37.4591 | 52.4994 | 7.9981 | ✅ Não |
| csv_categorico_100KB.csv | DES | CFB | 0.0977 | 0.0096 | 0.0087 | 10.2244 | 11.2610 | 7.9983 | ✅ Não |
| csv_categorico_100KB.csv | DES | OFB | 0.0977 | 0.0021 | 0.0026 | 45.4667 | 38.1684 | 7.9984 | ✅ Não |
| csv_categorico_100KB.csv | DES | CTR | 0.0977 | 0.0024 | 0.0022 | 41.1985 | 43.4700 | 7.9983 | ✅ Não |
| csv_categorico_100KB.csv | 3DES | ECB | 0.0977 | 0.0040 | 0.0037 | 24.3536 | 26.3539 | 7.9459 | ✅ Não |
| csv_categorico_100KB.csv | 3DES | CBC | 0.0977 | 0.0046 | 0.0038 | 21.2913 | 25.7506 | 7.9982 | ✅ Não |
| csv_categorico_100KB.csv | 3DES | CFB | 0.0977 | 0.0308 | 0.0367 | 3.1663 | 2.6620 | 7.9983 | ✅ Não |
| csv_categorico_100KB.csv | 3DES | OFB | 0.0977 | 0.0069 | 0.0037 | 14.1013 | 26.3770 | 7.9980 | ✅ Não |
| csv_categorico_100KB.csv | 3DES | CTR | 0.0977 | 0.0042 | 0.0037 | 23.0238 | 26.1734 | 7.9981 | ✅ Não |
| csv_categorico_100KB.csv | RSA-1024 | ECB | 0.0977 | 0.2119 | 0.8886 | 0.4609 | 0.1099 | 7.9987 | ✅ Não |
| csv_categorico_100KB.csv | RSA-1024 | CBC | 0.0977 | 0.2172 | 0.8812 | 0.4497 | 0.1108 | 7.9990 | ✅ Não |
| csv_categorico_100KB.csv | RSA-1024 | CTR | 0.0977 | 0.2763 | 0.2651 | 0.3534 | 0.3683 | 7.9984 | ✅ Não |
| csv_categorico_100KB.csv | RSA-2048 | ECB | 0.0977 | 0.6238 | 1.5138 | 0.1566 | 0.0645 | 7.9986 | ✅ Não |
| csv_categorico_100KB.csv | RSA-2048 | CBC | 0.0977 | 0.2512 | 1.4413 | 0.3888 | 0.0678 | 7.9984 | ✅ Não |
| csv_categorico_100KB.csv | RSA-2048 | CTR | 0.0977 | 0.2740 | 0.2860 | 0.3565 | 0.3414 | 7.9982 | ✅ Não |
| csv_categorico_100KB.csv | RSA-4096 | ECB | 0.0977 | 0.3687 | 3.6768 | 0.2648 | 0.0266 | 7.9986 | ✅ Não |
| csv_categorico_100KB.csv | RSA-4096 | CBC | 0.0977 | 0.3838 | 3.6725 | 0.2545 | 0.0266 | 7.9984 | ✅ Não |
| csv_categorico_100KB.csv | RSA-4096 | CTR | 0.0977 | 0.4446 | 0.3913 | 0.2196 | 0.2496 | 7.9982 | ✅ Não |
| csv_categorico_10KB.csv | AES-128 | ECB | 0.0098 | 0.0007 | 0.0022 | 14.8357 | 4.4508 | 7.9800 | ✅ Não |
| csv_categorico_10KB.csv | AES-128 | CBC | 0.0098 | 0.0006 | 0.0007 | 15.4958 | 13.2789 | 7.9825 | ✅ Não |
| csv_categorico_10KB.csv | AES-128 | CFB | 0.0098 | 0.0009 | 0.0010 | 10.3893 | 9.8374 | 7.9778 | ✅ Não |
| csv_categorico_10KB.csv | AES-128 | OFB | 0.0098 | 0.0007 | 0.0006 | 13.7215 | 16.2051 | 7.9811 | ✅ Não |
| csv_categorico_10KB.csv | AES-128 | CTR | 0.0098 | 0.0008 | 0.0007 | 12.2734 | 14.3207 | 7.9826 | ✅ Não |
| csv_categorico_10KB.csv | AES-256 | ECB | 0.0098 | 0.0006 | 0.0007 | 15.4217 | 14.0336 | 7.9817 | ✅ Não |
| csv_categorico_10KB.csv | AES-256 | CBC | 0.0098 | 0.0007 | 0.0008 | 13.3686 | 12.7031 | 7.9801 | ✅ Não |
| csv_categorico_10KB.csv | AES-256 | CFB | 0.0098 | 0.0010 | 0.0010 | 9.7568 | 9.7766 | 7.9812 | ✅ Não |
| csv_categorico_10KB.csv | AES-256 | OFB | 0.0098 | 0.0007 | 0.0006 | 13.9767 | 15.6509 | 7.9812 | ✅ Não |
| csv_categorico_10KB.csv | AES-256 | CTR | 0.0098 | 0.0009 | 0.0006 | 10.7220 | 15.6803 | 7.9785 | ✅ Não |
| csv_categorico_10KB.csv | DES | ECB | 0.0098 | 0.0007 | 0.0007 | 13.6871 | 13.7866 | 7.9292 | ✅ Não |
| csv_categorico_10KB.csv | DES | CBC | 0.0098 | 0.0009 | 0.0009 | 11.1428 | 11.3102 | 7.9833 | ✅ Não |
| csv_categorico_10KB.csv | DES | CFB | 0.0098 | 0.0016 | 0.0022 | 6.2772 | 4.3566 | 7.9841 | ✅ Não |
| csv_categorico_10KB.csv | DES | OFB | 0.0098 | 0.0012 | 0.0008 | 7.8395 | 11.8299 | 7.9826 | ✅ Não |
| csv_categorico_10KB.csv | DES | CTR | 0.0098 | 0.0008 | 0.0008 | 11.8673 | 12.9801 | 7.9806 | ✅ Não |
| csv_categorico_10KB.csv | 3DES | ECB | 0.0098 | 0.0012 | 0.0014 | 8.3014 | 6.7604 | 7.9279 | ✅ Não |
| csv_categorico_10KB.csv | 3DES | CBC | 0.0098 | 0.0012 | 0.0013 | 8.2793 | 7.3956 | 7.9822 | ✅ Não |
| csv_categorico_10KB.csv | 3DES | CFB | 0.0098 | 0.0039 | 0.0032 | 2.5336 | 3.0146 | 7.9806 | ✅ Não |
| csv_categorico_10KB.csv | 3DES | OFB | 0.0098 | 0.0010 | 0.0012 | 9.3148 | 8.3592 | 7.9801 | ✅ Não |
| csv_categorico_10KB.csv | 3DES | CTR | 0.0098 | 0.0012 | 0.0011 | 7.8962 | 9.2057 | 7.9822 | ✅ Não |
| csv_categorico_10KB.csv | RSA-1024 | ECB | 0.0098 | 0.0217 | 0.1155 | 0.4509 | 0.0846 | 7.9888 | ✅ Não |
| csv_categorico_10KB.csv | RSA-1024 | CBC | 0.0098 | 0.0267 | 0.0942 | 0.3651 | 0.1037 | 7.9886 | ✅ Não |
| csv_categorico_10KB.csv | RSA-1024 | CTR | 0.0098 | 0.0225 | 0.0230 | 0.4347 | 0.4255 | 7.9800 | ✅ Não |
| csv_categorico_10KB.csv | RSA-2048 | ECB | 0.0098 | 0.0294 | 0.1536 | 0.3320 | 0.0636 | 7.9863 | ✅ Não |
| csv_categorico_10KB.csv | RSA-2048 | CBC | 0.0098 | 0.0256 | 0.1469 | 0.3821 | 0.0665 | 7.9840 | ✅ Não |
| csv_categorico_10KB.csv | RSA-2048 | CTR | 0.0098 | 0.0254 | 0.0261 | 0.3848 | 0.3747 | 7.9824 | ✅ Não |
| csv_categorico_10KB.csv | RSA-4096 | ECB | 0.0098 | 0.0402 | 0.3584 | 0.2428 | 0.0272 | 7.9862 | ✅ Não |
| csv_categorico_10KB.csv | RSA-4096 | CBC | 0.0098 | 0.0394 | 0.3732 | 0.2477 | 0.0262 | 7.9856 | ✅ Não |
| csv_categorico_10KB.csv | RSA-4096 | CTR | 0.0098 | 0.0408 | 0.0427 | 0.2391 | 0.2289 | 7.9851 | ✅ Não |
| csv_categorico_1KB.csv | AES-128 | ECB | 0.0010 | 0.0005 | 0.0007 | 1.9581 | 1.3946 | 7.8018 | ✅ Não |
| csv_categorico_1KB.csv | AES-128 | CBC | 0.0010 | 0.0006 | 0.0006 | 1.6264 | 1.6285 | 7.8059 | ✅ Não |
| csv_categorico_1KB.csv | AES-128 | CFB | 0.0010 | 0.0006 | 0.0006 | 1.6277 | 1.6253 | 7.8310 | ✅ Não |
| csv_categorico_1KB.csv | AES-128 | OFB | 0.0010 | 0.0007 | 0.0006 | 1.3763 | 1.6301 | 7.8251 | ✅ Não |
| csv_categorico_1KB.csv | AES-128 | CTR | 0.0010 | 0.0007 | 0.0006 | 1.3952 | 1.6273 | 7.7989 | ✅ Não |
| csv_categorico_1KB.csv | AES-256 | ECB | 0.0010 | 0.0006 | 0.0005 | 1.6280 | 1.9489 | 7.7998 | ✅ Não |
| csv_categorico_1KB.csv | AES-256 | CBC | 0.0010 | 0.0006 | 0.0007 | 1.6273 | 1.3945 | 7.8070 | ✅ Não |
| csv_categorico_1KB.csv | AES-256 | CFB | 0.0010 | 0.0006 | 0.0007 | 1.6276 | 1.3952 | 7.8148 | ✅ Não |
| csv_categorico_1KB.csv | AES-256 | OFB | 0.0010 | 0.0006 | 0.0006 | 1.6280 | 1.6268 | 7.7840 | ✅ Não |
| csv_categorico_1KB.csv | AES-256 | CTR | 0.0010 | 0.0008 | 0.0006 | 1.2161 | 1.6339 | 7.7895 | ✅ Não |
| csv_categorico_1KB.csv | DES | ECB | 0.0010 | 0.0007 | 0.0006 | 1.4986 | 1.6286 | 7.7631 | ✅ Não |
| csv_categorico_1KB.csv | DES | CBC | 0.0010 | 0.0007 | 0.0007 | 1.3953 | 1.3952 | 7.8090 | ✅ Não |
| csv_categorico_1KB.csv | DES | CFB | 0.0010 | 0.0007 | 0.0007 | 1.3950 | 1.3953 | 7.8140 | ✅ Não |
| csv_categorico_1KB.csv | DES | OFB | 0.0010 | 0.0007 | 0.0007 | 1.3934 | 1.3962 | 7.8052 | ✅ Não |
| csv_categorico_1KB.csv | DES | CTR | 0.0010 | 0.0006 | 0.0006 | 1.6275 | 1.6275 | 7.8149 | ✅ Não |
| csv_categorico_1KB.csv | 3DES | ECB | 0.0010 | 0.0008 | 0.0008 | 1.2204 | 1.2205 | 7.7386 | ✅ Não |
| csv_categorico_1KB.csv | 3DES | CBC | 0.0010 | 0.0007 | 0.0010 | 1.3909 | 0.9767 | 7.7870 | ✅ Não |
| csv_categorico_1KB.csv | 3DES | CFB | 0.0010 | 0.0011 | 0.0009 | 0.9289 | 1.0853 | 7.8167 | ✅ Não |
| csv_categorico_1KB.csv | 3DES | OFB | 0.0010 | 0.0011 | 0.0009 | 0.8877 | 1.0847 | 7.7947 | ✅ Não |
| csv_categorico_1KB.csv | 3DES | CTR | 0.0010 | 0.0010 | 0.0010 | 0.9770 | 0.9936 | 7.8101 | ✅ Não |
| csv_categorico_1KB.csv | RSA-1024 | ECB | 0.0010 | 0.0028 | 0.0100 | 0.3487 | 0.0976 | 7.8793 | ✅ Não |
| csv_categorico_1KB.csv | RSA-1024 | CBC | 0.0010 | 0.0030 | 0.0104 | 0.3255 | 0.0943 | 7.8747 | ✅ Não |
| csv_categorico_1KB.csv | RSA-1024 | CTR | 0.0010 | 0.0033 | 0.0030 | 0.3003 | 0.3255 | 7.8373 | ✅ Não |
| csv_categorico_1KB.csv | RSA-2048 | ECB | 0.0010 | 0.0032 | 0.0155 | 0.3052 | 0.0628 | 7.8739 | ✅ Não |
| csv_categorico_1KB.csv | RSA-2048 | CBC | 0.0010 | 0.0035 | 0.0168 | 0.2791 | 0.0581 | 7.8776 | ✅ Não |
| csv_categorico_1KB.csv | RSA-2048 | CTR | 0.0010 | 0.0033 | 0.0034 | 0.2960 | 0.2872 | 7.8088 | ✅ Não |
| csv_categorico_1KB.csv | RSA-4096 | ECB | 0.0010 | 0.0059 | 0.0471 | 0.1668 | 0.0207 | 7.8791 | ✅ Não |
| csv_categorico_1KB.csv | RSA-4096 | CBC | 0.0010 | 0.0060 | 0.0495 | 0.1640 | 0.0197 | 7.9052 | ✅ Não |
| csv_categorico_1KB.csv | RSA-4096 | CTR | 0.0010 | 0.0056 | 0.0058 | 0.1743 | 0.1697 | 7.7907 | ✅ Não |
| csv_categorico_1MB.csv | AES-128 | ECB | 1.0000 | 0.0014 | 0.0013 | 715.1048 | 788.1808 | 7.9992 | ✅ Não |
| csv_categorico_1MB.csv | AES-128 | CBC | 1.0000 | 0.0032 | 0.0044 | 310.2434 | 228.0715 | 7.9998 | ✅ Não |
| csv_categorico_1MB.csv | AES-128 | CFB | 1.0000 | 0.0180 | 0.0173 | 55.6305 | 57.7229 | 7.9999 | ✅ Não |
| csv_categorico_1MB.csv | AES-128 | OFB | 1.0000 | 0.0057 | 0.0029 | 174.4958 | 349.3536 | 7.9998 | ✅ Não |
| csv_categorico_1MB.csv | AES-128 | CTR | 1.0000 | 0.0019 | 0.0017 | 536.6030 | 591.0967 | 7.9998 | ✅ Não |
| csv_categorico_1MB.csv | AES-256 | ECB | 1.0000 | 0.0013 | 0.0013 | 759.9340 | 761.5208 | 7.9993 | ✅ Não |
| csv_categorico_1MB.csv | AES-256 | CBC | 1.0000 | 0.0068 | 0.0026 | 147.3909 | 380.2909 | 7.9998 | ✅ Não |
| csv_categorico_1MB.csv | AES-256 | CFB | 1.0000 | 0.0219 | 0.0203 | 45.6280 | 49.2216 | 7.9998 | ✅ Não |
| csv_categorico_1MB.csv | AES-256 | OFB | 1.0000 | 0.0033 | 0.0045 | 307.1175 | 222.0536 | 7.9998 | ✅ Não |
| csv_categorico_1MB.csv | AES-256 | CTR | 1.0000 | 0.0020 | 0.0017 | 508.2403 | 582.4371 | 7.9998 | ✅ Não |
| csv_categorico_1MB.csv | DES | ECB | 1.0000 | 0.0112 | 0.0111 | 89.5650 | 89.7648 | 7.9369 | ✅ Não |
| csv_categorico_1MB.csv | DES | CBC | 1.0000 | 0.0156 | 0.0121 | 64.2612 | 82.4310 | 7.9998 | ✅ Não |
| csv_categorico_1MB.csv | DES | CFB | 1.0000 | 0.0887 | 0.0858 | 11.2801 | 11.6574 | 7.9998 | ✅ Não |
| csv_categorico_1MB.csv | DES | OFB | 1.0000 | 0.0154 | 0.0138 | 64.8191 | 72.6108 | 7.9999 | ✅ Não |
| csv_categorico_1MB.csv | DES | CTR | 1.0000 | 0.0116 | 0.0134 | 86.3948 | 74.3869 | 7.9998 | ✅ Não |
| csv_categorico_1MB.csv | 3DES | ECB | 1.0000 | 0.0321 | 0.0329 | 31.1513 | 30.4195 | 7.9442 | ✅ Não |
| csv_categorico_1MB.csv | 3DES | CBC | 1.0000 | 0.0346 | 0.0323 | 28.8702 | 30.9505 | 7.9998 | ✅ Não |
| csv_categorico_1MB.csv | 3DES | CFB | 1.0000 | 0.2532 | 0.2470 | 3.9490 | 4.0478 | 7.9998 | ✅ Não |
| csv_categorico_1MB.csv | 3DES | OFB | 1.0000 | 0.0356 | 0.0328 | 28.1220 | 30.5123 | 7.9998 | ✅ Não |
| csv_categorico_1MB.csv | 3DES | CTR | 1.0000 | 0.0333 | 0.0509 | 29.9925 | 19.6551 | 7.9998 | ✅ Não |
| csv_categorico_1MB.csv | RSA-1024 | ECB | 1.0000 | 2.0197 | 8.9974 | 0.4951 | 0.1111 | 7.9999 | ✅ Não |
| csv_categorico_1MB.csv | RSA-1024 | CBC | 1.0000 | 2.0803 | 10.0444 | 0.4807 | 0.0996 | 7.9999 | ✅ Não |
| csv_categorico_1MB.csv | RSA-1024 | CTR | 1.0000 | 2.0955 | 2.0395 | 0.4772 | 0.4903 | 7.9998 | ✅ Não |
| csv_categorico_1MB.csv | RSA-2048 | ECB | 1.0000 | 2.2738 | 14.0300 | 0.4398 | 0.0713 | 7.9998 | ✅ Não |
| csv_categorico_1MB.csv | RSA-2048 | CBC | 1.0000 | 2.3643 | 14.5407 | 0.4230 | 0.0688 | 7.9999 | ✅ Não |
| csv_categorico_1MB.csv | RSA-2048 | CTR | 1.0000 | 2.6977 | 2.6094 | 0.3707 | 0.3832 | 7.9998 | ✅ Não |
| csv_categorico_1MB.csv | RSA-4096 | ECB | 1.0000 | 3.7282 | 34.7735 | 0.2682 | 0.0288 | 7.9998 | ✅ Não |
| csv_categorico_1MB.csv | RSA-4096 | CBC | 1.0000 | 3.6902 | 34.5968 | 0.2710 | 0.0289 | 7.9999 | ✅ Não |
| csv_categorico_1MB.csv | RSA-4096 | CTR | 1.0000 | 3.5744 | 3.7101 | 0.2798 | 0.2695 | 7.9998 | ✅ Não |
| csv_incremental_100KB.csv | AES-128 | ECB | 0.0977 | 0.0011 | 0.0007 | 85.5561 | 132.4323 | 7.9873 | ✅ Não |
| csv_incremental_100KB.csv | AES-128 | CBC | 0.0977 | 0.0017 | 0.0011 | 57.9226 | 91.1985 | 7.9981 | ✅ Não |
| csv_incremental_100KB.csv | AES-128 | CFB | 0.0977 | 0.0025 | 0.0024 | 39.7361 | 41.1063 | 7.9984 | ✅ Não |
| csv_incremental_100KB.csv | AES-128 | OFB | 0.0977 | 0.0009 | 0.0008 | 108.0397 | 129.9121 | 7.9983 | ✅ Não |
| csv_incremental_100KB.csv | AES-128 | CTR | 0.0977 | 0.0007 | 0.0006 | 135.1592 | 152.4831 | 7.9981 | ✅ Não |
| csv_incremental_100KB.csv | AES-256 | ECB | 0.0977 | 0.0007 | 0.0007 | 147.3911 | 143.4324 | 7.9861 | ✅ Não |
| csv_incremental_100KB.csv | AES-256 | CBC | 0.0977 | 0.0009 | 0.0008 | 104.4978 | 123.5633 | 7.9979 | ✅ Não |
| csv_incremental_100KB.csv | AES-256 | CFB | 0.0977 | 0.0027 | 0.0027 | 36.8140 | 35.7751 | 7.9982 | ✅ Não |
| csv_incremental_100KB.csv | AES-256 | OFB | 0.0977 | 0.0009 | 0.0008 | 112.3392 | 123.5559 | 7.9983 | ✅ Não |
| csv_incremental_100KB.csv | AES-256 | CTR | 0.0977 | 0.0009 | 0.0009 | 108.1823 | 109.6947 | 7.9982 | ✅ Não |
| csv_incremental_100KB.csv | DES | ECB | 0.0977 | 0.0020 | 0.0019 | 49.5614 | 51.0513 | 7.2495 | ✅ Não |
| csv_incremental_100KB.csv | DES | CBC | 0.0977 | 0.0027 | 0.0020 | 36.6772 | 47.8913 | 7.9985 | ✅ Não |
| csv_incremental_100KB.csv | DES | CFB | 0.0977 | 0.0096 | 0.0096 | 10.1967 | 10.1559 | 7.9983 | ✅ Não |
| csv_incremental_100KB.csv | DES | OFB | 0.0977 | 0.0020 | 0.0020 | 48.8456 | 48.1011 | 7.9981 | ✅ Não |
| csv_incremental_100KB.csv | DES | CTR | 0.0977 | 0.0019 | 0.0018 | 51.0781 | 53.8282 | 7.9984 | ✅ Não |
| csv_incremental_100KB.csv | 3DES | ECB | 0.0977 | 0.0039 | 0.0039 | 25.0773 | 25.2666 | 7.2350 | ✅ Não |
| csv_incremental_100KB.csv | 3DES | CBC | 0.0977 | 0.0041 | 0.0038 | 24.1110 | 25.9641 | 7.9980 | ✅ Não |
| csv_incremental_100KB.csv | 3DES | CFB | 0.0977 | 0.0259 | 0.0252 | 3.7653 | 3.8701 | 7.9984 | ✅ Não |
| csv_incremental_100KB.csv | 3DES | OFB | 0.0977 | 0.0044 | 0.0036 | 22.2630 | 26.9146 | 7.9982 | ✅ Não |
| csv_incremental_100KB.csv | 3DES | CTR | 0.0977 | 0.0039 | 0.0038 | 25.2863 | 25.5835 | 7.9979 | ✅ Não |
| csv_incremental_100KB.csv | RSA-1024 | ECB | 0.0977 | 0.2109 | 0.8563 | 0.4630 | 0.1140 | 7.9990 | ✅ Não |
| csv_incremental_100KB.csv | RSA-1024 | CBC | 0.0977 | 0.2074 | 0.8632 | 0.4709 | 0.1131 | 7.9987 | ✅ Não |
| csv_incremental_100KB.csv | RSA-1024 | CTR | 0.0977 | 0.2062 | 0.2047 | 0.4736 | 0.4771 | 7.9981 | ✅ Não |
| csv_incremental_100KB.csv | RSA-2048 | ECB | 0.0977 | 0.2291 | 1.3870 | 0.4263 | 0.0704 | 7.9983 | ✅ Não |
| csv_incremental_100KB.csv | RSA-2048 | CBC | 0.0977 | 0.2360 | 1.4069 | 0.4138 | 0.0694 | 7.9984 | ✅ Não |
| csv_incremental_100KB.csv | RSA-2048 | CTR | 0.0977 | 0.2355 | 0.2297 | 0.4146 | 0.4251 | 7.9982 | ✅ Não |
| csv_incremental_100KB.csv | RSA-4096 | ECB | 0.0977 | 0.3679 | 3.4052 | 0.2655 | 0.0287 | 7.9983 | ✅ Não |
| csv_incremental_100KB.csv | RSA-4096 | CBC | 0.0977 | 0.3667 | 3.4641 | 0.2663 | 0.0282 | 7.9985 | ✅ Não |
| csv_incremental_100KB.csv | RSA-4096 | CTR | 0.0977 | 0.3993 | 0.3839 | 0.2446 | 0.2544 | 7.9982 | ✅ Não |
| csv_incremental_10KB.csv | AES-128 | ECB | 0.0098 | 0.0005 | 0.0008 | 19.4123 | 12.7784 | 7.8800 | ✅ Não |
| csv_incremental_10KB.csv | AES-128 | CBC | 0.0098 | 0.0008 | 0.0009 | 12.8906 | 11.2318 | 7.9812 | ✅ Não |
| csv_incremental_10KB.csv | AES-128 | CFB | 0.0098 | 0.0009 | 0.0009 | 10.6359 | 11.4455 | 7.9799 | ✅ Não |
| csv_incremental_10KB.csv | AES-128 | OFB | 0.0098 | 0.0008 | 0.0006 | 12.2065 | 17.5095 | 7.9818 | ✅ Não |
| csv_incremental_10KB.csv | AES-128 | CTR | 0.0098 | 0.0006 | 0.0007 | 15.4595 | 13.5724 | 7.9804 | ✅ Não |
| csv_incremental_10KB.csv | AES-256 | ECB | 0.0098 | 0.0006 | 0.0005 | 16.6322 | 18.3521 | 7.8673 | ✅ Não |
| csv_incremental_10KB.csv | AES-256 | CBC | 0.0098 | 0.0005 | 0.0007 | 19.3107 | 13.7510 | 7.9831 | ✅ Não |
| csv_incremental_10KB.csv | AES-256 | CFB | 0.0098 | 0.0008 | 0.0008 | 11.4969 | 12.9555 | 7.9824 | ✅ Não |
| csv_incremental_10KB.csv | AES-256 | OFB | 0.0098 | 0.0007 | 0.0007 | 13.4485 | 14.3448 | 7.9819 | ✅ Não |
| csv_incremental_10KB.csv | AES-256 | CTR | 0.0098 | 0.0009 | 0.0006 | 11.1980 | 16.0169 | 7.9838 | ✅ Não |
| csv_incremental_10KB.csv | DES | ECB | 0.0098 | 0.0008 | 0.0007 | 12.4095 | 14.5238 | 7.5064 | ✅ Não |
| csv_incremental_10KB.csv | DES | CBC | 0.0098 | 0.0009 | 0.0009 | 11.2438 | 11.4532 | 7.9801 | ✅ Não |
| csv_incremental_10KB.csv | DES | CFB | 0.0098 | 0.0015 | 0.0018 | 6.5406 | 5.3141 | 7.9813 | ✅ Não |
| csv_incremental_10KB.csv | DES | OFB | 0.0098 | 0.0011 | 0.0009 | 8.5223 | 11.4279 | 7.9817 | ✅ Não |
| csv_incremental_10KB.csv | DES | CTR | 0.0098 | 0.0009 | 0.0009 | 10.9273 | 10.7957 | 7.9807 | ✅ Não |
| csv_incremental_10KB.csv | 3DES | ECB | 0.0098 | 0.0012 | 0.0013 | 8.4464 | 7.5656 | 7.5120 | ✅ Não |
| csv_incremental_10KB.csv | 3DES | CBC | 0.0098 | 0.0012 | 0.0009 | 8.1294 | 10.6937 | 7.9833 | ✅ Não |
| csv_incremental_10KB.csv | 3DES | CFB | 0.0098 | 0.0036 | 0.0031 | 2.6883 | 3.1034 | 7.9839 | ✅ Não |
| csv_incremental_10KB.csv | 3DES | OFB | 0.0098 | 0.0010 | 0.0012 | 9.5867 | 8.3676 | 7.9809 | ✅ Não |
| csv_incremental_10KB.csv | 3DES | CTR | 0.0098 | 0.0011 | 0.0009 | 9.1826 | 11.0425 | 7.9824 | ✅ Não |
| csv_incremental_10KB.csv | RSA-1024 | ECB | 0.0098 | 0.0221 | 0.0997 | 0.4422 | 0.0980 | 7.9883 | ✅ Não |
| csv_incremental_10KB.csv | RSA-1024 | CBC | 0.0098 | 0.0236 | 0.0967 | 0.4141 | 0.1010 | 7.9860 | ✅ Não |
| csv_incremental_10KB.csv | RSA-1024 | CTR | 0.0098 | 0.0223 | 0.0233 | 0.4387 | 0.4199 | 7.9787 | ✅ Não |
| csv_incremental_10KB.csv | RSA-2048 | ECB | 0.0098 | 0.0244 | 0.1468 | 0.3996 | 0.0665 | 7.9861 | ✅ Não |
| csv_incremental_10KB.csv | RSA-2048 | CBC | 0.0098 | 0.0241 | 0.1480 | 0.4051 | 0.0660 | 7.9858 | ✅ Não |
| csv_incremental_10KB.csv | RSA-2048 | CTR | 0.0098 | 0.0262 | 0.0260 | 0.3722 | 0.3751 | 7.9839 | ✅ Não |
| csv_incremental_10KB.csv | RSA-4096 | ECB | 0.0098 | 0.0362 | 0.3446 | 0.2699 | 0.0283 | 7.9818 | ✅ Não |
| csv_incremental_10KB.csv | RSA-4096 | CBC | 0.0098 | 0.0376 | 0.3505 | 0.2597 | 0.0279 | 7.9860 | ✅ Não |
| csv_incremental_10KB.csv | RSA-4096 | CTR | 0.0098 | 0.0419 | 0.0439 | 0.2332 | 0.2223 | 7.9809 | ✅ Não |
| csv_incremental_1KB.csv | AES-128 | ECB | 0.0010 | 0.0004 | 0.0004 | 2.4444 | 2.7599 | 7.6680 | ✅ Não |
| csv_incremental_1KB.csv | AES-128 | CBC | 0.0010 | 0.0005 | 0.0007 | 2.1586 | 1.4999 | 7.7951 | ✅ Não |
| csv_incremental_1KB.csv | AES-128 | CFB | 0.0010 | 0.0007 | 0.0006 | 1.3789 | 1.7603 | 7.7834 | ✅ Não |
| csv_incremental_1KB.csv | AES-128 | OFB | 0.0010 | 0.0005 | 0.0005 | 1.9445 | 1.9433 | 7.8067 | ✅ Não |
| csv_incremental_1KB.csv | AES-128 | CTR | 0.0010 | 0.0007 | 0.0005 | 1.4999 | 2.1554 | 7.8229 | ✅ Não |
| csv_incremental_1KB.csv | AES-256 | ECB | 0.0010 | 0.0006 | 0.0005 | 1.7564 | 1.9399 | 7.6243 | ✅ Não |
| csv_incremental_1KB.csv | AES-256 | CBC | 0.0010 | 0.0006 | 0.0005 | 1.6305 | 1.9342 | 7.8205 | ✅ Não |
| csv_incremental_1KB.csv | AES-256 | CFB | 0.0010 | 0.0008 | 0.0005 | 1.2990 | 1.9315 | 7.8150 | ✅ Não |
| csv_incremental_1KB.csv | AES-256 | OFB | 0.0010 | 0.0006 | 0.0005 | 1.7715 | 1.9531 | 7.7978 | ✅ Não |
| csv_incremental_1KB.csv | AES-256 | CTR | 0.0010 | 0.0006 | 0.0005 | 1.7637 | 1.9229 | 7.7687 | ✅ Não |
| csv_incremental_1KB.csv | DES | ECB | 0.0010 | 0.0005 | 0.0006 | 2.0029 | 1.7212 | 7.0842 | ✅ Não |
| csv_incremental_1KB.csv | DES | CBC | 0.0010 | 0.0006 | 0.0005 | 1.7657 | 1.7760 | 7.7970 | ✅ Não |
| csv_incremental_1KB.csv | DES | CFB | 0.0010 | 0.0007 | 0.0005 | 1.4923 | 1.9355 | 7.8175 | ✅ Não |
| csv_incremental_1KB.csv | DES | OFB | 0.0010 | 0.0005 | 0.0005 | 1.9511 | 1.9322 | 7.8011 | ✅ Não |
| csv_incremental_1KB.csv | DES | CTR | 0.0010 | 0.0005 | 0.0005 | 1.8852 | 1.9543 | 7.7924 | ✅ Não |
| csv_incremental_1KB.csv | 3DES | ECB | 0.0010 | 0.0006 | 0.0006 | 1.6209 | 1.6258 | 7.1032 | ✅ Não |
| csv_incremental_1KB.csv | 3DES | CBC | 0.0010 | 0.0007 | 0.0013 | 1.4041 | 0.7463 | 7.8473 | ✅ Não |
| csv_incremental_1KB.csv | 3DES | CFB | 0.0010 | 0.0015 | 0.0013 | 0.6587 | 0.7796 | 7.8337 | ✅ Não |
| csv_incremental_1KB.csv | 3DES | OFB | 0.0010 | 0.0008 | 0.0006 | 1.2899 | 1.7719 | 7.7967 | ✅ Não |
| csv_incremental_1KB.csv | 3DES | CTR | 0.0010 | 0.0006 | 0.0007 | 1.7666 | 1.3842 | 7.7966 | ✅ Não |
| csv_incremental_1KB.csv | RSA-1024 | ECB | 0.0010 | 0.0027 | 0.0120 | 0.3652 | 0.0814 | 7.8790 | ✅ Não |
| csv_incremental_1KB.csv | RSA-1024 | CBC | 0.0010 | 0.0035 | 0.0104 | 0.2773 | 0.0941 | 7.9106 | ✅ Não |
| csv_incremental_1KB.csv | RSA-1024 | CTR | 0.0010 | 0.0031 | 0.0030 | 0.3178 | 0.3223 | 7.8164 | ✅ Não |
| csv_incremental_1KB.csv | RSA-2048 | ECB | 0.0010 | 0.0030 | 0.0157 | 0.3234 | 0.0621 | 7.8584 | ✅ Não |
| csv_incremental_1KB.csv | RSA-2048 | CBC | 0.0010 | 0.0032 | 0.0153 | 0.3051 | 0.0636 | 7.8774 | ✅ Não |
| csv_incremental_1KB.csv | RSA-2048 | CTR | 0.0010 | 0.0030 | 0.0033 | 0.3241 | 0.2969 | 7.8118 | ✅ Não |
| csv_incremental_1KB.csv | RSA-4096 | ECB | 0.0010 | 0.0057 | 0.0474 | 0.1722 | 0.0206 | 7.8779 | ✅ Não |
| csv_incremental_1KB.csv | RSA-4096 | CBC | 0.0010 | 0.0057 | 0.0465 | 0.1722 | 0.0210 | 7.9101 | ✅ Não |
| csv_incremental_1KB.csv | RSA-4096 | CTR | 0.0010 | 0.0056 | 0.0058 | 0.1747 | 0.1680 | 7.8297 | ✅ Não |
| csv_incremental_1MB.csv | AES-128 | ECB | 1.0000 | 0.0013 | 0.0012 | 792.1553 | 801.3267 | 7.9249 | ✅ Não |
| csv_incremental_1MB.csv | AES-128 | CBC | 1.0000 | 0.0029 | 0.0026 | 342.5823 | 385.0847 | 7.9998 | ✅ Não |
| csv_incremental_1MB.csv | AES-128 | CFB | 1.0000 | 0.0183 | 0.0181 | 54.5985 | 55.3380 | 7.9998 | ✅ Não |
| csv_incremental_1MB.csv | AES-128 | OFB | 1.0000 | 0.0033 | 0.0032 | 299.2746 | 308.1600 | 7.9998 | ✅ Não |
| csv_incremental_1MB.csv | AES-128 | CTR | 1.0000 | 0.0015 | 0.0018 | 664.3810 | 563.5157 | 7.9998 | ✅ Não |
| csv_incremental_1MB.csv | AES-256 | ECB | 1.0000 | 0.0012 | 0.0013 | 850.0302 | 761.9634 | 7.9386 | ✅ Não |
| csv_incremental_1MB.csv | AES-256 | CBC | 1.0000 | 0.0028 | 0.0029 | 352.0483 | 349.4205 | 7.9998 | ✅ Não |
| csv_incremental_1MB.csv | AES-256 | CFB | 1.0000 | 0.0211 | 0.0215 | 47.3395 | 46.5402 | 7.9998 | ✅ Não |
| csv_incremental_1MB.csv | AES-256 | OFB | 1.0000 | 0.0029 | 0.0025 | 345.0228 | 397.8849 | 7.9998 | ✅ Não |
| csv_incremental_1MB.csv | AES-256 | CTR | 1.0000 | 0.0017 | 0.0013 | 593.2286 | 762.6701 | 7.9998 | ✅ Não |
| csv_incremental_1MB.csv | DES | ECB | 1.0000 | 0.0112 | 0.0120 | 88.8978 | 83.5166 | 7.6146 | ✅ Não |
| csv_incremental_1MB.csv | DES | CBC | 1.0000 | 0.0155 | 0.0135 | 64.4612 | 73.8872 | 7.9998 | ✅ Não |
| csv_incremental_1MB.csv | DES | CFB | 1.0000 | 0.0886 | 0.0861 | 11.2904 | 11.6194 | 7.9998 | ✅ Não |
| csv_incremental_1MB.csv | DES | OFB | 1.0000 | 0.0135 | 0.0130 | 74.0635 | 76.7492 | 7.9998 | ✅ Não |
| csv_incremental_1MB.csv | DES | CTR | 1.0000 | 0.0115 | 0.0112 | 87.0936 | 89.0756 | 7.9998 | ✅ Não |
| csv_incremental_1MB.csv | 3DES | ECB | 1.0000 | 0.0320 | 0.0320 | 31.2463 | 31.2694 | 7.5966 | ✅ Não |
| csv_incremental_1MB.csv | 3DES | CBC | 1.0000 | 0.0344 | 0.0328 | 29.1015 | 30.4841 | 7.9998 | ✅ Não |
| csv_incremental_1MB.csv | 3DES | CFB | 1.0000 | 0.2518 | 0.2485 | 3.9719 | 4.0247 | 7.9998 | ✅ Não |
| csv_incremental_1MB.csv | 3DES | OFB | 1.0000 | 0.0343 | 0.0340 | 29.1528 | 29.4113 | 7.9998 | ✅ Não |
| csv_incremental_1MB.csv | 3DES | CTR | 1.0000 | 0.0327 | 0.0324 | 30.5746 | 30.8278 | 7.9998 | ✅ Não |
| csv_incremental_1MB.csv | RSA-1024 | ECB | 1.0000 | 1.9915 | 8.8294 | 0.5021 | 0.1133 | 7.9999 | ✅ Não |
| csv_incremental_1MB.csv | RSA-1024 | CBC | 1.0000 | 2.0779 | 8.9666 | 0.4813 | 0.1115 | 7.9999 | ✅ Não |
| csv_incremental_1MB.csv | RSA-1024 | CTR | 1.0000 | 2.0540 | 2.0518 | 0.4869 | 0.4874 | 7.9998 | ✅ Não |
| csv_incremental_1MB.csv | RSA-2048 | ECB | 1.0000 | 2.3192 | 14.1713 | 0.4312 | 0.0706 | 7.9999 | ✅ Não |
| csv_incremental_1MB.csv | RSA-2048 | CBC | 1.0000 | 2.3771 | 14.2667 | 0.4207 | 0.0701 | 7.9999 | ✅ Não |
| csv_incremental_1MB.csv | RSA-2048 | CTR | 1.0000 | 2.3860 | 2.3639 | 0.4191 | 0.4230 | 7.9998 | ✅ Não |
| csv_incremental_1MB.csv | RSA-4096 | ECB | 1.0000 | 3.5606 | 34.3233 | 0.2808 | 0.0291 | 7.9998 | ✅ Não |
| csv_incremental_1MB.csv | RSA-4096 | CBC | 1.0000 | 3.6233 | 34.1264 | 0.2760 | 0.0293 | 7.9998 | ✅ Não |
| csv_incremental_1MB.csv | RSA-4096 | CTR | 1.0000 | 3.5828 | 3.5698 | 0.2791 | 0.2801 | 7.9998 | ✅ Não |
| csv_realista_100KB.csv | AES-128 | ECB | 0.0977 | 0.0007 | 0.0006 | 147.7367 | 165.2879 | 7.9961 | ✅ Não |
| csv_realista_100KB.csv | AES-128 | CBC | 0.0977 | 0.0008 | 0.0008 | 119.9590 | 120.1138 | 7.9984 | ✅ Não |
| csv_realista_100KB.csv | AES-128 | CFB | 0.0977 | 0.0028 | 0.0025 | 34.9288 | 39.4708 | 7.9983 | ✅ Não |
| csv_realista_100KB.csv | AES-128 | OFB | 0.0977 | 0.0012 | 0.0007 | 83.2368 | 133.8781 | 7.9979 | ✅ Não |
| csv_realista_100KB.csv | AES-128 | CTR | 0.0977 | 0.0010 | 0.0007 | 95.8263 | 131.7381 | 7.9979 | ✅ Não |
| csv_realista_100KB.csv | AES-256 | ECB | 0.0977 | 0.0007 | 0.0007 | 143.7193 | 143.4978 | 7.9960 | ✅ Não |
| csv_realista_100KB.csv | AES-256 | CBC | 0.0977 | 0.0009 | 0.0008 | 109.1655 | 127.7844 | 7.9981 | ✅ Não |
| csv_realista_100KB.csv | AES-256 | CFB | 0.0977 | 0.0028 | 0.0026 | 34.7921 | 37.9692 | 7.9982 | ✅ Não |
| csv_realista_100KB.csv | AES-256 | OFB | 0.0977 | 0.0008 | 0.0007 | 120.5344 | 145.3874 | 7.9982 | ✅ Não |
| csv_realista_100KB.csv | AES-256 | CTR | 0.0977 | 0.0009 | 0.0008 | 111.7599 | 117.9282 | 7.9979 | ✅ Não |
| csv_realista_100KB.csv | DES | ECB | 0.0977 | 0.0017 | 0.0015 | 58.7350 | 64.1775 | 7.9457 | ✅ Não |
| csv_realista_100KB.csv | DES | CBC | 0.0977 | 0.0019 | 0.0017 | 50.6611 | 56.7046 | 7.9982 | ✅ Não |
| csv_realista_100KB.csv | DES | CFB | 0.0977 | 0.0089 | 0.0086 | 10.9362 | 11.3277 | 7.9981 | ✅ Não |
| csv_realista_100KB.csv | DES | OFB | 0.0977 | 0.0018 | 0.0019 | 54.3835 | 52.1923 | 7.9982 | ✅ Não |
| csv_realista_100KB.csv | DES | CTR | 0.0977 | 0.0017 | 0.0017 | 57.2131 | 58.5745 | 7.9981 | ✅ Não |
| csv_realista_100KB.csv | 3DES | ECB | 0.0977 | 0.0037 | 0.0036 | 26.4279 | 26.9864 | 7.9480 | ✅ Não |
| csv_realista_100KB.csv | 3DES | CBC | 0.0977 | 0.0039 | 0.0036 | 24.8732 | 27.0256 | 7.9983 | ✅ Não |
| csv_realista_100KB.csv | 3DES | CFB | 0.0977 | 0.0243 | 0.0247 | 4.0156 | 3.9535 | 7.9982 | ✅ Não |
| csv_realista_100KB.csv | 3DES | OFB | 0.0977 | 0.0047 | 0.0038 | 20.8252 | 25.9177 | 7.9983 | ✅ Não |
| csv_realista_100KB.csv | 3DES | CTR | 0.0977 | 0.0037 | 0.0036 | 26.1065 | 27.0504 | 7.9983 | ✅ Não |
| csv_realista_100KB.csv | RSA-1024 | ECB | 0.0977 | 0.1999 | 0.8605 | 0.4886 | 0.1135 | 7.9988 | ✅ Não |
| csv_realista_100KB.csv | RSA-1024 | CBC | 0.0977 | 0.2062 | 0.8669 | 0.4736 | 0.1126 | 7.9985 | ✅ Não |
| csv_realista_100KB.csv | RSA-1024 | CTR | 0.0977 | 0.2047 | 0.2033 | 0.4772 | 0.4804 | 7.9981 | ✅ Não |
| csv_realista_100KB.csv | RSA-2048 | ECB | 0.0977 | 0.2208 | 1.3619 | 0.4422 | 0.0717 | 7.9987 | ✅ Não |
| csv_realista_100KB.csv | RSA-2048 | CBC | 0.0977 | 0.2415 | 1.3694 | 0.4043 | 0.0713 | 7.9984 | ✅ Não |
| csv_realista_100KB.csv | RSA-2048 | CTR | 0.0977 | 0.2383 | 0.2243 | 0.4098 | 0.4354 | 7.9983 | ✅ Não |
| csv_realista_100KB.csv | RSA-4096 | ECB | 0.0977 | 0.3648 | 3.3798 | 0.2677 | 0.0289 | 7.9986 | ✅ Não |
| csv_realista_100KB.csv | RSA-4096 | CBC | 0.0977 | 0.3737 | 3.4159 | 0.2613 | 0.0286 | 7.9985 | ✅ Não |
| csv_realista_100KB.csv | RSA-4096 | CTR | 0.0977 | 0.3760 | 0.3716 | 0.2597 | 0.2628 | 7.9983 | ✅ Não |
| csv_realista_10KB.csv | AES-128 | ECB | 0.0098 | 0.0006 | 0.0005 | 16.2430 | 18.1601 | 7.9802 | ✅ Não |
| csv_realista_10KB.csv | AES-128 | CBC | 0.0098 | 0.0007 | 0.0005 | 13.7045 | 18.3710 | 7.9810 | ✅ Não |
| csv_realista_10KB.csv | AES-128 | CFB | 0.0098 | 0.0008 | 0.0006 | 12.4783 | 15.0860 | 7.9853 | ✅ Não |
| csv_realista_10KB.csv | AES-128 | OFB | 0.0098 | 0.0008 | 0.0005 | 12.8032 | 18.0321 | 7.9794 | ✅ Não |
| csv_realista_10KB.csv | AES-128 | CTR | 0.0098 | 0.0007 | 0.0005 | 14.1578 | 18.1279 | 7.9828 | ✅ Não |
| csv_realista_10KB.csv | AES-256 | ECB | 0.0098 | 0.0006 | 0.0005 | 15.4794 | 20.8905 | 7.9779 | ✅ Não |
| csv_realista_10KB.csv | AES-256 | CBC | 0.0098 | 0.0005 | 0.0006 | 18.3012 | 15.6881 | 7.9831 | ✅ Não |
| csv_realista_10KB.csv | AES-256 | CFB | 0.0098 | 0.0008 | 0.0007 | 12.3314 | 13.2901 | 7.9800 | ✅ Não |
| csv_realista_10KB.csv | AES-256 | OFB | 0.0098 | 0.0007 | 0.0007 | 14.6836 | 14.1129 | 7.9801 | ✅ Não |
| csv_realista_10KB.csv | AES-256 | CTR | 0.0098 | 0.0006 | 0.0006 | 15.2671 | 16.7156 | 7.9837 | ✅ Não |
| csv_realista_10KB.csv | DES | ECB | 0.0098 | 0.0006 | 0.0006 | 15.9340 | 15.1901 | 7.9432 | ✅ Não |
| csv_realista_10KB.csv | DES | CBC | 0.0098 | 0.0008 | 0.0007 | 12.4294 | 14.6485 | 7.9865 | ✅ Não |
| csv_realista_10KB.csv | DES | CFB | 0.0098 | 0.0016 | 0.0014 | 6.2420 | 6.7948 | 7.9792 | ✅ Não |
| csv_realista_10KB.csv | DES | OFB | 0.0098 | 0.0007 | 0.0006 | 13.8509 | 16.7526 | 7.9822 | ✅ Não |
| csv_realista_10KB.csv | DES | CTR | 0.0098 | 0.0008 | 0.0007 | 12.4775 | 13.8838 | 7.9815 | ✅ Não |
| csv_realista_10KB.csv | 3DES | ECB | 0.0098 | 0.0009 | 0.0009 | 11.3961 | 10.9995 | 7.9262 | ✅ Não |
| csv_realista_10KB.csv | 3DES | CBC | 0.0098 | 0.0011 | 0.0009 | 9.0258 | 10.7639 | 7.9799 | ✅ Não |
| csv_realista_10KB.csv | 3DES | CFB | 0.0098 | 0.0031 | 0.0031 | 3.1154 | 3.1738 | 7.9803 | ✅ Não |
| csv_realista_10KB.csv | 3DES | OFB | 0.0098 | 0.0010 | 0.0012 | 9.7726 | 8.2451 | 7.9846 | ✅ Não |
| csv_realista_10KB.csv | 3DES | CTR | 0.0098 | 0.0010 | 0.0010 | 9.5739 | 9.6522 | 7.9793 | ✅ Não |
| csv_realista_10KB.csv | RSA-1024 | ECB | 0.0098 | 0.0209 | 0.0875 | 0.4665 | 0.1116 | 7.9884 | ✅ Não |
| csv_realista_10KB.csv | RSA-1024 | CBC | 0.0098 | 0.0217 | 0.0894 | 0.4497 | 0.1092 | 7.9902 | ✅ Não |
| csv_realista_10KB.csv | RSA-1024 | CTR | 0.0098 | 0.0210 | 0.0205 | 0.4646 | 0.4772 | 7.9761 | ✅ Não |
| csv_realista_10KB.csv | RSA-2048 | ECB | 0.0098 | 0.0232 | 0.1499 | 0.4217 | 0.0651 | 7.9861 | ✅ Não |
| csv_realista_10KB.csv | RSA-2048 | CBC | 0.0098 | 0.0243 | 0.1425 | 0.4020 | 0.0685 | 7.9858 | ✅ Não |
| csv_realista_10KB.csv | RSA-2048 | CTR | 0.0098 | 0.0231 | 0.0233 | 0.4220 | 0.4184 | 7.9806 | ✅ Não |
| csv_realista_10KB.csv | RSA-4096 | ECB | 0.0098 | 0.0365 | 0.3488 | 0.2677 | 0.0280 | 7.9871 | ✅ Não |
| csv_realista_10KB.csv | RSA-4096 | CBC | 0.0098 | 0.0373 | 0.3401 | 0.2615 | 0.0287 | 7.9860 | ✅ Não |
| csv_realista_10KB.csv | RSA-4096 | CTR | 0.0098 | 0.0382 | 0.0381 | 0.2555 | 0.2562 | 7.9801 | ✅ Não |
| csv_realista_1KB.csv | AES-128 | ECB | 0.0010 | 0.0004 | 0.0005 | 2.4479 | 1.9532 | 7.7936 | ✅ Não |
| csv_realista_1KB.csv | AES-128 | CBC | 0.0010 | 0.0005 | 0.0005 | 1.9552 | 1.9507 | 7.8058 | ✅ Não |
| csv_realista_1KB.csv | AES-128 | CFB | 0.0010 | 0.0005 | 0.0005 | 1.9507 | 1.9504 | 7.8253 | ✅ Não |
| csv_realista_1KB.csv | AES-128 | OFB | 0.0010 | 0.0005 | 0.0006 | 1.9509 | 1.7668 | 7.8289 | ✅ Não |
| csv_realista_1KB.csv | AES-128 | CTR | 0.0010 | 0.0007 | 0.0005 | 1.3962 | 1.9533 | 7.7866 | ✅ Não |
| csv_realista_1KB.csv | AES-256 | ECB | 0.0010 | 0.0005 | 0.0004 | 1.9508 | 2.4414 | 7.7825 | ✅ Não |
| csv_realista_1KB.csv | AES-256 | CBC | 0.0010 | 0.0006 | 0.0005 | 1.6264 | 1.9558 | 7.7773 | ✅ Não |
| csv_realista_1KB.csv | AES-256 | CFB | 0.0010 | 0.0005 | 0.0005 | 1.9512 | 1.9528 | 7.8154 | ✅ Não |
| csv_realista_1KB.csv | AES-256 | OFB | 0.0010 | 0.0005 | 0.0005 | 1.9534 | 1.9561 | 7.8340 | ✅ Não |
| csv_realista_1KB.csv | AES-256 | CTR | 0.0010 | 0.0005 | 0.0005 | 1.9505 | 1.9557 | 7.8017 | ✅ Não |
| csv_realista_1KB.csv | DES | ECB | 0.0010 | 0.0005 | 0.0005 | 1.9505 | 1.9558 | 7.7926 | ✅ Não |
| csv_realista_1KB.csv | DES | CBC | 0.0010 | 0.0005 | 0.0006 | 1.9501 | 1.6226 | 7.8244 | ✅ Não |
| csv_realista_1KB.csv | DES | CFB | 0.0010 | 0.0006 | 0.0007 | 1.6293 | 1.4997 | 7.8310 | ✅ Não |
| csv_realista_1KB.csv | DES | OFB | 0.0010 | 0.0006 | 0.0005 | 1.6280 | 1.9536 | 7.7919 | ✅ Não |
| csv_realista_1KB.csv | DES | CTR | 0.0010 | 0.0006 | 0.0005 | 1.6232 | 1.9565 | 7.7930 | ✅ Não |
| csv_realista_1KB.csv | 3DES | ECB | 0.0010 | 0.0006 | 0.0005 | 1.6289 | 1.9533 | 7.7711 | ✅ Não |
| csv_realista_1KB.csv | 3DES | CBC | 0.0010 | 0.0006 | 0.0005 | 1.6293 | 1.9506 | 7.8125 | ✅ Não |
| csv_realista_1KB.csv | 3DES | CFB | 0.0010 | 0.0008 | 0.0014 | 1.2199 | 0.6978 | 7.8391 | ✅ Não |
| csv_realista_1KB.csv | 3DES | OFB | 0.0010 | 0.0006 | 0.0005 | 1.6276 | 1.9519 | 7.8006 | ✅ Não |
| csv_realista_1KB.csv | 3DES | CTR | 0.0010 | 0.0006 | 0.0006 | 1.6246 | 1.6246 | 7.8263 | ✅ Não |
| csv_realista_1KB.csv | RSA-1024 | ECB | 0.0010 | 0.0026 | 0.0096 | 0.3756 | 0.1022 | 7.8796 | ✅ Não |
| csv_realista_1KB.csv | RSA-1024 | CBC | 0.0010 | 0.0026 | 0.0095 | 0.3756 | 0.1032 | 7.8878 | ✅ Não |
| csv_realista_1KB.csv | RSA-1024 | CTR | 0.0010 | 0.0025 | 0.0029 | 0.3834 | 0.3366 | 7.8108 | ✅ Não |
| csv_realista_1KB.csv | RSA-2048 | ECB | 0.0010 | 0.0030 | 0.0293 | 0.3255 | 0.0333 | 7.8426 | ✅ Não |
| csv_realista_1KB.csv | RSA-2048 | CBC | 0.0010 | 0.0034 | 0.0145 | 0.2905 | 0.0673 | 7.8580 | ✅ Não |
| csv_realista_1KB.csv | RSA-2048 | CTR | 0.0010 | 0.0030 | 0.0031 | 0.3255 | 0.3199 | 7.8167 | ✅ Não |
| csv_realista_1KB.csv | RSA-4096 | ECB | 0.0010 | 0.0055 | 0.0465 | 0.1791 | 0.0210 | 7.8788 | ✅ Não |
| csv_realista_1KB.csv | RSA-4096 | CBC | 0.0010 | 0.0055 | 0.0461 | 0.1788 | 0.0212 | 7.9061 | ✅ Não |
| csv_realista_1KB.csv | RSA-4096 | CTR | 0.0010 | 0.0055 | 0.0055 | 0.1791 | 0.1760 | 7.8181 | ✅ Não |
| csv_realista_1MB.csv | AES-128 | ECB | 1.0000 | 0.0011 | 0.0011 | 942.2438 | 870.0612 | 7.9983 | ✅ Não |
| csv_realista_1MB.csv | AES-128 | CBC | 1.0000 | 0.0027 | 0.0025 | 365.6760 | 397.6171 | 7.9998 | ✅ Não |
| csv_realista_1MB.csv | AES-128 | CFB | 1.0000 | 0.0180 | 0.0170 | 55.4038 | 58.9571 | 7.9998 | ✅ Não |
| csv_realista_1MB.csv | AES-128 | OFB | 1.0000 | 0.0025 | 0.0024 | 393.3660 | 418.1008 | 7.9998 | ✅ Não |
| csv_realista_1MB.csv | AES-128 | CTR | 1.0000 | 0.0014 | 0.0013 | 717.6006 | 746.6097 | 7.9998 | ✅ Não |
| csv_realista_1MB.csv | AES-256 | ECB | 1.0000 | 0.0012 | 0.0012 | 808.6964 | 827.6054 | 7.9984 | ✅ Não |
| csv_realista_1MB.csv | AES-256 | CBC | 1.0000 | 0.0154 | 0.0027 | 64.9539 | 374.4413 | 7.9998 | ✅ Não |
| csv_realista_1MB.csv | AES-256 | CFB | 1.0000 | 0.0222 | 0.0213 | 45.1458 | 46.9774 | 7.9998 | ✅ Não |
| csv_realista_1MB.csv | AES-256 | OFB | 1.0000 | 0.0027 | 0.0024 | 364.7189 | 419.1873 | 7.9998 | ✅ Não |
| csv_realista_1MB.csv | AES-256 | CTR | 1.0000 | 0.0014 | 0.0015 | 706.6352 | 682.7000 | 7.9998 | ✅ Não |
| csv_realista_1MB.csv | DES | ECB | 1.0000 | 0.0108 | 0.0105 | 92.3624 | 94.9253 | 7.9521 | ✅ Não |
| csv_realista_1MB.csv | DES | CBC | 1.0000 | 0.0134 | 0.0140 | 74.8868 | 71.2172 | 7.9998 | ✅ Não |
| csv_realista_1MB.csv | DES | CFB | 1.0000 | 0.0870 | 0.0844 | 11.5006 | 11.8506 | 7.9998 | ✅ Não |
| csv_realista_1MB.csv | DES | OFB | 1.0000 | 0.0149 | 0.0130 | 67.0025 | 76.9690 | 7.9998 | ✅ Não |
| csv_realista_1MB.csv | DES | CTR | 1.0000 | 0.0112 | 0.0108 | 89.6255 | 92.8667 | 7.9998 | ✅ Não |
| csv_realista_1MB.csv | 3DES | ECB | 1.0000 | 0.0309 | 0.0312 | 32.3942 | 32.0944 | 7.9489 | ✅ Não |
| csv_realista_1MB.csv | 3DES | CBC | 1.0000 | 0.0355 | 0.0322 | 28.1836 | 31.0627 | 7.9998 | ✅ Não |
| csv_realista_1MB.csv | 3DES | CFB | 1.0000 | 0.2474 | 0.2415 | 4.0421 | 4.1406 | 7.9998 | ✅ Não |
| csv_realista_1MB.csv | 3DES | OFB | 1.0000 | 0.0338 | 0.0332 | 29.5737 | 30.0833 | 7.9998 | ✅ Não |
| csv_realista_1MB.csv | 3DES | CTR | 1.0000 | 0.0329 | 0.0325 | 30.4264 | 30.7356 | 7.9998 | ✅ Não |
| csv_realista_1MB.csv | RSA-1024 | ECB | 1.0000 | 1.9815 | 8.7392 | 0.5047 | 0.1144 | 7.9999 | ✅ Não |
| csv_realista_1MB.csv | RSA-1024 | CBC | 1.0000 | 2.0504 | 8.8017 | 0.4877 | 0.1136 | 7.9999 | ✅ Não |
| csv_realista_1MB.csv | RSA-1024 | CTR | 1.0000 | 2.0296 | 2.0348 | 0.4927 | 0.4914 | 7.9998 | ✅ Não |
| csv_realista_1MB.csv | RSA-2048 | ECB | 1.0000 | 2.2879 | 14.1447 | 0.4371 | 0.0707 | 7.9998 | ✅ Não |
| csv_realista_1MB.csv | RSA-2048 | CBC | 1.0000 | 2.3616 | 14.1695 | 0.4234 | 0.0706 | 7.9998 | ✅ Não |
| csv_realista_1MB.csv | RSA-2048 | CTR | 1.0000 | 2.3525 | 2.3752 | 0.4251 | 0.4210 | 7.9998 | ✅ Não |
| csv_realista_1MB.csv | RSA-4096 | ECB | 1.0000 | 3.6029 | 34.2766 | 0.2776 | 0.0292 | 7.9998 | ✅ Não |
| csv_realista_1MB.csv | RSA-4096 | CBC | 1.0000 | 3.6805 | 34.3510 | 0.2717 | 0.0291 | 7.9999 | ✅ Não |
| csv_realista_1MB.csv | RSA-4096 | CTR | 1.0000 | 3.6472 | 3.6567 | 0.2742 | 0.2735 | 7.9998 | ✅ Não |
| csv_repetitivo_100KB.csv | AES-128 | ECB | 0.0977 | 0.0006 | 0.0005 | 152.5626 | 180.5121 | 6.9059 | ⚠️ Sim |
| csv_repetitivo_100KB.csv | AES-128 | CBC | 0.0977 | 0.0021 | 0.0007 | 47.0637 | 144.4695 | 7.9983 | ✅ Não |
| csv_repetitivo_100KB.csv | AES-128 | CFB | 0.0977 | 0.0025 | 0.0022 | 39.4563 | 43.9395 | 7.9982 | ✅ Não |
| csv_repetitivo_100KB.csv | AES-128 | OFB | 0.0977 | 0.0008 | 0.0008 | 115.3770 | 129.7270 | 7.9981 | ✅ Não |
| csv_repetitivo_100KB.csv | AES-128 | CTR | 0.0977 | 0.0008 | 0.0007 | 128.9551 | 136.1747 | 7.9983 | ✅ Não |
| csv_repetitivo_100KB.csv | AES-256 | ECB | 0.0977 | 0.0006 | 0.0007 | 158.7474 | 144.0124 | 6.8868 | ⚠️ Sim |
| csv_repetitivo_100KB.csv | AES-256 | CBC | 0.0977 | 0.0009 | 0.0007 | 112.3669 | 130.2136 | 7.9979 | ✅ Não |
| csv_repetitivo_100KB.csv | AES-256 | CFB | 0.0977 | 0.0027 | 0.0026 | 35.8939 | 37.3979 | 7.9980 | ✅ Não |
| csv_repetitivo_100KB.csv | AES-256 | OFB | 0.0977 | 0.0009 | 0.0008 | 110.9907 | 120.7939 | 7.9984 | ✅ Não |
| csv_repetitivo_100KB.csv | AES-256 | CTR | 0.0977 | 0.0008 | 0.0008 | 121.7852 | 122.5760 | 7.9982 | ✅ Não |
| csv_repetitivo_100KB.csv | DES | ECB | 0.0977 | 0.0019 | 0.0018 | 51.4295 | 54.8650 | 6.1416 | ⚠️ Sim |
| csv_repetitivo_100KB.csv | DES | CBC | 0.0977 | 0.0020 | 0.0017 | 48.3498 | 56.9886 | 7.9982 | ✅ Não |
| csv_repetitivo_100KB.csv | DES | CFB | 0.0977 | 0.0092 | 0.0086 | 10.5926 | 11.3382 | 7.9980 | ✅ Não |
| csv_repetitivo_100KB.csv | DES | OFB | 0.0977 | 0.0018 | 0.0017 | 53.9466 | 56.2947 | 7.9982 | ✅ Não |
| csv_repetitivo_100KB.csv | DES | CTR | 0.0977 | 0.0018 | 0.0015 | 54.6039 | 63.8494 | 7.9983 | ✅ Não |
| csv_repetitivo_100KB.csv | 3DES | ECB | 0.0977 | 0.0037 | 0.0036 | 26.7347 | 27.4152 | 6.0140 | ⚠️ Sim |
| csv_repetitivo_100KB.csv | 3DES | CBC | 0.0977 | 0.0044 | 0.0037 | 22.2421 | 26.6656 | 7.9984 | ✅ Não |
| csv_repetitivo_100KB.csv | 3DES | CFB | 0.0977 | 0.0248 | 0.0270 | 3.9320 | 3.6145 | 7.9983 | ✅ Não |
| csv_repetitivo_100KB.csv | 3DES | OFB | 0.0977 | 0.0042 | 0.0040 | 23.3834 | 24.6321 | 7.9984 | ✅ Não |
| csv_repetitivo_100KB.csv | 3DES | CTR | 0.0977 | 0.0059 | 0.0038 | 16.6407 | 26.0108 | 7.9981 | ✅ Não |
| csv_repetitivo_100KB.csv | RSA-1024 | ECB | 0.0977 | 0.1990 | 0.8876 | 0.4907 | 0.1100 | 7.9990 | ✅ Não |
| csv_repetitivo_100KB.csv | RSA-1024 | CBC | 0.0977 | 0.2065 | 0.8720 | 0.4729 | 0.1120 | 7.9989 | ✅ Não |
| csv_repetitivo_100KB.csv | RSA-1024 | CTR | 0.0977 | 0.2055 | 0.2159 | 0.4752 | 0.4523 | 7.9984 | ✅ Não |
| csv_repetitivo_100KB.csv | RSA-2048 | ECB | 0.0977 | 0.2301 | 1.3887 | 0.4244 | 0.0703 | 7.9983 | ✅ Não |
| csv_repetitivo_100KB.csv | RSA-2048 | CBC | 0.0977 | 0.2356 | 1.3980 | 0.4145 | 0.0699 | 7.9985 | ✅ Não |
| csv_repetitivo_100KB.csv | RSA-2048 | CTR | 0.0977 | 0.2321 | 0.2328 | 0.4207 | 0.4195 | 7.9978 | ✅ Não |
| csv_repetitivo_100KB.csv | RSA-4096 | ECB | 0.0977 | 0.3608 | 3.3799 | 0.2706 | 0.0289 | 7.9986 | ✅ Não |
| csv_repetitivo_100KB.csv | RSA-4096 | CBC | 0.0977 | 0.3729 | 3.3722 | 0.2619 | 0.0290 | 7.9982 | ✅ Não |
| csv_repetitivo_100KB.csv | RSA-4096 | CTR | 0.0977 | 0.3746 | 0.3638 | 0.2607 | 0.2684 | 7.9982 | ✅ Não |
| csv_repetitivo_10KB.csv | AES-128 | ECB | 0.0098 | 0.0005 | 0.0005 | 20.2802 | 18.2223 | 6.8275 | ⚠️ Sim |
| csv_repetitivo_10KB.csv | AES-128 | CBC | 0.0098 | 0.0006 | 0.0006 | 16.4129 | 16.7883 | 7.9816 | ✅ Não |
| csv_repetitivo_10KB.csv | AES-128 | CFB | 0.0098 | 0.0009 | 0.0006 | 11.4082 | 16.8914 | 7.9794 | ✅ Não |
| csv_repetitivo_10KB.csv | AES-128 | OFB | 0.0098 | 0.0007 | 0.0007 | 13.6333 | 14.1319 | 7.9815 | ✅ Não |
| csv_repetitivo_10KB.csv | AES-128 | CTR | 0.0098 | 0.0007 | 0.0005 | 14.5615 | 17.9602 | 7.9832 | ✅ Não |
| csv_repetitivo_10KB.csv | AES-256 | ECB | 0.0098 | 0.0005 | 0.0006 | 18.8045 | 16.8970 | 6.9515 | ⚠️ Sim |
| csv_repetitivo_10KB.csv | AES-256 | CBC | 0.0098 | 0.0006 | 0.0006 | 15.2859 | 16.6558 | 7.9830 | ✅ Não |
| csv_repetitivo_10KB.csv | AES-256 | CFB | 0.0098 | 0.0008 | 0.0007 | 12.6377 | 13.8782 | 7.9815 | ✅ Não |
| csv_repetitivo_10KB.csv | AES-256 | OFB | 0.0098 | 0.0006 | 0.0005 | 15.1194 | 18.6233 | 7.9844 | ✅ Não |
| csv_repetitivo_10KB.csv | AES-256 | CTR | 0.0098 | 0.0007 | 0.0005 | 13.8753 | 18.3751 | 7.9810 | ✅ Não |
| csv_repetitivo_10KB.csv | DES | ECB | 0.0098 | 0.0006 | 0.0006 | 16.8144 | 16.5028 | 6.2914 | ⚠️ Sim |
| csv_repetitivo_10KB.csv | DES | CBC | 0.0098 | 0.0007 | 0.0006 | 13.1916 | 15.4467 | 7.9826 | ✅ Não |
| csv_repetitivo_10KB.csv | DES | CFB | 0.0098 | 0.0015 | 0.0013 | 6.4931 | 7.3160 | 7.9821 | ✅ Não |
| csv_repetitivo_10KB.csv | DES | OFB | 0.0098 | 0.0007 | 0.0007 | 14.3417 | 13.7459 | 7.9811 | ✅ Não |
| csv_repetitivo_10KB.csv | DES | CTR | 0.0098 | 0.0006 | 0.0007 | 15.7357 | 13.6347 | 7.9815 | ✅ Não |
| csv_repetitivo_10KB.csv | 3DES | ECB | 0.0098 | 0.0009 | 0.0009 | 10.8157 | 11.0907 | 6.2916 | ⚠️ Sim |
| csv_repetitivo_10KB.csv | 3DES | CBC | 0.0098 | 0.0010 | 0.0009 | 10.1029 | 10.6243 | 7.9806 | ✅ Não |
| csv_repetitivo_10KB.csv | 3DES | CFB | 0.0098 | 0.0032 | 0.0030 | 3.0219 | 3.2356 | 7.9840 | ✅ Não |
| csv_repetitivo_10KB.csv | 3DES | OFB | 0.0098 | 0.0011 | 0.0011 | 9.0720 | 8.5689 | 7.9816 | ✅ Não |
| csv_repetitivo_10KB.csv | 3DES | CTR | 0.0098 | 0.0011 | 0.0011 | 9.2246 | 9.1853 | 7.9844 | ✅ Não |
| csv_repetitivo_10KB.csv | RSA-1024 | ECB | 0.0098 | 0.0234 | 0.0886 | 0.4177 | 0.1103 | 7.9871 | ✅ Não |
| csv_repetitivo_10KB.csv | RSA-1024 | CBC | 0.0098 | 0.0207 | 0.0881 | 0.4716 | 0.1109 | 7.9870 | ✅ Não |
| csv_repetitivo_10KB.csv | RSA-1024 | CTR | 0.0098 | 0.0223 | 0.0214 | 0.4379 | 0.4574 | 7.9816 | ✅ Não |
| csv_repetitivo_10KB.csv | RSA-2048 | ECB | 0.0098 | 0.0246 | 0.1382 | 0.3963 | 0.0707 | 7.9860 | ✅ Não |
| csv_repetitivo_10KB.csv | RSA-2048 | CBC | 0.0098 | 0.0230 | 0.1485 | 0.4247 | 0.0658 | 7.9857 | ✅ Não |
| csv_repetitivo_10KB.csv | RSA-2048 | CTR | 0.0098 | 0.0249 | 0.0327 | 0.3922 | 0.2987 | 7.9816 | ✅ Não |
| csv_repetitivo_10KB.csv | RSA-4096 | ECB | 0.0098 | 0.0372 | 0.3377 | 0.2623 | 0.0289 | 7.9852 | ✅ Não |
| csv_repetitivo_10KB.csv | RSA-4096 | CBC | 0.0098 | 0.0474 | 0.3413 | 0.2061 | 0.0286 | 7.9851 | ✅ Não |
| csv_repetitivo_10KB.csv | RSA-4096 | CTR | 0.0098 | 0.0364 | 0.0366 | 0.2680 | 0.2671 | 7.9841 | ✅ Não |
| csv_repetitivo_1KB.csv | AES-128 | ECB | 0.0010 | 0.0006 | 0.0004 | 1.6298 | 2.4404 | 6.9158 | ⚠️ Sim |
| csv_repetitivo_1KB.csv | AES-128 | CBC | 0.0010 | 0.0005 | 0.0005 | 1.9533 | 1.9490 | 7.8104 | ✅ Não |
| csv_repetitivo_1KB.csv | AES-128 | CFB | 0.0010 | 0.0006 | 0.0004 | 1.6288 | 2.4374 | 7.8385 | ✅ Não |
| csv_repetitivo_1KB.csv | AES-128 | OFB | 0.0010 | 0.0006 | 0.0005 | 1.6293 | 1.9523 | 7.8180 | ✅ Não |
| csv_repetitivo_1KB.csv | AES-128 | CTR | 0.0010 | 0.0005 | 0.0006 | 1.9525 | 1.6279 | 7.7934 | ✅ Não |
| csv_repetitivo_1KB.csv | AES-256 | ECB | 0.0010 | 0.0005 | 0.0005 | 1.9511 | 1.9528 | 7.0464 | ✅ Não |
| csv_repetitivo_1KB.csv | AES-256 | CBC | 0.0010 | 0.0007 | 0.0005 | 1.4990 | 1.9470 | 7.8261 | ✅ Não |
| csv_repetitivo_1KB.csv | AES-256 | CFB | 0.0010 | 0.0005 | 0.0005 | 1.9534 | 1.9533 | 7.8112 | ✅ Não |
| csv_repetitivo_1KB.csv | AES-256 | OFB | 0.0010 | 0.0005 | 0.0006 | 1.9527 | 1.6279 | 7.8272 | ✅ Não |
| csv_repetitivo_1KB.csv | AES-256 | CTR | 0.0010 | 0.0005 | 0.0005 | 1.9528 | 1.9537 | 7.8064 | ✅ Não |
| csv_repetitivo_1KB.csv | DES | ECB | 0.0010 | 0.0006 | 0.0005 | 1.6281 | 1.9494 | 6.2643 | ⚠️ Sim |
| csv_repetitivo_1KB.csv | DES | CBC | 0.0010 | 0.0006 | 0.0005 | 1.6262 | 1.9557 | 7.8219 | ✅ Não |
| csv_repetitivo_1KB.csv | DES | CFB | 0.0010 | 0.0005 | 0.0006 | 1.9507 | 1.6267 | 7.7738 | ✅ Não |
| csv_repetitivo_1KB.csv | DES | OFB | 0.0010 | 0.0005 | 0.0005 | 1.9507 | 1.9532 | 7.8183 | ✅ Não |
| csv_repetitivo_1KB.csv | DES | CTR | 0.0010 | 0.0005 | 0.0005 | 1.9528 | 1.9538 | 7.8163 | ✅ Não |
| csv_repetitivo_1KB.csv | 3DES | ECB | 0.0010 | 0.0006 | 0.0006 | 1.7730 | 1.6255 | 6.1882 | ⚠️ Sim |
| csv_repetitivo_1KB.csv | 3DES | CBC | 0.0010 | 0.0006 | 0.0005 | 1.6258 | 1.9600 | 7.8081 | ✅ Não |
| csv_repetitivo_1KB.csv | 3DES | CFB | 0.0010 | 0.0008 | 0.0008 | 1.2193 | 1.2220 | 7.8308 | ✅ Não |
| csv_repetitivo_1KB.csv | 3DES | OFB | 0.0010 | 0.0006 | 0.0006 | 1.6275 | 1.6284 | 7.8011 | ✅ Não |
| csv_repetitivo_1KB.csv | 3DES | CTR | 0.0010 | 0.0007 | 0.0006 | 1.3951 | 1.6275 | 7.8310 | ✅ Não |
| csv_repetitivo_1KB.csv | RSA-1024 | ECB | 0.0010 | 0.0026 | 0.0097 | 0.3757 | 0.1006 | 7.8818 | ✅ Não |
| csv_repetitivo_1KB.csv | RSA-1024 | CBC | 0.0010 | 0.0025 | 0.0095 | 0.3907 | 0.1033 | 7.8903 | ✅ Não |
| csv_repetitivo_1KB.csv | RSA-1024 | CTR | 0.0010 | 0.0025 | 0.0028 | 0.3908 | 0.3549 | 7.8125 | ✅ Não |
| csv_repetitivo_1KB.csv | RSA-2048 | ECB | 0.0010 | 0.0029 | 0.0150 | 0.3367 | 0.0653 | 7.8702 | ✅ Não |
| csv_repetitivo_1KB.csv | RSA-2048 | CBC | 0.0010 | 0.0031 | 0.0157 | 0.3199 | 0.0622 | 7.8795 | ✅ Não |
| csv_repetitivo_1KB.csv | RSA-2048 | CTR | 0.0010 | 0.0033 | 0.0032 | 0.2985 | 0.3052 | 7.7956 | ✅ Não |
| csv_repetitivo_1KB.csv | RSA-4096 | ECB | 0.0010 | 0.0057 | 0.0463 | 0.1727 | 0.0211 | 7.8646 | ✅ Não |
| csv_repetitivo_1KB.csv | RSA-4096 | CBC | 0.0010 | 0.0056 | 0.0465 | 0.1758 | 0.0210 | 7.9222 | ✅ Não |
| csv_repetitivo_1KB.csv | RSA-4096 | CTR | 0.0010 | 0.0057 | 0.0061 | 0.1728 | 0.1600 | 7.7943 | ✅ Não |
| csv_repetitivo_1MB.csv | AES-128 | ECB | 1.0000 | 0.0013 | 0.0014 | 798.2460 | 725.2942 | 6.8161 | ⚠️ Sim |
| csv_repetitivo_1MB.csv | AES-128 | CBC | 1.0000 | 0.0028 | 0.0024 | 355.6002 | 408.7976 | 7.9998 | ✅ Não |
| csv_repetitivo_1MB.csv | AES-128 | CFB | 1.0000 | 0.0188 | 0.0168 | 53.1364 | 59.5382 | 7.9998 | ✅ Não |
| csv_repetitivo_1MB.csv | AES-128 | OFB | 1.0000 | 0.0036 | 0.0023 | 274.7229 | 430.9497 | 7.9998 | ✅ Não |
| csv_repetitivo_1MB.csv | AES-128 | CTR | 1.0000 | 0.0015 | 0.0013 | 645.9036 | 741.9345 | 7.9998 | ✅ Não |
| csv_repetitivo_1MB.csv | AES-256 | ECB | 1.0000 | 0.0011 | 0.0011 | 872.6316 | 942.2226 | 6.8843 | ⚠️ Sim |
| csv_repetitivo_1MB.csv | AES-256 | CBC | 1.0000 | 0.0030 | 0.0030 | 332.3564 | 334.7596 | 7.9998 | ✅ Não |
| csv_repetitivo_1MB.csv | AES-256 | CFB | 1.0000 | 0.0212 | 0.0195 | 47.1682 | 51.3001 | 7.9998 | ✅ Não |
| csv_repetitivo_1MB.csv | AES-256 | OFB | 1.0000 | 0.0029 | 0.0027 | 348.0086 | 364.7284 | 7.9998 | ✅ Não |
| csv_repetitivo_1MB.csv | AES-256 | CTR | 1.0000 | 0.0015 | 0.0015 | 652.6881 | 679.2285 | 7.9998 | ✅ Não |
| csv_repetitivo_1MB.csv | DES | ECB | 1.0000 | 0.0110 | 0.0173 | 90.7310 | 57.7144 | 6.1700 | ⚠️ Sim |
| csv_repetitivo_1MB.csv | DES | CBC | 1.0000 | 0.0133 | 0.0119 | 74.9312 | 83.7320 | 7.9998 | ✅ Não |
| csv_repetitivo_1MB.csv | DES | CFB | 1.0000 | 0.0855 | 0.0862 | 11.6958 | 11.6004 | 7.9998 | ✅ Não |
| csv_repetitivo_1MB.csv | DES | OFB | 1.0000 | 0.0130 | 0.0129 | 77.0843 | 77.4759 | 7.9998 | ✅ Não |
| csv_repetitivo_1MB.csv | DES | CTR | 1.0000 | 0.0110 | 0.0112 | 91.1706 | 89.5643 | 7.9998 | ✅ Não |
| csv_repetitivo_1MB.csv | 3DES | ECB | 1.0000 | 0.0303 | 0.0306 | 33.0017 | 32.6906 | 6.0649 | ⚠️ Sim |
| csv_repetitivo_1MB.csv | 3DES | CBC | 1.0000 | 0.0344 | 0.0327 | 29.0908 | 30.5624 | 7.9998 | ✅ Não |
| csv_repetitivo_1MB.csv | 3DES | CFB | 1.0000 | 0.2478 | 0.2410 | 4.0358 | 4.1500 | 7.9998 | ✅ Não |
| csv_repetitivo_1MB.csv | 3DES | OFB | 1.0000 | 0.0334 | 0.0338 | 29.9796 | 29.5837 | 7.9998 | ✅ Não |
| csv_repetitivo_1MB.csv | 3DES | CTR | 1.0000 | 0.0314 | 0.0310 | 31.8240 | 32.2406 | 7.9999 | ✅ Não |
| csv_repetitivo_1MB.csv | RSA-1024 | ECB | 1.0000 | 2.0179 | 8.9177 | 0.4956 | 0.1121 | 7.9999 | ✅ Não |
| csv_repetitivo_1MB.csv | RSA-1024 | CBC | 1.0000 | 2.0958 | 9.0113 | 0.4771 | 0.1110 | 7.9998 | ✅ Não |
| csv_repetitivo_1MB.csv | RSA-1024 | CTR | 1.0000 | 2.1131 | 2.1499 | 0.4732 | 0.4651 | 7.9998 | ✅ Não |
| csv_repetitivo_1MB.csv | RSA-2048 | ECB | 1.0000 | 2.2925 | 14.1761 | 0.4362 | 0.0705 | 7.9998 | ✅ Não |
| csv_repetitivo_1MB.csv | RSA-2048 | CBC | 1.0000 | 2.3495 | 14.0766 | 0.4256 | 0.0710 | 7.9998 | ✅ Não |
| csv_repetitivo_1MB.csv | RSA-2048 | CTR | 1.0000 | 2.3245 | 2.3573 | 0.4302 | 0.4242 | 7.9998 | ✅ Não |
| csv_repetitivo_1MB.csv | RSA-4096 | ECB | 1.0000 | 3.6018 | 34.2021 | 0.2776 | 0.0292 | 7.9998 | ✅ Não |
| csv_repetitivo_1MB.csv | RSA-4096 | CBC | 1.0000 | 3.6331 | 34.2857 | 0.2752 | 0.0292 | 7.9998 | ✅ Não |
| csv_repetitivo_1MB.csv | RSA-4096 | CTR | 1.0000 | 3.6378 | 3.6379 | 0.2749 | 0.2749 | 7.9998 | ✅ Não |
| dados_aninhados_100KB.json | AES-128 | ECB | 0.0977 | 0.0006 | 0.0006 | 161.5317 | 168.4333 | 7.9097 | ✅ Não |
| dados_aninhados_100KB.json | AES-128 | CBC | 0.0977 | 0.0008 | 0.0008 | 126.9868 | 130.0387 | 7.9983 | ✅ Não |
| dados_aninhados_100KB.json | AES-128 | CFB | 0.0977 | 0.0025 | 0.0023 | 39.6262 | 42.5744 | 7.9982 | ✅ Não |
| dados_aninhados_100KB.json | AES-128 | OFB | 0.0977 | 0.0009 | 0.0007 | 114.8196 | 142.7114 | 7.9984 | ✅ Não |
| dados_aninhados_100KB.json | AES-128 | CTR | 0.0977 | 0.0007 | 0.0006 | 141.8907 | 151.7865 | 7.9982 | ✅ Não |
| dados_aninhados_100KB.json | AES-256 | ECB | 0.0977 | 0.0006 | 0.0006 | 157.5309 | 160.6385 | 7.9141 | ✅ Não |
| dados_aninhados_100KB.json | AES-256 | CBC | 0.0977 | 0.0008 | 0.0008 | 127.1682 | 128.3155 | 7.9979 | ✅ Não |
| dados_aninhados_100KB.json | AES-256 | CFB | 0.0977 | 0.0028 | 0.0028 | 34.3431 | 35.3322 | 7.9982 | ✅ Não |
| dados_aninhados_100KB.json | AES-256 | OFB | 0.0977 | 0.0009 | 0.0010 | 105.4138 | 95.3991 | 7.9981 | ✅ Não |
| dados_aninhados_100KB.json | AES-256 | CTR | 0.0977 | 0.0008 | 0.0007 | 116.0164 | 149.5531 | 7.9981 | ✅ Não |
| dados_aninhados_100KB.json | DES | ECB | 0.0977 | 0.0016 | 0.0016 | 61.4926 | 60.9826 | 7.8344 | ✅ Não |
| dados_aninhados_100KB.json | DES | CBC | 0.0977 | 0.0019 | 0.0017 | 50.4242 | 55.8383 | 7.9981 | ✅ Não |
| dados_aninhados_100KB.json | DES | CFB | 0.0977 | 0.0091 | 0.0092 | 10.7177 | 10.5757 | 7.9980 | ✅ Não |
| dados_aninhados_100KB.json | DES | OFB | 0.0977 | 0.0022 | 0.0020 | 44.8966 | 48.5062 | 7.9981 | ✅ Não |
| dados_aninhados_100KB.json | DES | CTR | 0.0977 | 0.0023 | 0.0029 | 42.4333 | 33.4468 | 7.9985 | ✅ Não |
| dados_aninhados_100KB.json | 3DES | ECB | 0.0977 | 0.0037 | 0.0036 | 26.6003 | 27.1042 | 7.8170 | ✅ Não |
| dados_aninhados_100KB.json | 3DES | CBC | 0.0977 | 0.0044 | 0.0041 | 22.1422 | 23.7590 | 7.9982 | ✅ Não |
| dados_aninhados_100KB.json | 3DES | CFB | 0.0977 | 0.0269 | 0.0248 | 3.6326 | 3.9338 | 7.9984 | ✅ Não |
| dados_aninhados_100KB.json | 3DES | OFB | 0.0977 | 0.0040 | 0.0038 | 24.3393 | 25.7040 | 7.9985 | ✅ Não |
| dados_aninhados_100KB.json | 3DES | CTR | 0.0977 | 0.0036 | 0.0036 | 26.8981 | 27.3482 | 7.9982 | ✅ Não |
| dados_aninhados_100KB.json | RSA-1024 | ECB | 0.0977 | 0.1977 | 0.8701 | 0.4940 | 0.1122 | 7.9987 | ✅ Não |
| dados_aninhados_100KB.json | RSA-1024 | CBC | 0.0977 | 0.2166 | 0.8741 | 0.4508 | 0.1117 | 7.9988 | ✅ Não |
| dados_aninhados_100KB.json | RSA-1024 | CTR | 0.0977 | 0.2039 | 0.2021 | 0.4788 | 0.4831 | 7.9984 | ✅ Não |
| dados_aninhados_100KB.json | RSA-2048 | ECB | 0.0977 | 0.2296 | 1.3570 | 0.4254 | 0.0720 | 7.9985 | ✅ Não |
| dados_aninhados_100KB.json | RSA-2048 | CBC | 0.0977 | 0.2387 | 1.3914 | 0.4092 | 0.0702 | 7.9984 | ✅ Não |
| dados_aninhados_100KB.json | RSA-2048 | CTR | 0.0977 | 0.2303 | 0.2261 | 0.4240 | 0.4318 | 7.9982 | ✅ Não |
| dados_aninhados_100KB.json | RSA-4096 | ECB | 0.0977 | 0.3587 | 3.3753 | 0.2722 | 0.0289 | 7.9983 | ✅ Não |
| dados_aninhados_100KB.json | RSA-4096 | CBC | 0.0977 | 0.3603 | 3.3612 | 0.2711 | 0.0291 | 7.9982 | ✅ Não |
| dados_aninhados_100KB.json | RSA-4096 | CTR | 0.0977 | 0.3614 | 0.3625 | 0.2702 | 0.2694 | 7.9981 | ✅ Não |
| dados_aninhados_100KB.xml | AES-128 | ECB | 0.0977 | 0.0004 | 0.0006 | 248.1823 | 157.3085 | 7.9064 | ✅ Não |
| dados_aninhados_100KB.xml | AES-128 | CBC | 0.0977 | 0.0009 | 0.0007 | 111.7172 | 139.3292 | 7.9983 | ✅ Não |
| dados_aninhados_100KB.xml | AES-128 | CFB | 0.0977 | 0.0026 | 0.0022 | 38.1524 | 44.5406 | 7.9981 | ✅ Não |
| dados_aninhados_100KB.xml | AES-128 | OFB | 0.0977 | 0.0008 | 0.0007 | 119.8397 | 138.8522 | 7.9981 | ✅ Não |
| dados_aninhados_100KB.xml | AES-128 | CTR | 0.0977 | 0.0007 | 0.0006 | 131.5857 | 153.0242 | 7.9982 | ✅ Não |
| dados_aninhados_100KB.xml | AES-256 | ECB | 0.0977 | 0.0006 | 0.0007 | 170.2057 | 137.4128 | 7.8882 | ✅ Não |
| dados_aninhados_100KB.xml | AES-256 | CBC | 0.0977 | 0.0009 | 0.0007 | 108.8783 | 148.0999 | 7.9985 | ✅ Não |
| dados_aninhados_100KB.xml | AES-256 | CFB | 0.0977 | 0.0027 | 0.0025 | 36.1062 | 38.5060 | 7.9983 | ✅ Não |
| dados_aninhados_100KB.xml | AES-256 | OFB | 0.0977 | 0.0008 | 0.0007 | 127.5416 | 140.2932 | 7.9982 | ✅ Não |
| dados_aninhados_100KB.xml | AES-256 | CTR | 0.0977 | 0.0007 | 0.0007 | 139.8048 | 135.2753 | 7.9978 | ✅ Não |
| dados_aninhados_100KB.xml | DES | ECB | 0.0977 | 0.0018 | 0.0023 | 55.5021 | 43.0840 | 7.7810 | ✅ Não |
| dados_aninhados_100KB.xml | DES | CBC | 0.0977 | 0.0023 | 0.0024 | 42.0228 | 40.8615 | 7.9981 | ✅ Não |
| dados_aninhados_100KB.xml | DES | CFB | 0.0977 | 0.0094 | 0.0093 | 10.3346 | 10.4636 | 7.9981 | ✅ Não |
| dados_aninhados_100KB.xml | DES | OFB | 0.0977 | 0.0020 | 0.0018 | 49.7099 | 52.8434 | 7.9981 | ✅ Não |
| dados_aninhados_100KB.xml | DES | CTR | 0.0977 | 0.0016 | 0.0018 | 59.2781 | 55.4045 | 7.9981 | ✅ Não |
| dados_aninhados_100KB.xml | 3DES | ECB | 0.0977 | 0.0038 | 0.0039 | 25.5827 | 25.0805 | 7.7510 | ✅ Não |
| dados_aninhados_100KB.xml | 3DES | CBC | 0.0977 | 0.0043 | 0.0041 | 22.6263 | 24.0597 | 7.9981 | ✅ Não |
| dados_aninhados_100KB.xml | 3DES | CFB | 0.0977 | 0.0250 | 0.0240 | 3.9118 | 4.0723 | 7.9985 | ✅ Não |
| dados_aninhados_100KB.xml | 3DES | OFB | 0.0977 | 0.0043 | 0.0041 | 22.9092 | 23.7819 | 7.9985 | ✅ Não |
| dados_aninhados_100KB.xml | 3DES | CTR | 0.0977 | 0.0040 | 0.0038 | 24.4730 | 25.3910 | 7.9983 | ✅ Não |
| dados_aninhados_100KB.xml | RSA-1024 | ECB | 0.0977 | 0.2088 | 0.8619 | 0.4677 | 0.1133 | 7.9988 | ✅ Não |
| dados_aninhados_100KB.xml | RSA-1024 | CBC | 0.0977 | 0.2113 | 0.8907 | 0.4621 | 0.1096 | 7.9988 | ✅ Não |
| dados_aninhados_100KB.xml | RSA-1024 | CTR | 0.0977 | 0.2136 | 0.2020 | 0.4571 | 0.4834 | 7.9984 | ✅ Não |
| dados_aninhados_100KB.xml | RSA-2048 | ECB | 0.0977 | 0.2310 | 1.3592 | 0.4228 | 0.0718 | 7.9986 | ✅ Não |
| dados_aninhados_100KB.xml | RSA-2048 | CBC | 0.0977 | 0.2382 | 1.3626 | 0.4100 | 0.0717 | 7.9985 | ✅ Não |
| dados_aninhados_100KB.xml | RSA-2048 | CTR | 0.0977 | 0.2371 | 0.2247 | 0.4118 | 0.4346 | 7.9979 | ✅ Não |
| dados_aninhados_100KB.xml | RSA-4096 | ECB | 0.0977 | 0.3454 | 3.3393 | 0.2827 | 0.0292 | 7.9982 | ✅ Não |
| dados_aninhados_100KB.xml | RSA-4096 | CBC | 0.0977 | 0.3503 | 3.3327 | 0.2787 | 0.0293 | 7.9984 | ✅ Não |
| dados_aninhados_100KB.xml | RSA-4096 | CTR | 0.0977 | 0.3622 | 0.3486 | 0.2696 | 0.2801 | 7.9982 | ✅ Não |
| dados_aninhados_10KB.json | AES-128 | ECB | 0.0098 | 0.0004 | 0.0005 | 22.8104 | 18.2627 | 7.9100 | ✅ Não |
| dados_aninhados_10KB.json | AES-128 | CBC | 0.0098 | 0.0007 | 0.0005 | 14.9061 | 18.8616 | 7.9839 | ✅ Não |
| dados_aninhados_10KB.json | AES-128 | CFB | 0.0098 | 0.0006 | 0.0008 | 15.1886 | 12.4430 | 7.9820 | ✅ Não |
| dados_aninhados_10KB.json | AES-128 | OFB | 0.0098 | 0.0006 | 0.0006 | 16.8052 | 15.3773 | 7.9815 | ✅ Não |
| dados_aninhados_10KB.json | AES-128 | CTR | 0.0098 | 0.0007 | 0.0005 | 13.6853 | 17.9561 | 7.9779 | ✅ Não |
| dados_aninhados_10KB.json | AES-256 | ECB | 0.0098 | 0.0005 | 0.0005 | 18.3503 | 20.9708 | 7.9171 | ✅ Não |
| dados_aninhados_10KB.json | AES-256 | CBC | 0.0098 | 0.0006 | 0.0007 | 16.7598 | 14.7621 | 7.9818 | ✅ Não |
| dados_aninhados_10KB.json | AES-256 | CFB | 0.0098 | 0.0008 | 0.0007 | 12.1506 | 14.3053 | 7.9795 | ✅ Não |
| dados_aninhados_10KB.json | AES-256 | OFB | 0.0098 | 0.0007 | 0.0006 | 13.9510 | 16.4409 | 7.9837 | ✅ Não |
| dados_aninhados_10KB.json | AES-256 | CTR | 0.0098 | 0.0007 | 0.0005 | 14.0583 | 18.8572 | 7.9809 | ✅ Não |
| dados_aninhados_10KB.json | DES | ECB | 0.0098 | 0.0006 | 0.0007 | 15.3032 | 14.6801 | 7.8107 | ✅ Não |
| dados_aninhados_10KB.json | DES | CBC | 0.0098 | 0.0007 | 0.0007 | 14.4211 | 13.5634 | 7.9820 | ✅ Não |
| dados_aninhados_10KB.json | DES | CFB | 0.0098 | 0.0015 | 0.0014 | 6.4057 | 6.8958 | 7.9833 | ✅ Não |
| dados_aninhados_10KB.json | DES | OFB | 0.0098 | 0.0007 | 0.0007 | 14.4079 | 14.0265 | 7.9820 | ✅ Não |
| dados_aninhados_10KB.json | DES | CTR | 0.0098 | 0.0007 | 0.0007 | 14.5003 | 14.8591 | 7.9842 | ✅ Não |
| dados_aninhados_10KB.json | 3DES | ECB | 0.0098 | 0.0009 | 0.0009 | 10.8189 | 11.1987 | 7.7948 | ✅ Não |
| dados_aninhados_10KB.json | 3DES | CBC | 0.0098 | 0.0010 | 0.0009 | 9.4206 | 10.2881 | 7.9813 | ✅ Não |
| dados_aninhados_10KB.json | 3DES | CFB | 0.0098 | 0.0032 | 0.0030 | 3.0290 | 3.2928 | 7.9812 | ✅ Não |
| dados_aninhados_10KB.json | 3DES | OFB | 0.0098 | 0.0010 | 0.0010 | 9.4063 | 9.5947 | 7.9798 | ✅ Não |
| dados_aninhados_10KB.json | 3DES | CTR | 0.0098 | 0.0012 | 0.0010 | 8.3087 | 9.7018 | 7.9798 | ✅ Não |
| dados_aninhados_10KB.json | RSA-1024 | ECB | 0.0098 | 0.0211 | 0.0884 | 0.4633 | 0.1104 | 7.9899 | ✅ Não |
| dados_aninhados_10KB.json | RSA-1024 | CBC | 0.0098 | 0.0209 | 0.0918 | 0.4682 | 0.1063 | 7.9905 | ✅ Não |
| dados_aninhados_10KB.json | RSA-1024 | CTR | 0.0098 | 0.0209 | 0.0214 | 0.4663 | 0.4567 | 7.9781 | ✅ Não |
| dados_aninhados_10KB.json | RSA-2048 | ECB | 0.0098 | 0.0235 | 0.1417 | 0.4157 | 0.0689 | 7.9857 | ✅ Não |
| dados_aninhados_10KB.json | RSA-2048 | CBC | 0.0098 | 0.0239 | 0.1429 | 0.4084 | 0.0683 | 7.9854 | ✅ Não |
| dados_aninhados_10KB.json | RSA-2048 | CTR | 0.0098 | 0.0241 | 0.0240 | 0.4055 | 0.4075 | 7.9811 | ✅ Não |
| dados_aninhados_10KB.json | RSA-4096 | ECB | 0.0098 | 0.0348 | 0.3464 | 0.2807 | 0.0282 | 7.9843 | ✅ Não |
| dados_aninhados_10KB.json | RSA-4096 | CBC | 0.0098 | 0.0359 | 0.3373 | 0.2723 | 0.0290 | 7.9843 | ✅ Não |
| dados_aninhados_10KB.json | RSA-4096 | CTR | 0.0098 | 0.0356 | 0.0356 | 0.2741 | 0.2746 | 7.9842 | ✅ Não |
| dados_aninhados_10KB.xml | AES-128 | ECB | 0.0098 | 0.0005 | 0.0005 | 18.1649 | 18.0895 | 7.8748 | ✅ Não |
| dados_aninhados_10KB.xml | AES-128 | CBC | 0.0098 | 0.0007 | 0.0007 | 14.6453 | 13.1030 | 7.9806 | ✅ Não |
| dados_aninhados_10KB.xml | AES-128 | CFB | 0.0098 | 0.0008 | 0.0008 | 12.6490 | 12.7852 | 7.9812 | ✅ Não |
| dados_aninhados_10KB.xml | AES-128 | OFB | 0.0098 | 0.0007 | 0.0006 | 14.4607 | 17.0553 | 7.9835 | ✅ Não |
| dados_aninhados_10KB.xml | AES-128 | CTR | 0.0098 | 0.0007 | 0.0005 | 13.7464 | 18.2963 | 7.9827 | ✅ Não |
| dados_aninhados_10KB.xml | AES-256 | ECB | 0.0098 | 0.0005 | 0.0006 | 18.0847 | 17.2217 | 7.8538 | ✅ Não |
| dados_aninhados_10KB.xml | AES-256 | CBC | 0.0098 | 0.0006 | 0.0005 | 15.3673 | 18.3233 | 7.9816 | ✅ Não |
| dados_aninhados_10KB.xml | AES-256 | CFB | 0.0098 | 0.0009 | 0.0008 | 11.0333 | 12.3814 | 7.9818 | ✅ Não |
| dados_aninhados_10KB.xml | AES-256 | OFB | 0.0098 | 0.0007 | 0.0006 | 13.5553 | 16.6789 | 7.9834 | ✅ Não |
| dados_aninhados_10KB.xml | AES-256 | CTR | 0.0098 | 0.0006 | 0.0005 | 16.8248 | 18.3356 | 7.9804 | ✅ Não |
| dados_aninhados_10KB.xml | DES | ECB | 0.0098 | 0.0007 | 0.0006 | 14.3227 | 16.6092 | 7.7070 | ✅ Não |
| dados_aninhados_10KB.xml | DES | CBC | 0.0098 | 0.0007 | 0.0006 | 13.4670 | 15.1005 | 7.9805 | ✅ Não |
| dados_aninhados_10KB.xml | DES | CFB | 0.0098 | 0.0014 | 0.0015 | 6.7600 | 6.6268 | 7.9819 | ✅ Não |
| dados_aninhados_10KB.xml | DES | OFB | 0.0098 | 0.0008 | 0.0006 | 12.8919 | 15.1934 | 7.9811 | ✅ Não |
| dados_aninhados_10KB.xml | DES | CTR | 0.0098 | 0.0007 | 0.0007 | 14.2252 | 13.8047 | 7.9815 | ✅ Não |
| dados_aninhados_10KB.xml | 3DES | ECB | 0.0098 | 0.0009 | 0.0009 | 11.3469 | 11.0976 | 7.7009 | ✅ Não |
| dados_aninhados_10KB.xml | 3DES | CBC | 0.0098 | 0.0010 | 0.0011 | 9.4526 | 8.9728 | 7.9844 | ✅ Não |
| dados_aninhados_10KB.xml | 3DES | CFB | 0.0098 | 0.0033 | 0.0029 | 2.9155 | 3.3138 | 7.9824 | ✅ Não |
| dados_aninhados_10KB.xml | 3DES | OFB | 0.0098 | 0.0009 | 0.0010 | 10.8097 | 10.1459 | 7.9816 | ✅ Não |
| dados_aninhados_10KB.xml | 3DES | CTR | 0.0098 | 0.0010 | 0.0009 | 10.0105 | 10.6797 | 7.9818 | ✅ Não |
| dados_aninhados_10KB.xml | RSA-1024 | ECB | 0.0098 | 0.0221 | 0.0900 | 0.4426 | 0.1085 | 7.9862 | ✅ Não |
| dados_aninhados_10KB.xml | RSA-1024 | CBC | 0.0098 | 0.0216 | 0.0896 | 0.4531 | 0.1089 | 7.9880 | ✅ Não |
| dados_aninhados_10KB.xml | RSA-1024 | CTR | 0.0098 | 0.0218 | 0.0214 | 0.4472 | 0.4561 | 7.9813 | ✅ Não |
| dados_aninhados_10KB.xml | RSA-2048 | ECB | 0.0098 | 0.0233 | 0.1400 | 0.4184 | 0.0698 | 7.9845 | ✅ Não |
| dados_aninhados_10KB.xml | RSA-2048 | CBC | 0.0098 | 0.0264 | 0.1389 | 0.3704 | 0.0703 | 7.9866 | ✅ Não |
| dados_aninhados_10KB.xml | RSA-2048 | CTR | 0.0098 | 0.0257 | 0.0247 | 0.3803 | 0.3952 | 7.9814 | ✅ Não |
| dados_aninhados_10KB.xml | RSA-4096 | ECB | 0.0098 | 0.0354 | 0.3379 | 0.2760 | 0.0289 | 7.9829 | ✅ Não |
| dados_aninhados_10KB.xml | RSA-4096 | CBC | 0.0098 | 0.0359 | 0.3388 | 0.2721 | 0.0288 | 7.9848 | ✅ Não |
| dados_aninhados_10KB.xml | RSA-4096 | CTR | 0.0098 | 0.0362 | 0.0495 | 0.2701 | 0.1974 | 7.9819 | ✅ Não |
| dados_aninhados_1KB.json | AES-128 | ECB | 0.0010 | 0.0005 | 0.0005 | 1.9562 | 1.9510 | 7.7778 | ✅ Não |
| dados_aninhados_1KB.json | AES-128 | CBC | 0.0010 | 0.0005 | 0.0005 | 1.9502 | 1.9581 | 7.8149 | ✅ Não |
| dados_aninhados_1KB.json | AES-128 | CFB | 0.0010 | 0.0005 | 0.0006 | 1.9517 | 1.6253 | 7.8327 | ✅ Não |
| dados_aninhados_1KB.json | AES-128 | OFB | 0.0010 | 0.0005 | 0.0006 | 1.9517 | 1.6264 | 7.8077 | ✅ Não |
| dados_aninhados_1KB.json | AES-128 | CTR | 0.0010 | 0.0006 | 0.0005 | 1.6261 | 1.9508 | 7.8271 | ✅ Não |
| dados_aninhados_1KB.json | AES-256 | ECB | 0.0010 | 0.0005 | 0.0005 | 1.9512 | 1.9483 | 7.8075 | ✅ Não |
| dados_aninhados_1KB.json | AES-256 | CBC | 0.0010 | 0.0005 | 0.0005 | 1.9508 | 1.9524 | 7.8315 | ✅ Não |
| dados_aninhados_1KB.json | AES-256 | CFB | 0.0010 | 0.0005 | 0.0006 | 2.1620 | 1.6259 | 7.8371 | ✅ Não |
| dados_aninhados_1KB.json | AES-256 | OFB | 0.0010 | 0.0006 | 0.0005 | 1.6258 | 1.9514 | 7.8185 | ✅ Não |
| dados_aninhados_1KB.json | AES-256 | CTR | 0.0010 | 0.0006 | 0.0004 | 1.6268 | 2.4373 | 7.8125 | ✅ Não |
| dados_aninhados_1KB.json | DES | ECB | 0.0010 | 0.0005 | 0.0005 | 1.9504 | 1.9517 | 7.7793 | ✅ Não |
| dados_aninhados_1KB.json | DES | CBC | 0.0010 | 0.0005 | 0.0005 | 1.9508 | 1.9519 | 7.7961 | ✅ Não |
| dados_aninhados_1KB.json | DES | CFB | 0.0010 | 0.0006 | 0.0006 | 1.6261 | 1.6255 | 7.8504 | ✅ Não |
| dados_aninhados_1KB.json | DES | OFB | 0.0010 | 0.0006 | 0.0005 | 1.6256 | 1.9516 | 7.8210 | ✅ Não |
| dados_aninhados_1KB.json | DES | CTR | 0.0010 | 0.0007 | 0.0005 | 1.3938 | 1.9496 | 7.8278 | ✅ Não |
| dados_aninhados_1KB.json | 3DES | ECB | 0.0010 | 0.0006 | 0.0006 | 1.6261 | 1.7718 | 7.7968 | ✅ Não |
| dados_aninhados_1KB.json | 3DES | CBC | 0.0010 | 0.0006 | 0.0008 | 1.6270 | 1.2197 | 7.8017 | ✅ Não |
| dados_aninhados_1KB.json | 3DES | CFB | 0.0010 | 0.0009 | 0.0008 | 1.0841 | 1.2193 | 7.7984 | ✅ Não |
| dados_aninhados_1KB.json | 3DES | OFB | 0.0010 | 0.0007 | 0.0005 | 1.3912 | 1.9569 | 7.7988 | ✅ Não |
| dados_aninhados_1KB.json | 3DES | CTR | 0.0010 | 0.0006 | 0.0007 | 1.6258 | 1.3935 | 7.7782 | ✅ Não |
| dados_aninhados_1KB.json | RSA-1024 | ECB | 0.0010 | 0.0026 | 0.0096 | 0.3751 | 0.1021 | 7.8828 | ✅ Não |
| dados_aninhados_1KB.json | RSA-1024 | CBC | 0.0010 | 0.0027 | 0.0100 | 0.3613 | 0.0980 | 7.8839 | ✅ Não |
| dados_aninhados_1KB.json | RSA-1024 | CTR | 0.0010 | 0.0026 | 0.0031 | 0.3752 | 0.3196 | 7.7757 | ✅ Não |
| dados_aninhados_1KB.json | RSA-2048 | ECB | 0.0010 | 0.0079 | 0.0148 | 0.1232 | 0.0659 | 7.8472 | ✅ Não |
| dados_aninhados_1KB.json | RSA-2048 | CBC | 0.0010 | 0.0030 | 0.0151 | 0.3252 | 0.0646 | 7.8654 | ✅ Não |
| dados_aninhados_1KB.json | RSA-2048 | CTR | 0.0010 | 0.0030 | 0.0032 | 0.3253 | 0.3049 | 7.8171 | ✅ Não |
| dados_aninhados_1KB.json | RSA-4096 | ECB | 0.0010 | 0.0057 | 0.0461 | 0.1722 | 0.0211 | 7.8766 | ✅ Não |
| dados_aninhados_1KB.json | RSA-4096 | CBC | 0.0010 | 0.0055 | 0.0463 | 0.1774 | 0.0210 | 7.9111 | ✅ Não |
| dados_aninhados_1KB.json | RSA-4096 | CTR | 0.0010 | 0.0058 | 0.0059 | 0.1682 | 0.1650 | 7.8272 | ✅ Não |
| dados_aninhados_1KB.xml | AES-128 | ECB | 0.0010 | 0.0005 | 0.0004 | 1.9529 | 2.4414 | 7.8072 | ✅ Não |
| dados_aninhados_1KB.xml | AES-128 | CBC | 0.0010 | 0.0005 | 0.0005 | 1.9488 | 1.9575 | 7.8028 | ✅ Não |
| dados_aninhados_1KB.xml | AES-128 | CFB | 0.0010 | 0.0005 | 0.0004 | 1.9574 | 2.4417 | 7.8084 | ✅ Não |
| dados_aninhados_1KB.xml | AES-128 | OFB | 0.0010 | 0.0006 | 0.0006 | 1.6239 | 1.6293 | 7.8172 | ✅ Não |
| dados_aninhados_1KB.xml | AES-128 | CTR | 0.0010 | 0.0005 | 0.0005 | 1.9523 | 2.1680 | 7.8134 | ✅ Não |
| dados_aninhados_1KB.xml | AES-256 | ECB | 0.0010 | 0.0005 | 0.0005 | 1.9584 | 1.9526 | 7.8396 | ✅ Não |
| dados_aninhados_1KB.xml | AES-256 | CBC | 0.0010 | 0.0005 | 0.0005 | 1.9486 | 1.9582 | 7.8293 | ✅ Não |
| dados_aninhados_1KB.xml | AES-256 | CFB | 0.0010 | 0.0006 | 0.0006 | 1.6268 | 1.6279 | 7.7868 | ✅ Não |
| dados_aninhados_1KB.xml | AES-256 | OFB | 0.0010 | 0.0005 | 0.0005 | 1.9533 | 1.9510 | 7.8351 | ✅ Não |
| dados_aninhados_1KB.xml | AES-256 | CTR | 0.0010 | 0.0005 | 0.0006 | 1.9535 | 1.6290 | 7.8185 | ✅ Não |
| dados_aninhados_1KB.xml | DES | ECB | 0.0010 | 0.0006 | 0.0005 | 1.6269 | 1.9549 | 7.7092 | ✅ Não |
| dados_aninhados_1KB.xml | DES | CBC | 0.0010 | 0.0005 | 0.0006 | 1.9522 | 1.6275 | 7.8479 | ✅ Não |
| dados_aninhados_1KB.xml | DES | CFB | 0.0010 | 0.0006 | 0.0006 | 1.6275 | 1.6263 | 7.8283 | ✅ Não |
| dados_aninhados_1KB.xml | DES | OFB | 0.0010 | 0.0006 | 0.0005 | 1.6276 | 2.1650 | 7.8286 | ✅ Não |
| dados_aninhados_1KB.xml | DES | CTR | 0.0010 | 0.0005 | 0.0005 | 1.9579 | 1.9532 | 7.8037 | ✅ Não |
| dados_aninhados_1KB.xml | 3DES | ECB | 0.0010 | 0.0006 | 0.0229 | 1.6273 | 0.0426 | 7.7402 | ✅ Não |
| dados_aninhados_1KB.xml | 3DES | CBC | 0.0010 | 0.0006 | 0.0007 | 1.7069 | 1.3975 | 7.8198 | ✅ Não |
| dados_aninhados_1KB.xml | 3DES | CFB | 0.0010 | 0.0008 | 0.0010 | 1.1705 | 0.9658 | 7.8225 | ✅ Não |
| dados_aninhados_1KB.xml | 3DES | OFB | 0.0010 | 0.0006 | 0.0006 | 1.6327 | 1.6280 | 7.8101 | ✅ Não |
| dados_aninhados_1KB.xml | 3DES | CTR | 0.0010 | 0.0006 | 0.0006 | 1.6268 | 1.7720 | 7.8275 | ✅ Não |
| dados_aninhados_1KB.xml | RSA-1024 | ECB | 0.0010 | 0.0027 | 0.0097 | 0.3616 | 0.1012 | 7.8864 | ✅ Não |
| dados_aninhados_1KB.xml | RSA-1024 | CBC | 0.0010 | 0.0027 | 0.0096 | 0.3683 | 0.1017 | 7.8704 | ✅ Não |
| dados_aninhados_1KB.xml | RSA-1024 | CTR | 0.0010 | 0.0028 | 0.0029 | 0.3550 | 0.3367 | 7.8389 | ✅ Não |
| dados_aninhados_1KB.xml | RSA-2048 | ECB | 0.0010 | 0.0028 | 0.0279 | 0.3489 | 0.0350 | 7.8235 | ✅ Não |
| dados_aninhados_1KB.xml | RSA-2048 | CBC | 0.0010 | 0.0029 | 0.0148 | 0.3367 | 0.0660 | 7.8772 | ✅ Não |
| dados_aninhados_1KB.xml | RSA-2048 | CTR | 0.0010 | 0.0030 | 0.0033 | 0.3254 | 0.2959 | 7.8174 | ✅ Não |
| dados_aninhados_1KB.xml | RSA-4096 | ECB | 0.0010 | 0.0055 | 0.0458 | 0.1760 | 0.0213 | 7.8871 | ✅ Não |
| dados_aninhados_1KB.xml | RSA-4096 | CBC | 0.0010 | 0.0054 | 0.0479 | 0.1809 | 0.0204 | 7.9142 | ✅ Não |
| dados_aninhados_1KB.xml | RSA-4096 | CTR | 0.0010 | 0.0054 | 0.0057 | 0.1825 | 0.1713 | 7.8424 | ✅ Não |
| dados_aninhados_1MB.json | AES-128 | ECB | 1.0000 | 0.0010 | 0.0013 | 953.9004 | 781.0469 | 7.9091 | ✅ Não |
| dados_aninhados_1MB.json | AES-128 | CBC | 1.0000 | 0.0035 | 0.0026 | 283.1901 | 389.6057 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.json | AES-128 | CFB | 1.0000 | 0.0177 | 0.0171 | 56.4703 | 58.4874 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.json | AES-128 | OFB | 1.0000 | 0.0024 | 0.0025 | 415.4623 | 401.4260 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.json | AES-128 | CTR | 1.0000 | 0.0014 | 0.0014 | 712.1899 | 733.1795 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.json | AES-256 | ECB | 1.0000 | 0.0011 | 0.0011 | 887.5323 | 874.9244 | 7.9246 | ✅ Não |
| dados_aninhados_1MB.json | AES-256 | CBC | 1.0000 | 0.0027 | 0.0028 | 365.0805 | 354.5148 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.json | AES-256 | CFB | 1.0000 | 0.0224 | 0.0207 | 44.7110 | 48.2095 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.json | AES-256 | OFB | 1.0000 | 0.0029 | 0.0027 | 339.7047 | 366.0746 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.json | AES-256 | CTR | 1.0000 | 0.0018 | 0.0014 | 559.5235 | 697.8288 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.json | DES | ECB | 1.0000 | 0.0125 | 0.0121 | 79.8607 | 82.3989 | 7.8114 | ✅ Não |
| dados_aninhados_1MB.json | DES | CBC | 1.0000 | 0.0164 | 0.0129 | 60.9827 | 77.2872 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.json | DES | CFB | 1.0000 | 0.0917 | 0.0873 | 10.9006 | 11.4487 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.json | DES | OFB | 1.0000 | 0.0136 | 0.0132 | 73.5623 | 75.4987 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.json | DES | CTR | 1.0000 | 0.0284 | 0.0122 | 35.2005 | 81.9516 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.json | 3DES | ECB | 1.0000 | 0.0329 | 0.0323 | 30.4047 | 30.9731 | 7.8156 | ✅ Não |
| dados_aninhados_1MB.json | 3DES | CBC | 1.0000 | 0.0361 | 0.0343 | 27.7195 | 29.1273 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.json | 3DES | CFB | 1.0000 | 0.2573 | 0.2504 | 3.8867 | 3.9935 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.json | 3DES | OFB | 1.0000 | 0.0359 | 0.0344 | 27.8273 | 29.0286 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.json | 3DES | CTR | 1.0000 | 0.0334 | 0.0341 | 29.9684 | 29.3056 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.json | RSA-1024 | ECB | 1.0000 | 2.1112 | 9.1984 | 0.4737 | 0.1087 | 7.9999 | ✅ Não |
| dados_aninhados_1MB.json | RSA-1024 | CBC | 1.0000 | 2.2197 | 9.6711 | 0.4505 | 0.1034 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.json | RSA-1024 | CTR | 1.0000 | 2.2365 | 2.2021 | 0.4471 | 0.4541 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.json | RSA-2048 | ECB | 1.0000 | 2.4673 | 15.0523 | 0.4053 | 0.0664 | 7.9999 | ✅ Não |
| dados_aninhados_1MB.json | RSA-2048 | CBC | 1.0000 | 2.5699 | 15.1174 | 0.3891 | 0.0661 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.json | RSA-2048 | CTR | 1.0000 | 2.3938 | 2.4007 | 0.4178 | 0.4165 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.json | RSA-4096 | ECB | 1.0000 | 3.9679 | 36.9969 | 0.2520 | 0.0270 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.json | RSA-4096 | CBC | 1.0000 | 4.0870 | 37.0782 | 0.2447 | 0.0270 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.json | RSA-4096 | CTR | 1.0000 | 4.0201 | 3.7747 | 0.2487 | 0.2649 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.xml | AES-128 | ECB | 1.0000 | 0.0011 | 0.0012 | 930.9711 | 866.6634 | 7.8550 | ✅ Não |
| dados_aninhados_1MB.xml | AES-128 | CBC | 1.0000 | 0.0028 | 0.0024 | 353.9467 | 408.4393 | 7.9999 | ✅ Não |
| dados_aninhados_1MB.xml | AES-128 | CFB | 1.0000 | 0.0180 | 0.0195 | 55.4316 | 51.3614 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.xml | AES-128 | OFB | 1.0000 | 0.0034 | 0.0025 | 298.2871 | 406.8387 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.xml | AES-128 | CTR | 1.0000 | 0.0035 | 0.0019 | 286.2381 | 520.8569 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.xml | AES-256 | ECB | 1.0000 | 0.0018 | 0.0013 | 558.4438 | 775.2872 | 7.8722 | ✅ Não |
| dados_aninhados_1MB.xml | AES-256 | CBC | 1.0000 | 0.0031 | 0.0029 | 326.1664 | 349.1442 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.xml | AES-256 | CFB | 1.0000 | 0.0225 | 0.0204 | 44.3497 | 48.9265 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.xml | AES-256 | OFB | 1.0000 | 0.0030 | 0.0025 | 330.2888 | 397.1691 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.xml | AES-256 | CTR | 1.0000 | 0.0020 | 0.0018 | 495.7806 | 541.5709 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.xml | DES | ECB | 1.0000 | 0.0123 | 0.0113 | 81.1153 | 88.2354 | 7.7183 | ✅ Não |
| dados_aninhados_1MB.xml | DES | CBC | 1.0000 | 0.0143 | 0.0133 | 70.1324 | 75.1615 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.xml | DES | CFB | 1.0000 | 0.0906 | 0.0860 | 11.0423 | 11.6287 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.xml | DES | OFB | 1.0000 | 0.0133 | 0.0138 | 75.0567 | 72.5958 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.xml | DES | CTR | 1.0000 | 0.0131 | 0.0126 | 76.4724 | 79.6108 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.xml | 3DES | ECB | 1.0000 | 0.0330 | 0.0337 | 30.3160 | 29.6757 | 7.7715 | ✅ Não |
| dados_aninhados_1MB.xml | 3DES | CBC | 1.0000 | 0.0354 | 0.0346 | 28.2774 | 28.9028 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.xml | 3DES | CFB | 1.0000 | 0.2663 | 0.2513 | 3.7555 | 3.9793 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.xml | 3DES | OFB | 1.0000 | 0.0356 | 0.0468 | 28.1175 | 21.3825 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.xml | 3DES | CTR | 1.0000 | 0.0371 | 0.0321 | 26.9571 | 31.1404 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.xml | RSA-1024 | ECB | 1.0000 | 2.1006 | 9.4811 | 0.4760 | 0.1055 | 7.9999 | ✅ Não |
| dados_aninhados_1MB.xml | RSA-1024 | CBC | 1.0000 | 2.2415 | 9.5821 | 0.4461 | 0.1044 | 7.9999 | ✅ Não |
| dados_aninhados_1MB.xml | RSA-1024 | CTR | 1.0000 | 2.1064 | 2.0640 | 0.4748 | 0.4845 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.xml | RSA-2048 | ECB | 1.0000 | 2.2822 | 14.1055 | 0.4382 | 0.0709 | 7.9999 | ✅ Não |
| dados_aninhados_1MB.xml | RSA-2048 | CBC | 1.0000 | 2.3489 | 14.1773 | 0.4257 | 0.0705 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.xml | RSA-2048 | CTR | 1.0000 | 2.3359 | 2.3301 | 0.4281 | 0.4292 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.xml | RSA-4096 | ECB | 1.0000 | 3.5795 | 34.1156 | 0.2794 | 0.0293 | 7.9998 | ✅ Não |
| dados_aninhados_1MB.xml | RSA-4096 | CBC | 1.0000 | 3.6186 | 34.2854 | 0.2763 | 0.0292 | 7.9999 | ✅ Não |
| dados_aninhados_1MB.xml | RSA-4096 | CTR | 1.0000 | 3.6254 | 3.6476 | 0.2758 | 0.2742 | 7.9998 | ✅ Não |
| imagem_padrao_100KB.bmp | AES-128 | ECB | 0.0969 | 0.0006 | 0.0005 | 151.5276 | 207.8372 | 5.3230 | ⚠️ Sim |
| imagem_padrao_100KB.bmp | AES-128 | CBC | 0.0969 | 0.0083 | 0.0007 | 11.6992 | 140.7994 | 7.9985 | ✅ Não |
| imagem_padrao_100KB.bmp | AES-128 | CFB | 0.0969 | 0.0027 | 0.0023 | 35.8882 | 42.9996 | 7.9982 | ✅ Não |
| imagem_padrao_100KB.bmp | AES-128 | OFB | 0.0969 | 0.0008 | 0.0008 | 116.6795 | 124.9925 | 7.9982 | ✅ Não |
| imagem_padrao_100KB.bmp | AES-128 | CTR | 0.0969 | 0.0018 | 0.0006 | 55.1544 | 153.3049 | 7.9984 | ✅ Não |
| imagem_padrao_100KB.bmp | AES-256 | ECB | 0.0969 | 0.0006 | 0.0007 | 158.7348 | 143.9099 | 5.3913 | ⚠️ Sim |
| imagem_padrao_100KB.bmp | AES-256 | CBC | 0.0969 | 0.0009 | 0.0008 | 113.0044 | 121.4884 | 7.9983 | ✅ Não |
| imagem_padrao_100KB.bmp | AES-256 | CFB | 0.0969 | 0.0026 | 0.0025 | 37.8890 | 38.5889 | 7.9983 | ✅ Não |
| imagem_padrao_100KB.bmp | AES-256 | OFB | 0.0969 | 0.0008 | 0.0008 | 127.4097 | 127.9109 | 7.9981 | ✅ Não |
| imagem_padrao_100KB.bmp | AES-256 | CTR | 0.0969 | 0.0007 | 0.0007 | 130.8129 | 137.2019 | 7.9982 | ✅ Não |
| imagem_padrao_100KB.bmp | DES | ECB | 0.0969 | 0.0016 | 0.0015 | 61.7416 | 62.9014 | 4.5239 | ⚠️ Sim |
| imagem_padrao_100KB.bmp | DES | CBC | 0.0969 | 0.0019 | 0.0018 | 51.0965 | 52.7680 | 7.9981 | ✅ Não |
| imagem_padrao_100KB.bmp | DES | CFB | 0.0969 | 0.0283 | 0.0083 | 3.4281 | 11.6497 | 7.9984 | ✅ Não |
| imagem_padrao_100KB.bmp | DES | OFB | 0.0969 | 0.0018 | 0.0018 | 53.8366 | 54.3099 | 7.9984 | ✅ Não |
| imagem_padrao_100KB.bmp | DES | CTR | 0.0969 | 0.0017 | 0.0016 | 56.7475 | 61.8788 | 7.9983 | ✅ Não |
| imagem_padrao_100KB.bmp | 3DES | ECB | 0.0969 | 0.0035 | 0.0035 | 27.3082 | 28.0766 | 4.5222 | ⚠️ Sim |
| imagem_padrao_100KB.bmp | 3DES | CBC | 0.0969 | 0.0038 | 0.0036 | 25.6180 | 26.8383 | 7.9981 | ✅ Não |
| imagem_padrao_100KB.bmp | 3DES | CFB | 0.0969 | 0.0254 | 0.0246 | 3.8162 | 3.9329 | 7.9979 | ✅ Não |
| imagem_padrao_100KB.bmp | 3DES | OFB | 0.0969 | 0.0041 | 0.0041 | 23.5757 | 23.5618 | 7.9982 | ✅ Não |
| imagem_padrao_100KB.bmp | 3DES | CTR | 0.0969 | 0.0038 | 0.0037 | 25.7750 | 26.3404 | 7.9982 | ✅ Não |
| imagem_padrao_100KB.bmp | RSA-1024 | ECB | 0.0969 | 0.1960 | 0.8511 | 0.4945 | 0.1139 | 7.9988 | ✅ Não |
| imagem_padrao_100KB.bmp | RSA-1024 | CBC | 0.0969 | 0.2004 | 0.8720 | 0.4836 | 0.1111 | 7.9987 | ✅ Não |
| imagem_padrao_100KB.bmp | RSA-1024 | CTR | 0.0969 | 0.1989 | 0.2000 | 0.4872 | 0.4846 | 7.9983 | ✅ Não |
| imagem_padrao_100KB.bmp | RSA-2048 | ECB | 0.0969 | 0.2238 | 1.3712 | 0.4331 | 0.0707 | 7.9986 | ✅ Não |
| imagem_padrao_100KB.bmp | RSA-2048 | CBC | 0.0969 | 0.2418 | 1.3921 | 0.4007 | 0.0696 | 7.9983 | ✅ Não |
| imagem_padrao_100KB.bmp | RSA-2048 | CTR | 0.0969 | 0.2405 | 0.2292 | 0.4030 | 0.4228 | 7.9980 | ✅ Não |
| imagem_padrao_100KB.bmp | RSA-4096 | ECB | 0.0969 | 0.3500 | 3.3150 | 0.2769 | 0.0292 | 7.9983 | ✅ Não |
| imagem_padrao_100KB.bmp | RSA-4096 | CBC | 0.0969 | 0.3538 | 3.3413 | 0.2740 | 0.0290 | 7.9983 | ✅ Não |
| imagem_padrao_100KB.bmp | RSA-4096 | CTR | 0.0969 | 0.3684 | 0.3515 | 0.2630 | 0.2757 | 7.9984 | ✅ Não |
| imagem_padrao_10KB.bmp | AES-128 | ECB | 0.0098 | 0.0005 | 0.0005 | 18.0836 | 18.0605 | 5.8998 | ⚠️ Sim |
| imagem_padrao_10KB.bmp | AES-128 | CBC | 0.0098 | 0.0007 | 0.0006 | 13.2760 | 16.6814 | 7.9814 | ✅ Não |
| imagem_padrao_10KB.bmp | AES-128 | CFB | 0.0098 | 0.0009 | 0.0007 | 10.6835 | 13.4315 | 7.9800 | ✅ Não |
| imagem_padrao_10KB.bmp | AES-128 | OFB | 0.0098 | 0.0007 | 0.0005 | 13.9581 | 18.0637 | 7.9828 | ✅ Não |
| imagem_padrao_10KB.bmp | AES-128 | CTR | 0.0098 | 0.0007 | 0.0005 | 14.9065 | 18.0948 | 7.9823 | ✅ Não |
| imagem_padrao_10KB.bmp | AES-256 | ECB | 0.0098 | 0.0005 | 0.0005 | 18.3488 | 18.2136 | 5.8068 | ⚠️ Sim |
| imagem_padrao_10KB.bmp | AES-256 | CBC | 0.0098 | 0.0006 | 0.0005 | 15.5220 | 18.1636 | 7.9824 | ✅ Não |
| imagem_padrao_10KB.bmp | AES-256 | CFB | 0.0098 | 0.0008 | 0.0007 | 11.7988 | 14.3962 | 7.9809 | ✅ Não |
| imagem_padrao_10KB.bmp | AES-256 | OFB | 0.0098 | 0.0007 | 0.0005 | 14.1760 | 20.2626 | 7.9818 | ✅ Não |
| imagem_padrao_10KB.bmp | AES-256 | CTR | 0.0098 | 0.0006 | 0.0006 | 15.0795 | 16.1320 | 7.9818 | ✅ Não |
| imagem_padrao_10KB.bmp | DES | ECB | 0.0098 | 0.0006 | 0.0006 | 16.5676 | 16.6686 | 4.6064 | ⚠️ Sim |
| imagem_padrao_10KB.bmp | DES | CBC | 0.0098 | 0.0007 | 0.0007 | 13.1375 | 14.2940 | 7.9814 | ✅ Não |
| imagem_padrao_10KB.bmp | DES | CFB | 0.0098 | 0.0015 | 0.0013 | 6.3857 | 7.4339 | 7.9838 | ✅ Não |
| imagem_padrao_10KB.bmp | DES | OFB | 0.0098 | 0.0007 | 0.0006 | 13.3476 | 15.2272 | 7.9819 | ✅ Não |
| imagem_padrao_10KB.bmp | DES | CTR | 0.0098 | 0.0007 | 0.0007 | 14.3720 | 13.7976 | 7.9779 | ✅ Não |
| imagem_padrao_10KB.bmp | 3DES | ECB | 0.0098 | 0.0009 | 0.0010 | 11.4749 | 10.0838 | 4.7590 | ⚠️ Sim |
| imagem_padrao_10KB.bmp | 3DES | CBC | 0.0098 | 0.0011 | 0.0011 | 9.0820 | 9.2795 | 7.9826 | ✅ Não |
| imagem_padrao_10KB.bmp | 3DES | CFB | 0.0098 | 0.0036 | 0.0033 | 2.7441 | 3.0068 | 7.9817 | ✅ Não |
| imagem_padrao_10KB.bmp | 3DES | OFB | 0.0098 | 0.0010 | 0.0008 | 9.4830 | 11.5814 | 7.9837 | ✅ Não |
| imagem_padrao_10KB.bmp | 3DES | CTR | 0.0098 | 0.0011 | 0.0011 | 8.6692 | 8.6588 | 7.9806 | ✅ Não |
| imagem_padrao_10KB.bmp | RSA-1024 | ECB | 0.0098 | 0.0200 | 0.0871 | 0.4887 | 0.1124 | 7.9890 | ✅ Não |
| imagem_padrao_10KB.bmp | RSA-1024 | CBC | 0.0098 | 0.0210 | 0.0898 | 0.4661 | 0.1090 | 7.9882 | ✅ Não |
| imagem_padrao_10KB.bmp | RSA-1024 | CTR | 0.0098 | 0.0205 | 0.0208 | 0.4782 | 0.4704 | 7.9833 | ✅ Não |
| imagem_padrao_10KB.bmp | RSA-2048 | ECB | 0.0098 | 0.0419 | 0.1376 | 0.2334 | 0.0711 | 7.9870 | ✅ Não |
| imagem_padrao_10KB.bmp | RSA-2048 | CBC | 0.0098 | 0.0231 | 0.1387 | 0.4241 | 0.0706 | 7.9851 | ✅ Não |
| imagem_padrao_10KB.bmp | RSA-2048 | CTR | 0.0098 | 0.0232 | 0.0229 | 0.4223 | 0.4267 | 7.9815 | ✅ Não |
| imagem_padrao_10KB.bmp | RSA-4096 | ECB | 0.0098 | 0.0383 | 0.3426 | 0.2554 | 0.0286 | 7.9844 | ✅ Não |
| imagem_padrao_10KB.bmp | RSA-4096 | CBC | 0.0098 | 0.0372 | 0.3496 | 0.2632 | 0.0280 | 7.9850 | ✅ Não |
| imagem_padrao_10KB.bmp | RSA-4096 | CTR | 0.0098 | 0.0376 | 0.0385 | 0.2602 | 0.2542 | 7.9790 | ✅ Não |
| imagem_padrao_1KB.bmp | AES-128 | ECB | 0.0010 | 0.0006 | 0.0004 | 1.6879 | 2.5320 | 6.5051 | ⚠️ Sim |
| imagem_padrao_1KB.bmp | AES-128 | CBC | 0.0010 | 0.0006 | 0.0005 | 1.6885 | 2.0246 | 7.8401 | ✅ Não |
| imagem_padrao_1KB.bmp | AES-128 | CFB | 0.0010 | 0.0005 | 0.0004 | 2.0257 | 2.5316 | 7.8019 | ✅ Não |
| imagem_padrao_1KB.bmp | AES-128 | OFB | 0.0010 | 0.0006 | 0.0004 | 1.6880 | 2.5316 | 7.8356 | ✅ Não |
| imagem_padrao_1KB.bmp | AES-128 | CTR | 0.0010 | 0.0005 | 0.0005 | 2.0262 | 2.0193 | 7.8176 | ✅ Não |
| imagem_padrao_1KB.bmp | AES-256 | ECB | 0.0010 | 0.0005 | 0.0005 | 2.0264 | 2.0256 | 6.4953 | ⚠️ Sim |
| imagem_padrao_1KB.bmp | AES-256 | CBC | 0.0010 | 0.0006 | 0.0004 | 1.6878 | 2.5325 | 7.8119 | ✅ Não |
| imagem_padrao_1KB.bmp | AES-256 | CFB | 0.0010 | 0.0004 | 0.0006 | 2.5325 | 1.6859 | 7.8302 | ✅ Não |
| imagem_padrao_1KB.bmp | AES-256 | OFB | 0.0010 | 0.0006 | 0.0005 | 1.6882 | 2.2485 | 7.8296 | ✅ Não |
| imagem_padrao_1KB.bmp | AES-256 | CTR | 0.0010 | 0.0005 | 0.0005 | 2.0221 | 2.0261 | 7.7858 | ✅ Não |
| imagem_padrao_1KB.bmp | DES | ECB | 0.0010 | 0.0005 | 0.0005 | 2.0255 | 2.0260 | 5.2783 | ⚠️ Sim |
| imagem_padrao_1KB.bmp | DES | CBC | 0.0010 | 0.0006 | 0.0004 | 1.6881 | 2.5317 | 7.8287 | ✅ Não |
| imagem_padrao_1KB.bmp | DES | CFB | 0.0010 | 0.0009 | 0.0006 | 1.1253 | 1.6881 | 7.8190 | ✅ Não |
| imagem_padrao_1KB.bmp | DES | OFB | 0.0010 | 0.0005 | 0.0005 | 2.0256 | 2.0256 | 7.8349 | ✅ Não |
| imagem_padrao_1KB.bmp | DES | CTR | 0.0010 | 0.0005 | 0.0005 | 2.0257 | 2.0256 | 7.8488 | ✅ Não |
| imagem_padrao_1KB.bmp | 3DES | ECB | 0.0010 | 0.0006 | 0.0005 | 1.6882 | 2.0256 | 5.3330 | ⚠️ Sim |
| imagem_padrao_1KB.bmp | 3DES | CBC | 0.0010 | 0.0006 | 0.0006 | 1.6879 | 1.6868 | 7.8073 | ✅ Não |
| imagem_padrao_1KB.bmp | 3DES | CFB | 0.0010 | 0.0008 | 0.0008 | 1.2660 | 1.3482 | 7.8145 | ✅ Não |
| imagem_padrao_1KB.bmp | 3DES | OFB | 0.0010 | 0.0005 | 0.0005 | 2.0303 | 2.0248 | 7.8134 | ✅ Não |
| imagem_padrao_1KB.bmp | 3DES | CTR | 0.0010 | 0.0006 | 0.0005 | 1.6881 | 2.0258 | 7.7984 | ✅ Não |
| imagem_padrao_1KB.bmp | RSA-1024 | ECB | 0.0010 | 0.0028 | 0.0102 | 0.3619 | 0.0998 | 7.8806 | ✅ Não |
| imagem_padrao_1KB.bmp | RSA-1024 | CBC | 0.0010 | 0.0027 | 0.0099 | 0.3751 | 0.1021 | 7.9021 | ✅ Não |
| imagem_padrao_1KB.bmp | RSA-1024 | CTR | 0.0010 | 0.0028 | 0.0031 | 0.3620 | 0.3319 | 7.8099 | ✅ Não |
| imagem_padrao_1KB.bmp | RSA-2048 | ECB | 0.0010 | 0.0029 | 0.0147 | 0.3492 | 0.0689 | 7.8527 | ✅ Não |
| imagem_padrao_1KB.bmp | RSA-2048 | CBC | 0.0010 | 0.0029 | 0.0150 | 0.3493 | 0.0674 | 7.8606 | ✅ Não |
| imagem_padrao_1KB.bmp | RSA-2048 | CTR | 0.0010 | 0.0030 | 0.0032 | 0.3356 | 0.3172 | 7.7875 | ✅ Não |
| imagem_padrao_1KB.bmp | RSA-4096 | ECB | 0.0010 | 0.0054 | 0.0463 | 0.1890 | 0.0219 | 7.8711 | ✅ Não |
| imagem_padrao_1KB.bmp | RSA-4096 | CBC | 0.0010 | 0.0056 | 0.0616 | 0.1808 | 0.0164 | 7.9103 | ✅ Não |
| imagem_padrao_1KB.bmp | RSA-4096 | CTR | 0.0010 | 0.0063 | 0.0058 | 0.1605 | 0.1760 | 7.8088 | ✅ Não |
| imagem_padrao_1MB.bmp | AES-128 | ECB | 1.0010 | 0.0012 | 0.0013 | 812.0924 | 795.2648 | 5.4843 | ⚠️ Sim |
| imagem_padrao_1MB.bmp | AES-128 | CBC | 1.0010 | 0.0027 | 0.0026 | 371.5021 | 382.5921 | 7.9998 | ✅ Não |
| imagem_padrao_1MB.bmp | AES-128 | CFB | 1.0010 | 0.0185 | 0.0213 | 54.1583 | 47.0681 | 7.9998 | ✅ Não |
| imagem_padrao_1MB.bmp | AES-128 | OFB | 1.0010 | 0.0035 | 0.0032 | 288.0919 | 317.0035 | 7.9998 | ✅ Não |
| imagem_padrao_1MB.bmp | AES-128 | CTR | 1.0010 | 0.0020 | 0.0014 | 504.0372 | 736.1456 | 7.9998 | ✅ Não |
| imagem_padrao_1MB.bmp | AES-256 | ECB | 1.0010 | 0.0011 | 0.0011 | 951.7148 | 877.6872 | 5.6052 | ⚠️ Sim |
| imagem_padrao_1MB.bmp | AES-256 | CBC | 1.0010 | 0.0033 | 0.0027 | 301.8809 | 374.5210 | 7.9998 | ✅ Não |
| imagem_padrao_1MB.bmp | AES-256 | CFB | 1.0010 | 0.0209 | 0.0199 | 47.8557 | 50.2101 | 7.9998 | ✅ Não |
| imagem_padrao_1MB.bmp | AES-256 | OFB | 1.0010 | 0.0028 | 0.0025 | 353.5403 | 406.2859 | 7.9998 | ✅ Não |
| imagem_padrao_1MB.bmp | AES-256 | CTR | 1.0010 | 0.0014 | 0.0016 | 697.3393 | 634.7211 | 7.9998 | ✅ Não |
| imagem_padrao_1MB.bmp | DES | ECB | 1.0010 | 0.0112 | 0.0108 | 89.6518 | 93.0851 | 4.5381 | ⚠️ Sim |
| imagem_padrao_1MB.bmp | DES | CBC | 1.0010 | 0.0136 | 0.0126 | 73.8519 | 79.6322 | 7.9998 | ✅ Não |
| imagem_padrao_1MB.bmp | DES | CFB | 1.0010 | 0.0885 | 0.0829 | 11.3127 | 12.0745 | 7.9998 | ✅ Não |
| imagem_padrao_1MB.bmp | DES | OFB | 1.0010 | 0.0127 | 0.0128 | 78.6645 | 78.4164 | 7.9998 | ✅ Não |
| imagem_padrao_1MB.bmp | DES | CTR | 1.0010 | 0.0116 | 0.0108 | 85.9894 | 92.6109 | 7.9998 | ✅ Não |
| imagem_padrao_1MB.bmp | 3DES | ECB | 1.0010 | 0.0307 | 0.0325 | 32.6347 | 30.8394 | 4.3759 | ⚠️ Sim |
| imagem_padrao_1MB.bmp | 3DES | CBC | 1.0010 | 0.0337 | 0.0322 | 29.7441 | 31.1214 | 7.9998 | ✅ Não |
| imagem_padrao_1MB.bmp | 3DES | CFB | 1.0010 | 0.2483 | 0.2483 | 4.0323 | 4.0317 | 7.9998 | ✅ Não |
| imagem_padrao_1MB.bmp | 3DES | OFB | 1.0010 | 0.0436 | 0.0323 | 22.9363 | 30.9660 | 7.9998 | ✅ Não |
| imagem_padrao_1MB.bmp | 3DES | CTR | 1.0010 | 0.0324 | 0.0314 | 30.9277 | 31.9096 | 7.9998 | ✅ Não |
| imagem_padrao_1MB.bmp | RSA-1024 | ECB | 1.0010 | 1.9748 | 8.7087 | 0.5069 | 0.1149 | 7.9999 | ✅ Não |
| imagem_padrao_1MB.bmp | RSA-1024 | CBC | 1.0010 | 2.0366 | 8.8588 | 0.4915 | 0.1130 | 7.9999 | ✅ Não |
| imagem_padrao_1MB.bmp | RSA-1024 | CTR | 1.0010 | 2.0506 | 2.0239 | 0.4882 | 0.4946 | 7.9998 | ✅ Não |
| imagem_padrao_1MB.bmp | RSA-2048 | ECB | 1.0010 | 2.2353 | 13.9291 | 0.4478 | 0.0719 | 7.9999 | ✅ Não |
| imagem_padrao_1MB.bmp | RSA-2048 | CBC | 1.0010 | 2.3135 | 13.9724 | 0.4327 | 0.0716 | 7.9998 | ✅ Não |
| imagem_padrao_1MB.bmp | RSA-2048 | CTR | 1.0010 | 2.2877 | 2.2959 | 0.4376 | 0.4360 | 7.9998 | ✅ Não |
| imagem_padrao_1MB.bmp | RSA-4096 | ECB | 1.0010 | 3.5203 | 34.0466 | 0.2844 | 0.0294 | 7.9998 | ✅ Não |
| imagem_padrao_1MB.bmp | RSA-4096 | CBC | 1.0010 | 3.5864 | 34.1484 | 0.2791 | 0.0293 | 7.9998 | ✅ Não |
| imagem_padrao_1MB.bmp | RSA-4096 | CTR | 1.0010 | 3.5778 | 3.5647 | 0.2798 | 0.2808 | 7.9998 | ✅ Não |
| texto_aleatorio_100KB.txt | AES-128 | ECB | 0.0977 | 0.0006 | 0.0006 | 152.1489 | 173.8983 | 7.9984 | ✅ Não |
| texto_aleatorio_100KB.txt | AES-128 | CBC | 0.0977 | 0.0009 | 0.0007 | 107.6111 | 135.0345 | 7.9980 | ✅ Não |
| texto_aleatorio_100KB.txt | AES-128 | CFB | 0.0977 | 0.0024 | 0.0023 | 41.3474 | 42.0448 | 7.9982 | ✅ Não |
| texto_aleatorio_100KB.txt | AES-128 | OFB | 0.0977 | 0.0008 | 0.0007 | 127.8562 | 130.7457 | 7.9980 | ✅ Não |
| texto_aleatorio_100KB.txt | AES-128 | CTR | 0.0977 | 0.0007 | 0.0007 | 139.7046 | 130.7039 | 7.9981 | ✅ Não |
| texto_aleatorio_100KB.txt | AES-256 | ECB | 0.0977 | 0.0005 | 0.0006 | 189.5682 | 152.0867 | 7.9982 | ✅ Não |
| texto_aleatorio_100KB.txt | AES-256 | CBC | 0.0977 | 0.0008 | 0.0008 | 124.3662 | 126.2055 | 7.9981 | ✅ Não |
| texto_aleatorio_100KB.txt | AES-256 | CFB | 0.0977 | 0.0026 | 0.0025 | 37.9857 | 38.7200 | 7.9985 | ✅ Não |
| texto_aleatorio_100KB.txt | AES-256 | OFB | 0.0977 | 0.0009 | 0.0008 | 112.4194 | 126.7758 | 7.9983 | ✅ Não |
| texto_aleatorio_100KB.txt | AES-256 | CTR | 0.0977 | 0.0007 | 0.0007 | 139.5476 | 132.6339 | 7.9981 | ✅ Não |
| texto_aleatorio_100KB.txt | DES | ECB | 0.0977 | 0.0016 | 0.0017 | 59.7267 | 58.8269 | 7.9981 | ✅ Não |
| texto_aleatorio_100KB.txt | DES | CBC | 0.0977 | 0.0019 | 0.0018 | 51.4030 | 54.7755 | 7.9982 | ✅ Não |
| texto_aleatorio_100KB.txt | DES | CFB | 0.0977 | 0.0091 | 0.0087 | 10.6917 | 11.2121 | 7.9982 | ✅ Não |
| texto_aleatorio_100KB.txt | DES | OFB | 0.0977 | 0.0020 | 0.0021 | 49.2681 | 45.8679 | 7.9984 | ✅ Não |
| texto_aleatorio_100KB.txt | DES | CTR | 0.0977 | 0.0021 | 0.0017 | 46.2689 | 56.1827 | 7.9979 | ✅ Não |
| texto_aleatorio_100KB.txt | 3DES | ECB | 0.0977 | 0.0036 | 0.0035 | 26.9376 | 28.1836 | 7.9982 | ✅ Não |
| texto_aleatorio_100KB.txt | 3DES | CBC | 0.0977 | 0.0040 | 0.0037 | 24.6806 | 26.4192 | 7.9981 | ✅ Não |
| texto_aleatorio_100KB.txt | 3DES | CFB | 0.0977 | 0.0299 | 0.0248 | 3.2653 | 3.9445 | 7.9983 | ✅ Não |
| texto_aleatorio_100KB.txt | 3DES | OFB | 0.0977 | 0.0039 | 0.0039 | 24.7233 | 24.8891 | 7.9981 | ✅ Não |
| texto_aleatorio_100KB.txt | 3DES | CTR | 0.0977 | 0.0038 | 0.0035 | 25.5374 | 27.9430 | 7.9984 | ✅ Não |
| texto_aleatorio_100KB.txt | RSA-1024 | ECB | 0.0977 | 0.1984 | 0.8736 | 0.4921 | 0.1118 | 7.9988 | ✅ Não |
| texto_aleatorio_100KB.txt | RSA-1024 | CBC | 0.0977 | 0.2041 | 0.8677 | 0.4785 | 0.1125 | 7.9988 | ✅ Não |
| texto_aleatorio_100KB.txt | RSA-1024 | CTR | 0.0977 | 0.2099 | 0.2047 | 0.4653 | 0.4771 | 7.9983 | ✅ Não |
| texto_aleatorio_100KB.txt | RSA-2048 | ECB | 0.0977 | 0.2218 | 1.3763 | 0.4404 | 0.0710 | 7.9988 | ✅ Não |
| texto_aleatorio_100KB.txt | RSA-2048 | CBC | 0.0977 | 0.2273 | 1.3779 | 0.4296 | 0.0709 | 7.9985 | ✅ Não |
| texto_aleatorio_100KB.txt | RSA-2048 | CTR | 0.0977 | 0.2286 | 0.2257 | 0.4271 | 0.4326 | 7.9983 | ✅ Não |
| texto_aleatorio_100KB.txt | RSA-4096 | ECB | 0.0977 | 0.3854 | 3.3172 | 0.2534 | 0.0294 | 7.9982 | ✅ Não |
| texto_aleatorio_100KB.txt | RSA-4096 | CBC | 0.0977 | 0.3465 | 3.3371 | 0.2818 | 0.0293 | 7.9983 | ✅ Não |
| texto_aleatorio_100KB.txt | RSA-4096 | CTR | 0.0977 | 0.3532 | 0.3613 | 0.2765 | 0.2703 | 7.9982 | ✅ Não |
| texto_aleatorio_10KB.txt | AES-128 | ECB | 0.0098 | 0.0006 | 0.0006 | 17.6400 | 17.3420 | 7.9801 | ✅ Não |
| texto_aleatorio_10KB.txt | AES-128 | CBC | 0.0098 | 0.0006 | 0.0007 | 15.8667 | 14.4577 | 7.9792 | ✅ Não |
| texto_aleatorio_10KB.txt | AES-128 | CFB | 0.0098 | 0.0008 | 0.0007 | 12.4882 | 14.2227 | 7.9816 | ✅ Não |
| texto_aleatorio_10KB.txt | AES-128 | OFB | 0.0098 | 0.0007 | 0.0005 | 14.4817 | 20.2382 | 7.9814 | ✅ Não |
| texto_aleatorio_10KB.txt | AES-128 | CTR | 0.0098 | 0.0006 | 0.0005 | 15.6731 | 19.8690 | 7.9842 | ✅ Não |
| texto_aleatorio_10KB.txt | AES-256 | ECB | 0.0098 | 0.0005 | 0.0005 | 18.5987 | 19.8932 | 7.9853 | ✅ Não |
| texto_aleatorio_10KB.txt | AES-256 | CBC | 0.0098 | 0.0006 | 0.0005 | 17.5824 | 18.1456 | 7.9862 | ✅ Não |
| texto_aleatorio_10KB.txt | AES-256 | CFB | 0.0098 | 0.0007 | 0.0007 | 13.1269 | 14.0906 | 7.9816 | ✅ Não |
| texto_aleatorio_10KB.txt | AES-256 | OFB | 0.0098 | 0.0006 | 0.0005 | 16.6376 | 20.4350 | 7.9821 | ✅ Não |
| texto_aleatorio_10KB.txt | AES-256 | CTR | 0.0098 | 0.0006 | 0.0005 | 15.6169 | 18.6836 | 7.9829 | ✅ Não |
| texto_aleatorio_10KB.txt | DES | ECB | 0.0098 | 0.0006 | 0.0006 | 16.9747 | 15.8080 | 7.9810 | ✅ Não |
| texto_aleatorio_10KB.txt | DES | CBC | 0.0098 | 0.0007 | 0.0006 | 13.2197 | 16.0414 | 7.9814 | ✅ Não |
| texto_aleatorio_10KB.txt | DES | CFB | 0.0098 | 0.0014 | 0.0013 | 6.7809 | 7.4710 | 7.9806 | ✅ Não |
| texto_aleatorio_10KB.txt | DES | OFB | 0.0098 | 0.0007 | 0.0006 | 14.6805 | 15.3742 | 7.9813 | ✅ Não |
| texto_aleatorio_10KB.txt | DES | CTR | 0.0098 | 0.0007 | 0.0006 | 13.9041 | 16.0483 | 7.9819 | ✅ Não |
| texto_aleatorio_10KB.txt | 3DES | ECB | 0.0098 | 0.0008 | 0.0009 | 11.8265 | 11.2887 | 7.9800 | ✅ Não |
| texto_aleatorio_10KB.txt | 3DES | CBC | 0.0098 | 0.0009 | 0.0010 | 11.2918 | 10.1323 | 7.9809 | ✅ Não |
| texto_aleatorio_10KB.txt | 3DES | CFB | 0.0098 | 0.0031 | 0.0029 | 3.1801 | 3.3161 | 7.9821 | ✅ Não |
| texto_aleatorio_10KB.txt | 3DES | OFB | 0.0098 | 0.0009 | 0.0009 | 10.9323 | 11.1450 | 7.9804 | ✅ Não |
| texto_aleatorio_10KB.txt | 3DES | CTR | 0.0098 | 0.0010 | 0.0010 | 9.9386 | 9.3736 | 7.9828 | ✅ Não |
| texto_aleatorio_10KB.txt | RSA-1024 | ECB | 0.0098 | 0.0203 | 0.0886 | 0.4810 | 0.1102 | 7.9875 | ✅ Não |
| texto_aleatorio_10KB.txt | RSA-1024 | CBC | 0.0098 | 0.0213 | 0.0885 | 0.4585 | 0.1104 | 7.9880 | ✅ Não |
| texto_aleatorio_10KB.txt | RSA-1024 | CTR | 0.0098 | 0.0212 | 0.0210 | 0.4604 | 0.4651 | 7.9837 | ✅ Não |
| texto_aleatorio_10KB.txt | RSA-2048 | ECB | 0.0098 | 0.0295 | 0.1383 | 0.3313 | 0.0706 | 7.9862 | ✅ Não |
| texto_aleatorio_10KB.txt | RSA-2048 | CBC | 0.0098 | 0.0236 | 0.1407 | 0.4130 | 0.0694 | 7.9851 | ✅ Não |
| texto_aleatorio_10KB.txt | RSA-2048 | CTR | 0.0098 | 0.0235 | 0.0234 | 0.4162 | 0.4171 | 7.9826 | ✅ Não |
| texto_aleatorio_10KB.txt | RSA-4096 | ECB | 0.0098 | 0.0358 | 0.3404 | 0.2728 | 0.0287 | 7.9850 | ✅ Não |
| texto_aleatorio_10KB.txt | RSA-4096 | CBC | 0.0098 | 0.0368 | 0.3363 | 0.2655 | 0.0290 | 7.9849 | ✅ Não |
| texto_aleatorio_10KB.txt | RSA-4096 | CTR | 0.0098 | 0.0383 | 0.0370 | 0.2548 | 0.2637 | 7.9806 | ✅ Não |
| texto_aleatorio_1KB.txt | AES-128 | ECB | 0.0010 | 0.0006 | 0.0004 | 1.6276 | 2.4414 | 7.7973 | ✅ Não |
| texto_aleatorio_1KB.txt | AES-128 | CBC | 0.0010 | 0.0005 | 0.0005 | 1.9515 | 1.9541 | 7.8491 | ✅ Não |
| texto_aleatorio_1KB.txt | AES-128 | CFB | 0.0010 | 0.0005 | 0.0005 | 1.9365 | 1.9604 | 7.8120 | ✅ Não |
| texto_aleatorio_1KB.txt | AES-128 | OFB | 0.0010 | 0.0005 | 0.0006 | 1.9534 | 1.7727 | 7.8094 | ✅ Não |
| texto_aleatorio_1KB.txt | AES-128 | CTR | 0.0010 | 0.0005 | 0.0005 | 1.9534 | 1.9536 | 7.8291 | ✅ Não |
| texto_aleatorio_1KB.txt | AES-256 | ECB | 0.0010 | 0.0004 | 0.0005 | 2.4414 | 1.9533 | 7.8008 | ✅ Não |
| texto_aleatorio_1KB.txt | AES-256 | CBC | 0.0010 | 0.0005 | 0.0004 | 1.9545 | 2.4413 | 7.8142 | ✅ Não |
| texto_aleatorio_1KB.txt | AES-256 | CFB | 0.0010 | 0.0006 | 0.0005 | 1.6269 | 1.9536 | 7.8068 | ✅ Não |
| texto_aleatorio_1KB.txt | AES-256 | OFB | 0.0010 | 0.0005 | 0.0005 | 1.9525 | 1.9529 | 7.8239 | ✅ Não |
| texto_aleatorio_1KB.txt | AES-256 | CTR | 0.0010 | 0.0005 | 0.0005 | 1.9535 | 1.9535 | 7.8122 | ✅ Não |
| texto_aleatorio_1KB.txt | DES | ECB | 0.0010 | 0.0006 | 0.0005 | 1.6242 | 1.9574 | 7.8056 | ✅ Não |
| texto_aleatorio_1KB.txt | DES | CBC | 0.0010 | 0.0005 | 0.0006 | 1.9540 | 1.6262 | 7.8049 | ✅ Não |
| texto_aleatorio_1KB.txt | DES | CFB | 0.0010 | 0.0005 | 0.0006 | 1.9538 | 1.6274 | 7.8128 | ✅ Não |
| texto_aleatorio_1KB.txt | DES | OFB | 0.0010 | 0.0005 | 0.0005 | 2.1642 | 1.9539 | 7.8085 | ✅ Não |
| texto_aleatorio_1KB.txt | DES | CTR | 0.0010 | 0.0006 | 0.0006 | 1.6276 | 1.6224 | 7.8327 | ✅ Não |
| texto_aleatorio_1KB.txt | 3DES | ECB | 0.0010 | 0.0006 | 0.0006 | 1.6328 | 1.6277 | 7.8095 | ✅ Não |
| texto_aleatorio_1KB.txt | 3DES | CBC | 0.0010 | 0.0006 | 0.0005 | 1.6269 | 1.9534 | 7.8021 | ✅ Não |
| texto_aleatorio_1KB.txt | 3DES | CFB | 0.0010 | 0.0007 | 0.0007 | 1.3953 | 1.3952 | 7.8262 | ✅ Não |
| texto_aleatorio_1KB.txt | 3DES | OFB | 0.0010 | 0.0005 | 0.0006 | 1.9523 | 1.6282 | 7.8331 | ✅ Não |
| texto_aleatorio_1KB.txt | 3DES | CTR | 0.0010 | 0.0005 | 0.0006 | 1.9532 | 1.6265 | 7.8174 | ✅ Não |
| texto_aleatorio_1KB.txt | RSA-1024 | ECB | 0.0010 | 0.0024 | 0.0096 | 0.4069 | 0.1017 | 7.8667 | ✅ Não |
| texto_aleatorio_1KB.txt | RSA-1024 | CBC | 0.0010 | 0.0026 | 0.0092 | 0.3756 | 0.1067 | 7.8917 | ✅ Não |
| texto_aleatorio_1KB.txt | RSA-1024 | CTR | 0.0010 | 0.0025 | 0.0030 | 0.3907 | 0.3309 | 7.8083 | ✅ Não |
| texto_aleatorio_1KB.txt | RSA-2048 | ECB | 0.0010 | 0.0028 | 0.0163 | 0.3487 | 0.0599 | 7.8439 | ✅ Não |
| texto_aleatorio_1KB.txt | RSA-2048 | CBC | 0.0010 | 0.0030 | 0.0148 | 0.3254 | 0.0660 | 7.8541 | ✅ Não |
| texto_aleatorio_1KB.txt | RSA-2048 | CTR | 0.0010 | 0.0029 | 0.0031 | 0.3368 | 0.3149 | 7.8007 | ✅ Não |
| texto_aleatorio_1KB.txt | RSA-4096 | ECB | 0.0010 | 0.0058 | 0.0461 | 0.1692 | 0.0212 | 7.8620 | ✅ Não |
| texto_aleatorio_1KB.txt | RSA-4096 | CBC | 0.0010 | 0.0058 | 0.0483 | 0.1698 | 0.0202 | 7.9149 | ✅ Não |
| texto_aleatorio_1KB.txt | RSA-4096 | CTR | 0.0010 | 0.0055 | 0.0057 | 0.1790 | 0.1728 | 7.8153 | ✅ Não |
| texto_aleatorio_1MB.txt | AES-128 | ECB | 1.0000 | 0.0012 | 0.0012 | 845.2509 | 844.7402 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | AES-128 | CBC | 1.0000 | 0.0026 | 0.0025 | 391.1028 | 398.6450 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | AES-128 | CFB | 1.0000 | 0.0170 | 0.0170 | 58.6606 | 58.7884 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | AES-128 | OFB | 1.0000 | 0.0026 | 0.0023 | 386.8285 | 431.0870 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | AES-128 | CTR | 1.0000 | 0.0015 | 0.0014 | 670.0059 | 723.0686 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | AES-256 | ECB | 1.0000 | 0.0012 | 0.0011 | 817.8263 | 942.9640 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | AES-256 | CBC | 1.0000 | 0.0029 | 0.0027 | 344.2977 | 368.4288 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | AES-256 | CFB | 1.0000 | 0.0208 | 0.0201 | 48.1689 | 49.8473 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | AES-256 | OFB | 1.0000 | 0.0028 | 0.0024 | 354.3654 | 409.0527 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | AES-256 | CTR | 1.0000 | 0.0014 | 0.0014 | 712.6867 | 690.2045 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | DES | ECB | 1.0000 | 0.0107 | 0.0113 | 93.3445 | 88.3279 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | DES | CBC | 1.0000 | 0.0166 | 0.0124 | 60.3787 | 80.9288 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | DES | CFB | 1.0000 | 0.0862 | 0.0828 | 11.6045 | 12.0803 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | DES | OFB | 1.0000 | 0.0141 | 0.0128 | 71.0776 | 77.9447 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | DES | CTR | 1.0000 | 0.0119 | 0.0144 | 84.3812 | 69.2632 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | 3DES | ECB | 1.0000 | 0.0307 | 0.0320 | 32.5461 | 31.2797 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | 3DES | CBC | 1.0000 | 0.0339 | 0.0335 | 29.5227 | 29.8684 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | 3DES | CFB | 1.0000 | 0.2467 | 0.2443 | 4.0535 | 4.0938 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | 3DES | OFB | 1.0000 | 0.0330 | 0.0332 | 30.2573 | 30.1395 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | 3DES | CTR | 1.0000 | 0.0317 | 0.0312 | 31.5919 | 32.0358 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | RSA-1024 | ECB | 1.0000 | 1.9992 | 8.8352 | 0.5002 | 0.1132 | 7.9999 | ✅ Não |
| texto_aleatorio_1MB.txt | RSA-1024 | CBC | 1.0000 | 2.0520 | 8.9264 | 0.4873 | 0.1120 | 7.9999 | ✅ Não |
| texto_aleatorio_1MB.txt | RSA-1024 | CTR | 1.0000 | 2.0707 | 2.0599 | 0.4829 | 0.4855 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | RSA-2048 | ECB | 1.0000 | 2.2687 | 13.9806 | 0.4408 | 0.0715 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | RSA-2048 | CBC | 1.0000 | 2.3733 | 14.1060 | 0.4214 | 0.0709 | 7.9999 | ✅ Não |
| texto_aleatorio_1MB.txt | RSA-2048 | CTR | 1.0000 | 2.3686 | 2.3297 | 0.4222 | 0.4292 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | RSA-4096 | ECB | 1.0000 | 3.5926 | 34.2724 | 0.2783 | 0.0292 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | RSA-4096 | CBC | 1.0000 | 3.6617 | 34.3287 | 0.2731 | 0.0291 | 7.9998 | ✅ Não |
| texto_aleatorio_1MB.txt | RSA-4096 | CTR | 1.0000 | 3.6506 | 3.6593 | 0.2739 | 0.2733 | 7.9998 | ✅ Não |
| texto_natural_100KB.txt | AES-128 | ECB | 0.0977 | 0.0006 | 0.0005 | 165.0083 | 195.5785 | 7.9004 | ✅ Não |
| texto_natural_100KB.txt | AES-128 | CBC | 0.0977 | 0.0017 | 0.0008 | 56.1396 | 121.2983 | 7.9982 | ✅ Não |
| texto_natural_100KB.txt | AES-128 | CFB | 0.0977 | 0.0024 | 0.0022 | 40.3300 | 44.0530 | 7.9983 | ✅ Não |
| texto_natural_100KB.txt | AES-128 | OFB | 0.0977 | 0.0008 | 0.0011 | 123.9372 | 88.0728 | 7.9982 | ✅ Não |
| texto_natural_100KB.txt | AES-128 | CTR | 0.0977 | 0.0008 | 0.0006 | 115.2731 | 172.9511 | 7.9984 | ✅ Não |
| texto_natural_100KB.txt | AES-256 | ECB | 0.0977 | 0.0007 | 0.0007 | 144.6430 | 145.1556 | 7.8858 | ✅ Não |
| texto_natural_100KB.txt | AES-256 | CBC | 0.0977 | 0.0009 | 0.0007 | 113.2274 | 133.6030 | 7.9983 | ✅ Não |
| texto_natural_100KB.txt | AES-256 | CFB | 0.0977 | 0.0027 | 0.0025 | 35.8876 | 38.7058 | 7.9983 | ✅ Não |
| texto_natural_100KB.txt | AES-256 | OFB | 0.0977 | 0.0007 | 0.0007 | 130.6914 | 139.4810 | 7.9983 | ✅ Não |
| texto_natural_100KB.txt | AES-256 | CTR | 0.0977 | 0.0010 | 0.0008 | 97.1191 | 122.7082 | 7.9981 | ✅ Não |
| texto_natural_100KB.txt | DES | ECB | 0.0977 | 0.0018 | 0.0019 | 55.7196 | 52.2709 | 7.7607 | ✅ Não |
| texto_natural_100KB.txt | DES | CBC | 0.0977 | 0.0020 | 0.0020 | 49.1605 | 49.6352 | 7.9982 | ✅ Não |
| texto_natural_100KB.txt | DES | CFB | 0.0977 | 0.0094 | 0.0091 | 10.3787 | 10.7498 | 7.9981 | ✅ Não |
| texto_natural_100KB.txt | DES | OFB | 0.0977 | 0.0019 | 0.0021 | 50.2478 | 46.9160 | 7.9982 | ✅ Não |
| texto_natural_100KB.txt | DES | CTR | 0.0977 | 0.0021 | 0.0017 | 45.9940 | 56.2259 | 7.9984 | ✅ Não |
| texto_natural_100KB.txt | 3DES | ECB | 0.0977 | 0.0037 | 0.0037 | 26.6531 | 26.4670 | 7.7635 | ✅ Não |
| texto_natural_100KB.txt | 3DES | CBC | 0.0977 | 0.0040 | 0.0038 | 24.3337 | 25.9905 | 7.9983 | ✅ Não |
| texto_natural_100KB.txt | 3DES | CFB | 0.0977 | 0.0253 | 0.0244 | 3.8657 | 3.9962 | 7.9982 | ✅ Não |
| texto_natural_100KB.txt | 3DES | OFB | 0.0977 | 0.0040 | 0.0038 | 24.7213 | 25.9452 | 7.9986 | ✅ Não |
| texto_natural_100KB.txt | 3DES | CTR | 0.0977 | 0.0039 | 0.0037 | 25.2592 | 26.5715 | 7.9985 | ✅ Não |
| texto_natural_100KB.txt | RSA-1024 | ECB | 0.0977 | 0.1957 | 0.8661 | 0.4990 | 0.1128 | 7.9988 | ✅ Não |
| texto_natural_100KB.txt | RSA-1024 | CBC | 0.0977 | 0.2018 | 0.8765 | 0.4839 | 0.1114 | 7.9988 | ✅ Não |
| texto_natural_100KB.txt | RSA-1024 | CTR | 0.0977 | 0.2196 | 0.2004 | 0.4446 | 0.4874 | 7.9981 | ✅ Não |
| texto_natural_100KB.txt | RSA-2048 | ECB | 0.0977 | 0.2293 | 1.3955 | 0.4258 | 0.0700 | 7.9985 | ✅ Não |
| texto_natural_100KB.txt | RSA-2048 | CBC | 0.0977 | 0.2440 | 1.3856 | 0.4003 | 0.0705 | 7.9985 | ✅ Não |
| texto_natural_100KB.txt | RSA-2048 | CTR | 0.0977 | 0.2345 | 0.2347 | 0.4165 | 0.4162 | 7.9980 | ✅ Não |
| texto_natural_100KB.txt | RSA-4096 | ECB | 0.0977 | 0.3439 | 3.3380 | 0.2840 | 0.0293 | 7.9984 | ✅ Não |
| texto_natural_100KB.txt | RSA-4096 | CBC | 0.0977 | 0.3467 | 3.3328 | 0.2816 | 0.0293 | 7.9984 | ✅ Não |
| texto_natural_100KB.txt | RSA-4096 | CTR | 0.0977 | 0.3492 | 0.3610 | 0.2797 | 0.2705 | 7.9982 | ✅ Não |
| texto_natural_10KB.txt | AES-128 | ECB | 0.0098 | 0.0005 | 0.0005 | 20.5974 | 20.9140 | 7.8747 | ✅ Não |
| texto_natural_10KB.txt | AES-128 | CBC | 0.0098 | 0.0007 | 0.0005 | 13.8711 | 18.4173 | 7.9812 | ✅ Não |
| texto_natural_10KB.txt | AES-128 | CFB | 0.0098 | 0.0008 | 0.0007 | 12.8850 | 13.3425 | 7.9845 | ✅ Não |
| texto_natural_10KB.txt | AES-128 | OFB | 0.0098 | 0.0007 | 0.0006 | 13.2437 | 16.6119 | 7.9821 | ✅ Não |
| texto_natural_10KB.txt | AES-128 | CTR | 0.0098 | 0.0005 | 0.0007 | 18.2101 | 14.3102 | 7.9825 | ✅ Não |
| texto_natural_10KB.txt | AES-256 | ECB | 0.0098 | 0.0005 | 0.0006 | 18.2044 | 16.7704 | 7.8845 | ✅ Não |
| texto_natural_10KB.txt | AES-256 | CBC | 0.0098 | 0.0006 | 0.0005 | 15.0877 | 18.5365 | 7.9820 | ✅ Não |
| texto_natural_10KB.txt | AES-256 | CFB | 0.0098 | 0.0009 | 0.0007 | 11.0544 | 13.1624 | 7.9838 | ✅ Não |
| texto_natural_10KB.txt | AES-256 | OFB | 0.0098 | 0.0007 | 0.0005 | 14.8740 | 20.3599 | 7.9838 | ✅ Não |
| texto_natural_10KB.txt | AES-256 | CTR | 0.0098 | 0.0005 | 0.0006 | 18.3644 | 16.3383 | 7.9840 | ✅ Não |
| texto_natural_10KB.txt | DES | ECB | 0.0098 | 0.0006 | 0.0006 | 15.1980 | 16.5395 | 7.7805 | ✅ Não |
| texto_natural_10KB.txt | DES | CBC | 0.0098 | 0.0007 | 0.0007 | 13.7468 | 14.0785 | 7.9826 | ✅ Não |
| texto_natural_10KB.txt | DES | CFB | 0.0098 | 0.0016 | 0.0014 | 6.2950 | 7.0904 | 7.9822 | ✅ Não |
| texto_natural_10KB.txt | DES | OFB | 0.0098 | 0.0007 | 0.0006 | 13.9258 | 15.2285 | 7.9816 | ✅ Não |
| texto_natural_10KB.txt | DES | CTR | 0.0098 | 0.0007 | 0.0007 | 14.1329 | 14.1373 | 7.9804 | ✅ Não |
| texto_natural_10KB.txt | 3DES | ECB | 0.0098 | 0.0008 | 0.0010 | 11.8402 | 10.2633 | 7.7215 | ✅ Não |
| texto_natural_10KB.txt | 3DES | CBC | 0.0098 | 0.0010 | 0.0009 | 9.5688 | 10.8650 | 7.9834 | ✅ Não |
| texto_natural_10KB.txt | 3DES | CFB | 0.0098 | 0.0032 | 0.0029 | 3.0315 | 3.3638 | 7.9831 | ✅ Não |
| texto_natural_10KB.txt | 3DES | OFB | 0.0098 | 0.0010 | 0.0011 | 10.2667 | 9.2122 | 7.9834 | ✅ Não |
| texto_natural_10KB.txt | 3DES | CTR | 0.0098 | 0.0011 | 0.0011 | 9.0384 | 9.2234 | 7.9849 | ✅ Não |
| texto_natural_10KB.txt | RSA-1024 | ECB | 0.0098 | 0.0203 | 0.0873 | 0.4813 | 0.1119 | 7.9880 | ✅ Não |
| texto_natural_10KB.txt | RSA-1024 | CBC | 0.0098 | 0.0217 | 0.0945 | 0.4503 | 0.1034 | 7.9882 | ✅ Não |
| texto_natural_10KB.txt | RSA-1024 | CTR | 0.0098 | 0.0206 | 0.0206 | 0.4735 | 0.4730 | 7.9818 | ✅ Não |
| texto_natural_10KB.txt | RSA-2048 | ECB | 0.0098 | 0.0285 | 0.1416 | 0.3425 | 0.0690 | 7.9864 | ✅ Não |
| texto_natural_10KB.txt | RSA-2048 | CBC | 0.0098 | 0.0233 | 0.1384 | 0.4183 | 0.0706 | 7.9842 | ✅ Não |
| texto_natural_10KB.txt | RSA-2048 | CTR | 0.0098 | 0.0241 | 0.0237 | 0.4054 | 0.4123 | 7.9838 | ✅ Não |
| texto_natural_10KB.txt | RSA-4096 | ECB | 0.0098 | 0.0369 | 0.3407 | 0.2643 | 0.0287 | 7.9803 | ✅ Não |
| texto_natural_10KB.txt | RSA-4096 | CBC | 0.0098 | 0.0353 | 0.3348 | 0.2764 | 0.0292 | 7.9845 | ✅ Não |
| texto_natural_10KB.txt | RSA-4096 | CTR | 0.0098 | 0.0389 | 0.0353 | 0.2514 | 0.2764 | 7.9858 | ✅ Não |
| texto_natural_1KB.txt | AES-128 | ECB | 0.0010 | 0.0005 | 0.0005 | 1.9532 | 1.9522 | 7.8152 | ✅ Não |
| texto_natural_1KB.txt | AES-128 | CBC | 0.0010 | 0.0006 | 0.0006 | 1.6267 | 1.7746 | 7.8369 | ✅ Não |
| texto_natural_1KB.txt | AES-128 | CFB | 0.0010 | 0.0006 | 0.0005 | 1.6253 | 1.9547 | 7.7910 | ✅ Não |
| texto_natural_1KB.txt | AES-128 | OFB | 0.0010 | 0.0006 | 0.0005 | 1.6270 | 1.9537 | 7.8068 | ✅ Não |
| texto_natural_1KB.txt | AES-128 | CTR | 0.0010 | 0.0004 | 0.0005 | 2.4416 | 1.9528 | 7.8124 | ✅ Não |
| texto_natural_1KB.txt | AES-256 | ECB | 0.0010 | 0.0006 | 0.0005 | 1.6261 | 1.9547 | 7.8470 | ✅ Não |
| texto_natural_1KB.txt | AES-256 | CBC | 0.0010 | 0.0005 | 0.0005 | 1.9531 | 1.9530 | 7.8364 | ✅ Não |
| texto_natural_1KB.txt | AES-256 | CFB | 0.0010 | 0.0005 | 0.0005 | 1.9521 | 1.9546 | 7.7939 | ✅ Não |
| texto_natural_1KB.txt | AES-256 | OFB | 0.0010 | 0.0006 | 0.0005 | 1.6271 | 1.9531 | 7.7897 | ✅ Não |
| texto_natural_1KB.txt | AES-256 | CTR | 0.0010 | 0.0006 | 0.0005 | 1.6269 | 1.9508 | 7.8491 | ✅ Não |
| texto_natural_1KB.txt | DES | ECB | 0.0010 | 0.0005 | 0.0005 | 1.9527 | 1.9535 | 7.7651 | ✅ Não |
| texto_natural_1KB.txt | DES | CBC | 0.0010 | 0.0006 | 0.0004 | 1.6048 | 2.4420 | 7.8221 | ✅ Não |
| texto_natural_1KB.txt | DES | CFB | 0.0010 | 0.0005 | 0.0006 | 1.9527 | 1.6277 | 7.8066 | ✅ Não |
| texto_natural_1KB.txt | DES | OFB | 0.0010 | 0.0005 | 0.0005 | 1.9536 | 1.9534 | 7.8319 | ✅ Não |
| texto_natural_1KB.txt | DES | CTR | 0.0010 | 0.0006 | 0.0005 | 1.6280 | 1.9534 | 7.7823 | ✅ Não |
| texto_natural_1KB.txt | 3DES | ECB | 0.0010 | 0.0005 | 0.0006 | 1.9531 | 1.6276 | 7.7766 | ✅ Não |
| texto_natural_1KB.txt | 3DES | CBC | 0.0010 | 0.0005 | 0.0005 | 1.9532 | 1.9527 | 7.8085 | ✅ Não |
| texto_natural_1KB.txt | 3DES | CFB | 0.0010 | 0.0007 | 0.0008 | 1.3952 | 1.2208 | 7.7800 | ✅ Não |
| texto_natural_1KB.txt | 3DES | OFB | 0.0010 | 0.0006 | 0.0005 | 1.6224 | 1.9519 | 7.8040 | ✅ Não |
| texto_natural_1KB.txt | 3DES | CTR | 0.0010 | 0.0005 | 0.0006 | 1.9521 | 1.7735 | 7.8146 | ✅ Não |
| texto_natural_1KB.txt | RSA-1024 | ECB | 0.0010 | 0.0029 | 0.0091 | 0.3368 | 0.1070 | 7.8660 | ✅ Não |
| texto_natural_1KB.txt | RSA-1024 | CBC | 0.0010 | 0.0026 | 0.0094 | 0.3756 | 0.1044 | 7.8824 | ✅ Não |
| texto_natural_1KB.txt | RSA-1024 | CTR | 0.0010 | 0.0027 | 0.0032 | 0.3616 | 0.3098 | 7.8101 | ✅ Não |
| texto_natural_1KB.txt | RSA-2048 | ECB | 0.0010 | 0.0030 | 0.0153 | 0.3255 | 0.0640 | 7.8573 | ✅ Não |
| texto_natural_1KB.txt | RSA-2048 | CBC | 0.0010 | 0.0034 | 0.0164 | 0.2872 | 0.0596 | 7.8751 | ✅ Não |
| texto_natural_1KB.txt | RSA-2048 | CTR | 0.0010 | 0.0030 | 0.0032 | 0.3256 | 0.3052 | 7.7772 | ✅ Não |
| texto_natural_1KB.txt | RSA-4096 | ECB | 0.0010 | 0.0058 | 0.0471 | 0.1698 | 0.0207 | 7.8716 | ✅ Não |
| texto_natural_1KB.txt | RSA-4096 | CBC | 0.0010 | 0.0056 | 0.0486 | 0.1759 | 0.0201 | 7.9130 | ✅ Não |
| texto_natural_1KB.txt | RSA-4096 | CTR | 0.0010 | 0.0057 | 0.0057 | 0.1728 | 0.1728 | 7.8068 | ✅ Não |
| texto_natural_1MB.txt | AES-128 | ECB | 1.0000 | 0.0012 | 0.0012 | 824.3522 | 852.1371 | 7.8962 | ✅ Não |
| texto_natural_1MB.txt | AES-128 | CBC | 1.0000 | 0.0026 | 0.0025 | 390.8076 | 406.2201 | 7.9998 | ✅ Não |
| texto_natural_1MB.txt | AES-128 | CFB | 1.0000 | 0.0174 | 0.0268 | 57.6012 | 37.3641 | 7.9998 | ✅ Não |
| texto_natural_1MB.txt | AES-128 | OFB | 1.0000 | 0.0026 | 0.0023 | 384.2345 | 433.0498 | 7.9998 | ✅ Não |
| texto_natural_1MB.txt | AES-128 | CTR | 1.0000 | 0.0015 | 0.0016 | 675.9446 | 624.9335 | 7.9998 | ✅ Não |
| texto_natural_1MB.txt | AES-256 | ECB | 1.0000 | 0.0011 | 0.0014 | 947.9724 | 728.2536 | 7.9026 | ✅ Não |
| texto_natural_1MB.txt | AES-256 | CBC | 1.0000 | 0.0029 | 0.0028 | 349.7439 | 357.4640 | 7.9998 | ✅ Não |
| texto_natural_1MB.txt | AES-256 | CFB | 1.0000 | 0.0209 | 0.0204 | 47.8974 | 48.9666 | 7.9998 | ✅ Não |
| texto_natural_1MB.txt | AES-256 | OFB | 1.0000 | 0.0129 | 0.0028 | 77.5712 | 353.0499 | 7.9998 | ✅ Não |
| texto_natural_1MB.txt | AES-256 | CTR | 1.0000 | 0.0027 | 0.0014 | 374.1407 | 693.1245 | 7.9998 | ✅ Não |
| texto_natural_1MB.txt | DES | ECB | 1.0000 | 0.0123 | 0.0105 | 81.0104 | 95.2987 | 7.7656 | ✅ Não |
| texto_natural_1MB.txt | DES | CBC | 1.0000 | 0.0137 | 0.0118 | 72.8343 | 85.0894 | 7.9998 | ✅ Não |
| texto_natural_1MB.txt | DES | CFB | 1.0000 | 0.0864 | 0.0837 | 11.5787 | 11.9446 | 7.9998 | ✅ Não |
| texto_natural_1MB.txt | DES | OFB | 1.0000 | 0.0129 | 0.0127 | 77.7643 | 78.7638 | 7.9998 | ✅ Não |
| texto_natural_1MB.txt | DES | CTR | 1.0000 | 0.0114 | 0.0117 | 87.5519 | 85.6424 | 7.9998 | ✅ Não |
| texto_natural_1MB.txt | 3DES | ECB | 1.0000 | 0.0308 | 0.0309 | 32.4594 | 32.3453 | 7.8134 | ✅ Não |
| texto_natural_1MB.txt | 3DES | CBC | 1.0000 | 0.0339 | 0.0322 | 29.5369 | 31.0662 | 7.9998 | ✅ Não |
| texto_natural_1MB.txt | 3DES | CFB | 1.0000 | 0.2461 | 0.2472 | 4.0634 | 4.0456 | 7.9998 | ✅ Não |
| texto_natural_1MB.txt | 3DES | OFB | 1.0000 | 0.0324 | 0.0324 | 30.8425 | 30.8787 | 7.9998 | ✅ Não |
| texto_natural_1MB.txt | 3DES | CTR | 1.0000 | 0.0313 | 0.0309 | 31.9241 | 32.3981 | 7.9998 | ✅ Não |
| texto_natural_1MB.txt | RSA-1024 | ECB | 1.0000 | 1.9985 | 8.8008 | 0.5004 | 0.1136 | 7.9999 | ✅ Não |
| texto_natural_1MB.txt | RSA-1024 | CBC | 1.0000 | 2.0496 | 8.8540 | 0.4879 | 0.1129 | 7.9999 | ✅ Não |
| texto_natural_1MB.txt | RSA-1024 | CTR | 1.0000 | 2.0535 | 2.0690 | 0.4870 | 0.4833 | 7.9998 | ✅ Não |
| texto_natural_1MB.txt | RSA-2048 | ECB | 1.0000 | 2.2942 | 13.9879 | 0.4359 | 0.0715 | 7.9999 | ✅ Não |
| texto_natural_1MB.txt | RSA-2048 | CBC | 1.0000 | 2.3292 | 14.0694 | 0.4293 | 0.0711 | 7.9998 | ✅ Não |
| texto_natural_1MB.txt | RSA-2048 | CTR | 1.0000 | 2.3103 | 2.3331 | 0.4328 | 0.4286 | 7.9998 | ✅ Não |
| texto_natural_1MB.txt | RSA-4096 | ECB | 1.0000 | 3.6422 | 34.4098 | 0.2746 | 0.0291 | 7.9998 | ✅ Não |
| texto_natural_1MB.txt | RSA-4096 | CBC | 1.0000 | 3.7351 | 34.4446 | 0.2677 | 0.0290 | 7.9998 | ✅ Não |
| texto_natural_1MB.txt | RSA-4096 | CTR | 1.0000 | 3.6778 | 3.6864 | 0.2719 | 0.2713 | 7.9998 | ✅ Não |
| texto_repetitivo_100KB.txt | AES-128 | ECB | 0.0977 | 0.0006 | 0.0007 | 171.1015 | 144.0630 | 6.1734 | ⚠️ Sim |
| texto_repetitivo_100KB.txt | AES-128 | CBC | 0.0977 | 0.0008 | 0.0008 | 124.8058 | 127.3909 | 7.9980 | ✅ Não |
| texto_repetitivo_100KB.txt | AES-128 | CFB | 0.0977 | 0.0024 | 0.0023 | 40.5075 | 42.5046 | 7.9982 | ✅ Não |
| texto_repetitivo_100KB.txt | AES-128 | OFB | 0.0977 | 0.0008 | 0.0007 | 123.7350 | 131.8526 | 7.9980 | ✅ Não |
| texto_repetitivo_100KB.txt | AES-128 | CTR | 0.0977 | 0.0009 | 0.0006 | 114.4486 | 150.9378 | 7.9983 | ✅ Não |
| texto_repetitivo_100KB.txt | AES-256 | ECB | 0.0977 | 0.0007 | 0.0007 | 136.8161 | 138.3176 | 5.9297 | ⚠️ Sim |
| texto_repetitivo_100KB.txt | AES-256 | CBC | 0.0977 | 0.0008 | 0.0008 | 127.1457 | 129.5424 | 7.9981 | ✅ Não |
| texto_repetitivo_100KB.txt | AES-256 | CFB | 0.0977 | 0.0028 | 0.0027 | 34.4153 | 36.5147 | 7.9983 | ✅ Não |
| texto_repetitivo_100KB.txt | AES-256 | OFB | 0.0977 | 0.0009 | 0.0010 | 110.4788 | 97.5285 | 7.9984 | ✅ Não |
| texto_repetitivo_100KB.txt | AES-256 | CTR | 0.0977 | 0.0008 | 0.0008 | 126.3613 | 114.9851 | 7.9985 | ✅ Não |
| texto_repetitivo_100KB.txt | DES | ECB | 0.0977 | 0.0017 | 0.0018 | 58.0244 | 55.1293 | 5.2728 | ⚠️ Sim |
| texto_repetitivo_100KB.txt | DES | CBC | 0.0977 | 0.0022 | 0.0019 | 44.1698 | 51.3985 | 7.9982 | ✅ Não |
| texto_repetitivo_100KB.txt | DES | CFB | 0.0977 | 0.0097 | 0.0089 | 10.1140 | 10.9796 | 7.9983 | ✅ Não |
| texto_repetitivo_100KB.txt | DES | OFB | 0.0977 | 0.0019 | 0.0021 | 51.5616 | 47.0129 | 7.9981 | ✅ Não |
| texto_repetitivo_100KB.txt | DES | CTR | 0.0977 | 0.0018 | 0.0017 | 54.5908 | 58.4967 | 7.9982 | ✅ Não |
| texto_repetitivo_100KB.txt | 3DES | ECB | 0.0977 | 0.0038 | 0.0039 | 25.7881 | 25.2179 | 5.2726 | ⚠️ Sim |
| texto_repetitivo_100KB.txt | 3DES | CBC | 0.0977 | 0.0041 | 0.0035 | 23.5922 | 27.6751 | 7.9978 | ✅ Não |
| texto_repetitivo_100KB.txt | 3DES | CFB | 0.0977 | 0.0249 | 0.0244 | 3.9271 | 3.9987 | 7.9981 | ✅ Não |
| texto_repetitivo_100KB.txt | 3DES | OFB | 0.0977 | 0.0040 | 0.0037 | 24.4472 | 26.1951 | 7.9983 | ✅ Não |
| texto_repetitivo_100KB.txt | 3DES | CTR | 0.0977 | 0.0039 | 0.0038 | 25.0247 | 25.8834 | 7.9981 | ✅ Não |
| texto_repetitivo_100KB.txt | RSA-1024 | ECB | 0.0977 | 0.1982 | 0.8629 | 0.4927 | 0.1132 | 7.9989 | ✅ Não |
| texto_repetitivo_100KB.txt | RSA-1024 | CBC | 0.0977 | 0.2163 | 0.8846 | 0.4516 | 0.1104 | 7.9987 | ✅ Não |
| texto_repetitivo_100KB.txt | RSA-1024 | CTR | 0.0977 | 0.2019 | 0.2018 | 0.4836 | 0.4839 | 7.9979 | ✅ Não |
| texto_repetitivo_100KB.txt | RSA-2048 | ECB | 0.0977 | 0.2275 | 1.3823 | 0.4292 | 0.0706 | 7.9986 | ✅ Não |
| texto_repetitivo_100KB.txt | RSA-2048 | CBC | 0.0977 | 0.2317 | 1.3863 | 0.4214 | 0.0704 | 7.9984 | ✅ Não |
| texto_repetitivo_100KB.txt | RSA-2048 | CTR | 0.0977 | 0.2298 | 0.2408 | 0.4249 | 0.4055 | 7.9979 | ✅ Não |
| texto_repetitivo_100KB.txt | RSA-4096 | ECB | 0.0977 | 0.3541 | 3.3418 | 0.2758 | 0.0292 | 7.9981 | ✅ Não |
| texto_repetitivo_100KB.txt | RSA-4096 | CBC | 0.0977 | 0.3520 | 3.3286 | 0.2774 | 0.0293 | 7.9983 | ✅ Não |
| texto_repetitivo_100KB.txt | RSA-4096 | CTR | 0.0977 | 0.3582 | 0.3584 | 0.2727 | 0.2724 | 7.9981 | ✅ Não |
| texto_repetitivo_10KB.txt | AES-128 | ECB | 0.0098 | 0.0004 | 0.0005 | 22.9919 | 18.1883 | 5.9385 | ⚠️ Sim |
| texto_repetitivo_10KB.txt | AES-128 | CBC | 0.0098 | 0.0007 | 0.0005 | 14.1324 | 18.4521 | 7.9827 | ✅ Não |
| texto_repetitivo_10KB.txt | AES-128 | CFB | 0.0098 | 0.0009 | 0.0007 | 11.0841 | 14.6689 | 7.9794 | ✅ Não |
| texto_repetitivo_10KB.txt | AES-128 | OFB | 0.0098 | 0.0008 | 0.0005 | 12.3978 | 18.0266 | 7.9823 | ✅ Não |
| texto_repetitivo_10KB.txt | AES-128 | CTR | 0.0098 | 0.0007 | 0.0006 | 14.2494 | 17.0638 | 7.9828 | ✅ Não |
| texto_repetitivo_10KB.txt | AES-256 | ECB | 0.0098 | 0.0008 | 0.0005 | 12.3307 | 18.5247 | 5.9024 | ⚠️ Sim |
| texto_repetitivo_10KB.txt | AES-256 | CBC | 0.0098 | 0.0007 | 0.0005 | 14.0756 | 18.6768 | 7.9815 | ✅ Não |
| texto_repetitivo_10KB.txt | AES-256 | CFB | 0.0098 | 0.0008 | 0.0009 | 11.5537 | 10.4554 | 7.9808 | ✅ Não |
| texto_repetitivo_10KB.txt | AES-256 | OFB | 0.0098 | 0.0006 | 0.0006 | 15.5293 | 16.9853 | 7.9815 | ✅ Não |
| texto_repetitivo_10KB.txt | AES-256 | CTR | 0.0098 | 0.0007 | 0.0006 | 14.1027 | 15.4940 | 7.9840 | ✅ Não |
| texto_repetitivo_10KB.txt | DES | ECB | 0.0098 | 0.0006 | 0.0008 | 15.4153 | 12.1745 | 5.1295 | ⚠️ Sim |
| texto_repetitivo_10KB.txt | DES | CBC | 0.0098 | 0.0007 | 0.0008 | 13.1527 | 11.6972 | 7.9835 | ✅ Não |
| texto_repetitivo_10KB.txt | DES | CFB | 0.0098 | 0.0016 | 0.0013 | 6.1430 | 7.4098 | 7.9827 | ✅ Não |
| texto_repetitivo_10KB.txt | DES | OFB | 0.0098 | 0.0007 | 0.0007 | 13.9329 | 14.8929 | 7.9849 | ✅ Não |
| texto_repetitivo_10KB.txt | DES | CTR | 0.0098 | 0.0007 | 0.0007 | 13.3668 | 14.1917 | 7.9814 | ✅ Não |
| texto_repetitivo_10KB.txt | 3DES | ECB | 0.0098 | 0.0009 | 0.0009 | 11.1812 | 11.1138 | 5.2294 | ⚠️ Sim |
| texto_repetitivo_10KB.txt | 3DES | CBC | 0.0098 | 0.0009 | 0.0009 | 10.6166 | 10.5293 | 7.9823 | ✅ Não |
| texto_repetitivo_10KB.txt | 3DES | CFB | 0.0098 | 0.0033 | 0.0029 | 2.9540 | 3.3254 | 7.9776 | ✅ Não |
| texto_repetitivo_10KB.txt | 3DES | OFB | 0.0098 | 0.0010 | 0.0008 | 10.1346 | 12.4954 | 7.9814 | ✅ Não |
| texto_repetitivo_10KB.txt | 3DES | CTR | 0.0098 | 0.0011 | 0.0009 | 9.2815 | 11.3664 | 7.9816 | ✅ Não |
| texto_repetitivo_10KB.txt | RSA-1024 | ECB | 0.0098 | 0.0204 | 0.0870 | 0.4780 | 0.1123 | 7.9873 | ✅ Não |
| texto_repetitivo_10KB.txt | RSA-1024 | CBC | 0.0098 | 0.0208 | 0.0878 | 0.4697 | 0.1112 | 7.9886 | ✅ Não |
| texto_repetitivo_10KB.txt | RSA-1024 | CTR | 0.0098 | 0.0228 | 0.0208 | 0.4283 | 0.4687 | 7.9807 | ✅ Não |
| texto_repetitivo_10KB.txt | RSA-2048 | ECB | 0.0098 | 0.0235 | 0.1472 | 0.4161 | 0.0663 | 7.9822 | ✅ Não |
| texto_repetitivo_10KB.txt | RSA-2048 | CBC | 0.0098 | 0.0232 | 0.1401 | 0.4218 | 0.0697 | 7.9855 | ✅ Não |
| texto_repetitivo_10KB.txt | RSA-2048 | CTR | 0.0098 | 0.0237 | 0.0281 | 0.4114 | 0.3481 | 7.9852 | ✅ Não |
| texto_repetitivo_10KB.txt | RSA-4096 | ECB | 0.0098 | 0.0355 | 0.3412 | 0.2748 | 0.0286 | 7.9872 | ✅ Não |
| texto_repetitivo_10KB.txt | RSA-4096 | CBC | 0.0098 | 0.0354 | 0.3397 | 0.2760 | 0.0288 | 7.9830 | ✅ Não |
| texto_repetitivo_10KB.txt | RSA-4096 | CTR | 0.0098 | 0.0357 | 0.0359 | 0.2733 | 0.2720 | 7.9816 | ✅ Não |
| texto_repetitivo_1KB.txt | AES-128 | ECB | 0.0010 | 0.0004 | 0.0005 | 2.4468 | 2.1674 | 6.1594 | ⚠️ Sim |
| texto_repetitivo_1KB.txt | AES-128 | CBC | 0.0010 | 0.0005 | 0.0005 | 1.9555 | 1.9527 | 7.8294 | ✅ Não |
| texto_repetitivo_1KB.txt | AES-128 | CFB | 0.0010 | 0.0005 | 0.0006 | 1.9512 | 1.6279 | 7.8182 | ✅ Não |
| texto_repetitivo_1KB.txt | AES-128 | OFB | 0.0010 | 0.0005 | 0.0005 | 1.9484 | 1.9607 | 7.7878 | ✅ Não |
| texto_repetitivo_1KB.txt | AES-128 | CTR | 0.0010 | 0.0006 | 0.0004 | 1.6263 | 2.4410 | 7.8073 | ✅ Não |
| texto_repetitivo_1KB.txt | AES-256 | ECB | 0.0010 | 0.0004 | 0.0005 | 2.4346 | 1.9604 | 6.2562 | ⚠️ Sim |
| texto_repetitivo_1KB.txt | AES-256 | CBC | 0.0010 | 0.0006 | 0.0005 | 1.6269 | 1.9530 | 7.8374 | ✅ Não |
| texto_repetitivo_1KB.txt | AES-256 | CFB | 0.0010 | 0.0005 | 0.0004 | 1.9485 | 2.4517 | 7.8229 | ✅ Não |
| texto_repetitivo_1KB.txt | AES-256 | OFB | 0.0010 | 0.0005 | 0.0006 | 1.9547 | 1.6267 | 7.7611 | ✅ Não |
| texto_repetitivo_1KB.txt | AES-256 | CTR | 0.0010 | 0.0005 | 0.0005 | 1.9532 | 1.9521 | 7.8142 | ✅ Não |
| texto_repetitivo_1KB.txt | DES | ECB | 0.0010 | 0.0006 | 0.0005 | 1.7712 | 1.9531 | 5.2634 | ⚠️ Sim |
| texto_repetitivo_1KB.txt | DES | CBC | 0.0010 | 0.0006 | 0.0005 | 1.6251 | 1.9558 | 7.8241 | ✅ Não |
| texto_repetitivo_1KB.txt | DES | CFB | 0.0010 | 0.0006 | 0.0005 | 1.6277 | 1.9553 | 7.8234 | ✅ Não |
| texto_repetitivo_1KB.txt | DES | OFB | 0.0010 | 0.0005 | 0.0005 | 1.9533 | 1.9528 | 7.8065 | ✅ Não |
| texto_repetitivo_1KB.txt | DES | CTR | 0.0010 | 0.0005 | 0.0006 | 1.9510 | 1.6070 | 7.8302 | ✅ Não |
| texto_repetitivo_1KB.txt | 3DES | ECB | 0.0010 | 0.0006 | 0.0005 | 1.6454 | 1.9575 | 5.2140 | ⚠️ Sim |
| texto_repetitivo_1KB.txt | 3DES | CBC | 0.0010 | 0.0005 | 0.0006 | 1.9585 | 1.6275 | 7.8100 | ✅ Não |
| texto_repetitivo_1KB.txt | 3DES | CFB | 0.0010 | 0.0008 | 0.0007 | 1.2207 | 1.3927 | 7.8194 | ✅ Não |
| texto_repetitivo_1KB.txt | 3DES | OFB | 0.0010 | 0.0006 | 0.0006 | 1.6272 | 1.7734 | 7.8236 | ✅ Não |
| texto_repetitivo_1KB.txt | 3DES | CTR | 0.0010 | 0.0006 | 0.0006 | 1.6264 | 1.6275 | 7.8247 | ✅ Não |
| texto_repetitivo_1KB.txt | RSA-1024 | ECB | 0.0010 | 0.0026 | 0.0098 | 0.3758 | 0.1001 | 7.8744 | ✅ Não |
| texto_repetitivo_1KB.txt | RSA-1024 | CBC | 0.0010 | 0.0026 | 0.0092 | 0.3756 | 0.1065 | 7.8676 | ✅ Não |
| texto_repetitivo_1KB.txt | RSA-1024 | CTR | 0.0010 | 0.0026 | 0.0029 | 0.3755 | 0.3412 | 7.8035 | ✅ Não |
| texto_repetitivo_1KB.txt | RSA-2048 | ECB | 0.0010 | 0.0028 | 0.0148 | 0.3551 | 0.0662 | 7.8634 | ✅ Não |
| texto_repetitivo_1KB.txt | RSA-2048 | CBC | 0.0010 | 0.0030 | 0.0148 | 0.3301 | 0.0662 | 7.8742 | ✅ Não |
| texto_repetitivo_1KB.txt | RSA-2048 | CTR | 0.0010 | 0.0028 | 0.0033 | 0.3488 | 0.2994 | 7.8112 | ✅ Não |
| texto_repetitivo_1KB.txt | RSA-4096 | ECB | 0.0010 | 0.0055 | 0.0463 | 0.1791 | 0.0211 | 7.9008 | ✅ Não |
| texto_repetitivo_1KB.txt | RSA-4096 | CBC | 0.0010 | 0.0054 | 0.0464 | 0.1811 | 0.0211 | 7.9105 | ✅ Não |
| texto_repetitivo_1KB.txt | RSA-4096 | CTR | 0.0010 | 0.0055 | 0.0057 | 0.1776 | 0.1727 | 7.8085 | ✅ Não |
| texto_repetitivo_1MB.txt | AES-128 | ECB | 1.0000 | 0.0011 | 0.0012 | 911.0130 | 832.3023 | 6.1471 | ⚠️ Sim |
| texto_repetitivo_1MB.txt | AES-128 | CBC | 1.0000 | 0.0027 | 0.0027 | 367.1035 | 370.1194 | 7.9998 | ✅ Não |
| texto_repetitivo_1MB.txt | AES-128 | CFB | 1.0000 | 0.0179 | 0.0173 | 55.8185 | 57.8211 | 7.9998 | ✅ Não |
| texto_repetitivo_1MB.txt | AES-128 | OFB | 1.0000 | 0.0034 | 0.0023 | 290.9398 | 426.7361 | 7.9998 | ✅ Não |
| texto_repetitivo_1MB.txt | AES-128 | CTR | 1.0000 | 0.0015 | 0.0013 | 652.4545 | 763.0586 | 7.9999 | ✅ Não |
| texto_repetitivo_1MB.txt | AES-256 | ECB | 1.0000 | 0.0011 | 0.0011 | 878.8116 | 879.5856 | 6.0876 | ⚠️ Sim |
| texto_repetitivo_1MB.txt | AES-256 | CBC | 1.0000 | 0.0031 | 0.0028 | 324.9409 | 357.7110 | 7.9998 | ✅ Não |
| texto_repetitivo_1MB.txt | AES-256 | CFB | 1.0000 | 0.0216 | 0.0201 | 46.3905 | 49.8184 | 7.9998 | ✅ Não |
| texto_repetitivo_1MB.txt | AES-256 | OFB | 1.0000 | 0.0029 | 0.0024 | 348.2253 | 408.8972 | 7.9998 | ✅ Não |
| texto_repetitivo_1MB.txt | AES-256 | CTR | 1.0000 | 0.0014 | 0.0014 | 692.3807 | 724.2923 | 7.9998 | ✅ Não |
| texto_repetitivo_1MB.txt | DES | ECB | 1.0000 | 0.0119 | 0.0107 | 84.2880 | 93.4027 | 5.0720 | ⚠️ Sim |
| texto_repetitivo_1MB.txt | DES | CBC | 1.0000 | 0.0136 | 0.0116 | 73.6043 | 86.3733 | 7.9999 | ✅ Não |
| texto_repetitivo_1MB.txt | DES | CFB | 1.0000 | 0.0871 | 0.0861 | 11.4779 | 11.6211 | 7.9998 | ✅ Não |
| texto_repetitivo_1MB.txt | DES | OFB | 1.0000 | 0.0131 | 0.0125 | 76.4037 | 80.1955 | 7.9998 | ✅ Não |
| texto_repetitivo_1MB.txt | DES | CTR | 1.0000 | 0.0111 | 0.0149 | 90.2358 | 67.0776 | 7.9998 | ✅ Não |
| texto_repetitivo_1MB.txt | 3DES | ECB | 1.0000 | 0.0306 | 0.0305 | 32.7211 | 32.7910 | 5.2221 | ⚠️ Sim |
| texto_repetitivo_1MB.txt | 3DES | CBC | 1.0000 | 0.0344 | 0.0410 | 29.0312 | 24.4175 | 7.9998 | ✅ Não |
| texto_repetitivo_1MB.txt | 3DES | CFB | 1.0000 | 0.2460 | 0.2424 | 4.0654 | 4.1261 | 7.9998 | ✅ Não |
| texto_repetitivo_1MB.txt | 3DES | OFB | 1.0000 | 0.0328 | 0.0330 | 30.5322 | 30.2891 | 7.9998 | ✅ Não |
| texto_repetitivo_1MB.txt | 3DES | CTR | 1.0000 | 0.0325 | 0.0312 | 30.7508 | 32.0349 | 7.9998 | ✅ Não |
| texto_repetitivo_1MB.txt | RSA-1024 | ECB | 1.0000 | 2.0234 | 8.7901 | 0.4942 | 0.1138 | 7.9999 | ✅ Não |
| texto_repetitivo_1MB.txt | RSA-1024 | CBC | 1.0000 | 2.1074 | 8.8894 | 0.4745 | 0.1125 | 7.9999 | ✅ Não |
| texto_repetitivo_1MB.txt | RSA-1024 | CTR | 1.0000 | 2.0498 | 2.0942 | 0.4878 | 0.4775 | 7.9998 | ✅ Não |
| texto_repetitivo_1MB.txt | RSA-2048 | ECB | 1.0000 | 2.2691 | 13.9898 | 0.4407 | 0.0715 | 7.9998 | ✅ Não |
| texto_repetitivo_1MB.txt | RSA-2048 | CBC | 1.0000 | 2.3588 | 14.0427 | 0.4240 | 0.0712 | 7.9998 | ✅ Não |
| texto_repetitivo_1MB.txt | RSA-2048 | CTR | 1.0000 | 2.3239 | 2.3361 | 0.4303 | 0.4281 | 7.9998 | ✅ Não |
| texto_repetitivo_1MB.txt | RSA-4096 | ECB | 1.0000 | 3.5509 | 34.2050 | 0.2816 | 0.0292 | 7.9998 | ✅ Não |
| texto_repetitivo_1MB.txt | RSA-4096 | CBC | 1.0000 | 3.6596 | 34.2697 | 0.2733 | 0.0292 | 7.9998 | ✅ Não |
| texto_repetitivo_1MB.txt | RSA-4096 | CTR | 1.0000 | 3.6309 | 3.6108 | 0.2754 | 0.2769 | 7.9998 | ✅ Não |

## 2. Tabelas Resumo 

### 2.1. Comparativo de Tempos para Arquivos CSV

| Arquivo CSV | Algoritmo | Modo | Tamanho (MB) | T. Cifrar (s) | T. Decifrar (s) |
|-------------|-----------|------|--------------|---------------|-----------------|
| csv_categorico_100KB.csv | AES-128 | ECB | 0.0977 | 0.0008 | 0.0006 |
| csv_categorico_100KB.csv | AES-128 | CBC | 0.0977 | 0.0013 | 0.0026 |
| csv_categorico_100KB.csv | AES-128 | CFB | 0.0977 | 0.0026 | 0.0025 |
| csv_categorico_100KB.csv | AES-128 | OFB | 0.0977 | 0.0011 | 0.0010 |
| csv_categorico_100KB.csv | AES-128 | CTR | 0.0977 | 0.0009 | 0.0006 |
| csv_categorico_100KB.csv | AES-256 | ECB | 0.0977 | 0.0008 | 0.0008 |
| csv_categorico_100KB.csv | AES-256 | CBC | 0.0977 | 0.0010 | 0.0010 |
| csv_categorico_100KB.csv | AES-256 | CFB | 0.0977 | 0.0030 | 0.0026 |
| csv_categorico_100KB.csv | AES-256 | OFB | 0.0977 | 0.0008 | 0.0007 |
| csv_categorico_100KB.csv | AES-256 | CTR | 0.0977 | 0.0010 | 0.0010 |
| csv_categorico_100KB.csv | DES | ECB | 0.0977 | 0.0018 | 0.0016 |
| csv_categorico_100KB.csv | DES | CBC | 0.0977 | 0.0026 | 0.0019 |
| csv_categorico_100KB.csv | DES | CFB | 0.0977 | 0.0096 | 0.0087 |
| csv_categorico_100KB.csv | DES | OFB | 0.0977 | 0.0021 | 0.0026 |
| csv_categorico_100KB.csv | DES | CTR | 0.0977 | 0.0024 | 0.0022 |
| csv_categorico_100KB.csv | 3DES | ECB | 0.0977 | 0.0040 | 0.0037 |
| csv_categorico_100KB.csv | 3DES | CBC | 0.0977 | 0.0046 | 0.0038 |
| csv_categorico_100KB.csv | 3DES | CFB | 0.0977 | 0.0308 | 0.0367 |
| csv_categorico_100KB.csv | 3DES | OFB | 0.0977 | 0.0069 | 0.0037 |
| csv_categorico_100KB.csv | 3DES | CTR | 0.0977 | 0.0042 | 0.0037 |
| csv_categorico_100KB.csv | RSA-1024 | ECB | 0.0977 | 0.2119 | 0.8886 |
| csv_categorico_100KB.csv | RSA-1024 | CBC | 0.0977 | 0.2172 | 0.8812 |
| csv_categorico_100KB.csv | RSA-1024 | CTR | 0.0977 | 0.2763 | 0.2651 |
| csv_categorico_100KB.csv | RSA-2048 | ECB | 0.0977 | 0.6238 | 1.5138 |
| csv_categorico_100KB.csv | RSA-2048 | CBC | 0.0977 | 0.2512 | 1.4413 |
| csv_categorico_100KB.csv | RSA-2048 | CTR | 0.0977 | 0.2740 | 0.2860 |
| csv_categorico_100KB.csv | RSA-4096 | ECB | 0.0977 | 0.3687 | 3.6768 |
| csv_categorico_100KB.csv | RSA-4096 | CBC | 0.0977 | 0.3838 | 3.6725 |
| csv_categorico_100KB.csv | RSA-4096 | CTR | 0.0977 | 0.4446 | 0.3913 |
| csv_categorico_10KB.csv | AES-128 | ECB | 0.0098 | 0.0007 | 0.0022 |
| csv_categorico_10KB.csv | AES-128 | CBC | 0.0098 | 0.0006 | 0.0007 |
| csv_categorico_10KB.csv | AES-128 | CFB | 0.0098 | 0.0009 | 0.0010 |
| csv_categorico_10KB.csv | AES-128 | OFB | 0.0098 | 0.0007 | 0.0006 |
| csv_categorico_10KB.csv | AES-128 | CTR | 0.0098 | 0.0008 | 0.0007 |
| csv_categorico_10KB.csv | AES-256 | ECB | 0.0098 | 0.0006 | 0.0007 |
| csv_categorico_10KB.csv | AES-256 | CBC | 0.0098 | 0.0007 | 0.0008 |
| csv_categorico_10KB.csv | AES-256 | CFB | 0.0098 | 0.0010 | 0.0010 |
| csv_categorico_10KB.csv | AES-256 | OFB | 0.0098 | 0.0007 | 0.0006 |
| csv_categorico_10KB.csv | AES-256 | CTR | 0.0098 | 0.0009 | 0.0006 |
| csv_categorico_10KB.csv | DES | ECB | 0.0098 | 0.0007 | 0.0007 |
| csv_categorico_10KB.csv | DES | CBC | 0.0098 | 0.0009 | 0.0009 |
| csv_categorico_10KB.csv | DES | CFB | 0.0098 | 0.0016 | 0.0022 |
| csv_categorico_10KB.csv | DES | OFB | 0.0098 | 0.0012 | 0.0008 |
| csv_categorico_10KB.csv | DES | CTR | 0.0098 | 0.0008 | 0.0008 |
| csv_categorico_10KB.csv | 3DES | ECB | 0.0098 | 0.0012 | 0.0014 |
| csv_categorico_10KB.csv | 3DES | CBC | 0.0098 | 0.0012 | 0.0013 |
| csv_categorico_10KB.csv | 3DES | CFB | 0.0098 | 0.0039 | 0.0032 |
| csv_categorico_10KB.csv | 3DES | OFB | 0.0098 | 0.0010 | 0.0012 |
| csv_categorico_10KB.csv | 3DES | CTR | 0.0098 | 0.0012 | 0.0011 |
| csv_categorico_10KB.csv | RSA-1024 | ECB | 0.0098 | 0.0217 | 0.1155 |
| csv_categorico_10KB.csv | RSA-1024 | CBC | 0.0098 | 0.0267 | 0.0942 |
| csv_categorico_10KB.csv | RSA-1024 | CTR | 0.0098 | 0.0225 | 0.0230 |
| csv_categorico_10KB.csv | RSA-2048 | ECB | 0.0098 | 0.0294 | 0.1536 |
| csv_categorico_10KB.csv | RSA-2048 | CBC | 0.0098 | 0.0256 | 0.1469 |
| csv_categorico_10KB.csv | RSA-2048 | CTR | 0.0098 | 0.0254 | 0.0261 |
| csv_categorico_10KB.csv | RSA-4096 | ECB | 0.0098 | 0.0402 | 0.3584 |
| csv_categorico_10KB.csv | RSA-4096 | CBC | 0.0098 | 0.0394 | 0.3732 |
| csv_categorico_10KB.csv | RSA-4096 | CTR | 0.0098 | 0.0408 | 0.0427 |
| csv_categorico_1KB.csv | AES-128 | ECB | 0.0010 | 0.0005 | 0.0007 |
| csv_categorico_1KB.csv | AES-128 | CBC | 0.0010 | 0.0006 | 0.0006 |
| csv_categorico_1KB.csv | AES-128 | CFB | 0.0010 | 0.0006 | 0.0006 |
| csv_categorico_1KB.csv | AES-128 | OFB | 0.0010 | 0.0007 | 0.0006 |
| csv_categorico_1KB.csv | AES-128 | CTR | 0.0010 | 0.0007 | 0.0006 |
| csv_categorico_1KB.csv | AES-256 | ECB | 0.0010 | 0.0006 | 0.0005 |
| csv_categorico_1KB.csv | AES-256 | CBC | 0.0010 | 0.0006 | 0.0007 |
| csv_categorico_1KB.csv | AES-256 | CFB | 0.0010 | 0.0006 | 0.0007 |
| csv_categorico_1KB.csv | AES-256 | OFB | 0.0010 | 0.0006 | 0.0006 |
| csv_categorico_1KB.csv | AES-256 | CTR | 0.0010 | 0.0008 | 0.0006 |
| csv_categorico_1KB.csv | DES | ECB | 0.0010 | 0.0007 | 0.0006 |
| csv_categorico_1KB.csv | DES | CBC | 0.0010 | 0.0007 | 0.0007 |
| csv_categorico_1KB.csv | DES | CFB | 0.0010 | 0.0007 | 0.0007 |
| csv_categorico_1KB.csv | DES | OFB | 0.0010 | 0.0007 | 0.0007 |
| csv_categorico_1KB.csv | DES | CTR | 0.0010 | 0.0006 | 0.0006 |
| csv_categorico_1KB.csv | 3DES | ECB | 0.0010 | 0.0008 | 0.0008 |
| csv_categorico_1KB.csv | 3DES | CBC | 0.0010 | 0.0007 | 0.0010 |
| csv_categorico_1KB.csv | 3DES | CFB | 0.0010 | 0.0011 | 0.0009 |
| csv_categorico_1KB.csv | 3DES | OFB | 0.0010 | 0.0011 | 0.0009 |
| csv_categorico_1KB.csv | 3DES | CTR | 0.0010 | 0.0010 | 0.0010 |
| csv_categorico_1KB.csv | RSA-1024 | ECB | 0.0010 | 0.0028 | 0.0100 |
| csv_categorico_1KB.csv | RSA-1024 | CBC | 0.0010 | 0.0030 | 0.0104 |
| csv_categorico_1KB.csv | RSA-1024 | CTR | 0.0010 | 0.0033 | 0.0030 |
| csv_categorico_1KB.csv | RSA-2048 | ECB | 0.0010 | 0.0032 | 0.0155 |
| csv_categorico_1KB.csv | RSA-2048 | CBC | 0.0010 | 0.0035 | 0.0168 |
| csv_categorico_1KB.csv | RSA-2048 | CTR | 0.0010 | 0.0033 | 0.0034 |
| csv_categorico_1KB.csv | RSA-4096 | ECB | 0.0010 | 0.0059 | 0.0471 |
| csv_categorico_1KB.csv | RSA-4096 | CBC | 0.0010 | 0.0060 | 0.0495 |
| csv_categorico_1KB.csv | RSA-4096 | CTR | 0.0010 | 0.0056 | 0.0058 |
| csv_categorico_1MB.csv | AES-128 | ECB | 1.0000 | 0.0014 | 0.0013 |
| csv_categorico_1MB.csv | AES-128 | CBC | 1.0000 | 0.0032 | 0.0044 |
| csv_categorico_1MB.csv | AES-128 | CFB | 1.0000 | 0.0180 | 0.0173 |
| csv_categorico_1MB.csv | AES-128 | OFB | 1.0000 | 0.0057 | 0.0029 |
| csv_categorico_1MB.csv | AES-128 | CTR | 1.0000 | 0.0019 | 0.0017 |
| csv_categorico_1MB.csv | AES-256 | ECB | 1.0000 | 0.0013 | 0.0013 |
| csv_categorico_1MB.csv | AES-256 | CBC | 1.0000 | 0.0068 | 0.0026 |
| csv_categorico_1MB.csv | AES-256 | CFB | 1.0000 | 0.0219 | 0.0203 |
| csv_categorico_1MB.csv | AES-256 | OFB | 1.0000 | 0.0033 | 0.0045 |
| csv_categorico_1MB.csv | AES-256 | CTR | 1.0000 | 0.0020 | 0.0017 |
| csv_categorico_1MB.csv | DES | ECB | 1.0000 | 0.0112 | 0.0111 |
| csv_categorico_1MB.csv | DES | CBC | 1.0000 | 0.0156 | 0.0121 |
| csv_categorico_1MB.csv | DES | CFB | 1.0000 | 0.0887 | 0.0858 |
| csv_categorico_1MB.csv | DES | OFB | 1.0000 | 0.0154 | 0.0138 |
| csv_categorico_1MB.csv | DES | CTR | 1.0000 | 0.0116 | 0.0134 |
| csv_categorico_1MB.csv | 3DES | ECB | 1.0000 | 0.0321 | 0.0329 |
| csv_categorico_1MB.csv | 3DES | CBC | 1.0000 | 0.0346 | 0.0323 |
| csv_categorico_1MB.csv | 3DES | CFB | 1.0000 | 0.2532 | 0.2470 |
| csv_categorico_1MB.csv | 3DES | OFB | 1.0000 | 0.0356 | 0.0328 |
| csv_categorico_1MB.csv | 3DES | CTR | 1.0000 | 0.0333 | 0.0509 |
| csv_categorico_1MB.csv | RSA-1024 | ECB | 1.0000 | 2.0197 | 8.9974 |
| csv_categorico_1MB.csv | RSA-1024 | CBC | 1.0000 | 2.0803 | 10.0444 |
| csv_categorico_1MB.csv | RSA-1024 | CTR | 1.0000 | 2.0955 | 2.0395 |
| csv_categorico_1MB.csv | RSA-2048 | ECB | 1.0000 | 2.2738 | 14.0300 |
| csv_categorico_1MB.csv | RSA-2048 | CBC | 1.0000 | 2.3643 | 14.5407 |
| csv_categorico_1MB.csv | RSA-2048 | CTR | 1.0000 | 2.6977 | 2.6094 |
| csv_categorico_1MB.csv | RSA-4096 | ECB | 1.0000 | 3.7282 | 34.7735 |
| csv_categorico_1MB.csv | RSA-4096 | CBC | 1.0000 | 3.6902 | 34.5968 |
| csv_categorico_1MB.csv | RSA-4096 | CTR | 1.0000 | 3.5744 | 3.7101 |
| csv_incremental_100KB.csv | AES-128 | ECB | 0.0977 | 0.0011 | 0.0007 |
| csv_incremental_100KB.csv | AES-128 | CBC | 0.0977 | 0.0017 | 0.0011 |
| csv_incremental_100KB.csv | AES-128 | CFB | 0.0977 | 0.0025 | 0.0024 |
| csv_incremental_100KB.csv | AES-128 | OFB | 0.0977 | 0.0009 | 0.0008 |
| csv_incremental_100KB.csv | AES-128 | CTR | 0.0977 | 0.0007 | 0.0006 |
| csv_incremental_100KB.csv | AES-256 | ECB | 0.0977 | 0.0007 | 0.0007 |
| csv_incremental_100KB.csv | AES-256 | CBC | 0.0977 | 0.0009 | 0.0008 |
| csv_incremental_100KB.csv | AES-256 | CFB | 0.0977 | 0.0027 | 0.0027 |
| csv_incremental_100KB.csv | AES-256 | OFB | 0.0977 | 0.0009 | 0.0008 |
| csv_incremental_100KB.csv | AES-256 | CTR | 0.0977 | 0.0009 | 0.0009 |
| csv_incremental_100KB.csv | DES | ECB | 0.0977 | 0.0020 | 0.0019 |
| csv_incremental_100KB.csv | DES | CBC | 0.0977 | 0.0027 | 0.0020 |
| csv_incremental_100KB.csv | DES | CFB | 0.0977 | 0.0096 | 0.0096 |
| csv_incremental_100KB.csv | DES | OFB | 0.0977 | 0.0020 | 0.0020 |
| csv_incremental_100KB.csv | DES | CTR | 0.0977 | 0.0019 | 0.0018 |
| csv_incremental_100KB.csv | 3DES | ECB | 0.0977 | 0.0039 | 0.0039 |
| csv_incremental_100KB.csv | 3DES | CBC | 0.0977 | 0.0041 | 0.0038 |
| csv_incremental_100KB.csv | 3DES | CFB | 0.0977 | 0.0259 | 0.0252 |
| csv_incremental_100KB.csv | 3DES | OFB | 0.0977 | 0.0044 | 0.0036 |
| csv_incremental_100KB.csv | 3DES | CTR | 0.0977 | 0.0039 | 0.0038 |
| csv_incremental_100KB.csv | RSA-1024 | ECB | 0.0977 | 0.2109 | 0.8563 |
| csv_incremental_100KB.csv | RSA-1024 | CBC | 0.0977 | 0.2074 | 0.8632 |
| csv_incremental_100KB.csv | RSA-1024 | CTR | 0.0977 | 0.2062 | 0.2047 |
| csv_incremental_100KB.csv | RSA-2048 | ECB | 0.0977 | 0.2291 | 1.3870 |
| csv_incremental_100KB.csv | RSA-2048 | CBC | 0.0977 | 0.2360 | 1.4069 |
| csv_incremental_100KB.csv | RSA-2048 | CTR | 0.0977 | 0.2355 | 0.2297 |
| csv_incremental_100KB.csv | RSA-4096 | ECB | 0.0977 | 0.3679 | 3.4052 |
| csv_incremental_100KB.csv | RSA-4096 | CBC | 0.0977 | 0.3667 | 3.4641 |
| csv_incremental_100KB.csv | RSA-4096 | CTR | 0.0977 | 0.3993 | 0.3839 |
| csv_incremental_10KB.csv | AES-128 | ECB | 0.0098 | 0.0005 | 0.0008 |
| csv_incremental_10KB.csv | AES-128 | CBC | 0.0098 | 0.0008 | 0.0009 |
| csv_incremental_10KB.csv | AES-128 | CFB | 0.0098 | 0.0009 | 0.0009 |
| csv_incremental_10KB.csv | AES-128 | OFB | 0.0098 | 0.0008 | 0.0006 |
| csv_incremental_10KB.csv | AES-128 | CTR | 0.0098 | 0.0006 | 0.0007 |
| csv_incremental_10KB.csv | AES-256 | ECB | 0.0098 | 0.0006 | 0.0005 |
| csv_incremental_10KB.csv | AES-256 | CBC | 0.0098 | 0.0005 | 0.0007 |
| csv_incremental_10KB.csv | AES-256 | CFB | 0.0098 | 0.0008 | 0.0008 |
| csv_incremental_10KB.csv | AES-256 | OFB | 0.0098 | 0.0007 | 0.0007 |
| csv_incremental_10KB.csv | AES-256 | CTR | 0.0098 | 0.0009 | 0.0006 |
| csv_incremental_10KB.csv | DES | ECB | 0.0098 | 0.0008 | 0.0007 |
| csv_incremental_10KB.csv | DES | CBC | 0.0098 | 0.0009 | 0.0009 |
| csv_incremental_10KB.csv | DES | CFB | 0.0098 | 0.0015 | 0.0018 |
| csv_incremental_10KB.csv | DES | OFB | 0.0098 | 0.0011 | 0.0009 |
| csv_incremental_10KB.csv | DES | CTR | 0.0098 | 0.0009 | 0.0009 |
| csv_incremental_10KB.csv | 3DES | ECB | 0.0098 | 0.0012 | 0.0013 |
| csv_incremental_10KB.csv | 3DES | CBC | 0.0098 | 0.0012 | 0.0009 |
| csv_incremental_10KB.csv | 3DES | CFB | 0.0098 | 0.0036 | 0.0031 |
| csv_incremental_10KB.csv | 3DES | OFB | 0.0098 | 0.0010 | 0.0012 |
| csv_incremental_10KB.csv | 3DES | CTR | 0.0098 | 0.0011 | 0.0009 |
| csv_incremental_10KB.csv | RSA-1024 | ECB | 0.0098 | 0.0221 | 0.0997 |
| csv_incremental_10KB.csv | RSA-1024 | CBC | 0.0098 | 0.0236 | 0.0967 |
| csv_incremental_10KB.csv | RSA-1024 | CTR | 0.0098 | 0.0223 | 0.0233 |
| csv_incremental_10KB.csv | RSA-2048 | ECB | 0.0098 | 0.0244 | 0.1468 |
| csv_incremental_10KB.csv | RSA-2048 | CBC | 0.0098 | 0.0241 | 0.1480 |
| csv_incremental_10KB.csv | RSA-2048 | CTR | 0.0098 | 0.0262 | 0.0260 |
| csv_incremental_10KB.csv | RSA-4096 | ECB | 0.0098 | 0.0362 | 0.3446 |
| csv_incremental_10KB.csv | RSA-4096 | CBC | 0.0098 | 0.0376 | 0.3505 |
| csv_incremental_10KB.csv | RSA-4096 | CTR | 0.0098 | 0.0419 | 0.0439 |
| csv_incremental_1KB.csv | AES-128 | ECB | 0.0010 | 0.0004 | 0.0004 |
| csv_incremental_1KB.csv | AES-128 | CBC | 0.0010 | 0.0005 | 0.0007 |
| csv_incremental_1KB.csv | AES-128 | CFB | 0.0010 | 0.0007 | 0.0006 |
| csv_incremental_1KB.csv | AES-128 | OFB | 0.0010 | 0.0005 | 0.0005 |
| csv_incremental_1KB.csv | AES-128 | CTR | 0.0010 | 0.0007 | 0.0005 |
| csv_incremental_1KB.csv | AES-256 | ECB | 0.0010 | 0.0006 | 0.0005 |
| csv_incremental_1KB.csv | AES-256 | CBC | 0.0010 | 0.0006 | 0.0005 |
| csv_incremental_1KB.csv | AES-256 | CFB | 0.0010 | 0.0008 | 0.0005 |
| csv_incremental_1KB.csv | AES-256 | OFB | 0.0010 | 0.0006 | 0.0005 |
| csv_incremental_1KB.csv | AES-256 | CTR | 0.0010 | 0.0006 | 0.0005 |
| csv_incremental_1KB.csv | DES | ECB | 0.0010 | 0.0005 | 0.0006 |
| csv_incremental_1KB.csv | DES | CBC | 0.0010 | 0.0006 | 0.0005 |
| csv_incremental_1KB.csv | DES | CFB | 0.0010 | 0.0007 | 0.0005 |
| csv_incremental_1KB.csv | DES | OFB | 0.0010 | 0.0005 | 0.0005 |
| csv_incremental_1KB.csv | DES | CTR | 0.0010 | 0.0005 | 0.0005 |
| csv_incremental_1KB.csv | 3DES | ECB | 0.0010 | 0.0006 | 0.0006 |
| csv_incremental_1KB.csv | 3DES | CBC | 0.0010 | 0.0007 | 0.0013 |
| csv_incremental_1KB.csv | 3DES | CFB | 0.0010 | 0.0015 | 0.0013 |
| csv_incremental_1KB.csv | 3DES | OFB | 0.0010 | 0.0008 | 0.0006 |
| csv_incremental_1KB.csv | 3DES | CTR | 0.0010 | 0.0006 | 0.0007 |
| csv_incremental_1KB.csv | RSA-1024 | ECB | 0.0010 | 0.0027 | 0.0120 |
| csv_incremental_1KB.csv | RSA-1024 | CBC | 0.0010 | 0.0035 | 0.0104 |
| csv_incremental_1KB.csv | RSA-1024 | CTR | 0.0010 | 0.0031 | 0.0030 |
| csv_incremental_1KB.csv | RSA-2048 | ECB | 0.0010 | 0.0030 | 0.0157 |
| csv_incremental_1KB.csv | RSA-2048 | CBC | 0.0010 | 0.0032 | 0.0153 |
| csv_incremental_1KB.csv | RSA-2048 | CTR | 0.0010 | 0.0030 | 0.0033 |
| csv_incremental_1KB.csv | RSA-4096 | ECB | 0.0010 | 0.0057 | 0.0474 |
| csv_incremental_1KB.csv | RSA-4096 | CBC | 0.0010 | 0.0057 | 0.0465 |
| csv_incremental_1KB.csv | RSA-4096 | CTR | 0.0010 | 0.0056 | 0.0058 |
| csv_incremental_1MB.csv | AES-128 | ECB | 1.0000 | 0.0013 | 0.0012 |
| csv_incremental_1MB.csv | AES-128 | CBC | 1.0000 | 0.0029 | 0.0026 |
| csv_incremental_1MB.csv | AES-128 | CFB | 1.0000 | 0.0183 | 0.0181 |
| csv_incremental_1MB.csv | AES-128 | OFB | 1.0000 | 0.0033 | 0.0032 |
| csv_incremental_1MB.csv | AES-128 | CTR | 1.0000 | 0.0015 | 0.0018 |
| csv_incremental_1MB.csv | AES-256 | ECB | 1.0000 | 0.0012 | 0.0013 |
| csv_incremental_1MB.csv | AES-256 | CBC | 1.0000 | 0.0028 | 0.0029 |
| csv_incremental_1MB.csv | AES-256 | CFB | 1.0000 | 0.0211 | 0.0215 |
| csv_incremental_1MB.csv | AES-256 | OFB | 1.0000 | 0.0029 | 0.0025 |
| csv_incremental_1MB.csv | AES-256 | CTR | 1.0000 | 0.0017 | 0.0013 |
| csv_incremental_1MB.csv | DES | ECB | 1.0000 | 0.0112 | 0.0120 |
| csv_incremental_1MB.csv | DES | CBC | 1.0000 | 0.0155 | 0.0135 |
| csv_incremental_1MB.csv | DES | CFB | 1.0000 | 0.0886 | 0.0861 |
| csv_incremental_1MB.csv | DES | OFB | 1.0000 | 0.0135 | 0.0130 |
| csv_incremental_1MB.csv | DES | CTR | 1.0000 | 0.0115 | 0.0112 |
| csv_incremental_1MB.csv | 3DES | ECB | 1.0000 | 0.0320 | 0.0320 |
| csv_incremental_1MB.csv | 3DES | CBC | 1.0000 | 0.0344 | 0.0328 |
| csv_incremental_1MB.csv | 3DES | CFB | 1.0000 | 0.2518 | 0.2485 |
| csv_incremental_1MB.csv | 3DES | OFB | 1.0000 | 0.0343 | 0.0340 |
| csv_incremental_1MB.csv | 3DES | CTR | 1.0000 | 0.0327 | 0.0324 |
| csv_incremental_1MB.csv | RSA-1024 | ECB | 1.0000 | 1.9915 | 8.8294 |
| csv_incremental_1MB.csv | RSA-1024 | CBC | 1.0000 | 2.0779 | 8.9666 |
| csv_incremental_1MB.csv | RSA-1024 | CTR | 1.0000 | 2.0540 | 2.0518 |
| csv_incremental_1MB.csv | RSA-2048 | ECB | 1.0000 | 2.3192 | 14.1713 |
| csv_incremental_1MB.csv | RSA-2048 | CBC | 1.0000 | 2.3771 | 14.2667 |
| csv_incremental_1MB.csv | RSA-2048 | CTR | 1.0000 | 2.3860 | 2.3639 |
| csv_incremental_1MB.csv | RSA-4096 | ECB | 1.0000 | 3.5606 | 34.3233 |
| csv_incremental_1MB.csv | RSA-4096 | CBC | 1.0000 | 3.6233 | 34.1264 |
| csv_incremental_1MB.csv | RSA-4096 | CTR | 1.0000 | 3.5828 | 3.5698 |
| csv_realista_100KB.csv | AES-128 | ECB | 0.0977 | 0.0007 | 0.0006 |
| csv_realista_100KB.csv | AES-128 | CBC | 0.0977 | 0.0008 | 0.0008 |
| csv_realista_100KB.csv | AES-128 | CFB | 0.0977 | 0.0028 | 0.0025 |
| csv_realista_100KB.csv | AES-128 | OFB | 0.0977 | 0.0012 | 0.0007 |
| csv_realista_100KB.csv | AES-128 | CTR | 0.0977 | 0.0010 | 0.0007 |
| csv_realista_100KB.csv | AES-256 | ECB | 0.0977 | 0.0007 | 0.0007 |
| csv_realista_100KB.csv | AES-256 | CBC | 0.0977 | 0.0009 | 0.0008 |
| csv_realista_100KB.csv | AES-256 | CFB | 0.0977 | 0.0028 | 0.0026 |
| csv_realista_100KB.csv | AES-256 | OFB | 0.0977 | 0.0008 | 0.0007 |
| csv_realista_100KB.csv | AES-256 | CTR | 0.0977 | 0.0009 | 0.0008 |
| csv_realista_100KB.csv | DES | ECB | 0.0977 | 0.0017 | 0.0015 |
| csv_realista_100KB.csv | DES | CBC | 0.0977 | 0.0019 | 0.0017 |
| csv_realista_100KB.csv | DES | CFB | 0.0977 | 0.0089 | 0.0086 |
| csv_realista_100KB.csv | DES | OFB | 0.0977 | 0.0018 | 0.0019 |
| csv_realista_100KB.csv | DES | CTR | 0.0977 | 0.0017 | 0.0017 |
| csv_realista_100KB.csv | 3DES | ECB | 0.0977 | 0.0037 | 0.0036 |
| csv_realista_100KB.csv | 3DES | CBC | 0.0977 | 0.0039 | 0.0036 |
| csv_realista_100KB.csv | 3DES | CFB | 0.0977 | 0.0243 | 0.0247 |
| csv_realista_100KB.csv | 3DES | OFB | 0.0977 | 0.0047 | 0.0038 |
| csv_realista_100KB.csv | 3DES | CTR | 0.0977 | 0.0037 | 0.0036 |
| csv_realista_100KB.csv | RSA-1024 | ECB | 0.0977 | 0.1999 | 0.8605 |
| csv_realista_100KB.csv | RSA-1024 | CBC | 0.0977 | 0.2062 | 0.8669 |
| csv_realista_100KB.csv | RSA-1024 | CTR | 0.0977 | 0.2047 | 0.2033 |
| csv_realista_100KB.csv | RSA-2048 | ECB | 0.0977 | 0.2208 | 1.3619 |
| csv_realista_100KB.csv | RSA-2048 | CBC | 0.0977 | 0.2415 | 1.3694 |
| csv_realista_100KB.csv | RSA-2048 | CTR | 0.0977 | 0.2383 | 0.2243 |
| csv_realista_100KB.csv | RSA-4096 | ECB | 0.0977 | 0.3648 | 3.3798 |
| csv_realista_100KB.csv | RSA-4096 | CBC | 0.0977 | 0.3737 | 3.4159 |
| csv_realista_100KB.csv | RSA-4096 | CTR | 0.0977 | 0.3760 | 0.3716 |
| csv_realista_10KB.csv | AES-128 | ECB | 0.0098 | 0.0006 | 0.0005 |
| csv_realista_10KB.csv | AES-128 | CBC | 0.0098 | 0.0007 | 0.0005 |
| csv_realista_10KB.csv | AES-128 | CFB | 0.0098 | 0.0008 | 0.0006 |
| csv_realista_10KB.csv | AES-128 | OFB | 0.0098 | 0.0008 | 0.0005 |
| csv_realista_10KB.csv | AES-128 | CTR | 0.0098 | 0.0007 | 0.0005 |
| csv_realista_10KB.csv | AES-256 | ECB | 0.0098 | 0.0006 | 0.0005 |
| csv_realista_10KB.csv | AES-256 | CBC | 0.0098 | 0.0005 | 0.0006 |
| csv_realista_10KB.csv | AES-256 | CFB | 0.0098 | 0.0008 | 0.0007 |
| csv_realista_10KB.csv | AES-256 | OFB | 0.0098 | 0.0007 | 0.0007 |
| csv_realista_10KB.csv | AES-256 | CTR | 0.0098 | 0.0006 | 0.0006 |
| csv_realista_10KB.csv | DES | ECB | 0.0098 | 0.0006 | 0.0006 |
| csv_realista_10KB.csv | DES | CBC | 0.0098 | 0.0008 | 0.0007 |
| csv_realista_10KB.csv | DES | CFB | 0.0098 | 0.0016 | 0.0014 |
| csv_realista_10KB.csv | DES | OFB | 0.0098 | 0.0007 | 0.0006 |
| csv_realista_10KB.csv | DES | CTR | 0.0098 | 0.0008 | 0.0007 |
| csv_realista_10KB.csv | 3DES | ECB | 0.0098 | 0.0009 | 0.0009 |
| csv_realista_10KB.csv | 3DES | CBC | 0.0098 | 0.0011 | 0.0009 |
| csv_realista_10KB.csv | 3DES | CFB | 0.0098 | 0.0031 | 0.0031 |
| csv_realista_10KB.csv | 3DES | OFB | 0.0098 | 0.0010 | 0.0012 |
| csv_realista_10KB.csv | 3DES | CTR | 0.0098 | 0.0010 | 0.0010 |
| csv_realista_10KB.csv | RSA-1024 | ECB | 0.0098 | 0.0209 | 0.0875 |
| csv_realista_10KB.csv | RSA-1024 | CBC | 0.0098 | 0.0217 | 0.0894 |
| csv_realista_10KB.csv | RSA-1024 | CTR | 0.0098 | 0.0210 | 0.0205 |
| csv_realista_10KB.csv | RSA-2048 | ECB | 0.0098 | 0.0232 | 0.1499 |
| csv_realista_10KB.csv | RSA-2048 | CBC | 0.0098 | 0.0243 | 0.1425 |
| csv_realista_10KB.csv | RSA-2048 | CTR | 0.0098 | 0.0231 | 0.0233 |
| csv_realista_10KB.csv | RSA-4096 | ECB | 0.0098 | 0.0365 | 0.3488 |
| csv_realista_10KB.csv | RSA-4096 | CBC | 0.0098 | 0.0373 | 0.3401 |
| csv_realista_10KB.csv | RSA-4096 | CTR | 0.0098 | 0.0382 | 0.0381 |
| csv_realista_1KB.csv | AES-128 | ECB | 0.0010 | 0.0004 | 0.0005 |
| csv_realista_1KB.csv | AES-128 | CBC | 0.0010 | 0.0005 | 0.0005 |
| csv_realista_1KB.csv | AES-128 | CFB | 0.0010 | 0.0005 | 0.0005 |
| csv_realista_1KB.csv | AES-128 | OFB | 0.0010 | 0.0005 | 0.0006 |
| csv_realista_1KB.csv | AES-128 | CTR | 0.0010 | 0.0007 | 0.0005 |
| csv_realista_1KB.csv | AES-256 | ECB | 0.0010 | 0.0005 | 0.0004 |
| csv_realista_1KB.csv | AES-256 | CBC | 0.0010 | 0.0006 | 0.0005 |
| csv_realista_1KB.csv | AES-256 | CFB | 0.0010 | 0.0005 | 0.0005 |
| csv_realista_1KB.csv | AES-256 | OFB | 0.0010 | 0.0005 | 0.0005 |
| csv_realista_1KB.csv | AES-256 | CTR | 0.0010 | 0.0005 | 0.0005 |
| csv_realista_1KB.csv | DES | ECB | 0.0010 | 0.0005 | 0.0005 |
| csv_realista_1KB.csv | DES | CBC | 0.0010 | 0.0005 | 0.0006 |
| csv_realista_1KB.csv | DES | CFB | 0.0010 | 0.0006 | 0.0007 |
| csv_realista_1KB.csv | DES | OFB | 0.0010 | 0.0006 | 0.0005 |
| csv_realista_1KB.csv | DES | CTR | 0.0010 | 0.0006 | 0.0005 |
| csv_realista_1KB.csv | 3DES | ECB | 0.0010 | 0.0006 | 0.0005 |
| csv_realista_1KB.csv | 3DES | CBC | 0.0010 | 0.0006 | 0.0005 |
| csv_realista_1KB.csv | 3DES | CFB | 0.0010 | 0.0008 | 0.0014 |
| csv_realista_1KB.csv | 3DES | OFB | 0.0010 | 0.0006 | 0.0005 |
| csv_realista_1KB.csv | 3DES | CTR | 0.0010 | 0.0006 | 0.0006 |
| csv_realista_1KB.csv | RSA-1024 | ECB | 0.0010 | 0.0026 | 0.0096 |
| csv_realista_1KB.csv | RSA-1024 | CBC | 0.0010 | 0.0026 | 0.0095 |
| csv_realista_1KB.csv | RSA-1024 | CTR | 0.0010 | 0.0025 | 0.0029 |
| csv_realista_1KB.csv | RSA-2048 | ECB | 0.0010 | 0.0030 | 0.0293 |
| csv_realista_1KB.csv | RSA-2048 | CBC | 0.0010 | 0.0034 | 0.0145 |
| csv_realista_1KB.csv | RSA-2048 | CTR | 0.0010 | 0.0030 | 0.0031 |
| csv_realista_1KB.csv | RSA-4096 | ECB | 0.0010 | 0.0055 | 0.0465 |
| csv_realista_1KB.csv | RSA-4096 | CBC | 0.0010 | 0.0055 | 0.0461 |
| csv_realista_1KB.csv | RSA-4096 | CTR | 0.0010 | 0.0055 | 0.0055 |
| csv_realista_1MB.csv | AES-128 | ECB | 1.0000 | 0.0011 | 0.0011 |
| csv_realista_1MB.csv | AES-128 | CBC | 1.0000 | 0.0027 | 0.0025 |
| csv_realista_1MB.csv | AES-128 | CFB | 1.0000 | 0.0180 | 0.0170 |
| csv_realista_1MB.csv | AES-128 | OFB | 1.0000 | 0.0025 | 0.0024 |
| csv_realista_1MB.csv | AES-128 | CTR | 1.0000 | 0.0014 | 0.0013 |
| csv_realista_1MB.csv | AES-256 | ECB | 1.0000 | 0.0012 | 0.0012 |
| csv_realista_1MB.csv | AES-256 | CBC | 1.0000 | 0.0154 | 0.0027 |
| csv_realista_1MB.csv | AES-256 | CFB | 1.0000 | 0.0222 | 0.0213 |
| csv_realista_1MB.csv | AES-256 | OFB | 1.0000 | 0.0027 | 0.0024 |
| csv_realista_1MB.csv | AES-256 | CTR | 1.0000 | 0.0014 | 0.0015 |
| csv_realista_1MB.csv | DES | ECB | 1.0000 | 0.0108 | 0.0105 |
| csv_realista_1MB.csv | DES | CBC | 1.0000 | 0.0134 | 0.0140 |
| csv_realista_1MB.csv | DES | CFB | 1.0000 | 0.0870 | 0.0844 |
| csv_realista_1MB.csv | DES | OFB | 1.0000 | 0.0149 | 0.0130 |
| csv_realista_1MB.csv | DES | CTR | 1.0000 | 0.0112 | 0.0108 |
| csv_realista_1MB.csv | 3DES | ECB | 1.0000 | 0.0309 | 0.0312 |
| csv_realista_1MB.csv | 3DES | CBC | 1.0000 | 0.0355 | 0.0322 |
| csv_realista_1MB.csv | 3DES | CFB | 1.0000 | 0.2474 | 0.2415 |
| csv_realista_1MB.csv | 3DES | OFB | 1.0000 | 0.0338 | 0.0332 |
| csv_realista_1MB.csv | 3DES | CTR | 1.0000 | 0.0329 | 0.0325 |
| csv_realista_1MB.csv | RSA-1024 | ECB | 1.0000 | 1.9815 | 8.7392 |
| csv_realista_1MB.csv | RSA-1024 | CBC | 1.0000 | 2.0504 | 8.8017 |
| csv_realista_1MB.csv | RSA-1024 | CTR | 1.0000 | 2.0296 | 2.0348 |
| csv_realista_1MB.csv | RSA-2048 | ECB | 1.0000 | 2.2879 | 14.1447 |
| csv_realista_1MB.csv | RSA-2048 | CBC | 1.0000 | 2.3616 | 14.1695 |
| csv_realista_1MB.csv | RSA-2048 | CTR | 1.0000 | 2.3525 | 2.3752 |
| csv_realista_1MB.csv | RSA-4096 | ECB | 1.0000 | 3.6029 | 34.2766 |
| csv_realista_1MB.csv | RSA-4096 | CBC | 1.0000 | 3.6805 | 34.3510 |
| csv_realista_1MB.csv | RSA-4096 | CTR | 1.0000 | 3.6472 | 3.6567 |
| csv_repetitivo_100KB.csv | AES-128 | ECB | 0.0977 | 0.0006 | 0.0005 |
| csv_repetitivo_100KB.csv | AES-128 | CBC | 0.0977 | 0.0021 | 0.0007 |
| csv_repetitivo_100KB.csv | AES-128 | CFB | 0.0977 | 0.0025 | 0.0022 |
| csv_repetitivo_100KB.csv | AES-128 | OFB | 0.0977 | 0.0008 | 0.0008 |
| csv_repetitivo_100KB.csv | AES-128 | CTR | 0.0977 | 0.0008 | 0.0007 |
| csv_repetitivo_100KB.csv | AES-256 | ECB | 0.0977 | 0.0006 | 0.0007 |
| csv_repetitivo_100KB.csv | AES-256 | CBC | 0.0977 | 0.0009 | 0.0007 |
| csv_repetitivo_100KB.csv | AES-256 | CFB | 0.0977 | 0.0027 | 0.0026 |
| csv_repetitivo_100KB.csv | AES-256 | OFB | 0.0977 | 0.0009 | 0.0008 |
| csv_repetitivo_100KB.csv | AES-256 | CTR | 0.0977 | 0.0008 | 0.0008 |
| csv_repetitivo_100KB.csv | DES | ECB | 0.0977 | 0.0019 | 0.0018 |
| csv_repetitivo_100KB.csv | DES | CBC | 0.0977 | 0.0020 | 0.0017 |
| csv_repetitivo_100KB.csv | DES | CFB | 0.0977 | 0.0092 | 0.0086 |
| csv_repetitivo_100KB.csv | DES | OFB | 0.0977 | 0.0018 | 0.0017 |
| csv_repetitivo_100KB.csv | DES | CTR | 0.0977 | 0.0018 | 0.0015 |
| csv_repetitivo_100KB.csv | 3DES | ECB | 0.0977 | 0.0037 | 0.0036 |
| csv_repetitivo_100KB.csv | 3DES | CBC | 0.0977 | 0.0044 | 0.0037 |
| csv_repetitivo_100KB.csv | 3DES | CFB | 0.0977 | 0.0248 | 0.0270 |
| csv_repetitivo_100KB.csv | 3DES | OFB | 0.0977 | 0.0042 | 0.0040 |
| csv_repetitivo_100KB.csv | 3DES | CTR | 0.0977 | 0.0059 | 0.0038 |
| csv_repetitivo_100KB.csv | RSA-1024 | ECB | 0.0977 | 0.1990 | 0.8876 |
| csv_repetitivo_100KB.csv | RSA-1024 | CBC | 0.0977 | 0.2065 | 0.8720 |
| csv_repetitivo_100KB.csv | RSA-1024 | CTR | 0.0977 | 0.2055 | 0.2159 |
| csv_repetitivo_100KB.csv | RSA-2048 | ECB | 0.0977 | 0.2301 | 1.3887 |
| csv_repetitivo_100KB.csv | RSA-2048 | CBC | 0.0977 | 0.2356 | 1.3980 |
| csv_repetitivo_100KB.csv | RSA-2048 | CTR | 0.0977 | 0.2321 | 0.2328 |
| csv_repetitivo_100KB.csv | RSA-4096 | ECB | 0.0977 | 0.3608 | 3.3799 |
| csv_repetitivo_100KB.csv | RSA-4096 | CBC | 0.0977 | 0.3729 | 3.3722 |
| csv_repetitivo_100KB.csv | RSA-4096 | CTR | 0.0977 | 0.3746 | 0.3638 |
| csv_repetitivo_10KB.csv | AES-128 | ECB | 0.0098 | 0.0005 | 0.0005 |
| csv_repetitivo_10KB.csv | AES-128 | CBC | 0.0098 | 0.0006 | 0.0006 |
| csv_repetitivo_10KB.csv | AES-128 | CFB | 0.0098 | 0.0009 | 0.0006 |
| csv_repetitivo_10KB.csv | AES-128 | OFB | 0.0098 | 0.0007 | 0.0007 |
| csv_repetitivo_10KB.csv | AES-128 | CTR | 0.0098 | 0.0007 | 0.0005 |
| csv_repetitivo_10KB.csv | AES-256 | ECB | 0.0098 | 0.0005 | 0.0006 |
| csv_repetitivo_10KB.csv | AES-256 | CBC | 0.0098 | 0.0006 | 0.0006 |
| csv_repetitivo_10KB.csv | AES-256 | CFB | 0.0098 | 0.0008 | 0.0007 |
| csv_repetitivo_10KB.csv | AES-256 | OFB | 0.0098 | 0.0006 | 0.0005 |
| csv_repetitivo_10KB.csv | AES-256 | CTR | 0.0098 | 0.0007 | 0.0005 |
| csv_repetitivo_10KB.csv | DES | ECB | 0.0098 | 0.0006 | 0.0006 |
| csv_repetitivo_10KB.csv | DES | CBC | 0.0098 | 0.0007 | 0.0006 |
| csv_repetitivo_10KB.csv | DES | CFB | 0.0098 | 0.0015 | 0.0013 |
| csv_repetitivo_10KB.csv | DES | OFB | 0.0098 | 0.0007 | 0.0007 |
| csv_repetitivo_10KB.csv | DES | CTR | 0.0098 | 0.0006 | 0.0007 |
| csv_repetitivo_10KB.csv | 3DES | ECB | 0.0098 | 0.0009 | 0.0009 |
| csv_repetitivo_10KB.csv | 3DES | CBC | 0.0098 | 0.0010 | 0.0009 |
| csv_repetitivo_10KB.csv | 3DES | CFB | 0.0098 | 0.0032 | 0.0030 |
| csv_repetitivo_10KB.csv | 3DES | OFB | 0.0098 | 0.0011 | 0.0011 |
| csv_repetitivo_10KB.csv | 3DES | CTR | 0.0098 | 0.0011 | 0.0011 |
| csv_repetitivo_10KB.csv | RSA-1024 | ECB | 0.0098 | 0.0234 | 0.0886 |
| csv_repetitivo_10KB.csv | RSA-1024 | CBC | 0.0098 | 0.0207 | 0.0881 |
| csv_repetitivo_10KB.csv | RSA-1024 | CTR | 0.0098 | 0.0223 | 0.0214 |
| csv_repetitivo_10KB.csv | RSA-2048 | ECB | 0.0098 | 0.0246 | 0.1382 |
| csv_repetitivo_10KB.csv | RSA-2048 | CBC | 0.0098 | 0.0230 | 0.1485 |
| csv_repetitivo_10KB.csv | RSA-2048 | CTR | 0.0098 | 0.0249 | 0.0327 |
| csv_repetitivo_10KB.csv | RSA-4096 | ECB | 0.0098 | 0.0372 | 0.3377 |
| csv_repetitivo_10KB.csv | RSA-4096 | CBC | 0.0098 | 0.0474 | 0.3413 |
| csv_repetitivo_10KB.csv | RSA-4096 | CTR | 0.0098 | 0.0364 | 0.0366 |
| csv_repetitivo_1KB.csv | AES-128 | ECB | 0.0010 | 0.0006 | 0.0004 |
| csv_repetitivo_1KB.csv | AES-128 | CBC | 0.0010 | 0.0005 | 0.0005 |
| csv_repetitivo_1KB.csv | AES-128 | CFB | 0.0010 | 0.0006 | 0.0004 |
| csv_repetitivo_1KB.csv | AES-128 | OFB | 0.0010 | 0.0006 | 0.0005 |
| csv_repetitivo_1KB.csv | AES-128 | CTR | 0.0010 | 0.0005 | 0.0006 |
| csv_repetitivo_1KB.csv | AES-256 | ECB | 0.0010 | 0.0005 | 0.0005 |
| csv_repetitivo_1KB.csv | AES-256 | CBC | 0.0010 | 0.0007 | 0.0005 |
| csv_repetitivo_1KB.csv | AES-256 | CFB | 0.0010 | 0.0005 | 0.0005 |
| csv_repetitivo_1KB.csv | AES-256 | OFB | 0.0010 | 0.0005 | 0.0006 |
| csv_repetitivo_1KB.csv | AES-256 | CTR | 0.0010 | 0.0005 | 0.0005 |
| csv_repetitivo_1KB.csv | DES | ECB | 0.0010 | 0.0006 | 0.0005 |
| csv_repetitivo_1KB.csv | DES | CBC | 0.0010 | 0.0006 | 0.0005 |
| csv_repetitivo_1KB.csv | DES | CFB | 0.0010 | 0.0005 | 0.0006 |
| csv_repetitivo_1KB.csv | DES | OFB | 0.0010 | 0.0005 | 0.0005 |
| csv_repetitivo_1KB.csv | DES | CTR | 0.0010 | 0.0005 | 0.0005 |
| csv_repetitivo_1KB.csv | 3DES | ECB | 0.0010 | 0.0006 | 0.0006 |
| csv_repetitivo_1KB.csv | 3DES | CBC | 0.0010 | 0.0006 | 0.0005 |
| csv_repetitivo_1KB.csv | 3DES | CFB | 0.0010 | 0.0008 | 0.0008 |
| csv_repetitivo_1KB.csv | 3DES | OFB | 0.0010 | 0.0006 | 0.0006 |
| csv_repetitivo_1KB.csv | 3DES | CTR | 0.0010 | 0.0007 | 0.0006 |
| csv_repetitivo_1KB.csv | RSA-1024 | ECB | 0.0010 | 0.0026 | 0.0097 |
| csv_repetitivo_1KB.csv | RSA-1024 | CBC | 0.0010 | 0.0025 | 0.0095 |
| csv_repetitivo_1KB.csv | RSA-1024 | CTR | 0.0010 | 0.0025 | 0.0028 |
| csv_repetitivo_1KB.csv | RSA-2048 | ECB | 0.0010 | 0.0029 | 0.0150 |
| csv_repetitivo_1KB.csv | RSA-2048 | CBC | 0.0010 | 0.0031 | 0.0157 |
| csv_repetitivo_1KB.csv | RSA-2048 | CTR | 0.0010 | 0.0033 | 0.0032 |
| csv_repetitivo_1KB.csv | RSA-4096 | ECB | 0.0010 | 0.0057 | 0.0463 |
| csv_repetitivo_1KB.csv | RSA-4096 | CBC | 0.0010 | 0.0056 | 0.0465 |
| csv_repetitivo_1KB.csv | RSA-4096 | CTR | 0.0010 | 0.0057 | 0.0061 |
| csv_repetitivo_1MB.csv | AES-128 | ECB | 1.0000 | 0.0013 | 0.0014 |
| csv_repetitivo_1MB.csv | AES-128 | CBC | 1.0000 | 0.0028 | 0.0024 |
| csv_repetitivo_1MB.csv | AES-128 | CFB | 1.0000 | 0.0188 | 0.0168 |
| csv_repetitivo_1MB.csv | AES-128 | OFB | 1.0000 | 0.0036 | 0.0023 |
| csv_repetitivo_1MB.csv | AES-128 | CTR | 1.0000 | 0.0015 | 0.0013 |
| csv_repetitivo_1MB.csv | AES-256 | ECB | 1.0000 | 0.0011 | 0.0011 |
| csv_repetitivo_1MB.csv | AES-256 | CBC | 1.0000 | 0.0030 | 0.0030 |
| csv_repetitivo_1MB.csv | AES-256 | CFB | 1.0000 | 0.0212 | 0.0195 |
| csv_repetitivo_1MB.csv | AES-256 | OFB | 1.0000 | 0.0029 | 0.0027 |
| csv_repetitivo_1MB.csv | AES-256 | CTR | 1.0000 | 0.0015 | 0.0015 |
| csv_repetitivo_1MB.csv | DES | ECB | 1.0000 | 0.0110 | 0.0173 |
| csv_repetitivo_1MB.csv | DES | CBC | 1.0000 | 0.0133 | 0.0119 |
| csv_repetitivo_1MB.csv | DES | CFB | 1.0000 | 0.0855 | 0.0862 |
| csv_repetitivo_1MB.csv | DES | OFB | 1.0000 | 0.0130 | 0.0129 |
| csv_repetitivo_1MB.csv | DES | CTR | 1.0000 | 0.0110 | 0.0112 |
| csv_repetitivo_1MB.csv | 3DES | ECB | 1.0000 | 0.0303 | 0.0306 |
| csv_repetitivo_1MB.csv | 3DES | CBC | 1.0000 | 0.0344 | 0.0327 |
| csv_repetitivo_1MB.csv | 3DES | CFB | 1.0000 | 0.2478 | 0.2410 |
| csv_repetitivo_1MB.csv | 3DES | OFB | 1.0000 | 0.0334 | 0.0338 |
| csv_repetitivo_1MB.csv | 3DES | CTR | 1.0000 | 0.0314 | 0.0310 |
| csv_repetitivo_1MB.csv | RSA-1024 | ECB | 1.0000 | 2.0179 | 8.9177 |
| csv_repetitivo_1MB.csv | RSA-1024 | CBC | 1.0000 | 2.0958 | 9.0113 |
| csv_repetitivo_1MB.csv | RSA-1024 | CTR | 1.0000 | 2.1131 | 2.1499 |
| csv_repetitivo_1MB.csv | RSA-2048 | ECB | 1.0000 | 2.2925 | 14.1761 |
| csv_repetitivo_1MB.csv | RSA-2048 | CBC | 1.0000 | 2.3495 | 14.0766 |
| csv_repetitivo_1MB.csv | RSA-2048 | CTR | 1.0000 | 2.3245 | 2.3573 |
| csv_repetitivo_1MB.csv | RSA-4096 | ECB | 1.0000 | 3.6018 | 34.2021 |
| csv_repetitivo_1MB.csv | RSA-4096 | CBC | 1.0000 | 3.6331 | 34.2857 |
| csv_repetitivo_1MB.csv | RSA-4096 | CTR | 1.0000 | 3.6378 | 3.6379 |

### 2.2. Throughput Médio por Algoritmo/Modo

| Algoritmo | Modo | Throughput Médio Cifrar (MB/s) | Throughput Médio Decifrar (MB/s) |
|-----------|------|--------------------------------|----------------------------------|
| 3DES | CBC | 15.9042 | 16.8182 |
| 3DES | CFB | 2.9481 | 3.0521 |
| 3DES | CTR | 16.4081 | 17.0129 |
| 3DES | ECB | 17.6051 | 17.4367 |
| 3DES | OFB | 15.6774 | 16.5327 |
| AES-128 | CBC | 113.4274 | 128.5118 |
| AES-128 | CFB | 27.0596 | 27.9807 |
| AES-128 | CTR | 185.0690 | 210.4855 |
| AES-128 | ECB | 257.1943 | 250.6799 |
| AES-128 | OFB | 112.1449 | 134.0430 |
| AES-256 | CBC | 105.7383 | 126.3061 |
| AES-256 | CFB | 23.9275 | 25.3164 |
| AES-256 | CTR | 183.7453 | 203.1003 |
| AES-256 | ECB | 251.2784 | 249.9987 |
| AES-256 | OFB | 112.6753 | 129.6481 |
| DES | CBC | 32.4603 | 36.7905 |
| DES | CFB | 7.3000 | 7.7639 |
| DES | CTR | 36.9176 | 38.0036 |
| DES | ECB | 40.1636 | 40.0238 |
| DES | OFB | 34.5919 | 35.5092 |
| RSA-1024 | CBC | 0.4377 | 0.1074 |
| RSA-1024 | CTR | 0.4384 | 0.4343 |
| RSA-1024 | ECB | 0.4522 | 0.1077 |
| RSA-2048 | CBC | 0.3881 | 0.0683 |
| RSA-2048 | CTR | 0.3894 | 0.3826 |
| RSA-2048 | ECB | 0.3807 | 0.0669 |
| RSA-4096 | CBC | 0.2443 | 0.0266 |
| RSA-4096 | CTR | 0.2418 | 0.2408 |
| RSA-4096 | ECB | 0.2470 | 0.0268 |

### 2.3. Entropia Média por Abordagem

| Algoritmo | Modo | Entropia Média | Situação de Segurança |
|-----------|------|----------------|-----------------------|
| 3DES | CBC | 7.9476 | ✅ Alta |
| 3DES | CFB | 7.9495 | ✅ Alta |
| 3DES | CTR | 7.9481 | ✅ Alta |
| 3DES | ECB | 7.0534 | 🆗 Média |
| 3DES | OFB | 7.9469 | ✅ Alta |
| AES-128 | CBC | 7.9497 | ✅ Alta |
| AES-128 | CFB | 7.9483 | ✅ Alta |
| AES-128 | CTR | 7.9478 | ✅ Alta |
| AES-128 | ECB | 7.4079 | 🆗 Média |
| AES-128 | OFB | 7.9485 | ✅ Alta |
| AES-256 | CBC | 7.9499 | ✅ Alta |
| AES-256 | CFB | 7.9482 | ✅ Alta |
| AES-256 | CTR | 7.9465 | ✅ Alta |
| AES-256 | ECB | 7.4128 | 🆗 Média |
| AES-256 | OFB | 7.9476 | ✅ Alta |
| DES | CBC | 7.9495 | ✅ Alta |
| DES | CFB | 7.9494 | ✅ Alta |
| DES | CTR | 7.9484 | ✅ Alta |
| DES | ECB | 7.0556 | 🆗 Média |
| DES | OFB | 7.9487 | ✅ Alta |
| RSA-1024 | CBC | 7.9683 | ✅ Alta |
| RSA-1024 | CTR | 7.9477 | ✅ Alta |
| RSA-1024 | ECB | 7.9661 | ✅ Alta |
| RSA-2048 | CBC | 7.9634 | ✅ Alta |
| RSA-2048 | CTR | 7.9462 | ✅ Alta |
| RSA-2048 | ECB | 7.9593 | ✅ Alta |
| RSA-4096 | CBC | 7.9737 | ✅ Alta |
| RSA-4096 | CTR | 7.9486 | ✅ Alta |
| RSA-4096 | ECB | 7.9649 | ✅ Alta |

## 3. Gráficos de Análise

### Throughput vs Tamanho
![Gráfico de Throughput](../graficos/throughput_vs_tamanho_2026-04-13_04-11-23.png)

### Entropia vs Modo de Operação
![Gráfico de Entropia](../graficos/entropia_vs_modo_2026-04-13_04-11-24.png)
