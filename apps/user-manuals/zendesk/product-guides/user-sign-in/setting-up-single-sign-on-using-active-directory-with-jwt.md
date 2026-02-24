# Setting up single sign-on using Active Directory with JWT

Source: https://support.zendesk.com/hc/en-us/articles/4408832064922-Setting-up-single-sign-on-using-Active-Directory-with-JWT

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

**Disclaimer**: This article is provided for instructional purposes only. Zendesk does not support or guarantee the code. Post any issues you have in the comments section or try searching for a solution online.

You can authenticate users using JWT (JSON web token) single sign-on. This article describes how to configure JWT SSO authentication for Microsoft Active Directory users.

This article covers the following steps:

- [Step 1. Configuring your Windows server](#h_01HMA5N4HJ2ZKFWC5FT716P2PG)
- [Step 2. Configuring Zendesk](#h_01HMA5N4HJW996W82WXKKYB8TN)
- [Step 3. Downloading and configuring the authentication script](#h_01HMA5N4HJC93HKDQ9JCA6BQDE)
- [Step 4. Troubleshooting](#h_01HMA5N4HJE5HQP4J23R2M81X7)

## Step 1. Configuring your Windows server

You need IIS and ASP installed on your Windows server. Your IIS server has to be part of your domain and have direct access to your domain controller. The IIS server can be on the domain controller, but that is not required. If using Windows Server 2008, here is what role should be installed:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ad_image01.jpg)

For the IIS Role Services, you need the following installed:

- Application Development
- ASP.NET
- ASP
- Server Side Includes

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ad_image03.jpg)

And under Security

- Basic Authentication

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ad_image08.jpg)

Once your roles and services are installed properly, you have to configure the authentication of your IIS server. Zendesk works well with Basic Authentication so I usually make that my default. Make sure you disable Anonymous Authentication or else users will not get prompted for their Windows username and password and thus fail to login.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ad_image06.jpg)

## Step 2. Configuring Zendesk

For instructions, see  [Enabling JWT single sign-on in your Zendesk](https://support.zendesk.com/hc/en-us/articles/4408845838874)  in the article,  [Setting up single sign-on with JWT (JSON Web Token).](https://support.zendesk.com/hc/en-us/articles/4408845838874) For the  **Remote Login URL**  value, specify the location where you'll place the ASP authentication script described in the next section.

## Step 3. Downloading and configuring the authentication script

Download the ASP authentication script from this page on Github:

[https://github.com/zendesk/zendesk\_jwt\_sso\_examples/tree/master/bun...](https://github.com/zendesk/zendesk_jwt_sso_examples/tree/master/bundles)

Place the script (and its dependencies which are included in the above bundle) into your wwwroot directory. You can create a subdirectory, but remember that that will just extend the URL for the script. During a new install, IIS will create this directory in:

c:\inetpub\wwwroot\

For your web browser, files in that folder will appear in this URL:

http://serveraddress/classic\_asp\_jwt\_with\_ad.asp

Open the script in Notepad or any other text editor. The first part of the script that you need to configure is the following:

```
    ' Credentials for a domain user for LDAP access
    sLdapReaderUsername = "domain\username"
    sLdapReaderPassword = "password"
```

Enter your username and password of a user that has access to LDAP.

Next, you need to enter the Shared Secret Token that you got during the JWT Zendesk configuration (labeled sKey in the script) as well as enter your Zendesk subdomain:

```
' Set your shared secret and Zendesk subdomain  
 sKey = ""  
 sSubdomain = ""
```

Here's the part of the script that does the LDAP lookup of your user account:

```
sQuery = "<LDAP://" & sDomainContainer & ">;(sAMAccountName=" & sUsername & "); adspath," & sFields & ";subtree"  
 Set userRS = oConn.Execute(sQuery)
```

If you look at the code, we are getting the adspath, mail, displayName, and sAMAccountName of the user. If you want to pull more data to be used in your call, include it in that part of the code. For example if I want to include the Notes block below:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ad_image04.jpg)

I would update the code with the attribute “info” to look as follows:

```
    sQuery = ";(sAMAccountName=" & strUsername & ");adspath,mail,displayName,sAMAccountName,info;subtree"
    Set userRS = oConn.Execute(sQuery)
```

Once we have the attributes being looked up, we can use them. The code below performs the actual translation of the attributes:

```
    If Not userRS.EOF and not err then
        sFullName = userRS("displayName")
        sEmail = userRS("mail")
        sExternalID = userRS("sAMAccountName")
    if sOrg then
        sOrganization = ""
    end if
        sTags = ""
        sPhotoUrl = ""
```

You will see that we have already placed in the displayName, mail, and sAMAccountName. If you'd like to call the individual attributes of your user, you would use the “userRS(“nameofattribute”)” object. So for example, if you included the “info” lookup, and I want to use the Notes block for tags, I would update the code to read as follows:

```
    If Not userRS.EOF and not err then
        sFullName = userRS("displayName")
        sEmail = userRS("mail")
        sExternalID = userRS("sAMAccountName")
    if sOrg then
        sOrganization = ""
    end if
        sTags = userRS("info")
        sPhotoUrl = ""
```

So what individual attributes are available? You can see what options you have for attributes here:

<http://www.kouti.com/tables/userattributes.htm>

Also, if you enable “Advanced Features” in your Active Directory Users and Computers, you can change the individual attributes directly. To enable Advanced Features, go to View > Advanced Features:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ad_image00.jpg)

