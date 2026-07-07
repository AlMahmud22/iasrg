# Wazuh SIEM/XDR Feasibility Analysis

Prepared for: working record / Wazuh, SOC, and CTI feasibility phase  
Date checked: 2026-06-29  
Scope: research and feasibility analysis only. This file does not claim that a full Wazuh production deployment was completed.

## 1. Short Conclusion

Wazuh is a free and open-source security monitoring platform that combines SIEM and XDR-style functions. In simple terms, it collects security data from endpoints, servers, network devices, cloud workloads, and other sources; analyzes that data using rules, decoders, vulnerability intelligence, and dashboards; then helps a security team detect, investigate, and respond to suspicious activity.

The important point is that Wazuh is not only a dashboard. It is a monitoring stack that can support log collection, endpoint monitoring, vulnerability detection, rule-based alerting, compliance checks, and incident-response workflow. It can also sit beside an existing paid firewall, endpoint protection, or campus network system instead of replacing everything.

## 2. What Wazuh Is

Wazuh describes itself as an open-source security platform that provides unified XDR and SIEM protection for endpoints and cloud workloads. Its official documentation says the platform is composed of Wazuh agents plus three central components: Wazuh server, Wazuh indexer, and Wazuh dashboard. The agents collect security events from monitored systems, the server analyzes them, the indexer stores/searches them, and the dashboard visualizes alerts and system status.

Useful source links:

- Wazuh home page: https://wazuh.com/
- Wazuh architecture: https://documentation.wazuh.com/current/getting-started/architecture.html
- Wazuh installation guide: https://documentation.wazuh.com/current/installation-guide/index.html
- Wazuh release notes: https://documentation.wazuh.com/current/release-notes/index.html

As of the checked date, the current Wazuh 4.x release stream listed version 4.14.5, released on 23 April 2026. Version numbers matter because Wazuh components should be kept compatible during installation and upgrades.

## 3. Origin, Creator, and Why It Was Created

Wazuh comes from the OSSEC host-based intrusion detection ecosystem and is commonly described in public security-community sources as an OSSEC fork that grew into a broader platform. OSSEC was already a known open-source HIDS, while Wazuh expanded the idea into a wider platform with dashboards, integrations, rules, vulnerability detection, compliance support, and large-environment deployment options.

Wazuh's own material documents OSSEC-to-Wazuh migration and explains that Wazuh adds active development, scalability, threat detection, and third-party/cloud integrations beyond a traditional OSSEC deployment. Wazuh's official team page identifies Santiago Bassett as Founder and CEO, and the about page presents Wazuh as an open-source cybersecurity company that began in 2015.

Source links:

- Migrating from OSSEC to Wazuh: https://wazuh.com/blog/migrating-from-ossec-to-wazuh/
- Wazuh about us: https://wazuh.com/about-us/
- Wazuh team: https://wazuh.com/our-team/
- OSSEC official site: https://www.ossec.net/

The practical reason Wazuh exists is clear: many organizations need security visibility, alerting, compliance monitoring, and incident response support, but commercial SIEM/XDR platforms can be costly. Wazuh tries to provide a strong open-source route for smaller teams, students, labs, and organizations that want more control over their security monitoring stack.

## 4. What Category Wazuh Falls Under

Wazuh is not only one type of tool. It overlaps several categories.

| Category | Does Wazuh fit? | Explanation |
|---|---:|---|
| HIDS | Yes | Wazuh inherited and extended host-based intrusion detection ideas from OSSEC. It monitors endpoints, logs, files, processes, configuration, and suspicious activity. |
| SIEM | Yes | NIST defines a SIEM tool as an application that gathers security data from information system components and presents it as actionable information through a single interface. Wazuh does this through agents, server analysis, indexer storage, and dashboard visualization. Source: https://csrc.nist.gov/glossary/term/security_information_and_event_management_tool |
| XDR | Partly/Yes | Wazuh markets itself as unified XDR and SIEM. It has endpoint detection, cloud workload monitoring, vulnerability detection, response scripts, and integrations, but it is still more open and engineering-heavy than some commercial managed XDR products. |
| Vulnerability management | Partial | Wazuh can detect vulnerabilities by comparing endpoint inventory with Wazuh CTI/vulnerability content. It is useful for visibility, but patching still needs separate operational work. |
| Compliance monitoring | Yes | Wazuh includes configuration assessment, file integrity monitoring, audit-style reporting, and rules aligned with standards such as PCI DSS, GDPR, HIPAA, NIST, and similar frameworks. |
| Antivirus replacement | No | It can integrate with malware detection workflows and tools such as VirusTotal/YARA/ClamAV, but it should not be treated as a full standalone antivirus or EDR replacement in every environment. |
| Firewall replacement | No | It can trigger active responses such as blocking network access in some cases, but it is not a firewall product. |
| Full SOC by itself | No | Wazuh supports SOC work, but people, procedures, triage, tuning, escalation, and response playbooks are still needed. |

## 5. Main Jobs of Wazuh

