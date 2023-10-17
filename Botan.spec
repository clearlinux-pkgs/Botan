#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v2
# autospec commit: f032afc
#
# Source0 file verified with key 0x6211EBF1EFBADFBC (jack@randombit.net)
#
Name     : Botan
Version  : 2.19.1
Release  : 36
URL      : https://botan.randombit.net/releases/Botan-2.19.1.tar.xz
Source0  : https://botan.randombit.net/releases/Botan-2.19.1.tar.xz
Source1  : https://botan.randombit.net/releases/Botan-2.19.1.tar.xz.asc
Summary  : Crypto and TLS for C++11
Group    : Development/Tools
License  : BSD-2-Clause
Requires: Botan-bin = %{version}-%{release}
Requires: Botan-lib = %{version}-%{release}
Requires: Botan-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : bzip2-dev
BuildRequires : openssl-dev
BuildRequires : xz-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Add-more-autoconf-compatibility-options.patch
Patch2: 0002-Enable-genentropy-3-on-Linux.patch

%description
Botan: Crypto and TLS for Modern C++
========================================
Botan (Japanese for peony flower) is a C++ cryptography library released under the
permissive `Simplified BSD <https://botan.randombit.net/license.txt>`_ license.

%package bin
Summary: bin components for the Botan package.
Group: Binaries
Requires: Botan-license = %{version}-%{release}

%description bin
bin components for the Botan package.


%package dev
Summary: dev components for the Botan package.
Group: Development
Requires: Botan-lib = %{version}-%{release}
Requires: Botan-bin = %{version}-%{release}
Provides: Botan-devel = %{version}-%{release}
Requires: Botan = %{version}-%{release}

%description dev
dev components for the Botan package.


%package doc
Summary: doc components for the Botan package.
Group: Documentation

%description doc
doc components for the Botan package.


%package lib
Summary: lib components for the Botan package.
Group: Libraries
Requires: Botan-license = %{version}-%{release}

%description lib
lib components for the Botan package.


%package license
Summary: license components for the Botan package.
Group: Default

%description license
license components for the Botan package.


%prep
%setup -q -n Botan-2.19.1
cd %{_builddir}/Botan-2.19.1
%patch -P 1 -p1
%patch -P 2 -p1

%build
## build_prepend content
ln -s configure.py configure
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697569752
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%configure --disable-static --enable-modules=bzip2,zlib,openssl,lzma \
--with-debug-info \
--disable-modules=camellia,`sed -n '1,/<prohibited>/d;/<\/prohibited>/{x;s/\n/,/gp};s/#.*//;/^$/d;H' src/build-data/policy/modern.txt`
make  %{?_smp_mflags}

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1697569752
rm -rf %{buildroot}
## install_prepend content
sed -i 's/env python/env python3/' src/scripts/install.py
## install_prepend end
mkdir -p %{buildroot}/usr/share/package-licenses/Botan
cp %{_builddir}/Botan-%{version}/license.txt %{buildroot}/usr/share/package-licenses/Botan/7efe3a290c99654892b03dd4fc15cd5ebac6b788 || :
%make_install
## install_append content
sed -e '1{/^#!/d}' -i %{buildroot}/usr/lib64/python*/site-packages/botan2.py
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/python3.12/site-packages/botan2.py

%files bin
%defattr(-,root,root,-)
/usr/bin/botan

