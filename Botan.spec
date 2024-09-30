#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v20
# autospec commit: f35655a
#
# Source0 file verified with key 0x6211EBF1EFBADFBC (jack@randombit.net)
#
Name     : Botan
Version  : 3.5.0
Release  : 52
URL      : https://botan.randombit.net/releases/Botan-3.5.0.tar.xz
Source0  : https://botan.randombit.net/releases/Botan-3.5.0.tar.xz
Source1  : https://botan.randombit.net/releases/Botan-3.5.0.tar.xz.asc
Source2  : 6211EBF1EFBADFBC.pkey
Summary  : Crypto and TLS for Modern C++
Group    : Development/Tools
License  : BSD-2-Clause
Requires: Botan-bin = %{version}-%{release}
Requires: Botan-lib = %{version}-%{release}
Requires: Botan-license = %{version}-%{release}
Requires: Botan-python = %{version}-%{release}
Requires: Botan-python3 = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : bzip2-dev
BuildRequires : gnupg
BuildRequires : openssl-dev
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


%package python
Summary: python components for the Botan package.
Group: Default
Requires: Botan-python3 = %{version}-%{release}
Provides: botan-python

%description python
python components for the Botan package.


%package python3
Summary: python3 components for the Botan package.
Group: Default
Requires: python3-core

%description python3
python3 components for the Botan package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 6211EBF1EFBADFBC' gpg.status
%setup -q -n Botan-3.5.0
cd %{_builddir}/Botan-3.5.0
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
export SOURCE_DATE_EPOCH=1727720137
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
export GOAMD64=v2
%configure --disable-static --enable-modules=bzip2,zlib \
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
export SOURCE_DATE_EPOCH=1727720137
rm -rf %{buildroot}
## install_prepend content
sed -i 's/env python/env python3/' src/scripts/install.py
## install_prepend end
mkdir -p %{buildroot}/usr/share/package-licenses/Botan
cp %{_builddir}/Botan-%{version}/license.txt %{buildroot}/usr/share/package-licenses/Botan/62940cf2327ab98c3edbb00eaf5e38dc5e78ccc2 || :
export GOAMD64=v2
GOAMD64=v2
%make_install
## install_append content
mkdir -p %{buildroot}/usr/lib
mv %{buildroot}/usr/lib64/python* %{buildroot}/usr/lib
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/botan