Wazuh mainly solves visibility and monitoring problems. Without a tool like this, security teams often have logs scattered across many machines, no central way to search them, no consistent alerting, and limited awareness of endpoint changes or vulnerabilities.

The main jobs are:

1. Collect endpoint and server logs.
2. Detect suspicious events using rules and decoders.
3. Monitor file integrity and configuration changes.
4. Identify vulnerable software and operating system packages.
5. Support malware detection workflows through integrations.
6. Map alerts to MITRE ATT&CK tactics and techniques.
7. Provide dashboards for investigation and reporting.
8. Support compliance monitoring.
9. Trigger active response actions when configured carefully.
10. Give a SOC team a central place to investigate alerts.

Official Wazuh capability areas include file integrity monitoring, malware detection, security configuration assessment, active response, log collection, vulnerability detection, command monitoring, container security, system inventory, and agentless monitoring.

Source links:

- Wazuh capabilities: https://documentation.wazuh.com/current/user-manual/capabilities/index.html
- File integrity monitoring: https://documentation.wazuh.com/current/user-manual/capabilities/file-integrity/index.html
- Vulnerability detection: https://documentation.wazuh.com/current/user-manual/capabilities/vulnerability-detection/index.html
- Active response: https://documentation.wazuh.com/current/user-manual/capabilities/active-response/index.html
- MITRE ATT&CK module: https://documentation.wazuh.com/current/user-manual/ruleset/mitre.html

## 6. Problems It Solves

### 6.1 Lack of central log visibility

In many systems, useful evidence is spread across Windows event logs, Linux syslog, application logs, authentication logs, web server logs, cloud logs, and endpoint activity. Wazuh centralizes much of this data so analysts can search and review alerts from one place.

### 6.2 Delayed detection

Without monitoring, suspicious login attempts, malware-like file changes, privilege changes, or vulnerable packages may only be noticed after damage is already done. Wazuh helps detect these signals earlier.

### 6.3 Poor endpoint awareness

Wazuh agents collect system inventory and endpoint security data. This helps a team understand which machines exist, what software is installed, what services are running, and what changed.

### 6.4 Weak compliance evidence

Compliance normally needs evidence that logs are collected, access is monitored, file changes are tracked, and configurations are checked. Wazuh helps prepare this kind of audit and monitoring evidence, although policy and human review are still required.

### 6.5 Manual response overload

The Active Response module can run scripts based on rule triggers. For example, it can help block a repeated brute-force source or remove a known malicious file when a careful rule and integration is configured. This is useful, but it must be tested carefully because bad automation can block valid activity or damage systems.

## 7. How Wazuh Deployment Works

Wazuh has four core parts:

| Component | Simple role |
|---|---|
| Wazuh agent | Installed on endpoints such as Windows, Linux, macOS, servers, cloud instances, and some other supported platforms. It collects security data. |
| Wazuh server | Receives agent data, decodes events, applies rules, manages agents, and triggers alerts. |
| Wazuh indexer | Stores and indexes alerts and event data so they can be searched quickly. |
| Wazuh dashboard | Web interface used by analysts/admins to view alerts, agents, vulnerabilities, compliance status, and dashboards. |

The basic data flow is:

```text
Endpoint/server/cloud workload
  -> Wazuh agent
  -> Wazuh server
  -> Wazuh indexer
  -> Wazuh dashboard
  -> analyst investigation or response
```

Official architecture details say the agent connects to the Wazuh server on TCP 1514 by default. Filebeat forwards alert and event data from the Wazuh server to the Wazuh indexer, normally using port 9200/TCP. The dashboard queries the Wazuh server API, normally on port 55000/TCP, and also queries indexed data for visualization.

Source: https://documentation.wazuh.com/current/getting-started/architecture.html

## 8. Deployment Models

| Deployment model | Best for | Notes |
|---|---|---|
| All-in-one | Lab, learning, small environments | Server, indexer, and dashboard on one machine. Fastest way to test. Wazuh says this is usually enough for up to 100 endpoints and 90 days of queryable/indexed alert data, depending on resources. |
| Single-node separated components | Medium environments | Server, indexer, and dashboard can be placed on separate servers for better performance and clearer management. |
| Multi-node cluster | Larger environments | Multiple Wazuh server and indexer nodes for high event throughput, high availability, and load balancing. |
| Docker | Testing, containerized labs, repeatable setup | Wazuh supports Docker deployment for central components and agents. |
| Kubernetes | Containerized/cloud-native deployment | Useful where the organization already runs Kubernetes. |
| Ansible/Puppet | Automated infrastructure management | Useful when deploying or maintaining multiple nodes repeatedly. |
| Wazuh Cloud | Managed service | Wazuh operates the platform. This reduces maintenance work but adds subscription cost. |

Source links:

- Wazuh architecture/deployment models: https://documentation.wazuh.com/current/getting-started/architecture.html
- Wazuh quickstart: https://documentation.wazuh.com/current/quickstart.html
- Wazuh Docker deployment: https://documentation.wazuh.com/current/deployment-options/docker/wazuh-container.html
- Wazuh Cloud deployment options: https://documentation.wazuh.com/current/cloud-service/index.html

