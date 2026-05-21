# Crypto Architecture Kit 总览与主题路由

## 使用方式

- 当用户问题主题不明确时，先根据下面的主题索引定位主主题，再读取对应 reference。
- 默认先看开发指南；需要接口细节时再看 API；需要避坑和排障时再补最佳实践或 FAQ。

## 主题索引

### Crypto Architecture Kit（加解密算法框架服务）

#### 主题入口

- 开发指南入口
  - 1 Crypto Architecture Kit（加解密算法框架服务）开发指南：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-architecture-kit
    - 关键词：Crypto Architecture Kit（加解密算法框架服务）

### Crypto Architecture Kit

#### 主题入口

- 开发指南入口
  - 1.1 Crypto Architecture Kit简介：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-architecture-kit-intro
    - 关键词：Crypto Architecture Kit

### 密钥生成和转换

#### 主题入口

- 开发指南入口
  - 1.2 密钥生成和转换：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-generation-conversion
    - 关键词：密钥生成和转换
  - 1.2.1 密钥生成与转换介绍：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-generation-conversion-overview
    - 关键词：密钥生成与转换介绍
  - 1.2.2 密钥生成和转换规格：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-generation-conversion-spec
    - 关键词：密钥生成和转换规格
  - 1.2.3 密钥生成和转换开发指导：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-generation-conversion-dev
    - 关键词：密钥生成和转换

### 密钥生成和转换规格

#### 主题入口

- 开发指南入口
  - 1.2.2.1 对称密钥生成和转换规格：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-key-generation-conversion-spec
    - 关键词：对称密钥生成和转换规格
  - 1.2.2.2 非对称密钥生成和转换规格：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec
    - 关键词：非对称密钥生成和转换规格

### 密钥生成和转换开发指导

#### 主题入口

