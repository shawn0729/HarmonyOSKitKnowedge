# 1 Crypto Architecture Kit（加解密算法框架服务）开发指南:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-architecture-kit

## 1.1 Crypto Architecture Kit简介:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-architecture-kit-intro

## 1.2 密钥生成和转换:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-generation-conversion

### 1.2.1 密钥生成与转换介绍:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-generation-conversion-overview

### 1.2.2 密钥生成和转换规格:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-generation-conversion-spec

#### 1.2.2.1 对称密钥生成和转换规格:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-key-generation-conversion-spec

#### 1.2.2.2 非对称密钥生成和转换规格:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec

### 1.2.3 密钥生成和转换开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-generation-conversion-dev

#### 1.2.3.1 随机生成对称密钥(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-sym-key-randomly

#### 1.2.3.2 随机生成对称密钥(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-sym-key-randomly-ndk

#### 1.2.3.3 指定二进制数据转换对称密钥(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-convert-binary-data-to-sym-key

#### 1.2.3.4 指定二进制数据转换对称密钥(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-convert-binary-data-to-sym-key-ndk

#### 1.2.3.5 随机生成非对称密钥对(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-asym-key-pair-randomly

#### 1.2.3.6 随机生成非对称密钥对(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-asym-key-pair-randomly-ndk

#### 1.2.3.7 指定二进制数据转换非对称密钥对(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-convert-binary-data-to-asym-key-pair

#### 1.2.3.8 指定二进制数据转换非对称密钥对(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-convert-binary-data-to-asym-key-pair-ndk

#### 1.2.3.9 指定密钥参数生成非对称密钥对(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-asym-key-pair-from-key-spec

#### 1.2.3.10 指定密钥参数生成非对称密钥对(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-asym-key-pair-from-key-spec-ndk

#### 1.2.3.11 使用ECC压缩/非压缩公钥格式转换(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ypto-convert-compressed-or-uncompressed-ecc-pubkey

#### 1.2.3.12 使用ECC压缩/非压缩公钥格式转换(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/-convert-compressed-or-uncompressed-ecc-pubkey-ndk

#### 1.2.3.13 使用ECC压缩/非压缩点格式转换(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rypto-convert-compressed-or-uncompressed-ecc-point

#### 1.2.3.14 使用ECC压缩/非压缩点格式转换(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/o-convert-compressed-or-uncompressed-ecc-point-ndk

#### 1.2.3.15 指定PEM格式字符串数据转换非对称密钥对(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-convert-string-data-to-asym-key-pair

#### 1.2.3.16 指定PEM格式字符串数据转换非对称密钥对(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-convert-string-data-to-asym-key-pair-ndk

#### 1.2.3.17 使用RSA私钥进行编码解码(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-encoded-decoded

#### 1.2.3.18 使用RSA私钥进行编码解码(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-encoded-decoded-ndk

## 1.3 加解密:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-encryption-decryption

### 1.3.1 加解密介绍:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-encryption-decryption-overview

### 1.3.2 加解密算法规格:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-encrypt-decrypt-spec

#### 1.3.2.1 对称密钥加解密算法规格:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-encrypt-decrypt-spec

#### 1.3.2.2 非对称密钥加解密算法规格:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-encrypt-decrypt-spec

#### 1.3.2.3 分段加解密说明:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-encrypt-decrypt-by-segment

### 1.3.3 加解密开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-encrypt-decrypt-dev

#### 1.3.3.1 使用AES对称密钥（GCM模式）加解密(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm

#### 1.3.3.2 使用AES对称密钥（GCM模式）加解密(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm-ndk

#### 1.3.3.3 使用AES对称密钥（CCM模式）加解密(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-ccm

#### 1.3.3.4 使用AES对称密钥（CCM模式）加解密(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-ccm-ndk

#### 1.3.3.5 使用AES对称密钥（CBC模式）加解密(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-cbc

#### 1.3.3.6 使用AES对称密钥（CBC模式）加解密(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-cbc-ndk

#### 1.3.3.7 使用AES对称密钥（ECB模式）加解密(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-ecb

#### 1.3.3.8 使用AES对称密钥（ECB模式）加解密(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-ecb-ndk

#### 1.3.3.9 使用AES对称密钥（GCM模式）分段加解密(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm-by-segment

#### 1.3.3.10 使用AES对称密钥（GCM模式）分段加解密(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm-by-segment-ndk

#### 1.3.3.11 使用DES对称密钥（ECB模式）加解密(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-des-sym-encrypt-decrypt-ecb

#### 1.3.3.12 使用DES对称密钥（ECB模式）加解密(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-des-sym-encrypt-decrypt-ecb-ndk