## 9. Hardware and Lab Requirements

For the quickstart all-in-one setup, Wazuh documentation gives these guideline resources:

| Agents | CPU | RAM | Storage for 90 days indexed alerts |
|---:|---:|---:|---:|
| 1 to 25 | 4 vCPU | 8 GiB | 50 GB |
| 25 to 50 | 8 vCPU | 8 GiB | 100 GB |
| 50 to 100 | 8 vCPU | 8 GiB | 200 GB |

For a student lab, a realistic setup would be:

- One Ubuntu Server VM for Wazuh central components.
- One Windows VM as an endpoint agent.
- One Linux VM as another endpoint agent.
- Optional: a test web server or Docker host if container/security log monitoring is needed.
- No real personal data, banking details, passwords, or victim data should be used.

Source: https://documentation.wazuh.com/current/quickstart.html

## 10. How To Create a Basic Wazuh Lab

This is the clean learning path.

### Step 1: Prepare a Linux server

Use a supported 64-bit Linux server. Ubuntu 22.04 or 24.04 is a common choice for a lab. Allocate at least 4 vCPU, 8 GiB RAM, and 50 GB storage for a small test.

### Step 2: Install Wazuh central components

For an all-in-one lab installation, Wazuh gives this assisted installation pattern:

```bash
curl -sO https://packages.wazuh.com/4.14/wazuh-install.sh
sudo bash ./wazuh-install.sh -a
```

After installation, the script displays dashboard access details. Passwords can be extracted from the generated install archive:

```bash
sudo tar -O -xvf wazuh-install-files.tar wazuh-install-files/wazuh-passwords.txt
```

Source: https://documentation.wazuh.com/current/quickstart.html

### Step 3: Open the dashboard

Access:

```text
https://<WAZUH_DASHBOARD_IP_ADDRESS>
```

Log in with the admin credentials generated during installation.

### Step 4: Enroll agents

From the dashboard, add agents for Windows/Linux/macOS endpoints. Wazuh gives OS-specific agent installation commands from the dashboard. After the agent is installed and connected, it should appear in the agent list.

### Step 5: Enable or review key modules

Start with:

- Log collection
- File integrity monitoring
- Security configuration assessment
- Vulnerability detection
- System inventory
- MITRE ATT&CK dashboard

Do not immediately enable aggressive active response in a real machine. First test it in a controlled VM.

### Step 6: Generate safe test events

Safe test examples:

- Create or modify a test file in a monitored folder to check FIM.
- Review failed login events on a lab system.
- Install a deliberately outdated package only inside a disposable lab VM to observe vulnerability detection.
- Review dashboard alerts and map them to rule IDs and MITRE ATT&CK where available.

### Step 7: Tune rules and reduce noise

The first setup may generate many alerts. This is normal. A real SOC must tune rules, set priorities, define escalation paths, and document what counts as high severity in the actual environment.

## 11. Threat Intelligence and CTI Relevance

Wazuh has a built-in Cyber Threat Intelligence direction mainly around vulnerability intelligence. The Wazuh CTI platform supports the vulnerability detection feature and has a public CVE/vulnerability explorer.

Source links:

- Wazuh CTI/vulnerability detection explanation: https://documentation.wazuh.com/current/user-manual/capabilities/vulnerability-detection/how-it-works.html
- Wazuh CTI public site: https://cti.wazuh.com/

Wazuh can also integrate with external threat intelligence tools and services. For example:

- VirusTotal integration can check suspicious files together with file integrity monitoring.
- MISP can be used to correlate alerts or indicators with threat intelligence feeds, although this normally requires custom integration work and careful setup.

Source links:

- VirusTotal integration: https://documentation.wazuh.com/current/user-manual/capabilities/malware-detection/virus-total-integration.html
- Wazuh threat hunting use case mentioning MISP: https://documentation.wazuh.com/current/getting-started/use-cases/threat-hunting.html

The clean CTI angle is that Wazuh helps with security monitoring and threat intelligence for IT environments. Its CTI use is mainly around vulnerability intelligence, suspicious files, external intelligence feeds, and alert enrichment. It does not directly solve public-facing scam awareness or victim-support problems by itself.

## 12. Cost, License, and Paid/Free Options

### 12.1 Wazuh self-hosted

Wazuh self-hosted is free and open source. The official quickstart says Wazuh components use GNU GPL v2 and Apache License 2.0. This means there is no software license fee for self-hosting, but there are still infrastructure and human costs:

- server/VM/cloud compute cost,
- storage cost,
- maintenance and upgrade time,
- analyst time,
- rule tuning time,
- backup and security hardening effort.

Source: https://documentation.wazuh.com/current/quickstart.html

### 12.2 Wazuh Cloud

Wazuh Cloud is the managed version operated by Wazuh. As checked on the official Wazuh Cloud page, listed starting prices were:

| Plan | Active agents | Indexed retention | Archive retention | Starting price |
|---|---:|---:|---:|---:|
| Small | Up to 100 | 1 month | 3 months | USD 571/month |
| Medium | Up to 250 | 3 months | 1 year | USD 923/month |
| Large | Up to 500 | 3 months | 1 year | USD 1467/month |
| Custom | Custom | Custom | Custom | Custom quote |