- 开发指南入口
  - 1.2.3.1 随机生成对称密钥(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-sym-key-randomly
    - 关键词：随机生成对称密钥 / ArkTS
  - 1.2.3.2 随机生成对称密钥(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-sym-key-randomly-ndk
    - 关键词：随机生成对称密钥 / C++
  - 1.2.3.3 指定二进制数据转换对称密钥(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-convert-binary-data-to-sym-key
    - 关键词：ArkTS
  - 1.2.3.4 指定二进制数据转换对称密钥(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-convert-binary-data-to-sym-key-ndk
    - 关键词：C++
  - 1.2.3.5 随机生成非对称密钥对(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-asym-key-pair-randomly
    - 关键词：随机生成非对称密钥对 / ArkTS
  - 1.2.3.6 随机生成非对称密钥对(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-asym-key-pair-randomly-ndk
    - 关键词：随机生成非对称密钥对 / C++
  - 1.2.3.7 指定二进制数据转换非对称密钥对(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-convert-binary-data-to-asym-key-pair
    - 关键词：ArkTS
  - 1.2.3.8 指定二进制数据转换非对称密钥对(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-convert-binary-data-to-asym-key-pair-ndk
    - 关键词：C++
  - 1.2.3.9 指定密钥参数生成非对称密钥对(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-asym-key-pair-from-key-spec
    - 关键词：ArkTS
  - 1.2.3.10 指定密钥参数生成非对称密钥对(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-asym-key-pair-from-key-spec-ndk
    - 关键词：C++
  - 1.2.3.11 使用ECC压缩/非压缩公钥格式转换(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ypto-convert-compressed-or-uncompressed-ecc-pubkey
    - 关键词：ECC压缩 / 非压缩公钥格式转换 / ArkTS
  - 1.2.3.12 使用ECC压缩/非压缩公钥格式转换(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/-convert-compressed-or-uncompressed-ecc-pubkey-ndk
    - 关键词：ECC压缩 / 非压缩公钥格式转换 / C++
  - 1.2.3.13 使用ECC压缩/非压缩点格式转换(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rypto-convert-compressed-or-uncompressed-ecc-point
    - 关键词：ECC压缩 / 非压缩点格式转换 / ArkTS
  - 1.2.3.14 使用ECC压缩/非压缩点格式转换(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/o-convert-compressed-or-uncompressed-ecc-point-ndk
    - 关键词：ECC压缩 / 非压缩点格式转换 / C++
  - 1.2.3.15 指定PEM格式字符串数据转换非对称密钥对(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-convert-string-data-to-asym-key-pair
    - 关键词：指定PEM格式字符串数据转换非对称密钥对 / ArkTS
  - 1.2.3.16 指定PEM格式字符串数据转换非对称密钥对(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-convert-string-data-to-asym-key-pair-ndk
    - 关键词：指定PEM格式字符串数据转换非对称密钥对 / C++
  - 1.2.3.17 使用RSA私钥进行编码解码(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-encoded-decoded
    - 关键词：RSA私钥进行编码解码 / ArkTS
  - 1.2.3.18 使用RSA私钥进行编码解码(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-encoded-decoded-ndk
    - 关键词：RSA私钥进行编码解码 / C++

### 加解密

#### 主题入口

- 开发指南入口
  - 1.3 加解密：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-encryption-decryption
    - 关键词：加解密
  - 1.3.1 加解密介绍：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-encryption-decryption-overview
    - 关键词：加解密介绍
  - 1.3.2 加解密算法规格：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-encrypt-decrypt-spec
    - 关键词：加解密算法规格
  - 1.3.3 加解密开发指导：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-encrypt-decrypt-dev
    - 关键词：加解密

### 加解密算法规格

#### 主题入口

- 开发指南入口
  - 1.3.2.1 对称密钥加解密算法规格：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-encrypt-decrypt-spec
    - 关键词：对称密钥加解密算法规格
  - 1.3.2.2 非对称密钥加解密算法规格：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-encrypt-decrypt-spec
    - 关键词：非对称密钥加解密算法规格
  - 1.3.2.3 分段加解密说明：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-encrypt-decrypt-by-segment
    - 关键词：分段加解密说明

### 加解密开发指导

#### 主题入口

- 开发指南入口
  - 1.3.3.1 使用AES对称密钥（GCM模式）加解密(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm
    - 关键词：AES对称密钥（GCM模式）加解密 / ArkTS
  - 1.3.3.2 使用AES对称密钥（GCM模式）加解密(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm-ndk
    - 关键词：AES对称密钥（GCM模式）加解密 / C++
  - 1.3.3.3 使用AES对称密钥（CCM模式）加解密(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-ccm
    - 关键词：AES对称密钥（CCM模式）加解密 / ArkTS
  - 1.3.3.4 使用AES对称密钥（CCM模式）加解密(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-ccm-ndk
    - 关键词：AES对称密钥（CCM模式）加解密 / C++
  - 1.3.3.5 使用AES对称密钥（CBC模式）加解密(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-cbc
    - 关键词：AES对称密钥（CBC模式）加解密 / ArkTS
  - 1.3.3.6 使用AES对称密钥（CBC模式）加解密(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-cbc-ndk
    - 关键词：AES对称密钥（CBC模式）加解密 / C++
  - 1.3.3.7 使用AES对称密钥（ECB模式）加解密(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-ecb
    - 关键词：AES对称密钥（ECB模式）加解密 / ArkTS
  - 1.3.3.8 使用AES对称密钥（ECB模式）加解密(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-ecb-ndk
    - 关键词：AES对称密钥（ECB模式）加解密 / C++
  - 1.3.3.9 使用AES对称密钥（GCM模式）分段加解密(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm-by-segment
    - 关键词：AES对称密钥（GCM模式）分段加解密 / ArkTS
  - 1.3.3.10 使用AES对称密钥（GCM模式）分段加解密(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm-by-segment-ndk
    - 关键词：AES对称密钥（GCM模式）分段加解密 / C++
  - 1.3.3.11 使用DES对称密钥（ECB模式）加解密(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-des-sym-encrypt-decrypt-ecb
    - 关键词：DES对称密钥（ECB模式）加解密 / ArkTS
  - 1.3.3.12 使用DES对称密钥（ECB模式）加解密(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-des-sym-encrypt-decrypt-ecb-ndk
    - 关键词：DES对称密钥（ECB模式）加解密 / C++
  - 1.3.3.13 使用3DES对称密钥加解密(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-3des-sym-encrypt-decrypt-ecb
    - 关键词：3DES对称密钥加解密 / ArkTS
  - 1.3.3.14 使用3DES对称密钥加解密(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-3des-sym-encrypt-decrypt-ecb-ndk
    - 关键词：3DES对称密钥加解密 / C++
  - 1.3.3.15 使用SM4对称密钥（ECB模式）加解密(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm4-sym-encrypt-decrypt-ecb
    - 关键词：SM4对称密钥（ECB模式）加解密 / ArkTS
  - 1.3.3.16 使用SM4对称密钥（ECB模式）加解密(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm4-sym-encrypt-decrypt-ecb-ndk
    - 关键词：SM4对称密钥（ECB模式）加解密 / C++
  - 1.3.3.17 使用SM4对称密钥（CBC模式）加解密(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm4-sym-encrypt-decrypt-cbc
    - 关键词：SM4对称密钥（CBC模式）加解密 / ArkTS
  - 1.3.3.18 使用SM4对称密钥（CBC模式）加解密(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm4-sym-encrypt-decrypt-cbc-ndk
    - 关键词：SM4对称密钥（CBC模式）加解密 / C++
  - 1.3.3.19 使用SM4对称密钥（GCM模式）加解密(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm4-sym-encrypt-decrypt-gcm
    - 关键词：SM4对称密钥（GCM模式）加解密 / ArkTS
  - 1.3.3.20 使用SM4对称密钥（GCM模式）加解密(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm4-sym-encrypt-decrypt-gcm-ndk
    - 关键词：SM4对称密钥（GCM模式）加解密 / C++
  - 1.3.3.21 使用SM4对称密钥（GCM模式）分段加解密(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm4-sym-encrypt-decrypt-gcm-by-segment
    - 关键词：SM4对称密钥（GCM模式）分段加解密 / ArkTS
  - 1.3.3.22 使用SM4对称密钥（GCM模式）分段加解密(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm4-sym-encrypt-decrypt-gcm-by-segment-ndk
    - 关键词：SM4对称密钥（GCM模式）分段加解密 / C++
  - 1.3.3.23 使用ChaCha20对称密钥加解密(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-chacha20-encrypt-decrypt
    - 关键词：ChaCha20对称密钥加解密 / ArkTS
  - 1.3.3.24 使用ChaCha20对称密钥加解密(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-chacha20-encrypt-decrypt-ndk
    - 关键词：ChaCha20对称密钥加解密 / C++
  - 1.3.3.25 使用ChaCha20对称密钥（Poly1305模式）加解密(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-chacha20-encrypt-decrypt-poly1305
    - 关键词：ChaCha20对称密钥（Poly1305模式）加解密 / ArkTS
  - 1.3.3.26 使用ChaCha20对称密钥（Poly1305模式）加解密(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-chacha20-encrypt-decrypt-poly1305-ndk
    - 关键词：ChaCha20对称密钥（Poly1305模式）加解密 / C++
  - 1.3.3.27 使用RSA非对称密钥（PKCS1模式）加解密(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-pkcs1
    - 关键词：RSA非对称密钥（PKCS1模式）加解密 / ArkTS
  - 1.3.3.28 使用RSA非对称密钥（PKCS1模式）加解密(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-pkcs1-ndk
    - 关键词：RSA非对称密钥（PKCS1模式）加解密 / C++
  - 1.3.3.29 使用RSA非对称密钥分段加解密(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-by-segment
    - 关键词：RSA非对称密钥分段加解密 / ArkTS
  - 1.3.3.30 使用RSA非对称密钥分段加解密(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-by-segment-ndk
    - 关键词：RSA非对称密钥分段加解密 / C++
  - 1.3.3.31 使用RSA非对称密钥（PKCS1_OAEP模式）加解密：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-pkcs1_oaep
    - 关键词：RSA非对称密钥（PKCS1_OAEP模式）加解密
  - 1.3.3.32 使用SM2非对称密钥加解密(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm2-asym-encrypt-decrypt
    - 关键词：SM2非对称密钥加解密 / ArkTS
  - 1.3.3.33 使用SM2非对称密钥加解密(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm2-asym-encrypt-decrypt-ndk
    - 关键词：SM2非对称密钥加解密 / C++
  - 1.3.3.34 使用AES-WRAP算法对对称密钥加解密(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-wrap-encrypt-decrypt
    - 关键词：AES / WRAP算法对对称密钥加解密 / ArkTS
  - 1.3.3.35 使用AES-WRAP算法对对称密钥加解密(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-wrap-encrypt-decrypt-ndk
    - 关键词：AES / WRAP算法对对称密钥加解密 / C++
  - 1.3.3.36 使用SM2密文格式转换(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm2-ciphertext-conversion
    - 关键词：SM2密文格式转换 / ArkTS
  - 1.3.3.37 使用SM2密文格式转换(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm2-ciphertext-conversion-ndk
    - 关键词：SM2密文格式转换 / C++

### 签名验签

#### 主题入口

- 开发指南入口
  - 1.4 签名验签：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sign-sig-verify
    - 关键词：签名验签
  - 1.4.1 签名验签介绍及算法规格：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sign-sig-verify-overview
    - 关键词：签名验签介绍及算法规格
  - 1.4.2 签名验签开发指导：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sign-sig-verify-dev
    - 关键词：签名验签

### 签名验签开发指导

#### 主题入口

- 开发指南入口
  - 1.4.2.1 使用RSA密钥对（PKCS1模式）签名验签(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1
    - 关键词：RSA密钥对（PKCS1模式）签名验签 / ArkTS
  - 1.4.2.2 使用RSA密钥对签名验签 (PKCS1模式)(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1-ndk
    - 关键词：RSA密钥对签名验签 / PKCS1模式 / C++
  - 1.4.2.3 使用RSA密钥对（PKCS1模式）签名及签名恢复(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-recover-pkcs1
    - 关键词：RSA密钥对（PKCS1模式）签名及签名恢复 / ArkTS
  - 1.4.2.4 使用RSA密钥对（PKCS1模式）签名恢复(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-recover-pkcs1-ndk
    - 关键词：RSA密钥对（PKCS1模式）签名恢复 / C++
  - 1.4.2.5 使用RSA密钥对分段签名验签（PKCS1模式）(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1-by-segment
    - 关键词：RSA密钥对分段签名验签（PKCS1模式） / ArkTS
  - 1.4.2.6 使用RSA密钥对分段签名验签 (PKCS1模式)(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1-by-segment-ndk
    - 关键词：RSA密钥对分段签名验签 / PKCS1模式 / C++
  - 1.4.2.7 使用RSA密钥对签名验签（PSS模式）(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pss
    - 关键词：RSA密钥对签名验签（PSS模式） / ArkTS
  - 1.4.2.8 使用RSA密钥对签名验签 (PSS模式)(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pss-ndk
    - 关键词：RSA密钥对签名验签 / PSS模式 / C++
  - 1.4.2.9 使用ECDSA密钥对签名验签(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-ecdsa-sign-sig-verify
    - 关键词：ECDSA密钥对签名验签 / ArkTS
  - 1.4.2.10 使用ECDSA密钥对签名验签 (C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-ecdsa-sign-sig-verify-ndk
    - 关键词：ECDSA密钥对签名验签 / C++
  - 1.4.2.11 使用SM2密钥对签名验签(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm2-sign-sig-verify-pkcs1
    - 关键词：SM2密钥对签名验签 / ArkTS
  - 1.4.2.12 使用SM2密钥对签名验签 (C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm2-sign-sig-verify-pkcs1-ndk
    - 关键词：SM2密钥对签名验签 / C++
  - 1.4.2.13 SM2签名数据格式转换(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm2-sign-data-format-conversion
    - 关键词：SM2签名数据格式转换 / ArkTS
  - 1.4.2.14 SM2签名数据格式转换 (C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm2-sign-data-format-conversion-ndk
    - 关键词：SM2签名数据格式转换 / C++

### 密钥协商

#### 主题入口

- 开发指南入口
  - 1.5 密钥协商：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement
    - 关键词：密钥协商
  - 1.5.1 密钥协商介绍及算法规格：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-overview
    - 关键词：密钥协商介绍及算法规格
  - 1.5.2 密钥协商开发指导：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-dev
    - 关键词：密钥协商

### 密钥协商开发指导

#### 主题入口

- 开发指南入口
  - 1.5.2.1 使用ECDH进行密钥协商(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-using-ecdh
    - 关键词：ECDH进行密钥协商 / ArkTS
  - 1.5.2.2 使用ECDH进行密钥协商(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-using-ecdh-ndk
    - 关键词：ECDH进行密钥协商 / C++
  - 1.5.2.3 使用X25519进行密钥协商(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-using-x25519
    - 关键词：X25519进行密钥协商 / ArkTS
  - 1.5.2.4 使用X25519进行密钥协商(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-using-x25519-ndk
    - 关键词：X25519进行密钥协商 / C++
  - 1.5.2.5 使用DH进行密钥协商(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-using-dh
    - 关键词：DH进行密钥协商 / ArkTS
  - 1.5.2.6 使用DH进行密钥协商(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-using-dh-ndk
    - 关键词：DH进行密钥协商 / C++

### 消息摘要计算

#### 主题入口

- 开发指南入口
  - 1.6 消息摘要计算：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message
    - 关键词：消息摘要计算
  - 1.6.1 消息摘要计算介绍及算法规格：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest-overview
  - 1.6.2 消息摘要计算开发指导：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest-dev
    - 关键词：消息摘要计算

### 消息摘要计算开发指导

#### 主题入口

- 开发指南入口
  - 1.6.2.1 消息摘要计算SHA256(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest
    - 关键词：消息摘要计算SHA256 / ArkTS
  - 1.6.2.2 消息摘要计算SHA256(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest-ndk
    - 关键词：消息摘要计算SHA256 / C++
  - 1.6.2.3 消息摘要计算MD5(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest-md5
    - 关键词：消息摘要计算MD5 / ArkTS
  - 1.6.2.4 消息摘要计算MD5(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest-md5-ndk
    - 关键词：消息摘要计算MD5 / C++
  - 1.6.2.5 消息摘要计算SHA3(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest-sha3
    - 关键词：消息摘要计算SHA3 / ArkTS
  - 1.6.2.6 消息摘要计算SHA3-256(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest-sha3-ndk
    - 关键词：消息摘要计算SHA3 / C++

### 消息认证码

#### 主题入口

- 开发指南入口
  - 1.7 消息认证码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-compute-mac
    - 关键词：消息认证码
  - 1.7.1 消息认证码计算介绍及算法规格：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-compute-mac-overview
  - 1.7.2 消息认证码计算HMAC(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-compute-hmac
    - 关键词：消息认证码计算HMAC / ArkTS
  - 1.7.3 消息认证码计算HMAC(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-compute-hmac-ndk
    - 关键词：消息认证码计算HMAC / C++
  - 1.7.4 消息认证码计算CMAC(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-compute-cmac
    - 关键词：消息认证码计算CMAC / ArkTS
  - 1.7.5 消息认证码计算CMAC(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-compute-cmac-ndk
    - 关键词：消息认证码计算CMAC / C++

### 随机数

#### 主题入口

- 开发指南入口
  - 1.8 随机数：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-compute-rand
    - 关键词：随机数
  - 1.8.1 安全随机数生成(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-random-number
    - 关键词：安全随机数生成 / ArkTS
  - 1.8.2 安全随机数生成(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-random-number-ndk
    - 关键词：安全随机数生成 / C++
  - 1.8.3 使用硬件熵源生成安全随机数(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-random-number-hardware
    - 关键词：硬件熵源生成安全随机数 / ArkTS
  - 1.8.4 使用硬件熵源生成安全随机数(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-random-number-hardware-ndk
    - 关键词：硬件熵源生成安全随机数 / C++

### 密钥派生

#### 主题入口

- 开发指南入口
  - 1.9 密钥派生：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation
    - 关键词：密钥派生
  - 1.9.1 密钥派生介绍及算法规格：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-overview
    - 关键词：密钥派生介绍及算法规格
  - 1.9.2 使用PBKDF2进行密钥派生(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-pbkdf2
    - 关键词：PBKDF2进行密钥派生 / ArkTS
  - 1.9.3 使用PBKDF2进行密钥派生(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-pbkdf2-ndk
    - 关键词：PBKDF2进行密钥派生 / C++
  - 1.9.4 使用HKDF进行密钥派生(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-hkdf
    - 关键词：HKDF进行密钥派生 / ArkTS
  - 1.9.5 使用HKDF进行密钥派生(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-hkdf-ndk
    - 关键词：HKDF进行密钥派生 / C++
  - 1.9.6 使用SCRYPT进行密钥派生(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-scrypt
    - 关键词：SCRYPT进行密钥派生 / ArkTS
  - 1.9.7 使用SCRYPT进行密钥派生(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-scrypt-ndk
    - 关键词：SCRYPT进行密钥派生 / C++
  - 1.9.8 使用X963KDF进行密钥派生(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-x963kdf
    - 关键词：X963KDF进行密钥派生 / ArkTS
  - 1.9.9 使用X963KDF进行密钥派生(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-x963kdf-ndk
    - 关键词：X963KDF进行密钥派生 / C++

### 跨平台数据兼容实践指导

#### 主题入口

- 开发指南入口
  - 1.10 跨平台数据兼容实践指导：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-development-practice
    - 关键词：跨平台数据兼容实践指导

### 最佳实践与FAQ

#### 最佳实践

- 最佳实践入口
  - 3 Crypto Architecture Kit（加解密算法框架服务）最佳实践：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-cross-platform-compatibility
    - 关键词：Crypto Architecture Kit（加解密算法框架服务）

#### 常见问题

- FAQ入口
  - 1.11 Crypto Architecture Kit常见问题：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-faqs
    - 关键词：Crypto Architecture Kit
  - 4 Crypto Architecture Kit（加解密算法框架服务）FAQ：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-kit
    - 关键词：Crypto Architecture Kit（加解密算法框架服务）

#### 场景排障

- FAQ入口
  - 1.11.1 AES解密失败返回17630001：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-decryption-error-faq
    - 关键词：AES解密失败返回17630001
  - 4.1 ECC算法是否支持secp256r1：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-5
    - 关键词：ECC算法是否支持secp256r1
  - 4.2 如何使用AES算法加密：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs-V5/faqs-crypto-architecture-15-V5
    - 关键词：如何使用AES算法加密
  - 4.3 在进行aes加密的时候，如何把字符串转换成Key对象：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-28
    - 关键词：在进行aes加密的时候 / 如何把字符串转换成Key对象
  - 4.4 如何使用SM3算法生成散列值：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-29
    - 关键词：如何使用SM3算法生成散列值

### API与错误码

#### 核心 API

- API入口
  - 2 Crypto Architecture Kit（加解密算法框架服务）API参考：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/crypto-architecture-api
    - 关键词：Crypto Architecture Kit（加解密算法框架服务）
  - 2.1 ArkTS API：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/crypto-architecture-arkts
    - 关键词：ArkTS
  - 2.1.1 @ohos.security.cryptoFramework (加解密算法库框架)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework
    - 关键词：@ohos.security.cryptoFramework / 加解密算法库框架
  - 2.1.2.1 @system.cipher (加密算法)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-cipher
    - 关键词：@system.cipher / 加密算法
  - 2.2 C API：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/crypto-architecture-c
  - 2.2.1 模块：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/crypto-architecture-module
  - 2.2.1.1 CryptoArchitectureKit：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoarchitecturekit
    - 关键词：CryptoArchitectureKit
  - 2.2.1.2 CryptoAsymCipherApi：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymcipherapi
    - 关键词：CryptoAsymCipherApi
  - 2.2.1.3 CryptoAsymKeyApi：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi
    - 关键词：CryptoAsymKeyApi
  - 2.2.1.4 CryptoCommonApi：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi
    - 关键词：CryptoCommonApi
  - 2.2.1.5 CryptoDigestApi：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptodigestapi
    - 关键词：CryptoDigestApi
  - 2.2.1.6 CryptoKdfApi：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptokdfapi
    - 关键词：CryptoKdfApi
  - 2.2.1.7 CryptoKeyAgreementApi：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptokeyagreementapi
    - 关键词：CryptoKeyAgreementApi
  - 2.2.1.8 CryptoMacApi：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptomacapi
    - 关键词：CryptoMacApi
  - 2.2.1.9 CryptoRandApi：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptorandapi
    - 关键词：CryptoRandApi
  - 2.2.1.10 CryptoSignatureApi：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosignatureapi
    - 关键词：CryptoSignatureApi
  - 2.2.1.11 CryptoSymCipherApi：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosymcipherapi
    - 关键词：CryptoSymCipherApi
  - 2.2.1.12 CryptoSymKeyApi：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosymkeyapi
    - 关键词：CryptoSymKeyApi
  - 2.2.2 头文件：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/crypto-architecture-headerfile
  - 2.2.2.1 crypto_architecture_kit.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-architecture-kit-h
    - 关键词：crypto_architecture_kit.h
  - 2.2.2.2 crypto_asym_cipher.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h
    - 关键词：crypto_asym_cipher.h
  - 2.2.2.3 crypto_asym_key.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h
    - 关键词：crypto_asym_key.h
  - 2.2.2.4 crypto_common.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h
    - 关键词：crypto_common.h
  - 2.2.2.5 crypto_digest.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-digest-h
    - 关键词：crypto_digest.h
  - 2.2.2.6 crypto_kdf.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-kdf-h
    - 关键词：crypto_kdf.h
  - 2.2.2.7 crypto_key_agreement.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-key-agreement-h
    - 关键词：crypto_key_agreement.h
  - 2.2.2.8 crypto_mac.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-mac-h
    - 关键词：crypto_mac.h
  - 2.2.2.9 crypto_rand.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-rand-h
    - 关键词：crypto_rand.h
  - 2.2.2.10 crypto_signature.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-signature-h
    - 关键词：crypto_signature.h
  - 2.2.2.11 crypto_sym_cipher.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h
    - 关键词：crypto_sym_cipher.h
  - 2.2.2.12 crypto_sym_key.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h
    - 关键词：crypto_sym_key.h
  - 2.2.3 结构体：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/crypto-architecture-struct
  - 2.2.3.1 Crypto_DataBlob：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi-crypto-datablob
    - 关键词：Crypto_DataBlob
  - 2.2.3.2 OH_CryptoAsymCipher：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymcipherapi-oh-cryptoasymcipher
    - 关键词：OH_CryptoAsymCipher
  - 2.2.3.3 OH_CryptoSm2CiphertextSpec：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-cryptoasymcipherapi-oh-cryptosm2ciphertextspec
    - 关键词：OH_CryptoSm2CiphertextSpec
  - 2.2.3.4 OH_CryptoKeyPair：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi-oh-cryptokeypair
    - 关键词：OH_CryptoKeyPair
  - 2.2.3.5 OH_CryptoPubKey：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi-oh-cryptopubkey
    - 关键词：OH_CryptoPubKey
  - 2.2.3.6 OH_CryptoPrivKey：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi-oh-cryptoprivkey
    - 关键词：OH_CryptoPrivKey
  - 2.2.3.7 OH_CryptoAsymKeyGenerator：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi-oh-cryptoasymkeygenerator
    - 关键词：OH_CryptoAsymKeyGenerator
  - 2.2.3.8 OH_CryptoPrivKeyEncodingParams：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-cryptoasymkeyapi-oh-cryptoprivkeyencodingparams
    - 关键词：OH_CryptoPrivKeyEncodingParams
  - 2.2.3.9 OH_CryptoAsymKeySpec：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi-oh-cryptoasymkeyspec
    - 关键词：OH_CryptoAsymKeySpec
  - 2.2.3.10 OH_CryptoAsymKeyGeneratorWithSpec：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cryptoasymkeyapi-oh-cryptoasymkeygeneratorwithspec
    - 关键词：OH_CryptoAsymKeyGeneratorWithSpec
  - 2.2.3.11 OH_CryptoEcPoint：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi-oh-cryptoecpoint
    - 关键词：OH_CryptoEcPoint
  - 2.2.3.12 OH_CryptoDigest：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptodigestapi-oh-cryptodigest
    - 关键词：OH_CryptoDigest
  - 2.2.3.13 OH_CryptoKdf：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptokdfapi-oh-cryptokdf
    - 关键词：OH_CryptoKdf
  - 2.2.3.14 OH_CryptoKdfParams：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptokdfapi-oh-cryptokdfparams
    - 关键词：OH_CryptoKdfParams
  - 2.2.3.15 OH_CryptoKeyAgreement：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptokeyagreementapi-oh-cryptokeyagreement
    - 关键词：OH_CryptoKeyAgreement
  - 2.2.3.16 OH_CryptoMac：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptomacapi-oh-cryptomac
    - 关键词：OH_CryptoMac
  - 2.2.3.17 OH_CryptoRand：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptorandapi-oh-cryptorand
    - 关键词：OH_CryptoRand
  - 2.2.3.18 OH_CryptoVerify：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosignatureapi-oh-cryptoverify
    - 关键词：OH_CryptoVerify
  - 2.2.3.19 OH_CryptoSign：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosignatureapi-oh-cryptosign
    - 关键词：OH_CryptoSign
  - 2.2.3.20 OH_CryptoEccSignatureSpec：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosignatureapi-oh-cryptoeccsignaturespec
    - 关键词：OH_CryptoEccSignatureSpec
  - 2.2.3.21 OH_CryptoSymCipher：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosymcipherapi-oh-cryptosymcipher
    - 关键词：OH_CryptoSymCipher
  - 2.2.3.22 OH_CryptoSymCipherParams：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosymcipherapi-oh-cryptosymcipherparams
    - 关键词：OH_CryptoSymCipherParams
  - 2.2.3.23 OH_CryptoSymKey：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosymkeyapi-oh-cryptosymkey
    - 关键词：OH_CryptoSymKey
  - 2.2.3.24 OH_CryptoSymKeyGenerator：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosymkeyapi-oh-cryptosymkeygenerator
    - 关键词：OH_CryptoSymKeyGenerator

#### 已停止维护接口

- API入口
  - 2.1.2 已停止维护的接口：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/crypto-architecture-arkts-dep
    - 关键词：已停止维护的接口

#### 错误码

- API入口
  - 2.3 错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/crypto-architecture-arkts-errcode
    - 关键词：错误码
  - 2.3.1 crypto framework错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-crypto-framework
    - 关键词：crypto framework错误码

## 路由提示

- 问 Crypto Architecture Kit（加解密算法框架服务） 相关问题时，转到 `crypto-architecture-kit.md`
- 问 Crypto Architecture Kit 相关问题时，转到 `crypto-architecture-kit.md`
- 问 密钥生成和转换 相关问题时，转到 `topic-e7a37a4c.md`
- 问 密钥生成和转换规格 相关问题时，转到 `topic-f29df0c9.md`
- 问 密钥生成和转换开发指导 相关问题时，转到 `topic-73f6d990.md`
- 问 加解密 相关问题时，转到 `topic-93b13c0b.md`
- 问 加解密算法规格 相关问题时，转到 `topic-3f69fcf8.md`
- 问 加解密开发指导 相关问题时，转到 `topic-b269997c.md`
- 问 签名验签 相关问题时，转到 `topic-37c48bae.md`
- 问 签名验签开发指导 相关问题时，转到 `topic-dea5b287.md`
- 问 密钥协商 相关问题时，转到 `topic-7f49bf0c.md`
- 问 密钥协商开发指导 相关问题时，转到 `topic-966a788d.md`
- 问 消息摘要计算 相关问题时，转到 `topic-64238e20.md`
- 问 消息摘要计算开发指导 相关问题时，转到 `topic-eb6e73a9.md`
- 问 消息认证码 相关问题时，转到 `topic-9088e9bc.md`
- 问 随机数 相关问题时，转到 `topic-5bfedcff.md`
- 问 密钥派生 相关问题时，转到 `topic-b535db4c.md`
- 问 跨平台数据兼容实践指导 相关问题时，转到 `topic-a70c4d21.md`
- 问 Crypto Architecture Kit、AES解密失败返回17630001、ECC算法是否支持secp256r1、如何使用AES算法加密、在进行aes加密的时候 时，转到 `best-practices-and-faq.md`
- 问 加解密算法库框架、已停止维护的接口、@system.cipher、加密算法、CryptoArchitectureKit 时，转到 `api-and-error-codes.md`
