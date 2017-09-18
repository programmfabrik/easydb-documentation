#Self-registration

## Register as a user

Once set up, users can register themselves for easydb. If easydb is opened in the browser, the button for registration appears in the upper right corner of the browser.

![Registration](register.png)

## Set up self-registration as an admin 

To set up a public access with self-registration, the easydb administrator must place the following settings.

### 1) Make settings in the basic configuration
*PATH: Basic Configuration> Tab: Login*

* Enable "Anonymous over Internet Allowed"
* Complete all fields in the section "Self-Registration"

![Basic Configuration: Login](register_baseconfig.png)

### 2) Adjust system rights for user group
*PATH: Rights management> Groups/Roles> Anonymous users> Tab: System rights*

* Activate "Search"
* "Create user registration"
	* Select all fields required for self-registration
	* Type "easydb self-registration"

![System permissions for Anonymous Users](group_systemrights.png)

### 3) Share content for the groups/roles "Anonymous Users"
*PATH: Tags & Workflows> Tabs: Tags*

* In the "Tags & Workflows" area, create the tag group "Release"
* Create the tag "external" inside

![Create Release](tags_register.png)

*PATH: Pool Management> Pools> Pool (level)> Tab: Permissions*

* In the "Pools" section, add rights for the group "Anonymous Users" (see Minutes, Enable Allowed Masks and Pool and, depending on requirements, also display/download rights)
* Select the tag "external" as tag filter

![Pool Authorization](pool_permission.png)