Pricing changes over time, so this table should be rechecked before any real budget decision.

Source: https://wazuh.com/cloud/

## 13. Alternatives and Competitors

| Tool | Free or paid | Main category | Strong points | Limits / tradeoff |
|---|---|---|---|---|
| Wazuh | Free self-hosted; paid cloud/support | Open-source SIEM/XDR/HIDS | Good for labs, endpoint monitoring, FIM, vulnerability detection, compliance, open-source control | Needs technical setup, tuning, maintenance, and SOC process |
| OSSEC | Free/open source, with related paid ecosystem options | HIDS | Lightweight, mature HIDS base, file/log monitoring | Less complete as a modern SIEM/XDR platform compared with Wazuh |
| Security Onion | Free/open source; paid support/appliances available | Threat hunting, network security monitoring, log management | Strong for network visibility, Zeek/Suricata style monitoring, hunting labs | Heavier setup; more network/SOC lab focused than endpoint-only monitoring |
| Elastic Security | Free/basic options plus paid Elastic Cloud/subscriptions | SIEM/XDR/search analytics | Strong search, scale, dashboards, detection rules, flexible data ingestion | Can require engineering skill and paid tiers for advanced features/support |
| Graylog | Graylog Open free; Enterprise/Security paid | Log management/SIEM | Good log management, SIEM features in paid Security edition, predictable platform model | Some SIEM features are paid; Graylog Security listed from USD 18,000/year |
| Microsoft Sentinel | Paid cloud SIEM/SOAR | Cloud-native SIEM/SOAR | Strong for Microsoft/Azure environments, many connectors, cloud scale | Cost depends heavily on ingestion, retention, and region |
| Splunk Enterprise Security | Paid enterprise SIEM | Enterprise SIEM/security analytics | Mature ecosystem, powerful search/correlation, large enterprise use | Cost can be high; pricing can be workload/ingest based |
| IBM QRadar SIEM | Paid enterprise SIEM | Enterprise SIEM | Mature enterprise SIEM with event/flow orientation | Usually commercial/enterprise cost and sizing complexity |
| Google Security Operations | Paid enterprise/cloud SecOps | Cloud SIEM/SOAR/security operations | Strong large-scale telemetry and Google/Mandiant intelligence ecosystem | Enterprise pricing and cloud platform dependency |

Main source links:

- OSSEC: https://www.ossec.net/
- Security Onion: https://securityonionsolutions.com/
- Elastic pricing/security: https://www.elastic.co/pricing and https://www.elastic.co/security/siem
- Graylog pricing: https://graylog.org/pricing/
- Microsoft Sentinel pricing: https://www.microsoft.com/en-us/security/pricing/microsoft-sentinel
- Splunk pricing: https://www.splunk.com/en_us/products/pricing.html
- IBM QRadar pricing: https://www.ibm.com/products/qradar-siem/pricing
- Google Security Operations: https://cloud.google.com/security/products/security-operations

## 14. Wazuh vs Alternatives - Practical Reading

If the goal is learning SOC basics on a limited budget, Wazuh is a strong choice. It is free to self-host and has enough real security features to teach endpoint monitoring, logs, alerts, rules, dashboards, vulnerability detection, and response concepts.

If the goal is large-scale enterprise detection with a mature commercial ecosystem, Splunk Enterprise Security, Microsoft Sentinel, Google Security Operations, IBM QRadar, or Elastic Security may be more common depending on the organization. These tools usually need paid licensing and trained staff.

If the goal is network traffic monitoring and packet-level investigation, Security Onion may be more suitable than Wazuh alone because Security Onion is built around threat hunting and network security monitoring tools such as Suricata and Zeek.

If the goal is pure endpoint protection, tools such as Microsoft Defender for Endpoint, CrowdStrike Falcon, SentinelOne, or similar EDR/XDR products may provide stronger endpoint prevention and managed detection features. Wazuh can support endpoint monitoring, but it should not automatically be treated as equivalent to every commercial EDR product.

## 15. UTM JB Public ICT and Security Context

This section is based only on public UTM and UTM Digital information. It should not be read as a full disclosure of UTM's internal security stack because universities normally do not publish every SOC, SIEM, firewall, endpoint, or monitoring product for security reasons.

Public sources show that UTM has a large digital environment. UTM's facts and figures page lists 32,004 students and 4,837 staff, with data updated on 21 January 2026. That does not mean all of these people have university-owned endpoints, but it shows the account, network, Wi-Fi, email, identity, support, and security-monitoring scale that the digital team must handle.

UTM Digital's public structure shows a Centre of Digital Infrastructure that manages network, servers, and cybersecurity to keep the university digital environment stable and secure. The same public pages list areas such as network, data centre, cybersecurity, digital support, software/subscriptions, and ICT service reporting through SISPAA.

Public source links:

