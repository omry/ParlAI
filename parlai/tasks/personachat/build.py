#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
# Download and build the data if it does not exist.

import parlai.core.build_data as build_data
import os

URLS = ['http://parl.ai/downloads/personachat/' + 'personachat.tgz']
FILE_NAMES = ['personachat.tgz']
SHA256 = ['507cf8641d333240654798870ea584d854ab5261071c5e3521c20d8fa41d5622']

def build(opt):
    version = 'v1.0'
    dpath = os.path.join(opt['datapath'], 'Persona-Chat')

    if not build_data.built(dpath, version):
        print('[building data: ' + dpath + ']')
        if build_data.built(dpath):
            # An older version exists, so remove these outdated files.
            build_data.remove_dir(dpath)
        build_data.make_dir(dpath)

        # Download the data.
        build_data.download_check(dpath, URLS, FILE_NAMES, SHA256)

        for zipfile in FILE_NAMES:
            build_data.untar(dpath, zipfile)

        # Mark the data as built.
        build_data.mark_done(dpath, version)
