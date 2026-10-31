---
name: HashAlgorithm
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "A Cryptographic hash function to use in EncodingService methods."
---

# HashAlgorithm

A Cryptographic hash function to use in [EncodingService](/docs/reference/engine/classes/EncodingService.md) methods.

**Type:** enum

## Description

A
[Cryptographic hash function](https://en.wikipedia.org/wiki/Cryptographic_hash_function)
to use in [EncodingService](/docs/reference/engine/classes/EncodingService.md) methods.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Blake2b` | 0 | Used to compute a 256-bit (32-byte) hash digest using the [BLAKE2b](https://en.wikipedia.org/wiki/BLAKE2) algorithm. |
| `Blake3` | 1 | Used to compute a 256-bit (32-byte) hash digest using the [BLAKE3](https://en.wikipedia.org/wiki/BLAKE3) algorithm. |
| `Md5` | 2 | Used to compute a 128-bit (16-byte) hash digest using the [MD5](https://en.wikipedia.org/wiki/MD5) algorithm. |
| `Sha1` | 3 | Used to compute a 160-bit (20-byte) hash digest using the [SHA-1](https://en.wikipedia.org/wiki/SHA-1) algorithm. |
| `Sha256` | 4 | Used to compute a 256-bit (32-byte) hash digest using the [SHA256](https://en.wikipedia.org/wiki/SHA-2) algorithm. |