- UTM facts and figures: https://www.utm.my/about/facts-and-figures/
- UTM Digital Centre of Digital Infrastructure: https://digital.utm.my/pusat-infrastruktur-digital/
- UTM Digital CDI page: https://digital.utm.my/cdi/
- UTM Digital support/reporting page: https://digital.utm.my/support/

## 16. What UTM Publicly Shows It Uses or Requires

### 16.1 Publicly named service areas

The public evidence points to these areas:

| Public evidence | What it means for a Wazuh feasibility study |
|---|---|
| UTM Digital provides and manages ICT security using Next Generation Firewall. Its ICT Security page lists Firewall Policy, URL Filtering, Application Control, and Intruder Prevention System. | UTM already has perimeter/security-control functions. Wazuh would not replace the NGFW. It could collect and analyze firewall/syslog/security events from it if log export is allowed. |
| A public Sangfor vendor success story says UTM used Sangfor IAG, described as a secure web gateway, to support BYOD, URL filtering, traffic management, malware detection, traffic decryption, application control, device onboarding, and reporting. | This is the clearest public vendor-specific clue. Because it is a vendor case study and not an internal UTM inventory page, it should be treated as public third-party evidence that needs current confirmation from UTM Digital before final procurement claims. |
| The Centre of Digital Infrastructure manages network, servers, and cybersecurity. | Wazuh would fit as a central visibility layer for servers, selected managed endpoints, and network/security logs. |
| UTM uses SISPAA support reporting for ICT issues. | Wazuh alerts would still need a human workflow. Alerts may be linked to tickets manually or later integrated through an ITSM workflow. |
| UTM has a paid Google Workspace for Education Plus package. | Email/collaboration security is part of the wider environment. Wazuh does not replace Google security controls. Logs could be integrated only if UTM exports them through supported/custom log pipelines. |
| UTM's older ICT security policy mentions audit trails, log systems, log monitoring, incident reporting, UTMCERT, firewall, IDS/IPS, antivirus/anti-malware, and ICT incident handling. | These are directly related to SIEM/SOC functions. Wazuh can support many of these monitoring and evidence requirements, but it does not replace policy, staff, or incident governance. |

Public source links:

- UTM ICT Security page: https://digital.utm.my/ict-security/
- Sangfor UTM success story: https://www.sangfor.com/success-stories/universiti-teknologi-malaysia-utm
- Google Workspace for Education Plus at UTM: https://digital.utm.my/google-workspace-for-education-plus/
- UTM ICT security policy PDF: https://digital.utm.my/wp-content/uploads/2022/12/CICT-UTM-ISMS-P1-001-DKICT-Ver-0.1-new-22-Mac-2017-review-for-UTM.pdf
- UTM Digital profile PDF: https://digital.utm.my/wp-content/uploads/2022/02/SEKSYEN-2-PROFIL-JABATAN-PERKHIDMATAN-DIGITAL-UTMDIGITAL-13012022.pdf

### 16.2 What cannot be confirmed publicly

The public sources checked do not confirm the exact SIEM/SOC platform used by UTM JB. They also do not confirm whether UTM currently uses Splunk, Microsoft Sentinel, QRadar, Elastic, Graylog, Wazuh, a managed SOC vendor, or another internal platform. The Sangfor success story is useful because it gives a vendor-specific clue for secure web gateway / internet access control, but it still does not prove UTM's current SIEM/SOC platform. The safer statement is:

> UTM publicly shows NGFW/SWG-style controls, cybersecurity, NOC/support, incident handling, logging, IDS/IPS, antivirus/anti-malware, and audit requirements, with Sangfor IAG appearing in a public vendor case study; however, its exact current SIEM/SOC product stack is not publicly confirmed.

This matters because the recommendation should not claim that Wazuh will replace an unknown paid system. A better feasibility question is:

> If UTM already uses paid tools for firewall, endpoint, email, or monitoring, can Wazuh reduce cost or improve visibility by covering selected SIEM/XDR use cases as an open-source layer?

## 17. Can Wazuh Solve UTM's Security-Monitoring Purpose?

Wazuh can solve part of the purpose, but not all of it.

