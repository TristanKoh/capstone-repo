# Annotator Instructions

## A.	General Instructions

A policy is analyzed solely based on its content and not on any external information (e.g., news articles describing the privacy practices of the company in question or an annotator's personal experience with the app of the company).

The annotation should be made in the provided excel sheet. The sentence(s) that refer to a particular practice should be also copied into the excel sheet. A sentence can have multiple labels.

Annotating a policy is essentially an exercise in reading comprehension. A privacy practice must be explicitly mentioned. For example, "We may allow third parties to collect technical information, such as your SIM card number." would be annotated with Identifier_SIM_Serial_3rdParty. However, "We may allow third parties to collect technical information from your phone." would not be sufficient. However, synonyms should be considered as well. Thus, for example, "We may allow third party ad networks to collect technical information, such as your Subscriber Identity Module serial." should also be annotated with Identifier_SIM_Serial_3rdParty.

While a practice must be explicitly described in a policy, it can also follow from its systematic reading. For example, if a policy defines "Personal Information covers advertising identifiers, ... ." and in a later section states "We share Personal Information with ad networks." the policy should be annotated with Identifier_Ad_ID_3rdParty.

There are broad annotation categories Location, Identifier, Demographic, and Contact and fine categories, e.g., Age and Gender. The broad and fine categories should be only annotated if they are explicitly mentioned. For example, "We collect location information." should be annotated with Location_1stParty. It should not be annotated with Location_Bluetooth_1stParty or other fine categories. Also, a statement such as "We collect your location from the IP address of your device." should be annotated with both Location_IP_Address_1stParty and with Location_1stParty (and also Identifier_IP_Address_1stParty).

The broad categories (e.g., Demographic) cover general statements (e.g., "We collect your demographics."). They are not catch-all categories and do not cover any specific fine categories that are not included in the annotation scheme (e.g., Demographic_1stParty should not be used to annotate statements such as "We collect your ethnicity.").

Collection of information (whether by a first or third party) means the gathering of information from the user of the service. Such collection does not necessarily mean that a user is manually entering information into an app (e.g., entering his or her e-mail address into a form field). Information is also collected as a matter of the user's phone communicating with a web server that receives IP addresses or other automatically transmitted information.

Collection generally means that the app user is the source of the information. Thus, third-party submissions of information about a user are generally not covered. For example, no collection practice should be annotated for policy statements describing that an app receives information about a user from a data broker. An exception is the Facebook and $SSO annotation. This latter annotation (SSO = Single Sign On) covers statements, such as "We might also receive information about you from social network services that you are using to log into our apps."

The annotation scheme makes a fundamental distinction between first and third parties. A first party is the developer of the app (or the publisher if the app was developed in a work for hire situation). Third parties are ad networks and analytics companies. These types of companies allow developers to include software development kits (SDKs) in the apps' program code. These SDKs may then send data to the ad networks' or analytics' servers. This practice is not uniformly described in privacy policies. Sometimes policies describe it as third party collection "We allow third parties to collect inside our app your location information." Other policies state that "We share location information with ad networks." Both of these policies should be annotated with Location_3rdParty. Note: For third party "sharing" we require mention of ad or analytics companies (and not generic "third parties" or "service providers" or other specific non-advertising third parties, e.g., e-mail marketers). However, if "collection" by a third party is mentioned explicitly, advertisers do not need to be mentioned. Because ad networks and analytics companies are the only third party companies that can directly collect information from inside an app, we know that the policy must refer to those.

Third party collection practices (ie, sharing) do not cover collection by or sharing information with other users.

Collection (whether by a first or third party) covers information gathering in many different ways. For example, collection can happen by phone, e-mail, or postal mail. An annotation should be made independently of whether the policy specifically mentions that it is an app that is the means for collecting the information. In fact, even if the policy states that "We collect your e-mail when you contact us through a form on our website.", an annotation of Contact_E-Mail_Address_1stParty should be made.

Collection can have many different purposes, such as applying for a job or obtaining an e-mail newsletter. The purpose for first party collection does not matter. The purpose of third party collection is advertising or analytics, which should become clear from the policy.

If certain privacy practices described in a policy are contingent upon user registration, login, or participation, the policy is analyzed from the perspective of a registered, logged in, or participating user. Thus, for example, if location information is only collected from logged in users, the policy is classified as allowing location collection. Similarly, if certain practices are dependent on a user's consent, opt-in, or opt-out, it is assumed that the user consented, opted in, or did not opt out, respectively.

The annotations should be also made for the negative instances, i.e., when a policy explicitly says that a practice does not occur. For example, a statement, such as "We do not access your phone number on your device." should be annotated with No_Contact_Phone_Number_1stParty. In some cases it may be difficult to distinguish whether a statement should cover a positive or negative instance. For example, "We will not receive your age except when you submit demographic data to us voluntarily." should be annotated with Demographic_Age_1stParty and Demographic_1stParty because under some circumstance the exception may apply and the information may be collected.

## B.	Instructions for Specific Practices

If a policy speaks of “collection of fine-grained location data” (or “exact” locations etc.), the practice should be annotated with Location_GPS_1stParty, Location_Bluetooth_1stParty, Location_Wi-Fi_1stParty, and Location_1stParty. If a policy speaks of “collection of coarse-grained location data (or “approximate” location etc.), the practice should be annotated with Location_Cell_Tower_1stParty and Location_IP_Address_1stParty.

The difference between the Location and Contact categories is that Location (GPS, cell tower, etc.) covers dynamic data and Contact (addresses, ZIPs, etc.) covers static data.

Hashed data should be annotated in the same way as other data (e.g., hashed device IDs should be treated as device IDs).

Ad identifiers covers Apple’s IDFA, Google’s AdID, and other similar ad identifiers.

Age can also be date of birth, year, or age range.

Location does not cover locale.

Address Book does not cover Facebook ids of friends but rather refers to contacts contained in the address book of the phone.

Hardware identifier is a synonym for MAC.

Device IDs, also known as Android IDs for Android, cover created IDs on the services (e.g., We will create a custom identifier for you. "). However, Device IDs do not cover application numbers assigned by an app upon installation.

Postal addresses also cover billing and shipping addresses.