#### 1.3.3.13 使用3DES对称密钥加解密(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-3des-sym-encrypt-decrypt-ecb

#### 1.3.3.14 使用3DES对称密钥加解密(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-3des-sym-encrypt-decrypt-ecb-ndk

#### 1.3.3.15 使用SM4对称密钥（ECB模式）加解密(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm4-sym-encrypt-decrypt-ecb

#### 1.3.3.16 使用SM4对称密钥（ECB模式）加解密(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm4-sym-encrypt-decrypt-ecb-ndk

#### 1.3.3.17 使用SM4对称密钥（CBC模式）加解密(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm4-sym-encrypt-decrypt-cbc

#### 1.3.3.18 使用SM4对称密钥（CBC模式）加解密(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm4-sym-encrypt-decrypt-cbc-ndk

#### 1.3.3.19 使用SM4对称密钥（GCM模式）加解密(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm4-sym-encrypt-decrypt-gcm

#### 1.3.3.20 使用SM4对称密钥（GCM模式）加解密(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm4-sym-encrypt-decrypt-gcm-ndk

#### 1.3.3.21 使用SM4对称密钥（GCM模式）分段加解密(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm4-sym-encrypt-decrypt-gcm-by-segment

#### 1.3.3.22 使用SM4对称密钥（GCM模式）分段加解密(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm4-sym-encrypt-decrypt-gcm-by-segment-ndk

#### 1.3.3.23 使用ChaCha20对称密钥加解密(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-chacha20-encrypt-decrypt

#### 1.3.3.24 使用ChaCha20对称密钥加解密(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-chacha20-encrypt-decrypt-ndk

#### 1.3.3.25 使用ChaCha20对称密钥（Poly1305模式）加解密(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-chacha20-encrypt-decrypt-poly1305

#### 1.3.3.26 使用ChaCha20对称密钥（Poly1305模式）加解密(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-chacha20-encrypt-decrypt-poly1305-ndk

#### 1.3.3.27 使用RSA非对称密钥（PKCS1模式）加解密(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-pkcs1

#### 1.3.3.28 使用RSA非对称密钥（PKCS1模式）加解密(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-pkcs1-ndk

#### 1.3.3.29 使用RSA非对称密钥分段加解密(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-by-segment

#### 1.3.3.30 使用RSA非对称密钥分段加解密(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-by-segment-ndk

#### 1.3.3.31 使用RSA非对称密钥（PKCS1_OAEP模式）加解密:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-pkcs1_oaep

#### 1.3.3.32 使用SM2非对称密钥加解密(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm2-asym-encrypt-decrypt

#### 1.3.3.33 使用SM2非对称密钥加解密(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm2-asym-encrypt-decrypt-ndk

#### 1.3.3.34 使用AES-WRAP算法对对称密钥加解密(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-wrap-encrypt-decrypt

#### 1.3.3.35 使用AES-WRAP算法对对称密钥加解密(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-wrap-encrypt-decrypt-ndk

#### 1.3.3.36 使用SM2密文格式转换(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm2-ciphertext-conversion

#### 1.3.3.37 使用SM2密文格式转换(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm2-ciphertext-conversion-ndk

## 1.4 签名验签:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sign-sig-verify

### 1.4.1 签名验签介绍及算法规格:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sign-sig-verify-overview

### 1.4.2 签名验签开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sign-sig-verify-dev

#### 1.4.2.1 使用RSA密钥对（PKCS1模式）签名验签(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1

#### 1.4.2.2 使用RSA密钥对签名验签 (PKCS1模式)(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1-ndk

#### 1.4.2.3 使用RSA密钥对（PKCS1模式）签名及签名恢复(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-recover-pkcs1

#### 1.4.2.4 使用RSA密钥对（PKCS1模式）签名恢复(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-recover-pkcs1-ndk

#### 1.4.2.5 使用RSA密钥对分段签名验签（PKCS1模式）(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1-by-segment

#### 1.4.2.6 使用RSA密钥对分段签名验签 (PKCS1模式)(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1-by-segment-ndk

#### 1.4.2.7 使用RSA密钥对签名验签（PSS模式）(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pss

#### 1.4.2.8 使用RSA密钥对签名验签 (PSS模式)(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pss-ndk

#### 1.4.2.9 使用ECDSA密钥对签名验签(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-ecdsa-sign-sig-verify

#### 1.4.2.10 使用ECDSA密钥对签名验签 (C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-ecdsa-sign-sig-verify-ndk

#### 1.4.2.11 使用SM2密钥对签名验签(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm2-sign-sig-verify-pkcs1

