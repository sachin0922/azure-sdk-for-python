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


class VirtualMachineConfiguration(Model):
    """
    The configuration for compute nodes in a pool based on the Azure Virtual
    Machines infrastructure.

    :param image_reference: A reference to the Azure Virtual Machines
     Marketplace image to use.
    :type image_reference: :class:`ImageReference
     <azure.batch.models.ImageReference>`
    :param node_agent_sku_id: The SKU of Batch Node Agent to be provisioned
     on the compute node. The Batch node agent is a program that runs on each
     node in the pool, and provides the command-and-control interface between
     the node and the Batch service. There are different implementations of
     the node agent, known as SKUs, for different operating systems.
    :type node_agent_sku_id: str
    :param windows_configuration: Windows operating system settings on the
     virtual machine. This property must not be specified if the
     ImageReference property specifies a Linux OS image.
    :type windows_configuration: :class:`WindowsConfiguration
     <azure.batch.models.WindowsConfiguration>`
    """ 

    _validation = {
        'image_reference': {'required': True},
    }

    _attribute_map = {
        'image_reference': {'key': 'imageReference', 'type': 'ImageReference'},
        'node_agent_sku_id': {'key': 'nodeAgentSKUId', 'type': 'str'},
        'windows_configuration': {'key': 'windowsConfiguration', 'type': 'WindowsConfiguration'},
    }

    def __init__(self, image_reference, node_agent_sku_id=None, windows_configuration=None):
        self.image_reference = image_reference
        self.node_agent_sku_id = node_agent_sku_id
        self.windows_configuration = windows_configuration
