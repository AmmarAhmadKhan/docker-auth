phpipam_components = {
    "sections": [
        "id", "name", "description", "masterSection", "permissions", "strictMode", "subnetOrdering",
        "order", "editDate", "showSubnet", "showVLAN", "showVRF", "showSupernetOnly", "DNS"
    ],
    "subnets": [
        "id", "subnet", "mask", "sectionId", "description", "linked_subnet", "firewallAddressObject", "vrfId",
        "masterSubnetId", "allowRequests", "vlanId", "showName", "device", "permissions", "pingSubnet",
        "discoverSubnet", "resolveDNS", "DNSrecursive", "DNSrecords", "nameserverId", "scanAgent", "customer_id",
        "isFolder", "isFull", "isPool", "tag", "threshold", "location", "editDate", "lastScan", "lastDiscovery",
        {
            "usage": [
                "Used", "Reserved", "used", "Used_percent", "Reserved_percent", "freehosts", "freehosts_percent", "maxhosts"
            ]
        }
    ],
    "addresses": [
        "id", "subnetId", "ip", "is_gateway", "description", "hostname", "mac", "owner", "tag", "deviceId",
        "location", "port", "note", "lastSeen", "excludePing", "PTRignore", "PTR", "firewallAddressObject",
        "editDate", "customer_id"
    ],
    "vlans": [
        "id", "domainId", "name", "number", "description", "editDate", "customer_id"
    ],
    "vrfs": [
        "id", "name", "rd", "description", "sections", "editDate", "customer_id"
    ],
    "devices": [
        "id", "hostname", "ip", "type", "description", "sections", "snmp_community", "snmp_version", 
        "snmp_port", "snmp_timeout", "snmp_queries", "snmp_v3_sec_level", "snmp_v3_auth_protocol", "snmp_v3_auth_pass",
        "snmp_v3_priv_protocol", "snmp_v3_priv_pass", "snmp_v3_ctx_name", "snmp_v3_ctx_engine_id", "rack", "rack_start",
        "rack_size", "location", "editDate", "custom_Monitoring_Link", "custom_Asset_Information"
    ],
    "customer_info": [
        "id", "title", "address", "postcode", "city", "tag", "lat", "long", "contact_person", 
        "contact_phone", "contact_mail", "note", "status", "custom_Customer_URN", "custom_Parent_Company", "custom_Primary_Site"
    ]
}


corero_components = {
    "tenant": [
        "id", "name", "description", "status", "servicePolicyId", "address", "countryId", "Business_Unit", "Customer_ID"
    ],
    "asset_group": [
        "id", "name"
    ],
    "named_asset": [
        "id", "ip", "name", "assetGroupId"
    ],
    "service_policy": [
        "id", "serviceLevel", "maxMitigation", "description",
        {
            "serviceLevelAlertConfig": [
                "alertTemplateId", "emailAlertsEnabled", "emailAlertTo", "webhookAlertsEnabled", "webhookAlertMspEnabled", "webhookAlertTenantEnabled"
            ]
        },
        {
            "attackStatusAlertConfig": [
                "alertTemplateId", "emailAlertsEnabled", "emailAlertTo", "webhookAlertsEnabled", "webhookAlertMspEnabled", "webhookAlertTenantEnabled"
            ]
        },
        {
            "remoteMitigationAlertConfig": [
                "alertTemplateId", "emailAlertsEnabled", "emailAlertTo", "webhookAlertsEnabled", "webhookAlertMspEnabled", "webhookAlertTenantEnabled"
            ]
        }
    ]
}