Once that is enabled, if you go to the properties of the user, you will see an “Attribute Editor”:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ad_image05.jpg)

**Note about passing through organization and tags**

To successfully pass through an organization for a user, an organization already must exist in Zendesk. If an organization does not exist in Zendesk (or the names are not an exact match), Zendesk will not create the organization on the fly like it does the user. You first must create the organizations involved.

To successfully pass through tags, the attribute must have them listed as such:

“tag1, tag2, tag3”

If you do not include the “,” between the tags, it will fail.

For more information on the different fields we accept, take a look at this  [post.](https://support.zendesk.com/hc/en-us/articles/4408845838874#topic_otw_jfh_3fb)

After you have made your changes in the script, save it. Go to your Zendesk site and click Login. This should redirect you to the script where you will put in your Windows credentials and be sent back to Zendesk logged in!

## Step 4. Troubleshooting

So you clicked login and it failed? As part of the script we have included a debugging option. If you turn the Debug flag to 'True' in the script, Debug information will be printed when accessing your script.  It will look something like:

```
[DEBUG] ZENDESK\test - should be of the form DOMAIN\username - if blank, your IIS probably allows anonymous access to this file.  
[DEBUG] DomainContainer: DC=zendesk,DC=internal  
[DEBUG] Attribute name: Test User  
[DEBUG] Attribute email: test@zendesk.com  
[DEBUG] Attribute jti: 2968942290171.981  
[DEBUG] Attribute iat: 1380123848  
[DEBUG] Redirecting to https://subdomain.zendesk.com/access/jwt?jwt=eyJ0eXAiOiJKV1QiLA0KICJhbGciOiJIUzI1NiJ9.eyJpYXQiOjEzODAxMjM4NDgsImp0aSI6Mjk2ODk0MjI5MDE3MS45ODEsIm5hbWUiOiJUZXN0IFVzZXIiLCJlbWFpbCI6InRlc3RAemVuZGVzay5jb20ifQ.QuRC6Ig7x_nK86Wc38u2viIVjshtTDohcgXTYpmU6VY
```

Here you should get all of your information properly listed. If you configured an Organization, tags, or the PhotoURL, you should see this data. If you are seeing some of the data, but not all of the data, verify the attribute data of the user, along with making sure the code references the proper attribute.

If you are getting to the page but are not getting any data this means that the script is failing to connect to your domain controller or has no permission. Verify on the server that you can access the domain controller by going to the server’s share (\\dcservername\ in the run prompt). Next verify that the user name and password that you placed in the code is correct. Also, if you have anonymous access enabled, you may get a blank page as it never asked for authentication. Ensure that anonymous access is turned off.

If you are unable to get to the page and your browser throws an error, the problem lies within IIS. Confirm that you have installed the needed roles/services on your server and that they are running. If you are still having issues, you may have to consult an IIS Administrator as errors of this kind are outside the scope of this guide.

If you do experience an error, please let us know what your resolution was. I would be happy to update this post with additional tips to problems that people are having and how to resolve them.