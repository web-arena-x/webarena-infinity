# Using multiple JWT single sign-on URLs for multiple brands

Source: https://support.zendesk.com/hc/en-us/articles/4408886711066-Using-multiple-JWT-single-sign-on-URLs-for-multiple-brands

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

**Disclaimer**: This article is provided for instructional purposes only. Zendesk does not support or guarantee custom code.

When you [set up multiple brands](https://support.zendesk.com/hc/en-us/articles/4408829476378), security settings only allow you to set up one single URL for remote logins. This might be problematic if you have different user databases for each of your brands.

The approach described in this article allows you to create a script between Zendesk and the SSO login script in your server that will allow you to route your customers to specific URLs based on which brand they are trying to log in to.

This procedure assumes that you have already configured JWT on your server. Otherwise, make sure that you follow the instructions listed in the article [Enabling JWT single sign-on](https://support.zendesk.com/hc/en-us/articles/203663816-Setting-up-single-sign-on-with-JWT-JSON-Web-Token-) first.

This example in this article uses PHP, but you can adapt it to other languages if you need to.

This article contains the following sections:

- [Two or more brands or more set up](#h_9143e170-5cd3-4be3-98c3-e908fb650480)
- [Two or more user authentication systems set up with JWT SSO](#h_a26a144f-c694-477f-99a9-cca737f0efde)
- [The scripts](#h_9ff13ace-1a75-4eff-8290-2927b29a961f)
- [Update security settings](#h_7e415489-4f38-45d5-b250-c96e18434c5d)
- [Important considerations](#h_01GM4B7G5B73P4KQRZ92Z6A12P)
- [Troubleshooting](#h_378d438b-cb76-4c0f-bed9-809fcbf176ff)

## Two or more brands set up

You need to configure at least two brands to follow this procedure, if you haven't already. For details, see  [Setting up multiple brands](https://support.zendesk.com/hc/en-us/articles/204108983). After you set it up, save the brand URL and the host-mapped brand URL. You will use them in the script later.

## Two or more user authentication systems set up with JWT SSO

You must create one JWT SSO configuration in Zendesk and two or more configurations on your user authentication systems. You can do one for each brand already, but bear in mind that the shared secret that you obtain from security options will have to be the same in all your authentication systems.

Save the login URL and logout URL along with the information from the previous section.

## The scripts

Your list of saved URLs might look like this:

**Brand 1**

Non-Hostmapped URL: https://brand1.zendesk.com

Hostmapped URL: https://support1.example.com

**Brand 2**

Non-Hostmapped URL: https://brand2.zendesk.com

Hostmapped URL: https://support2.example.com

**System 1**

Login URL: https://page1.example.com/zdlogin.php

Logout URL: https://page1.example.com/zdlogout.php

**System 2**

Login URL: https://page2.example.com/zdlogin.php

Logout URL: https://page2.example.com/zdlogout.php

Next, create the script. Remove the  *https://*  from the URL for each brand URL. Keep them on the website links.

You can also find the scripts here:

- [zdlogin.php](https://github.com/abmartinr/zdscripts/blob/master/php/zdlogin.php)
- [zdlogout.php](https://github.com/abmartinr/zdscripts/blob/master/php/zdlogout.php)

**Login script**

```
<?

$brand_URLs = array(
	"brand1.zendesk.com" => "https://page1.example.com/yourcustomloginjwtscript.php",
	"support1.example.com" => "https://page1.example.com/yourcustomloginjwtscript.php",
	"brand2.zendesk.com" => "https://page2.example.com/yourcustomloginjwtscript2.php",
	"support2.example.com" => "https://page2.example.com/yourcustomloginjwtscript2.php"
	);

foreach($brand_URLs as $k => $v){
	if(strpos($_GET['return_to'],$k)){
		header("Location: ". $v);
		die();
	}
}

?>
```

**Logout script**

```
<?

$brand_URLs = array(
	"brand1.zendesk.com" => "https://page1.example.com/yourcustomlogoutjwtscript.php",
	"support1.example.com" => "https://page1.example.com/yourcustomlogoutjwtscript.php",
	"brand2.zendesk.com" => "https://page2.example.com/yourcustomlogoutjwtscript.php",
	"support2.example.com" => "https://page2.example.com/yourcustomlogoutjwtscript.php"
	);

foreach($brand_URLs as $k => $v){
	if(strpos($_GET['return_to'],$k)){
		header("Location: ". $v);
		die();
	}
}
?>
```

## Update security settings

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/217743418), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)**Account** in the sidebar, then select **Security > Single sign-on**.
2. Click **Create SSO configuration** then select **JSON Web Token**.
3. Enter a unique **Configuration name**.
4. For the **Remote login URL**, enter the URL for the login script.
5. For the **Remote logout URL**, enter the URL for the logout script.
6. To avoid conflicts in case some of your customers have an account in more than one user authentication system with the same email address, you can set **Update of external IDs** to **On**.
7. Provide the **Shared** **secret** to your IT team. They'll need it for their JWT implementation.
8. **Save** your changes.

![Screen_Shot_2022-12-12_at_6.08.07_PM.png](https://support.zendesk.com/hc/article_attachments/7856559996058)

### Important considerations

Consider the following:

- Security risk is low if you use the script as-is. If you modify it extensively other than the changes mentioned here, you may create a security vulnerability on your own server (not Zendesk’s).
- Since we only provide one JWT Token, all your SSO Scripts will use the same tokens in your authentication systems. If one of your systems is compromised, it may lead to all of your brands being compromised.
- If you get an "Invalid JWT Request" error when you try to SSO, refer to the [Troubleshooting](#h_378d438b-cb76-4c0f-bed9-809fcbf176ff) instructions below.

### Troubleshooting

To prevent invalid JWT request errors, hardcode https://(*defaultsubdomain*).zendesk.com/ as `/access/jwt?jwt=` for both brands where *(defaultsubdomain)* is your main brand subdomain. For example, mydomain.zendesk.com.

1. Hardcode https://(*defaultsubdomain*).zendesk.com into the SSO script, so the JWT payload always gets sent to https://(*defaultsubdomain*).zendesk.com/access/jwt
2. Implement that snippet into the script to use 'return\_to' so the end user is redirected back to the origin Help Center. Make sure to append the payload for both brand marking URLs as fixed as '(*defaultsubdomain*)' and append 'return\_to'.  
     
   The snippet for your reference:

```
if(isset($_GET["return_to"])) {  
  $location .= "&return_to=" . urlencode($_GET["return_to"]);  
}
```