%files dev
%defattr(-,root,root,-)
/usr/include/botan-2/botan/adler32.h
/usr/include/botan-2/botan/aead.h
/usr/include/botan-2/botan/aes.h
/usr/include/botan-2/botan/alg_id.h
/usr/include/botan-2/botan/argon2.h
/usr/include/botan-2/botan/aria.h
/usr/include/botan-2/botan/asn1_alt_name.h
/usr/include/botan-2/botan/asn1_attribute.h
/usr/include/botan-2/botan/asn1_obj.h
/usr/include/botan-2/botan/asn1_oid.h
/usr/include/botan-2/botan/asn1_print.h
/usr/include/botan-2/botan/asn1_str.h
/usr/include/botan-2/botan/asn1_time.h
/usr/include/botan-2/botan/assert.h
/usr/include/botan-2/botan/auto_rng.h
/usr/include/botan-2/botan/b64_filt.h
/usr/include/botan-2/botan/base32.h
/usr/include/botan-2/botan/base58.h
/usr/include/botan-2/botan/base64.h
/usr/include/botan-2/botan/basefilt.h
/usr/include/botan-2/botan/bcrypt.h
/usr/include/botan-2/botan/bcrypt_pbkdf.h
/usr/include/botan-2/botan/ber_dec.h
/usr/include/botan-2/botan/bigint.h
/usr/include/botan-2/botan/blake2b.h
/usr/include/botan-2/botan/blinding.h
/usr/include/botan-2/botan/block_cipher.h
/usr/include/botan-2/botan/blowfish.h
/usr/include/botan-2/botan/botan.h
/usr/include/botan-2/botan/bswap.h
/usr/include/botan-2/botan/buf_comp.h
/usr/include/botan-2/botan/buf_filt.h
/usr/include/botan-2/botan/build.h
/usr/include/botan-2/botan/bzip2.h
/usr/include/botan-2/botan/calendar.h
/usr/include/botan-2/botan/cascade.h
/usr/include/botan-2/botan/cbc.h
/usr/include/botan-2/botan/ccm.h
/usr/include/botan-2/botan/cecpq1.h
/usr/include/botan-2/botan/cert_status.h
/usr/include/botan-2/botan/certstor.h
/usr/include/botan-2/botan/certstor_flatfile.h
/usr/include/botan-2/botan/certstor_sql.h
/usr/include/botan-2/botan/certstor_system.h
/usr/include/botan-2/botan/chacha.h
/usr/include/botan-2/botan/chacha20poly1305.h
/usr/include/botan-2/botan/chacha_rng.h
/usr/include/botan-2/botan/charset.h
/usr/include/botan-2/botan/cipher_filter.h
/usr/include/botan-2/botan/cipher_mode.h
/usr/include/botan-2/botan/cmac.h
/usr/include/botan-2/botan/comb4p.h
/usr/include/botan-2/botan/comp_filter.h
/usr/include/botan-2/botan/compiler.h
/usr/include/botan-2/botan/compression.h
/usr/include/botan-2/botan/cpuid.h
/usr/include/botan-2/botan/crc24.h
/usr/include/botan-2/botan/crc32.h
/usr/include/botan-2/botan/credentials_manager.h
/usr/include/botan-2/botan/crl_ent.h
/usr/include/botan-2/botan/ctr.h
/usr/include/botan-2/botan/curve25519.h
/usr/include/botan-2/botan/curve_gfp.h
/usr/include/botan-2/botan/curve_nistp.h
/usr/include/botan-2/botan/data_snk.h
/usr/include/botan-2/botan/data_src.h
/usr/include/botan-2/botan/database.h
/usr/include/botan-2/botan/datastor.h
/usr/include/botan-2/botan/der_enc.h
/usr/include/botan-2/botan/dh.h
/usr/include/botan-2/botan/divide.h
/usr/include/botan-2/botan/dl_algo.h
/usr/include/botan-2/botan/dl_group.h
/usr/include/botan-2/botan/dlies.h
/usr/include/botan-2/botan/dsa.h
/usr/include/botan-2/botan/dyn_load.h
/usr/include/botan-2/botan/eax.h
/usr/include/botan-2/botan/ec_group.h
/usr/include/botan-2/botan/ecc_key.h
/usr/include/botan-2/botan/ecdh.h
/usr/include/botan-2/botan/ecdsa.h
/usr/include/botan-2/botan/ecgdsa.h
/usr/include/botan-2/botan/ecies.h
/usr/include/botan-2/botan/eckcdsa.h
/usr/include/botan-2/botan/ed25519.h
/usr/include/botan-2/botan/eme.h
/usr/include/botan-2/botan/eme_pkcs.h
/usr/include/botan-2/botan/eme_raw.h
/usr/include/botan-2/botan/emsa.h
/usr/include/botan-2/botan/emsa1.h
/usr/include/botan-2/botan/emsa_pkcs1.h
/usr/include/botan-2/botan/emsa_raw.h
/usr/include/botan-2/botan/entropy_src.h
/usr/include/botan-2/botan/exceptn.h
/usr/include/botan-2/botan/fd_unix.h
/usr/include/botan-2/botan/ffi.h
/usr/include/botan-2/botan/filter.h
/usr/include/botan-2/botan/filters.h
/usr/include/botan-2/botan/fpe_fe1.h
/usr/include/botan-2/botan/gcm.h
/usr/include/botan-2/botan/gf2m_small_m.h
/usr/include/botan-2/botan/ghash.h
/usr/include/botan-2/botan/gmac.h
/usr/include/botan-2/botan/hash.h
/usr/include/botan-2/botan/hash_id.h
/usr/include/botan-2/botan/hex.h
/usr/include/botan-2/botan/hex_filt.h
/usr/include/botan-2/botan/hkdf.h
/usr/include/botan-2/botan/hmac.h
/usr/include/botan-2/botan/hmac_drbg.h
/usr/include/botan-2/botan/hotp.h
/usr/include/botan-2/botan/http_util.h
/usr/include/botan-2/botan/init.h
/usr/include/botan-2/botan/iso9796.h
/usr/include/botan-2/botan/kdf.h
/usr/include/botan-2/botan/kdf1.h
/usr/include/botan-2/botan/kdf1_iso18033.h
/usr/include/botan-2/botan/kdf2.h
/usr/include/botan-2/botan/keccak.h
/usr/include/botan-2/botan/key_constraint.h
/usr/include/botan-2/botan/key_filt.h
/usr/include/botan-2/botan/key_spec.h
/usr/include/botan-2/botan/keypair.h
/usr/include/botan-2/botan/loadstor.h
/usr/include/botan-2/botan/locking_allocator.h
/usr/include/botan-2/botan/lookup.h
/usr/include/botan-2/botan/lzma.h
/usr/include/botan-2/botan/mac.h
/usr/include/botan-2/botan/mceies.h
/usr/include/botan-2/botan/mceliece.h
/usr/include/botan-2/botan/md5.h
/usr/include/botan-2/botan/mdx_hash.h
/usr/include/botan-2/botan/mem_ops.h
/usr/include/botan-2/botan/mgf1.h
/usr/include/botan-2/botan/mode_pad.h
/usr/include/botan-2/botan/monty.h
/usr/include/botan-2/botan/mul128.h
/usr/include/botan-2/botan/mutex.h
/usr/include/botan-2/botan/name_constraint.h
/usr/include/botan-2/botan/newhope.h
/usr/include/botan-2/botan/nist_keywrap.h
/usr/include/botan-2/botan/noekeon.h
/usr/include/botan-2/botan/numthry.h
/usr/include/botan-2/botan/oaep.h
/usr/include/botan-2/botan/ocb.h
/usr/include/botan-2/botan/ocsp.h
/usr/include/botan-2/botan/ocsp_types.h
/usr/include/botan-2/botan/oids.h
/usr/include/botan-2/botan/otp.h
/usr/include/botan-2/botan/p11.h
/usr/include/botan-2/botan/p11_ecc_key.h
/usr/include/botan-2/botan/p11_ecdh.h
/usr/include/botan-2/botan/p11_ecdsa.h
/usr/include/botan-2/botan/p11_module.h
/usr/include/botan-2/botan/p11_object.h
/usr/include/botan-2/botan/p11_randomgenerator.h
/usr/include/botan-2/botan/p11_rsa.h
/usr/include/botan-2/botan/p11_session.h
/usr/include/botan-2/botan/p11_slot.h
/usr/include/botan-2/botan/p11_types.h
/usr/include/botan-2/botan/p11_x509.h
/usr/include/botan-2/botan/package.h
/usr/include/botan-2/botan/par_hash.h
/usr/include/botan-2/botan/parsing.h
/usr/include/botan-2/botan/pbes2.h
/usr/include/botan-2/botan/pbkdf.h
/usr/include/botan-2/botan/pbkdf2.h
/usr/include/botan-2/botan/pem.h
/usr/include/botan-2/botan/pgp_s2k.h
/usr/include/botan-2/botan/pipe.h
/usr/include/botan-2/botan/pk_algs.h
/usr/include/botan-2/botan/pk_keys.h
/usr/include/botan-2/botan/pk_ops.h
/usr/include/botan-2/botan/pk_ops_fwd.h
/usr/include/botan-2/botan/pkcs10.h
/usr/include/botan-2/botan/pkcs11.h
/usr/include/botan-2/botan/pkcs11f.h
/usr/include/botan-2/botan/pkcs11t.h
/usr/include/botan-2/botan/pkcs8.h
/usr/include/botan-2/botan/pkix_enums.h
/usr/include/botan-2/botan/pkix_types.h
/usr/include/botan-2/botan/point_gfp.h
/usr/include/botan-2/botan/poly1305.h
/usr/include/botan-2/botan/polyn_gf2m.h
/usr/include/botan-2/botan/pow_mod.h
/usr/include/botan-2/botan/prf_tls.h
/usr/include/botan-2/botan/processor_rng.h
/usr/include/botan-2/botan/psk_db.h
/usr/include/botan-2/botan/psk_db_sql.h
/usr/include/botan-2/botan/pssr.h
/usr/include/botan-2/botan/pubkey.h
/usr/include/botan-2/botan/pwdhash.h
/usr/include/botan-2/botan/rdrand_rng.h
/usr/include/botan-2/botan/reducer.h
/usr/include/botan-2/botan/rfc3394.h
/usr/include/botan-2/botan/rfc6979.h
/usr/include/botan-2/botan/rmd160.h
/usr/include/botan-2/botan/rng.h
/usr/include/botan-2/botan/rotate.h
/usr/include/botan-2/botan/roughtime.h
/usr/include/botan-2/botan/rsa.h
/usr/include/botan-2/botan/salsa20.h
/usr/include/botan-2/botan/scan_name.h
/usr/include/botan-2/botan/scrypt.h
/usr/include/botan-2/botan/secmem.h
/usr/include/botan-2/botan/secqueue.h
/usr/include/botan-2/botan/serpent.h
/usr/include/botan-2/botan/sha160.h
/usr/include/botan-2/botan/sha2_32.h
/usr/include/botan-2/botan/sha2_64.h
/usr/include/botan-2/botan/sha3.h
/usr/include/botan-2/botan/shacal2.h
/usr/include/botan-2/botan/shake.h
/usr/include/botan-2/botan/shake_cipher.h
/usr/include/botan-2/botan/siphash.h
/usr/include/botan-2/botan/siv.h
/usr/include/botan-2/botan/skein_512.h
/usr/include/botan-2/botan/sm2.h
/usr/include/botan-2/botan/sm2_enc.h
/usr/include/botan-2/botan/sm3.h
/usr/include/botan-2/botan/sm4.h
/usr/include/botan-2/botan/sodium.h
/usr/include/botan-2/botan/sp800_108.h
/usr/include/botan-2/botan/sp800_56a.h
/usr/include/botan-2/botan/sp800_56c.h
/usr/include/botan-2/botan/srp6.h
/usr/include/botan-2/botan/stateful_rng.h
/usr/include/botan-2/botan/stl_compatibility.h
/usr/include/botan-2/botan/stream_cipher.h
/usr/include/botan-2/botan/stream_mode.h
/usr/include/botan-2/botan/streebog.h
/usr/include/botan-2/botan/sym_algo.h
/usr/include/botan-2/botan/symkey.h
/usr/include/botan-2/botan/system_rng.h
/usr/include/botan-2/botan/threefish.h
/usr/include/botan-2/botan/threefish_512.h
/usr/include/botan-2/botan/tiger.h
/usr/include/botan-2/botan/tls_alert.h
/usr/include/botan-2/botan/tls_algos.h
/usr/include/botan-2/botan/tls_blocking.h
/usr/include/botan-2/botan/tls_callbacks.h
/usr/include/botan-2/botan/tls_channel.h
/usr/include/botan-2/botan/tls_ciphersuite.h
/usr/include/botan-2/botan/tls_client.h
/usr/include/botan-2/botan/tls_exceptn.h
/usr/include/botan-2/botan/tls_extensions.h
/usr/include/botan-2/botan/tls_handshake_msg.h
/usr/include/botan-2/botan/tls_magic.h
/usr/include/botan-2/botan/tls_messages.h
/usr/include/botan-2/botan/tls_policy.h
/usr/include/botan-2/botan/tls_server.h
/usr/include/botan-2/botan/tls_server_info.h
/usr/include/botan-2/botan/tls_session.h
/usr/include/botan-2/botan/tls_session_manager.h
/usr/include/botan-2/botan/tls_session_manager_sql.h
/usr/include/botan-2/botan/tls_version.h
/usr/include/botan-2/botan/totp.h
/usr/include/botan-2/botan/tss.h
/usr/include/botan-2/botan/twofish.h
/usr/include/botan-2/botan/types.h
/usr/include/botan-2/botan/uuid.h
/usr/include/botan-2/botan/version.h
/usr/include/botan-2/botan/whrlpool.h
/usr/include/botan-2/botan/workfactor.h
/usr/include/botan-2/botan/x509_ca.h
/usr/include/botan-2/botan/x509_crl.h
/usr/include/botan-2/botan/x509_dn.h
/usr/include/botan-2/botan/x509_ext.h
/usr/include/botan-2/botan/x509_key.h
/usr/include/botan-2/botan/x509_obj.h
/usr/include/botan-2/botan/x509cert.h
/usr/include/botan-2/botan/x509path.h
/usr/include/botan-2/botan/x509self.h
/usr/include/botan-2/botan/xmss.h
/usr/include/botan-2/botan/xmss_hash.h
/usr/include/botan-2/botan/xmss_key_pair.h
/usr/include/botan-2/botan/xmss_parameters.h
/usr/include/botan-2/botan/xmss_privatekey.h
/usr/include/botan-2/botan/xmss_publickey.h
/usr/include/botan-2/botan/xmss_wots.h
/usr/include/botan-2/botan/xmss_wots_parameters.h
/usr/include/botan-2/botan/xmss_wots_privatekey.h
/usr/include/botan-2/botan/xmss_wots_publickey.h
/usr/include/botan-2/botan/xts.h
/usr/include/botan-2/botan/zfec.h
/usr/include/botan-2/botan/zlib.h
/usr/lib64/libbotan-2.so
/usr/lib64/pkgconfig/botan-2.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/botan-2.19.1/authors.txt
/usr/share/doc/botan-2.19.1/handbook/abi.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/bigint.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/block_cipher.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/cipher_modes.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/compression.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/contents.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/credentials_manager.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/cryptobox.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/ecc.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/env_vars.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/ffi.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/filters.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/fpe.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/hash.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/kdf.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/keywrap.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/message_auth_codes.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/otp.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/passhash.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/pbkdf.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/pkcs11.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/psk_db.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/pubkey.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/python.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/rng.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/roughtime.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/secmem.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/srp.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/stream_ciphers.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/tls.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/tpm.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/tss.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/versions.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/x509.rst
/usr/share/doc/botan-2.19.1/handbook/api_ref/zfec.rst
/usr/share/doc/botan-2.19.1/handbook/authors.txt
/usr/share/doc/botan-2.19.1/handbook/building.rst
/usr/share/doc/botan-2.19.1/handbook/cli.rst
/usr/share/doc/botan-2.19.1/handbook/contents.rst
/usr/share/doc/botan-2.19.1/handbook/credits.rst
/usr/share/doc/botan-2.19.1/handbook/deprecated.rst
/usr/share/doc/botan-2.19.1/handbook/dev_ref/configure.rst
/usr/share/doc/botan-2.19.1/handbook/dev_ref/contents.rst
/usr/share/doc/botan-2.19.1/handbook/dev_ref/continuous_integration.rst
/usr/share/doc/botan-2.19.1/handbook/dev_ref/contributing.rst
/usr/share/doc/botan-2.19.1/handbook/dev_ref/fuzzing.rst
/usr/share/doc/botan-2.19.1/handbook/dev_ref/mistakes.rst
/usr/share/doc/botan-2.19.1/handbook/dev_ref/oids.rst
/usr/share/doc/botan-2.19.1/handbook/dev_ref/os.rst
/usr/share/doc/botan-2.19.1/handbook/dev_ref/reading_list.rst
/usr/share/doc/botan-2.19.1/handbook/dev_ref/release_process.rst
/usr/share/doc/botan-2.19.1/handbook/dev_ref/test_framework.rst
/usr/share/doc/botan-2.19.1/handbook/dev_ref/todo.rst
/usr/share/doc/botan-2.19.1/handbook/goals.rst
/usr/share/doc/botan-2.19.1/handbook/index.rst
/usr/share/doc/botan-2.19.1/handbook/old_news.rst
/usr/share/doc/botan-2.19.1/handbook/packaging.rst
/usr/share/doc/botan-2.19.1/handbook/pgpkey.txt
/usr/share/doc/botan-2.19.1/handbook/roadmap.rst
/usr/share/doc/botan-2.19.1/handbook/security.rst
/usr/share/doc/botan-2.19.1/handbook/side_channels.rst
/usr/share/doc/botan-2.19.1/handbook/support.rst
/usr/share/doc/botan-2.19.1/license.txt
/usr/share/doc/botan-2.19.1/news.txt
/usr/share/doc/botan-2.19.1/pgpkey.txt

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbotan-2.so.19
/usr/lib64/libbotan-2.so.19.19.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Botan/7efe3a290c99654892b03dd4fc15cd5ebac6b788
