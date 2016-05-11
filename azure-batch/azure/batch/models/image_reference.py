# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ImageReference(Model):
    """
    A reference to an Azure Virtual Machines Marketplace image.

    :param publisher: The publisher of the Azure Virtual Machines Marketplace
     image. For example, Canonical or MicrosoftWindowsServer.
    :type publisher: str
    :param offer: The offer type of the Azure Virtual Machines Marketplace
     image. For example, UbuntuServer or WindowsServer.
    :type offer: str
    :param sku: The SKU of the Azure Virtual Machines Marketplace image. For
     example, 14.04.0-LTS or 2012-R2-Datacenter.
    :type sku: str
    :param version: The version of the Azure Virtual Machines Marketplace
     image. A value of 'latest' can be specified to select the latest version
     of an image. If omitted, the default is 'latest'.
    :type version: str
    """ 

    _validation = {
        'publisher': {'required': True},
        'offer': {'required': True},
        'sku': {'required': True},
    }

    _attribute_map = {
        'publisher': {'key': 'publisher', 'type': 'str'},
        'offer': {'key': 'offer', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, publisher, offer, sku, version=None):
        self.publisher = publisher
        self.offer = offer
        self.sku = sku
        self.version = version
