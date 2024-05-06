# Overview

This project addresses problems with the default Windows log settings. By default, Windows does not log many events that are necessary for detecting malicious activity and performing forensic investigations. To enhance visibility in your Windows environment, the audit policies must be configured properly.

> [!IMPORTANT]  
> Make changes to your systems at your own risk! The suggestions in this project are based on my research from Microsoft documentation and other sources.

> This is a work in progress; please check back periodically for updates.

# Acknowledgements

This project's knowledge base is primarily drawn from Microsoft's "Advanced Security Audit Policy Settings" [document](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/advanced-security-audit-policy-settings). Special thanks to Michel de Crevoisier for the [Windows-auditing-baseline](https://github.com/mdecrevoisier/Windows-auditing-baseline) project. Utilizing Michel de Crevoisier's Excel table, I have adapted some audit policy settings based on my research, added the number of Sigma rules per Event ID, and included descriptions for each subcategory (using GPT-3.5/4.0).

Additional thanks go to Yamato-Security for their "Security Log Audit Settings" [guide](https://github.com/Yamato-Security/EnableWindowsLogSettings/blob/main/ConfiguringSecurityLogAuditPolicies.md), and the use of the Hayabusa tool in this project to count Sigma rules per Event ID.

# Access to Document

You can access it through the following link: [Access Document](https://1drv.ms/x/s!Aq8mUjPGWpnIjfhczbceN-J1qHXdKQ?e=cGaksE).

# Custom Script Instructions

This section provides instructions on using the [Hayabusa](https://github.com/Yamato-Security/hayabusa) tool along with custom scripts to build a dictionary of statistics for each Event ID.

1. **Update Sigma Rules Using Hayabusa Tool**:
   - For Linux:
     ```
     ./hayabusa-2.13.0-lin-x64-musl update-rules
     ```
   - For Windows:
     ```
     hayabusa.exe update-rules
     ```

2. **Place Scripts Inside the Hayabusa Directory**

3. **Install PyYAML**:
   - Run the following command to install PyYAML:
     ```
     pip install PyYAML
     ```

4. **Build the Dictionary**:
   - Execute the script to generate statistics by Event ID:
     ```
     python3 win_sec_generate_stats_by_event_id.py
     ```

5. **Retrieve Statistics by Event ID**:
   - Use the following command to get statistics for a specific Event ID:
     ```
     python3 win_sec_get_event_id_stats.py
     ```
