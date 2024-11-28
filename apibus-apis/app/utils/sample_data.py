sample_customer_data = {
    "sections": {
        "code": 200,
        "success": True,
        "data": [
            {
                "id": "3",
                "name": "IPv4",
                "description": None,
                "masterSection": "0",
                "permissions": "{\"2\":\"3\",\"3\":\"1\"}",
                "strictMode": "1",
                "subnetOrdering": "default",
                "order": None,
                "editDate": "2022-05-25 09:29:28",
                "showSubnet": "1",
                "showVLAN": "1",
                "showVRF": "1",
                "showSupernetOnly": "1",
                "DNS": None
            },
            {
                "id": "2",
                "name": "IPv6",
                "description": "Section for IPv6 addresses",
                "masterSection": "0",
                "permissions": "{\"3\":\"1\",\"2\":\"2\"}",
                "strictMode": "1",
                "subnetOrdering": None,
                "order": None,
                "editDate": None,
                "showSubnet": "1",
                "showVLAN": "0",
                "showVRF": "0",
                "showSupernetOnly": "0",
                "DNS": None
            },
            {
                "id": "6",
                "name": "Privates",
                "description": "Private IP ranges",
                "masterSection": "0",
                "permissions": "{\"2\":\"3\",\"3\":\"2\"}",
                "strictMode": "1",
                "subnetOrdering": "default",
                "order": None,
                "editDate": None,
                "showSubnet": "1",
                "showVLAN": "1",
                "showVRF": "1",
                "showSupernetOnly": "1",
                "DNS": None
            }
        ],
        "time": 0.002
    },
    "subnets": {
        "code": 200,
        "success": True,
        "data": [
            {
                "id": "60",
                "subnet": "5.133.16.0",
                "mask": "21",
                "sectionId": "3",
                "description": "UK-SOUTHERNCOMMS-20120704 Efar Ltd | EFAR",
                "linked_subnet": None,
                "firewallAddressObject": None,
                "vrfId": "0",
                "masterSubnetId": "0",
                "allowRequests": "0",
                "vlanId": None,
                "showName": "0",
                "device": None,
                "permissions": "{\"2\":\"3\",\"3\":\"1\"}",
                "pingSubnet": "0",
                "discoverSubnet": "0",
                "resolveDNS": "0",
                "DNSrecursive": "0",
                "DNSrecords": "0",
                "nameserverId": "0",
                "scanAgent": "0",
                "customer_id": None,
                "isFolder": "0",
                "isFull": "0",
                "isPool": "0",
                "tag": "2",
                "threshold": "0",
                "location": None,
                "editDate": "2022-05-25 09:29:28",
                "lastScan": None,
                "lastDiscovery": None,
                "usage": {
                    "Used": "2",
                    "Reserved": "362",
                    "Used_percent": 0.1,
                    "used": "364",
                    "Reserved_percent": 17.68,
                    "freehosts": "1684",
                    "freehosts_percent": 82.23,
                    "maxhosts": "2048"
                }
            }
        ]
    },
    "addresses": {
        "code": 200,
        "success": True,
        "data": [
            {
                "id": "24",
                "subnetId": "258",
                "ip": "5.133.16.20",
                "is_gateway": "0",
                "description": None,
                "hostname": "lo0.cr1-ngd.sclcore.net",
                "mac": None,
                "owner": None,
                "tag": "2",
                "deviceId": None,
                "location": "24",
                "port": None,
                "note": None,
                "lastSeen": "2022-05-25 15:48:37",
                "excludePing": "0",
                "PTRignore": "0",
                "PTR": "0",
                "firewallAddressObject": None,
                "editDate": "2022-11-03 12:15:08",
                "customer_id": "6"
            },
            {
                "id": "30",
                "subnetId": "774",
                "ip": "5.133.16.153",
                "is_gateway": "0",
                "description": "Jola test",
                "hostname": "Jolatest",
                "mac": None,
                "owner": None,
                "tag": "2",
                "deviceId": None,
                "location": None,
                "port": None,
                "note": None,
                "lastSeen": "1970-01-01 00:00:01",
                "excludePing": "0",
                "PTRignore": "0",
                "PTR": None,
                "firewallAddressObject": None,
                "editDate": None,
                "customer_id": None
            }
        ],
        "time": 0.004
    },
    "vlan": {
        "code": 200,
        "success": True,
        "data": [
            {
                "id": "1",
                "domainId": "1",
                "name": "IPv6 private 1",
                "number": "2001",
                "description": "IPv6 private 1 subnets",
                "editDate": None,
                "customer_id": None
            },
            {
                "id": "2",
                "domainId": "1",
                "name": "Servers DMZ",
                "number": "4001",
                "description": "DMZ public",
                "editDate": None,
                "customer_id": None
            },
            {
                "id": "8040",
                "domainId": "4518",
                "name": "name",
                "number": "404",
                "description": "description",
                "editDate": None,
                "customer_id": None
            }
        ]
    },
    "vrf": {
        "code": 200,
        "success": True,
        "data": [
            {
                "id": "6",
                "name": "vpn_3000",
                "rd": "59395:3000",
                "description": "nms_inside - Server VRF",
                "sections": None,
                "editDate": "2022-06-28 14:47:00",
                "customer_id": None
            },
            {
                "id": "1364",
                "name": "vpn_3108",
                "rd": "59395:3108",
                "description": "eurolink_infra-bt_wbmc",
                "sections": None,
                "editDate": "2023-05-10 11:40:15",
                "customer_id": None
            }
        ],
        "time": 0.004
    },
    "devices": {
        "code": 200,
        "success": True,
        "data": [{
            "id": "6",
            "hostname": "h67-0708-left_pdu",
            "ip": "10.192.1.106",
            "type": "12",
            "description": None,
            "sections": "3",
            "snmp_community": None,
            "snmp_version": "0",
            "snmp_port": "161",
            "snmp_timeout": "1000",
            "snmp_queries": None,
            "snmp_v3_sec_level": "none",
            "snmp_v3_auth_protocol": "none",
            "snmp_v3_auth_pass": None,
            "snmp_v3_priv_protocol": "none",
            "snmp_v3_priv_pass": None,
            "snmp_v3_ctx_name": None,
            "snmp_v3_ctx_engine_id": None,
            "rack": "6",
            "rack_start": "1",
            "rack_size": "0",
            "location": "12",
            "editDate": "2022-04-21 10:57:58",
            "custom_Monitoring_Link": None,
            "custom_Asset_Information": None
        },
            {
                "id": "1086",
                "hostname": "class-sbc-01",
                "ip": None,
                "type": "9",
                "description": None,
                "sections": None,
                "snmp_community": None,
                "snmp_version": "0",
                "snmp_port": "161",
                "snmp_timeout": "1000",
                "snmp_queries": None,
                "snmp_v3_sec_level": "none",
                "snmp_v3_auth_protocol": "none",
                "snmp_v3_auth_pass": None,
                "snmp_v3_priv_protocol": "none",
                "snmp_v3_priv_pass": None,
                "snmp_v3_ctx_name": None,
                "snmp_v3_ctx_engine_id": None,
                "rack": "18",
                "rack_start": "10",
                "rack_size": "1",
                "location": "24",
                "editDate": "2024-10-29 17:46:22",
                "custom_Monitoring_Link": None,
                "custom_Asset_Information": None
            },
            {
                "id": "1092",
                "hostname": "class-sbc-02",
                "ip": None,
                "type": "9",
                "description": None,
                "sections": None,
                "snmp_community": None,
                "snmp_version": "0",
                "snmp_port": "161",
                "snmp_timeout": "1000",
                "snmp_queries": None,
                "snmp_v3_sec_level": "none",
                "snmp_v3_auth_protocol": "none",
                "snmp_v3_auth_pass": None,
                "snmp_v3_priv_protocol": "none",
                "snmp_v3_priv_pass": None,
                "snmp_v3_ctx_name": None,
                "snmp_v3_ctx_engine_id": None,
                "rack": "18",
                "rack_start": "9",
                "rack_size": "1",
                "location": "24",
                "editDate": "2024-10-29 17:45:49",
                "custom_Monitoring_Link": None,
                "custom_Asset_Information": None
            }
        ],
        "time": 0.004
    },
    "customers": {
        "code": 200,
        "success": True,
        "data": [
            {
                "id": "1",
                "title": "Cloud-Sentry Limited",
                "address": "7 Pimpernel Mead",
                "postcode": "BS32 8ET",
                "city": "Bristol",
                "tag": "United Kingdom",
                "lat": None,
                "long": None,
                "contact_person": "Andy Conway",
                "contact_phone": "+447456836883",
                "contact_mail": "andy.conway@cloud-sentry.co.uk",
                "note": "sadfsdf",
                "status": "Active",
                "custom_Customer_URN": None,
                "custom_Parent_Company": None,
                "custom_Primary_Site": None
            },
            {
                "id": "6",
                "title": "Group Network Operations",
                "address": "Glebe Farm",
                "postcode": "RG25 2AD",
                "city": "Dummer",
                "tag": "United Kingdom",
                "lat": "51.2157783",
                "long": "-1.1515895885802148",
                "contact_person": "Paul  Martin",
                "contact_phone": None,
                "contact_mail": "paul.martin@southern-comms.co.uk",
                "note": None,
                "status": "Active",
                "custom_Customer_URN": None,
                "custom_Parent_Company": None,
                "custom_Primary_Site": None
            },
            {
                "id": "12",
                "title": "Twogether Creative Ltd",
                "address": "Globe House",
                "postcode": "SL7 1EY",
                "city": "Marlow",
                "tag": "United Kingdom",
                "lat": "51.573076900000004",
                "long": "-0.7597834371757755",
                "contact_person": None,
                "contact_phone": None,
                "contact_mail": None,
                "note": None,
                "status": "Active",
                "custom_Customer_URN": "28157",
                "custom_Parent_Company": "ID01",
                "custom_Primary_Site": "YES"
            },
            {
                "id": "15",
                "title": "DS Total Solutions",
                "address": "Unit 68-69 Shrivenham Hundred, Watchfield",
                "postcode": "SN6 8TY",
                "city": "Swindon",
                "tag": "United Kingdom",
                "lat": None,
                "long": None,
                "contact_person": "Farooq Sheikh",
                "contact_phone": "0800 240 4632",
                "contact_mail": "farooq@ds-totalsolutions.co.uk",
                "note": None,
                "status": "Active",
                "custom_Customer_URN": "43548",
                "custom_Parent_Company": "43919",
                "custom_Primary_Site": None
            },
            {
                "id": "21",
                "title": "Transvault Software",
                "address": "8 Hill Road",
                "postcode": "BS21 7NE",
                "city": "Clevedon",
                "tag": "United Kingdom",
                "lat": "51.44185695",
                "long": "-2.8558233040991956",
                "contact_person": "Matt Caulson",
                "contact_phone": None,
                "contact_mail": None,
                "note": None,
                "status": "Active",
                "custom_Customer_URN": "C17880",
                "custom_Parent_Company": "ID08",
                "custom_Primary_Site": None
            },
            {
                "id": "26",
                "title": "Medwyn Surgery",
                "address": "Reigate Rd",
                "postcode": "RH4 1SD",
                "city": "Dorking",
                "tag": "United Kingdom",
                "lat": "51.2353475",
                "long": "-0.3243001",
                "contact_person": None,
                "contact_phone": None,
                "contact_mail": None,
                "note": None,
                "status": "Active",
                "custom_Customer_URN": "C40436",
                "custom_Parent_Company": "ID18",
                "custom_Primary_Site": None
            },
            {
                "id": "32",
                "title": "Carter Towler",
                "address": "1 Brewery Place",
                "postcode": "LS10 1NE",
                "city": "Leeds",
                "tag": "United Kingdom",
                "lat": "53.7936919",
                "long": "-1.5377829350682592",
                "contact_person": None,
                "contact_phone": None,
                "contact_mail": None,
                "note": None,
                "status": "Active",
                "custom_Customer_URN": "C48133",
                "custom_Parent_Company": "ID01",
                "custom_Primary_Site": None
            },
            {
                "id": "34",
                "title": "Capital Hair & Beauty",
                "address": "10 Crowhurst Road",
                "postcode": "BN1 8AP",
                "city": "Brighton",
                "tag": "United Kingdom",
                "lat": "50.868248",
                "long": "-0.1229952",
                "contact_person": "Phil Carter",
                "contact_phone": "01273331122",
                "contact_mail": "pcater@capitalhb.co.uk",
                "note": None,
                "status": "Active",
                "custom_Customer_URN": "55784",
                "custom_Parent_Company": None,
                "custom_Primary_Site": None
            },
            {
                "id": "40",
                "title": "Leeways Packaging Services Ltd",
                "address": "Churcham",
                "postcode": "GL2 8AN",
                "city": "Gloucester",
                "tag": "United Kingdom",
                "lat": "51.86682745",
                "long": "-2.3498069410104017",
                "contact_person": "Tina Coult",
                "contact_phone": None,
                "contact_mail": None,
                "note": None,
                "status": "Active",
                "custom_Customer_URN": "57222",
                "custom_Parent_Company": "ID46",
                "custom_Primary_Site": "43730"
            },
            {
                "id": "52",
                "title": "Refuge",
                "address": "4th Floor, International House, 1 St Katherine's Way",
                "postcode": "E1W 1UN",
                "city": "London",
                "tag": "United Kingdom",
                "lat": None,
                "long": None,
                "contact_person": None,
                "contact_phone": None,
                "contact_mail": None,
                "note": None,
                "status": "Active",
                "custom_Customer_URN": "18983",
                "custom_Parent_Company": "18770",
                "custom_Primary_Site": None
            },
            {
                "id": "54",
                "title": "Assystem",
                "address": "xxxx",
                "postcode": "BS21 6ND",
                "city": "Clevedon",
                "tag": "United Kingdom",
                "lat": None,
                "long": None,
                "contact_person": "Brian Whitiker",
                "contact_phone": None,
                "contact_mail": None,
                "note": None,
                "status": "Active",
                "custom_Customer_URN": None,
                "custom_Parent_Company": None,
                "custom_Primary_Site": None
            },
            {
                "id": "60",
                "title": "Kanes Foods Ltd",
                "address": "Cleeve Road",
                "postcode": "WR11 8SJ",
                "city": "Evesham",
                "tag": "United Kingdom",
                "lat": None,
                "long": None,
                "contact_person": "Callum Kinnersley",
                "contact_phone": "01386835648",
                "contact_mail": "callumkinnersley@kanefoods.co.uk",
                "note": None,
                "status": "Active",
                "custom_Customer_URN": "37240",
                "custom_Parent_Company": None,
                "custom_Primary_Site": "37240"
            }
        ],
        "time": 0.004
    }
}
