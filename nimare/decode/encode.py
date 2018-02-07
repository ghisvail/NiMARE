# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""
Methods for encoding text into brain maps.
"""
from ...due import due, Doi


@due.dcite(Doi('10.1371/journal.pcbi.1005649'),
           description='Citation for GCLDA encoding.')
class GCLDAEncoder(object):
    def __init__(self, model, text, topic_priors, prior_weight):
        pass