#### 1.4.2.12 使用SM2密钥对签名验签 (C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm2-sign-sig-verify-pkcs1-ndk

#### 1.4.2.13 SM2签名数据格式转换(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm2-sign-data-format-conversion

#### 1.4.2.14 SM2签名数据格式转换 (C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm2-sign-data-format-conversion-ndk

## 1.5 密钥协商:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement

### 1.5.1 密钥协商介绍及算法规格:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-overview

### 1.5.2 密钥协商开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-dev

#### 1.5.2.1 使用ECDH进行密钥协商(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-using-ecdh

#### 1.5.2.2 使用ECDH进行密钥协商(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-using-ecdh-ndk

#### 1.5.2.3 使用X25519进行密钥协商(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-using-x25519

#### 1.5.2.4 使用X25519进行密钥协商(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-using-x25519-ndk

#### 1.5.2.5 使用DH进行密钥协商(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-using-dh

#### 1.5.2.6 使用DH进行密钥协商(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-using-dh-ndk

## 1.6 消息摘要计算:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message

### 1.6.1 消息摘要计算介绍及算法规格:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest-overview

### 1.6.2 消息摘要计算开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest-dev

#### 1.6.2.1 消息摘要计算SHA256(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest

#### 1.6.2.2 消息摘要计算SHA256(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest-ndk

#### 1.6.2.3 消息摘要计算MD5(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest-md5

#### 1.6.2.4 消息摘要计算MD5(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest-md5-ndk

#### 1.6.2.5 消息摘要计算SHA3(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest-sha3

#### 1.6.2.6 消息摘要计算SHA3-256(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest-sha3-ndk

## 1.7 消息认证码:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-compute-mac

### 1.7.1 消息认证码计算介绍及算法规格:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-compute-mac-overview

### 1.7.2 消息认证码计算HMAC(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-compute-hmac

### 1.7.3 消息认证码计算HMAC(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-compute-hmac-ndk

### 1.7.4 消息认证码计算CMAC(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-compute-cmac

### 1.7.5 消息认证码计算CMAC(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-compute-cmac-ndk

## 1.8 随机数:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-compute-rand

### 1.8.1 安全随机数生成(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-random-number

### 1.8.2 安全随机数生成(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-random-number-ndk

### 1.8.3 使用硬件熵源生成安全随机数(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-random-number-hardware

### 1.8.4 使用硬件熵源生成安全随机数(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-random-number-hardware-ndk

## 1.9 密钥派生:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation

### 1.9.1 密钥派生介绍及算法规格:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-overview

### 1.9.2 使用PBKDF2进行密钥派生(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-pbkdf2

### 1.9.3 使用PBKDF2进行密钥派生(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-pbkdf2-ndk

### 1.9.4 使用HKDF进行密钥派生(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-hkdf

### 1.9.5 使用HKDF进行密钥派生(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-hkdf-ndk

### 1.9.6 使用SCRYPT进行密钥派生(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-scrypt

### 1.9.7 使用SCRYPT进行密钥派生(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-scrypt-ndk

### 1.9.8 使用X963KDF进行密钥派生(ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-x963kdf

### 1.9.9 使用X963KDF进行密钥派生(C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-x963kdf-ndk

## 1.10 跨平台数据兼容实践指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-development-practice

## 1.11 Crypto Architecture Kit常见问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-faqs

### 1.11.1 AES解密失败返回17630001:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-decryption-error-faq

---

# 2 Crypto Architecture Kit（加解密算法框架服务）API参考:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/crypto-architecture-api

## 2.1 ArkTS API:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/crypto-architecture-arkts

### 2.1.1 @ohos.security.cryptoFramework (加解密算法库框架):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework

### 2.1.2 已停止维护的接口:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/crypto-architecture-arkts-dep

#### 2.1.2.1 @system.cipher (加密算法):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-cipher

## 2.2 C API:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/crypto-architecture-c

### 2.2.1 模块:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/crypto-architecture-module

#### 2.2.1.1 CryptoArchitectureKit:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoarchitecturekit

#### 2.2.1.2 CryptoAsymCipherApi:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymcipherapi

#### 2.2.1.3 CryptoAsymKeyApi:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi

#### 2.2.1.4 CryptoCommonApi:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi

#### 2.2.1.5 CryptoDigestApi:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptodigestapi

#### 2.2.1.6 CryptoKdfApi:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptokdfapi

#### 2.2.1.7 CryptoKeyAgreementApi:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptokeyagreementapi

#### 2.2.1.8 CryptoMacApi:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptomacapi

#### 2.2.1.9 CryptoRandApi:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptorandapi

#### 2.2.1.10 CryptoSignatureApi:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosignatureapi

#### 2.2.1.11 CryptoSymCipherApi:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosymcipherapi

#### 2.2.1.12 CryptoSymKeyApi:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosymkeyapi

### 2.2.2 头文件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/crypto-architecture-headerfile

#### 2.2.2.1 crypto_architecture_kit.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-architecture-kit-h

#### 2.2.2.2 crypto_asym_cipher.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h

#### 2.2.2.3 crypto_asym_key.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h

#### 2.2.2.4 crypto_common.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h

#### 2.2.2.5 crypto_digest.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-digest-h

#### 2.2.2.6 crypto_kdf.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-kdf-h

#### 2.2.2.7 crypto_key_agreement.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-key-agreement-h

#### 2.2.2.8 crypto_mac.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-mac-h

#### 2.2.2.9 crypto_rand.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-rand-h

#### 2.2.2.10 crypto_signature.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-signature-h

#### 2.2.2.11 crypto_sym_cipher.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h

#### 2.2.2.12 crypto_sym_key.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h

### 2.2.3 结构体:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/crypto-architecture-struct

#### 2.2.3.1 Crypto_DataBlob:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi-crypto-datablob

#### 2.2.3.2 OH_CryptoAsymCipher:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymcipherapi-oh-cryptoasymcipher

#### 2.2.3.3 OH_CryptoSm2CiphertextSpec:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-cryptoasymcipherapi-oh-cryptosm2ciphertextspec

#### 2.2.3.4 OH_CryptoKeyPair:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi-oh-cryptokeypair

#### 2.2.3.5 OH_CryptoPubKey:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi-oh-cryptopubkey

#### 2.2.3.6 OH_CryptoPrivKey:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi-oh-cryptoprivkey

#### 2.2.3.7 OH_CryptoAsymKeyGenerator:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi-oh-cryptoasymkeygenerator

#### 2.2.3.8 OH_CryptoPrivKeyEncodingParams:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-cryptoasymkeyapi-oh-cryptoprivkeyencodingparams

#### 2.2.3.9 OH_CryptoAsymKeySpec:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi-oh-cryptoasymkeyspec

#### 2.2.3.10 OH_CryptoAsymKeyGeneratorWithSpec:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cryptoasymkeyapi-oh-cryptoasymkeygeneratorwithspec

#### 2.2.3.11 OH_CryptoEcPoint:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi-oh-cryptoecpoint

#### 2.2.3.12 OH_CryptoDigest:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptodigestapi-oh-cryptodigest

#### 2.2.3.13 OH_CryptoKdf:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptokdfapi-oh-cryptokdf

#### 2.2.3.14 OH_CryptoKdfParams:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptokdfapi-oh-cryptokdfparams

#### 2.2.3.15 OH_CryptoKeyAgreement:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptokeyagreementapi-oh-cryptokeyagreement

#### 2.2.3.16 OH_CryptoMac:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptomacapi-oh-cryptomac

#### 2.2.3.17 OH_CryptoRand:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptorandapi-oh-cryptorand

#### 2.2.3.18 OH_CryptoVerify:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosignatureapi-oh-cryptoverify

#### 2.2.3.19 OH_CryptoSign:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosignatureapi-oh-cryptosign

#### 2.2.3.20 OH_CryptoEccSignatureSpec:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosignatureapi-oh-cryptoeccsignaturespec

#### 2.2.3.21 OH_CryptoSymCipher:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosymcipherapi-oh-cryptosymcipher

#### 2.2.3.22 OH_CryptoSymCipherParams:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosymcipherapi-oh-cryptosymcipherparams

#### 2.2.3.23 OH_CryptoSymKey:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosymkeyapi-oh-cryptosymkey

#### 2.2.3.24 OH_CryptoSymKeyGenerator:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosymkeyapi-oh-cryptosymkeygenerator

## 2.3 错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/crypto-architecture-arkts-errcode

### 2.3.1 crypto framework错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-crypto-framework


---

# 3 Crypto Architecture Kit（加解密算法框架服务）最佳实践：https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-cross-platform-compatibility

---

# 4 Crypto Architecture Kit（加解密算法框架服务）FAQ：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-kit


## 4.1 ECC算法是否支持secp256r1:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-5


## 4.2 如何使用AES算法加密:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs-V5/faqs-crypto-architecture-15-V5


## 4.3 在进行aes加密的时候，如何把字符串转换成Key对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-28


## 4.4 如何使用SM3算法生成散列值:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-29