| UTM need or visible requirement | Can Wazuh help? | Practical explanation |
|---|---:|---|
| Central log visibility | Yes | Wazuh can collect endpoint, application, server, and network-device logs. Wazuh documentation says it can collect logs from monitored endpoints, applications, and network devices, and can collect syslog from firewalls, switches, and routers. |
| Firewall policy, URL filtering, application control | No, not as a replacement | UTM's public ICT Security page already points to NGFW functions. Wazuh should ingest NGFW logs and alerts, not replace the firewall. |
| Secure web gateway / Sangfor IAG-style access control | No, not as a replacement | If UTM still uses Sangfor IAG or a similar SWG/NGFW product, Wazuh can use its logs for monitoring and correlation, but Wazuh does not provide the same inline web-gateway enforcement function. |
| IDS/IPS requirement | Partly | Wazuh has host-based detection and can ingest logs from IDS/IPS tools. It is not the same as a high-throughput network IPS appliance. |
| Antivirus/anti-malware requirement | Partly | Wazuh can integrate with malware workflows such as VirusTotal/YARA/ClamAV and can collect endpoint security events. It should not be treated as a full antivirus replacement. |
| Audit trail and log monitoring | Yes | This is one of Wazuh's strongest fits. It can centralize alerts, system logs, file integrity events, and compliance evidence. |
| Incident response / UTMCERT workflow | Yes, with process | Wazuh can support alert triage, evidence collection, dashboards, and active response. Human review and formal incident process remain necessary. |
| Vulnerability visibility | Yes | Wazuh can identify vulnerable software/packages using inventory and vulnerability intelligence. Patching still requires separate IT operations. |
| Network operations monitoring | Partly | Wazuh is security-focused. It can complement NOC monitoring, but it does not replace network uptime tools, Wi-Fi controllers, or performance monitoring. |
| Google Workspace/email security | Limited/depends | Wazuh does not replace Google Workspace security features. Some logs may be integrated through Google Cloud/custom pipelines, but this needs technical validation. |
| Student BYOD devices | Usually no | Installing Wazuh agents on personal student devices would be a privacy, consent, and management issue. Wazuh is better for UTM-owned servers, managed endpoints, and approved systems. |

Source links:

- Wazuh log collection: https://documentation.wazuh.com/current/user-manual/capabilities/log-data-collection/index.html
- Wazuh syslog collection: https://documentation.wazuh.com/current/user-manual/capabilities/log-data-collection/syslog.html
- Wazuh vulnerability detection: https://documentation.wazuh.com/current/user-manual/capabilities/vulnerability-detection/index.html
- Wazuh malware detection / VirusTotal: https://documentation.wazuh.com/current/user-manual/capabilities/malware-detection/virus-total-integration.html

## 18. Proposed Wazuh Deployment for a UTM-Style Environment

The most realistic approach is not to deploy Wazuh to the whole university immediately. It should start with a controlled pilot, then expand only after log volume, alert quality, storage, and staffing are understood.

### 18.1 Pilot scope

Suggested first scope:

1. Critical Linux and Windows servers.
2. Selected UTM-owned administrator/staff workstations.
3. Public-facing web or application servers.
4. DNS, DHCP, VPN, and authentication-related logs if available.
5. NGFW/firewall/security gateway logs through syslog if approved.
6. Existing IDS/IPS or network-security alert logs if export is available.
7. SISPAA/ICT support linkage as a manual process first.

Avoid in the first phase:

- full student BYOD monitoring,
- personal devices,
- sensitive research data without approval,
- aggressive active-response automation,
- replacing current firewall, email, or endpoint tools.

### 18.2 Suggested architecture

For UTM, a separated-component architecture is better than a single all-in-one server once the pilot grows beyond a small lab.

```text
Managed endpoints / servers
  -> Wazuh agents
  -> Wazuh server cluster
  -> Wazuh indexer cluster
  -> Wazuh dashboard

Network/security devices
  -> Syslog / log forwarding
  -> Wazuh server
  -> Wazuh indexer
  -> Wazuh dashboard
```

Minimum production-style components:

- Wazuh servers/managers for receiving and analyzing events.
- Wazuh indexers for storing searchable alerts.
- Wazuh dashboard for analyst use.
- Secure backup/storage for configuration and alert data.
- Separate management network or restricted firewall rules.
- Role-based access for security/admin users.
- Documented retention policy.

### 18.3 Data sources to integrate

| Data source | Collection method | Priority |
|---|---|---:|
| Linux servers | Wazuh agent | High |
| Windows servers | Wazuh agent | High |
| Managed staff/admin endpoints | Wazuh agent | Medium to high |
| NGFW/firewall | Syslog if supported and approved | High |
| Sangfor IAG/SWG or similar web gateway | Syslog/API/export if supported and approved | High if confirmed current |
| VPN/authentication | Agent, syslog, or API depending on system | High |
| DNS/DHCP | Syslog or server agent | Medium |
| Web/app servers | Agent plus application logs | High for public-facing systems |
| Existing antivirus/EDR logs | Syslog/API/Windows event logs depending on vendor | Medium |
| Google Workspace | Requires separate validation; possibly export/API/custom pipeline | Medium but not first-day critical |
| SISPAA/ICT tickets | Manual correlation first; later API integration if available | Medium |

## 19. Server and Costing Scenarios

These are planning estimates, not vendor quotations. The real cost depends on log volume, retention, high availability, storage type, support contract, and whether UTM uses existing virtualization resources.

### 19.1 Option A - Small pilot, up to 100 managed agents

Purpose: prove whether Wazuh can monitor selected UTM-owned servers, selected admin endpoints, and a small number of infrastructure logs.