%files dev
%defattr(-,root,root,-)
/usr/include/botan-3/botan/aead.h
/usr/include/botan-3/botan/allocator.h
/usr/include/botan-3/botan/argon2.h
/usr/include/botan-3/botan/argon2fmt.h
/usr/include/botan-3/botan/asn1_obj.h
/usr/include/botan-3/botan/asn1_print.h
/usr/include/botan-3/botan/assert.h
/usr/include/botan-3/botan/auto_rng.h
/usr/include/botan-3/botan/base32.h
/usr/include/botan-3/botan/base58.h
/usr/include/botan-3/botan/base64.h
/usr/include/botan-3/botan/bcrypt.h
/usr/include/botan-3/botan/bcrypt_pbkdf.h
/usr/include/botan-3/botan/ber_dec.h
/usr/include/botan-3/botan/bigint.h
/usr/include/botan-3/botan/block_cipher.h
/usr/include/botan-3/botan/buf_comp.h
/usr/include/botan-3/botan/build.h
/usr/include/botan-3/botan/bzip2.h
/usr/include/botan-3/botan/certstor.h
/usr/include/botan-3/botan/certstor_flatfile.h
/usr/include/botan-3/botan/certstor_sql.h
/usr/include/botan-3/botan/certstor_system.h
/usr/include/botan-3/botan/chacha_rng.h
/usr/include/botan-3/botan/cipher_mode.h
/usr/include/botan-3/botan/compiler.h
/usr/include/botan-3/botan/compression.h
/usr/include/botan-3/botan/concepts.h
/usr/include/botan-3/botan/credentials_manager.h
/usr/include/botan-3/botan/curve25519.h
/usr/include/botan-3/botan/curve_gfp.h
/usr/include/botan-3/botan/data_snk.h
/usr/include/botan-3/botan/data_src.h
/usr/include/botan-3/botan/database.h
/usr/include/botan-3/botan/der_enc.h
/usr/include/botan-3/botan/dh.h
/usr/include/botan-3/botan/dilithium.h
/usr/include/botan-3/botan/dl_group.h
/usr/include/botan-3/botan/dlies.h
/usr/include/botan-3/botan/dsa.h
/usr/include/botan-3/botan/ec_group.h
/usr/include/botan-3/botan/ec_point.h
/usr/include/botan-3/botan/ecc_key.h
/usr/include/botan-3/botan/ecdh.h
/usr/include/botan-3/botan/ecdsa.h
/usr/include/botan-3/botan/ecgdsa.h
/usr/include/botan-3/botan/ecies.h
/usr/include/botan-3/botan/eckcdsa.h
/usr/include/botan-3/botan/ed25519.h
/usr/include/botan-3/botan/ed448.h
/usr/include/botan-3/botan/entropy_src.h
/usr/include/botan-3/botan/exceptn.h
/usr/include/botan-3/botan/fd_unix.h
/usr/include/botan-3/botan/ffi.h
/usr/include/botan-3/botan/filter.h
/usr/include/botan-3/botan/filters.h
/usr/include/botan-3/botan/fpe_fe1.h
/usr/include/botan-3/botan/frodo_mode.h
/usr/include/botan-3/botan/frodokem.h
/usr/include/botan-3/botan/hash.h
/usr/include/botan-3/botan/hex.h
/usr/include/botan-3/botan/hmac_drbg.h
/usr/include/botan-3/botan/hss_lms.h
/usr/include/botan-3/botan/kdf.h
/usr/include/botan-3/botan/kyber.h
/usr/include/botan-3/botan/mac.h
/usr/include/botan-3/botan/mceliece.h
/usr/include/botan-3/botan/mem_ops.h
/usr/include/botan-3/botan/mutex.h
/usr/include/botan-3/botan/nist_keywrap.h
/usr/include/botan-3/botan/numthry.h
/usr/include/botan-3/botan/ocsp.h
/usr/include/botan-3/botan/oids.h
/usr/include/botan-3/botan/otp.h
/usr/include/botan-3/botan/p11.h
/usr/include/botan-3/botan/p11_ecc_key.h
/usr/include/botan-3/botan/p11_ecdh.h
/usr/include/botan-3/botan/p11_ecdsa.h
/usr/include/botan-3/botan/p11_object.h
/usr/include/botan-3/botan/p11_randomgenerator.h
/usr/include/botan-3/botan/p11_rsa.h
/usr/include/botan-3/botan/p11_types.h
/usr/include/botan-3/botan/p11_x509.h
/usr/include/botan-3/botan/pbkdf.h
/usr/include/botan-3/botan/pbkdf2.h
/usr/include/botan-3/botan/pem.h
/usr/include/botan-3/botan/pgp_s2k.h
/usr/include/botan-3/botan/pipe.h
/usr/include/botan-3/botan/pk_algs.h
/usr/include/botan-3/botan/pk_keys.h
/usr/include/botan-3/botan/pk_ops.h
/usr/include/botan-3/botan/pk_ops_fwd.h
/usr/include/botan-3/botan/pkcs10.h
/usr/include/botan-3/botan/pkcs11.h
/usr/include/botan-3/botan/pkcs11f.h
/usr/include/botan-3/botan/pkcs11t.h
/usr/include/botan-3/botan/pkcs8.h
/usr/include/botan-3/botan/pkix_enums.h
/usr/include/botan-3/botan/pkix_types.h
/usr/include/botan-3/botan/processor_rng.h
/usr/include/botan-3/botan/psk_db.h
/usr/include/botan-3/botan/pubkey.h
/usr/include/botan-3/botan/pwdhash.h
/usr/include/botan-3/botan/reducer.h
/usr/include/botan-3/botan/rfc3394.h
/usr/include/botan-3/botan/rfc4880.h
/usr/include/botan-3/botan/rng.h
/usr/include/botan-3/botan/roughtime.h
/usr/include/botan-3/botan/rsa.h
/usr/include/botan-3/botan/scrypt.h
/usr/include/botan-3/botan/secmem.h
/usr/include/botan-3/botan/sm2.h
/usr/include/botan-3/botan/sodium.h
/usr/include/botan-3/botan/sp_parameters.h
/usr/include/botan-3/botan/sphincsplus.h
/usr/include/botan-3/botan/srp6.h
/usr/include/botan-3/botan/stateful_rng.h
/usr/include/botan-3/botan/stream_cipher.h
/usr/include/botan-3/botan/strong_type.h
/usr/include/botan-3/botan/sym_algo.h
/usr/include/botan-3/botan/symkey.h
/usr/include/botan-3/botan/system_rng.h
/usr/include/botan-3/botan/tls.h
/usr/include/botan-3/botan/tls_alert.h
/usr/include/botan-3/botan/tls_algos.h
/usr/include/botan-3/botan/tls_callbacks.h
/usr/include/botan-3/botan/tls_channel.h
/usr/include/botan-3/botan/tls_ciphersuite.h
/usr/include/botan-3/botan/tls_client.h
/usr/include/botan-3/botan/tls_exceptn.h
/usr/include/botan-3/botan/tls_extensions.h
/usr/include/botan-3/botan/tls_external_psk.h
/usr/include/botan-3/botan/tls_handshake_msg.h
/usr/include/botan-3/botan/tls_magic.h
/usr/include/botan-3/botan/tls_messages.h
/usr/include/botan-3/botan/tls_policy.h
/usr/include/botan-3/botan/tls_psk_identity_13.h
/usr/include/botan-3/botan/tls_server.h
/usr/include/botan-3/botan/tls_server_info.h
/usr/include/botan-3/botan/tls_session.h
/usr/include/botan-3/botan/tls_session_manager.h
/usr/include/botan-3/botan/tls_session_manager_hybrid.h
/usr/include/botan-3/botan/tls_session_manager_memory.h
/usr/include/botan-3/botan/tls_session_manager_noop.h
/usr/include/botan-3/botan/tls_session_manager_sql.h
/usr/include/botan-3/botan/tls_session_manager_stateless.h
/usr/include/botan-3/botan/tls_signature_scheme.h
/usr/include/botan-3/botan/tls_version.h
/usr/include/botan-3/botan/tss.h
/usr/include/botan-3/botan/types.h
/usr/include/botan-3/botan/uuid.h
/usr/include/botan-3/botan/version.h
/usr/include/botan-3/botan/x25519.h
/usr/include/botan-3/botan/x448.h
/usr/include/botan-3/botan/x509_ca.h
/usr/include/botan-3/botan/x509_crl.h
/usr/include/botan-3/botan/x509_ext.h
/usr/include/botan-3/botan/x509_key.h
/usr/include/botan-3/botan/x509_obj.h
/usr/include/botan-3/botan/x509cert.h
/usr/include/botan-3/botan/x509path.h
/usr/include/botan-3/botan/x509self.h
/usr/include/botan-3/botan/xmss.h
/usr/include/botan-3/botan/xmss_parameters.h
/usr/include/botan-3/botan/xof.h
/usr/include/botan-3/botan/zfec.h
/usr/include/botan-3/botan/zlib.h
/usr/lib64/cmake/Botan-3.5.0/botan-config-version.cmake
/usr/lib64/cmake/Botan-3.5.0/botan-config.cmake
/usr/lib64/libbotan-3.so
/usr/lib64/pkgconfig/botan-3.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/botan-3.5.0/authors.txt
/usr/share/doc/botan-3.5.0/handbook/abi.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/bigint.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/block_cipher.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/cipher_modes.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/compression.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/contents.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/credentials_manager.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/cryptobox.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/ecc.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/env_vars.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/ffi.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/filters.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/footguns.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/fpe.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/hash.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/kdf.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/keywrap.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/message_auth_codes.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/otp.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/passhash.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/pbkdf.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/pkcs11.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/providers.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/psk_db.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/pubkey.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/python.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/rng.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/roughtime.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/secmem.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/srp.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/stream_ciphers.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/tls.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/tpm.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/tss.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/versions.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/x509.rst
/usr/share/doc/botan-3.5.0/handbook/api_ref/zfec.rst
/usr/share/doc/botan-3.5.0/handbook/authors.txt
/usr/share/doc/botan-3.5.0/handbook/building.rst
/usr/share/doc/botan-3.5.0/handbook/cli.rst
/usr/share/doc/botan-3.5.0/handbook/contents.rst
/usr/share/doc/botan-3.5.0/handbook/credits.rst
/usr/share/doc/botan-3.5.0/handbook/deprecated.rst
/usr/share/doc/botan-3.5.0/handbook/dev_ref/configure.rst
/usr/share/doc/botan-3.5.0/handbook/dev_ref/contents.rst
/usr/share/doc/botan-3.5.0/handbook/dev_ref/continuous_integration.rst
/usr/share/doc/botan-3.5.0/handbook/dev_ref/contributing.rst
/usr/share/doc/botan-3.5.0/handbook/dev_ref/fuzzing.rst
/usr/share/doc/botan-3.5.0/handbook/dev_ref/mistakes.rst
/usr/share/doc/botan-3.5.0/handbook/dev_ref/next_major.rst
/usr/share/doc/botan-3.5.0/handbook/dev_ref/oids.rst
/usr/share/doc/botan-3.5.0/handbook/dev_ref/os.rst
/usr/share/doc/botan-3.5.0/handbook/dev_ref/reading_list.rst
/usr/share/doc/botan-3.5.0/handbook/dev_ref/release_process.rst
/usr/share/doc/botan-3.5.0/handbook/dev_ref/test_framework.rst
/usr/share/doc/botan-3.5.0/handbook/dev_ref/todo.rst
/usr/share/doc/botan-3.5.0/handbook/goals.rst
/usr/share/doc/botan-3.5.0/handbook/hardware_acceleration.rst
/usr/share/doc/botan-3.5.0/handbook/index.rst
/usr/share/doc/botan-3.5.0/handbook/migration_guide.rst
/usr/share/doc/botan-3.5.0/handbook/old_news.rst
/usr/share/doc/botan-3.5.0/handbook/openssl_migration_guide.rst
/usr/share/doc/botan-3.5.0/handbook/packaging.rst
/usr/share/doc/botan-3.5.0/handbook/pgpkey.txt
/usr/share/doc/botan-3.5.0/handbook/roadmap.rst
/usr/share/doc/botan-3.5.0/handbook/security.rst
/usr/share/doc/botan-3.5.0/handbook/sem_ver.rst
/usr/share/doc/botan-3.5.0/handbook/side_channels.rst
/usr/share/doc/botan-3.5.0/handbook/support.rst
/usr/share/doc/botan-3.5.0/license.txt
/usr/share/doc/botan-3.5.0/news.txt
/usr/share/doc/botan-3.5.0/pgpkey.txt

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbotan-3.so.5
/usr/lib64/libbotan-3.so.5.5.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Botan/62940cf2327ab98c3edbb00eaf5e38dc5e78ccc2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
