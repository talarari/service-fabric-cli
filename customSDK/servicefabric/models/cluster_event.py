# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .fabric_event import FabricEvent


class ClusterEvent(FabricEvent):
    """Represents the base for all Cluster Events.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: ClusterHealthReportCreatedEvent,
    ClusterHealthReportExpiredEvent, ClusterUpgradeCompleteEvent,
    ClusterUpgradeDomainCompleteEvent, ClusterUpgradeRollbackCompleteEvent,
    ClusterUpgradeRollbackStartEvent, ClusterUpgradeStartEvent,
    ChaosStoppedEvent, ChaosStartedEvent

    :param event_instance_id: The identifier for the FabricEvent instance.
    :type event_instance_id: str
    :param time_stamp: The time event was logged.
    :type time_stamp: datetime
    :param has_correlated_events: Shows there is existing related events
     available.
    :type has_correlated_events: bool
    :param kind: Constant filled by server.
    :type kind: str
    """

    _validation = {
        'event_instance_id': {'required': True},
        'time_stamp': {'required': True},
        'kind': {'required': True},
    }

    _subtype_map = {
        'kind': {'ClusterHealthReportCreated': 'ClusterHealthReportCreatedEvent', 'ClusterHealthReportExpired': 'ClusterHealthReportExpiredEvent', 'ClusterUpgradeComplete': 'ClusterUpgradeCompleteEvent', 'ClusterUpgradeDomainComplete': 'ClusterUpgradeDomainCompleteEvent', 'ClusterUpgradeRollbackComplete': 'ClusterUpgradeRollbackCompleteEvent', 'ClusterUpgradeRollbackStart': 'ClusterUpgradeRollbackStartEvent', 'ClusterUpgradeStart': 'ClusterUpgradeStartEvent', 'ChaosStopped': 'ChaosStoppedEvent', 'ChaosStarted': 'ChaosStartedEvent'}
    }

    def __init__(self, event_instance_id, time_stamp, has_correlated_events=None):
        super(ClusterEvent, self).__init__(event_instance_id=event_instance_id, time_stamp=time_stamp, has_correlated_events=has_correlated_events)
        self.kind = 'ClusterEvent'