| Item | Suggested sizing / cost |
|---|---|
| Wazuh model | All-in-one or small separated deployment |
| Agents | Up to 100 |
| Minimum Wazuh guideline | 8 vCPU, 8 GiB RAM, 200 GB storage for up to 100 agents and 90 days indexed alerts |
| Practical UTM pilot sizing | 8 to 12 vCPU, 16 GiB RAM, 500 GB to 1 TB SSD/NVMe |
| Software license | USD 0 for self-hosted Wazuh |
| Wazuh Cloud alternative | Small plan, up to 100 active agents, USD 571/month listed price |
| Local hardware/VM cost | If existing VM capacity is available, direct hardware cost may be low. If new hardware is required, a small server/storage purchase may be roughly RM 8,000 to RM 25,000 depending on specs and procurement. |
| Staffing | At least one security/infra owner, part-time analyst/admin effort, documented escalation process |

### 19.2 Option B - Department or critical-services deployment, up to 250 agents

Purpose: cover critical servers, security infrastructure logs, IT/admin endpoints, and selected high-value systems.

| Item | Suggested sizing / cost |
|---|---|
| Wazuh model | Separated server, indexer, and dashboard |
| Agents | Up to 250 |
| Suggested VMs | 1 Wazuh server, 1 Wazuh indexer, 1 dashboard/management VM; add a second indexer if log volume is high |
| Practical sizing | Around 24 to 32 total vCPU, 48 to 96 GiB total RAM, 1 to 3 TB fast storage |
| Software license | USD 0 for self-hosted Wazuh |
| Wazuh Cloud alternative | Medium plan, up to 250 active agents, USD 923/month listed price |
| Local hardware/VM cost | Rough planning range RM 25,000 to RM 80,000 if new server/storage capacity is needed. Less if UTM can allocate existing virtualization/storage. |
| Staffing | 1 system/security admin plus analyst coverage for daily triage; rule tuning needed during first 1 to 3 months |

### 19.3 Option C - Campus critical-security deployment, up to 500 agents

Purpose: support wider critical-service monitoring, multiple infrastructure sources, and more formal SOC-style use.

| Item | Suggested sizing / cost |
|---|---|
| Wazuh model | Multi-node production cluster |
| Agents | Up to 500 |
| Suggested nodes | 2 Wazuh servers, 3 Wazuh indexers, 1 dashboard/management node; backup/monitoring storage separate |
| Practical sizing | Around 48 to 80 total vCPU, 128 to 256 GiB total RAM, 4 to 10 TB SSD/NVMe depending on retention and log rate |
| Software license | USD 0 for self-hosted Wazuh |
| Wazuh Cloud alternative | Large plan, up to 500 active agents, USD 1467/month listed price |
| Local hardware/VM cost | Rough planning range RM 80,000 to RM 250,000 if new redundant hardware/storage is needed. Storage and redundancy can push this higher. |
| Staffing | Dedicated security operations ownership; daily triage, monthly tuning, vulnerability management, and incident-reporting process |

### 19.4 Option D - University-wide managed endpoint monitoring

This should not be assumed as the first Wazuh target. UTM's total students and staff count is much larger than 500, but not every person equals a managed device. A university-wide endpoint project would need:

- confirmed number of UTM-owned managed endpoints,
- confirmed server count,
- network-device and firewall log EPS estimate,
- BYOD policy decision,
- endpoint management/MDM readiness,
- privacy and consent model,
- retention and legal review,
- high-availability architecture,
- 24/7 or business-hours SOC decision,
- custom Wazuh Cloud quote or larger self-hosted cluster.

If the target goes beyond 500 managed agents, Wazuh Cloud would require a custom quote. For self-hosted Wazuh, storage sizing becomes the main cost driver because campus firewall/DNS/authentication logs can generate much more data than endpoint alerts alone.

## 20. Paid System Replacement vs Complementary Use

The most sensible proposal is not "replace UTM's paid system with Wazuh" immediately. A safer and more professional proposal is:

> Use Wazuh as an open-source SIEM/XDR layer for selected servers, endpoints, and infrastructure logs, then compare its coverage, cost, maintenance effort, and alert quality against the current paid or existing tools.

### 20.1 What Wazuh can replace or reduce

Wazuh may reduce the need for some paid SIEM/log-monitoring features if the current paid system is mainly used for:

- collecting server and endpoint logs,
- file integrity monitoring,
- vulnerability visibility,
- basic compliance dashboards,
- rule-based alerts,
- MITRE ATT&CK mapping,
- central alert review for selected systems.

### 20.2 What Wazuh should not replace directly

Wazuh should not directly replace:

- NGFW firewall functions,
- URL filtering and application control,
- network IPS throughput inspection,
- endpoint antivirus/EDR prevention,
- Google Workspace security features,
- NOC uptime/performance monitoring,
- incident governance and human response.

### 20.3 When a paid platform may still be better

A paid SIEM/SOC tool may still be better if UTM requires:

- strong native SaaS connectors,
- vendor-managed 24/7 monitoring,
- guaranteed support SLA,
- easier executive reporting,
- built-in SOAR playbooks,
- large-scale ingestion with enterprise support,
- integration with an existing Microsoft/Azure/Google/Splunk ecosystem.

## 21. Implementation Work Needed Before UTM Could Adopt Wazuh

Before adoption, these tasks must be completed:

