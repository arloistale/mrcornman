# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from whitenoise.storage import CompressedManifestStaticFilesStorage

class BlogCompressedManifestStaticFilesStorage(CompressedManifestStaticFilesStorage):
    manifest_strict = False
