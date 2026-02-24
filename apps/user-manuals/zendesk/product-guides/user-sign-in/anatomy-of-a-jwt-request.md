# Anatomy of a JWT request

Source: https://support.zendesk.com/hc/en-us/articles/4408881965722-Anatomy-of-a-JWT-request

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

At the core of single sign-on authentication is a technology called JSON Web Token (JWT) that allows Zendesk to trust the login requests it gets from your systems. See [Setting up single sign-on with JWT (JSON Web Token)](https://support.zendesk.com/hc/en-us/articles/4408845838874) for details

For Zendesk SSO integrations, a server-side mechanism should generate the JWT and redirect the user's browser to a Zendesk-specific URL, passing the JWT as a parameter in the query string rather than in the HTTP header.

A JWT typically consists of three parts separated by periods (full stops). Each part serves a different purpose within the JWT structure: the header, payload, and signature.

**Important:** Using HTTP POST requests (instead of HTTP GET requests) is a best practice for your SSO security. Using HTTP POST, the user data is passed in the body of the request. With HTTP GET requests, data related to the user (like phone numbers or tags) are passed in the URL along with the JWT, which can be stored in a browser’s history or cache, putting it at risk for exposure.

This article contains the following sections:

- [Chunk 1: JWT Header](#h_01HKN3KKP3FBPVBYFZ0HTR7RW9)
- [Chunk 2: JWT Claims Set/Payload](#h_01HKN3KKP4DB1VX6BMY7ZSKGFS)
- [Chunk 3: JWS Signature](#h_01HKN3KKP4KSK6GFJNNJ83DNM7)

## Chunk 1: JWT Header

The first chunk is the JWT header. It indicates that it's a JWT request, and indicates the type of hashing algorithm used. (More on that later.)

```
eyJ0eXAiOiJKV1QiLA0KICJhbGciOiJIUzI1NiJ9
```

The big reveal about this (and the rest of the data) is that it is base64 encoded. This is not actually encryption so it can be easily decoded by tools like the following:

- Web tool: [http://www.base64decode.org/](http://www.base64decode.org/ "http://www.base64decode.org/")
- Terminal: [http://drewsymo.com/how-to/quick-and-simple-base64-encode-on-mac-osx-terminal/](http://www.opinionatedgeek.com/dotnet/tools/base64decode/ "http://www.opinionatedgeek.com/dotnet/tools/base64decode/")

This is what that string looks like decoded:

```
{"typ":"JWT", 
 "alg":"HS256"}
```

You can see that it takes a JSON structure and has two key-value pairs that effectively mean `type: JWT` and `Algorithm: HMAC SHA 256`. SHA 256 is a 256-bit encryption algorithm designed by the U.S. National Security Agency. It's used to generate the third chunk -- the signature -- which we'll get to in a bit.

## Chunk 2: JWT Claims Set/Payload

The second chunk is considerably longer because it contains the payload. It's known as the 'JWT Claims Set'.

```
eyJpYXQiOjEzNzIxMTMzMDUsImp0aSI6ODg4MzM2MjUzMTE5Ni4zMjYsIm5hbWUiOiJUZXN0IFVzZXIiLCJlbWFpbCI6InR1c2VyQGV4YW1wbGUub3JnIiwiZXh0ZXJuYWxfaWQiOiI1Njc4Iiwib3JnYW5pemF0aW9uIjoiQXBwbGUiLCJ0YWdzIjoidmlwX3VzZXIiLCJyZW1vdGVfcGhvdG9fdXJsIjoiaHR0cDovL21pdC56ZW5mcy5jb20vMjA2LzIwMTEvMDUvQmFybmFieV9NYXR0X2Nyb3BwZWQuanBnIiwibG9jYWxlX2lkIjoiOCJ9
```

This contains a timestamp, a random value, a user name, email address, external ID, and some tags. There are even more options available. Again, just base64 decode it to make sense of the payload. I'll split the lines to make it easier to digest.

```
{ 
"iat":1372113305, 
"jti":8883362531196.326, 
"name":"Test User", 
"email":"tuser@example.org", 
"external_id":"5678", 
"organization":"Apple", 
"tags":"vip_user", 
"remote_photo_url":"http://mit.zenfs.com/206/2011/05/Barnaby_Matt_cropped.jpg", 
"locale_id":"8" 
}
```

### Required properties

#### IAT

The first key is **iat**, which stands for **issued at**. This is a timestamp formatted as whole seconds since January 01, 1970, which is a standard UNIX representation of time. The timestamp must be an integer (no decimals) and it must be in UTC. It also must be within 3 minutes of the current time when the Zendesk server receives it. This puts a self-destruct mechanism in each remote authentication request, preventing any single request from being used more than 3 minutes after it was generated.

#### JTI

The second key, **jti**, stands for **JSON Token ID**. It's really just a random string. It has to be sufficiently long and random so that it's very unlikely to be used again on this account. If, by accident or chance, it is re-used for another authentication request, the request will fail. What this amounts to is a disposable key. By including a (mandatorily) random value like this, we ensure that no two authentication requests are ever the same. This prevents reuse of a valid request URL. For example, imagine that someone succeeded in installing malware on your computer or network and has started logging your traffic. They can see every URL you hit. If they see and grab the URL you were issued to log in to Zendesk, they could use it themselves to log in as you within 3 minutes without this single-use key.

#### Name

Next is the user's full **name** with spaces included. Whatever Zendesk receives here is set as the user name, even if they had a different name set before.

#### Email

After that is the user's email. Email is always required. It is used as the unique identifier for a user **unless an external ID is received\***. This means that if we get an email and an external ID, we try to match the ID first. If we do, we update that user with the specified email address.

**\*****Note:** If the option '*Allow update of external IDs*' is enabled in Zendesk, we'll continue to key off the email even if an external ID is received. If the email and external ID differ, we'll change the ID.

### Optional properties

#### External ID

External ID is an optional ID you can use to identify users instead of using their email address (noted above).

#### Organization

You can also pass an **organization** value to add a user to an organization. The named organization must already exist and the name must match exactly. Otherwise no action is taken.

#### Tags

The **tags**key allows you to set tagson the user being logged in. The key replaces any existing tags on the user with the tags you specify, so use it carefully. Passing a blank tags parameter *removes all tags* from a user.

#### Remote Photo URL

You can also pass a value for **remote\_photo\_url**, which accepts a public URL containing a photo and sets this photo as the user's profile picture.

#### Locale (Language)

You can pass a value for **locale\_id** to set or update the authenticated user's language in Zendesk. The value must be a number that matches a currently activated locale in your Zendesk. You can find the locales by using the locales.json endpoint of our API: <https://developer.zendesk.com/api-reference/ticketing/account-configuration/locales/#list-locales>

#### User Fields (not shown in example)

This must be a JSON object that includes key-value pairs for each field key and value. The field key can be found or defined in the User Fields interface. Note that only custom user fields can be passed.

Example:

```
"user_fields": {"checked": false,"date_joined": "2013-08-14T00:00:00+00:00","region": "EMEA","text_field": null}
```

Checkboxes use boolean values, date codes follow the example above, and drop-downs accept the name of the option. Text fields accept strings.

#### Phone Number (not shown in example)

This accepts a string for a phone number identity. Make sure to specify the phone number in an accepted format. For more information, see [What are the accepted phone number formats?](https://support.zendesk.com/hc/en-us/articles/4408823756570)

## Chunk 3: JWS Signature

The last chunk of the request is the encrypted part. You don't need to worry too much about this, but basically it takes all the information above (iat, jti, name, email, etc) along with the **shared secret** and generates an encrypted string out of all of it. Then, per JWT standards, a chunk of that encrypted string is taken (known as a **checksum**), and that is the JWS signature.

So how is this secure?

To generate a valid encrypted string, you must know the **shared secret**.

Encryption is designed so that you cannot work backwards from the encrypted string to the data and the key. Even if you have the data contents, it's practically impossible to deduce the key.

But since you have the key, and we have the key, and you send us the same data unencrypted as you do encrypted, we can build the signature ourselves and check that it matches what you sent.

It also insures nobody can tamper with the data in transit.

This is how you build it in pseudo-code:

```
URLBase64Encode(   
    HMAC-SHA256(   
        URLBase64Encode( header_json ).URLBase64Encode( payload_json )   
    ) 
)
```

When generating the HMAC-SHA256 of the encoded header and payload, you include the shared secret.

This is the result:

```
Zv9P7PNIcgHfxZaMwQtMpty3TZnmVHRWcsmAMM-mNHg
```