1. Confirm current security stack.
   - Current firewall/NGFW vendor and logging capability.
   - Whether Sangfor IAG/SWG is still in use, replaced, or only historical.
   - Existing SIEM/SOC/log-management platform, if any.
   - Existing endpoint protection/EDR.
   - Existing NOC monitoring tools.
   - Existing ticketing/incident workflow.

2. Define exact scope.
   - Servers only, admin endpoints, public systems, or wider managed endpoints.
   - Whether cloud/SaaS logs are included.
   - Whether student-owned devices are excluded.

3. Estimate log volume.
   - Number of agents.
   - Firewall/syslog events per second.
   - Windows event volume.
   - Web/app server log volume.
   - Retention period: 30, 90, 180, or 365 days.

4. Prepare infrastructure.
   - VMs or physical servers.
   - Storage type and backup.
   - Network segmentation.
   - TLS/certificate management.
   - Admin access control and MFA.

5. Build pilot.
   - Install Wazuh central components.
   - Enroll selected agents.
   - Forward firewall/syslog logs.
   - Enable vulnerability detection, FIM, SCA, and key rules.
   - Create dashboards and alert priorities.

6. Evaluate output.
   - Alert volume.
   - False positive rate.
   - Detection coverage.
   - Analyst workload.
   - Storage growth.
   - Incident usefulness.
   - Comparison against current paid/existing tools.

7. Decide adoption model.
   - Keep only as lab/proof of concept.
   - Use beside paid tools.
   - Replace selected paid log-monitoring functions.
   - Expand to formal SOC use.

## 22. Suggested Mini-Lab If Needed Later

If a practical demonstration is needed later, the safest mini-lab would be:

1. Deploy Wazuh all-in-one on Ubuntu.
2. Add one Windows agent and one Linux agent.
3. Test file integrity monitoring with a harmless test folder.
4. Test vulnerability detection using normal package inventory.
5. Review MITRE ATT&CK mapping for generated alerts.
6. Integrate VirusTotal only with a valid API key and harmless test conditions.
7. Document screenshots:
   - dashboard login,
   - agent list,
   - FIM event,
   - vulnerability dashboard,
   - MITRE ATT&CK view,
   - sample alert details.

This mini-lab would produce evidence without overclaiming that a real SOC was built.

## 23. Risks and Practical Limitations

| Risk / limitation | Why it matters | Practical response |
|---|---|---|
| Alert noise | SIEM tools can generate many alerts that are not all urgent. | Tune rules, define severity levels, document triage process. |
| Resource usage | Logs and alerts can use a lot of CPU, RAM, and storage. | Start small, estimate endpoints, set retention properly. |
| Maintenance | Self-hosted Wazuh needs updates, backup, certificates, and health checks. | Use a maintenance checklist or managed Wazuh Cloud if budget allows. |
| False confidence | Installing a dashboard does not mean security is solved. | Treat Wazuh as one part of monitoring, not the whole security program. |
| Active response mistakes | Bad response rules can block valid users or disrupt systems. | Test in lab first and keep production automation conservative. |
| CTI interpretation | Threat intelligence needs context; not every CVE or IOC means active compromise. | Validate alerts manually and use CTI as support evidence. |
| Privacy/log sensitivity | Logs may contain usernames, IPs, hostnames, and operational data. | Avoid personal data in student labs and apply privacy controls in real systems. |
| Unknown current UTM stack | Public sources do not confirm the exact paid SIEM/SOC platform, if any. | Ask UTM Digital/CDI or supervisor for approved internal information before making replacement claims. |
| BYOD privacy | Student-owned devices are not the same as university-managed endpoints. | Limit Wazuh agents to UTM-owned/managed systems unless there is explicit policy, consent, and endpoint management. |
| Storage growth | Firewall, DNS, VPN, and authentication logs can grow quickly. | Run a 30-day pilot and calculate real daily GB before final sizing. |
| Integration complexity | Google Workspace, NGFW, endpoint tools, and tickets may need custom integration. | Start with agents and syslog; add API integrations after the pilot proves value. |

## 24. Final Assessment

Wazuh is suitable as a serious feasibility option for a UTM-style environment because it can cover many SIEM/XDR needs without a software license fee: server and endpoint monitoring, log collection, vulnerability detection, file integrity monitoring, rule-based alerts, compliance support, and SOC-style dashboards.

The strongest case for Wazuh is not that it replaces every paid system. The stronger case is that it can complement the existing security stack and possibly reduce paid SIEM/log-monitoring dependency for selected use cases. UTM's public information already shows cybersecurity, NGFW, NOC/support, incident handling, log/audit, IDS/IPS, and antivirus requirements. Wazuh aligns well with the monitoring and evidence side of those requirements, but it should sit beside firewall, endpoint protection, email security, and formal incident process.

Recommended next decision:

> Run a small Wazuh pilot for UTM-owned servers, selected managed endpoints, and exported NGFW/syslog sources. After 30 days, compare alert usefulness, storage growth, staff workload, and cost against the current paid/existing tools. Only then decide whether Wazuh should remain a lab tool, become a complementary monitoring layer, or replace selected paid SIEM/log-monitoring functions.
