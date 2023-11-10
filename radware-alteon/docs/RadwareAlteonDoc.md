
<h2>About the connector</h2>

<p>Radware Alteon is a robust and feature-rich application delivery controller that helps organizations optimize application performance, enhance security, and ensure high availability, making it a valuable component of modern IT infrastructure</p>

<p>This document provides information about the Radware Alteon Connector, which facilitates automated interactions, with a Radware Alteon server using FortiSOAR&trade; playbooks. Add the Radware Alteon Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Radware Alteon.</p>

<h3>Version information</h3>

<p>Connector Version: 1.0.0</p>

<p>Authored By: Fortinet CSE</p>

<p>Certified: No</p>

<h2>Installing the connector</h2>

<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>

<pre>yum install cyops-connector-radware-alteon</pre>

<h2>Prerequisites to configuring the connector</h2>

<ul>
<li>You must have the credentials of Radware Alteon server to which you will connect and perform automated operations.</li>
<li>The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Radware Alteon server.</li>
</ul>

<h2>Minimum Permissions Required</h2>

<ul>
<li>Not applicable</li>
</ul>

<h2>Configuring the connector</h2>

<p>For the procedure to configure a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector">here</a></p>

<h3>Configuration parameters</h3>

<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Radware Alteon</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the URL of the Radware Alteon server to connect and perform the automated operations.</td>
</tr><tr><td>Authentication Type</td><td>Select this authentication type as Basic or Token Based.<br><strong>If you choose 'Basic Authentication'</strong><ul><li>Username: Specify the username for your account to access the Radware Alteon server to connect and perform the automated operations.</li><li>Password: Specify the password for your account to access the Radware Alteon server to connect and perform the automated operations.</li></ul><strong>If you choose 'Token Based'</strong><ul><li>API Token: Specify the Base64 encoded API Token to access the Radware Alteon Rest API server to connect and perform the automated operations.</li></ul></td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

<h2>Actions supported by the connector</h2>

<p>The following automated operations can be included in playbooks and you can also use the annotations to access operations:</p>

<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Add Table Element</td><td>Add the IP addresses entry in Access Control Lists (ACLs) in the table.</td><td>add_table_element <br/>Investigation</td></tr>
<tr><td>View Table</td><td>Retrieves Access Control Lists (ACLs) for IP addresses in tabular format</td><td>view_table <br/>Investigation</td></tr>
<tr><td>View Table Element</td><td>View the  Access Control Lists (ACLs) for IP addresses elements of the table.</td><td>view_table_element <br/>Investigation</td></tr>
<tr><td>Edit Table Element</td><td>Edit the  Access Control Lists (ACLs) for IP addresses elements of the table.</td><td> <br/>Investigation</td></tr>
<tr><td>Delete Table Element</td><td>Delete the entry from the Access Control Lists (ACLs).</td><td>delete_table_element <br/>Investigation</td></tr>
</tbody></table>

<h3>operation: Add Table Element</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>IP Address</td><td>Specify the IP address of the entry which you want to add Access Control Lists (ACLs).
</td></tr><tr><td>Mask</td><td>Specify the IP address Mask of the entry.
</td></tr><tr><td>Index</td><td>Specify the index of the IP ACL list where you want to add IP address
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "result": "",
    "api_data": ""
}</pre>

<h3>operation: View Table</h3>

<h4>Input parameters</h4>

<p>None.</p>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "result": "",
    "api_data": ""
}</pre>

<h3>operation: View Table Element</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Index</td><td>The index of the IP ACL table. Note: This table is not supported in VX instance of Virtualization.
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "result": "",
    "api_data": ""
}</pre>

<h3>operation: Edit Table Element</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>IP Address</td><td>Specify the IP address of the entry.
</td></tr><tr><td>Mask</td><td>Specify the IP address Mask of the entry.
</td></tr><tr><td>Index</td><td>The index of the IP ACL table.
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "result": "",
    "api_data": ""
}</pre>

<h3>operation: Delete Table Element</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Index</td><td>The index of the IP ACL table. Note: This table is not supported in VX instance of Virtualization.
</td></tr></tbody></table>

<h4>Output</h4>

<p>No output schema is available at this time.</p>

<h2>Included playbooks</h2>

<p>The <code>Sample - radware-alteon - 1.0.0</code> playbook collection comes bundled with the Radware Alteon connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the <strong>Automation</strong> &gt; <strong>Playbooks</strong> section in FortiSOAR&trade; after importing the Radware Alteon connector.</p>

<ul>
<li>Add Table Element</li>
<li>Delete Table Element</li>
<li>Edit Table Element</li>
<li>View Table</li>
<li>View Table Element</li>
</ul>

<p><strong>Note</strong>: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.</p>
